import argparse
from validators import (
    is_valid_email,
    is_valid_phone,
    is_valid_inn,
    is_valid_ogrnip,
    is_valid_bik,
)
from menus import get_menu_option, update_info_menu, display_info_menu
def run_audit(path: str):
    checks = {
        "email": is_valid_email,
        "phone": is_valid_phone,
        "inn": is_valid_inn,
        "ogrnip": is_valid_ogrnip,
        "bik": is_valid_bik,
    }

    total = 0
    passed = 0

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            field, value = line.split(",", 1)
            total += 1

            if field not in checks:
                print(f"[SKIP] {field}")
                continue

            if checks[field](value):
                print(f"[OK]   {field}: {value}")
                passed += 1
            else:
                print(f"[FAIL] {field}: {value}")

    print(f"\nResult: {passed}/{total} passed")
def main_menu():
    profile = {
        'name': '',
        'age': 0,
        'phone': '',
        'email': '',
        'postal_code': '',
        'postal_address': '',
        'additional_info': '',
    }

    business = {
        'ogrnip': '',
        'inn': '',
        'account_number': '',
        'bank_name': '',
        'bik': '',
        'correspondent_account': '',
    }

    while True:
        print('ГЛАВНОЕ МЕНЮ')
        print('1 - Внести или изменить информацию')
        print('2 - Вывести информацию')
        print('0 - Выход')

        option = get_menu_option('Введите номер пункта меню: ', [0, 1, 2])

        if option == 0:
            print('Выход из приложения.')
            break
        elif option == 1:
            update_info_menu(profile, business)
        elif option == 2:
            display_info_menu(profile, business)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", help="Path to audit input file")
    args = parser.parse_args()

    if args.audit:
        run_audit(args.audit)
    else:
        print('Приложение MyProfile для предпринимателей')
        main_menu()

if __name__ == "__main__":
    main()