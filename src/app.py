from menus import get_menu_option, update_info_menu, display_info_menu

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

if __name__ == "__main__":
    print('Приложение MyProfile для предпринимателей')
    print('Сохраняй информацию о себе и выводи ее в разных форматах')
    main_menu()