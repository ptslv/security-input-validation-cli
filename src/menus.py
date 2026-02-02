from validators import (
    get_valid_age,
    get_valid_phone,
    get_valid_email,
    get_valid_postal_code,
    get_valid_ogrnip,
    get_valid_inn,
    get_valid_account_number,
    get_valid_bik,
    get_valid_correspondent_account,
)
from display import general_info_user, business_info_user

def get_menu_option(prompt, options):
    while True:
        try:
            option = int(input(prompt))
            if option in options:
                return option
            else:
                print('Пожалуйста, введите корректный пункт меню.')
        except ValueError:
            print('Пожалуйста, введите число.')

def update_personal_info(profile: dict):
    profile['name'] = input('Введите имя: ')
    profile['age'] = get_valid_age()
    profile['phone'] = get_valid_phone()
    profile['email'] = get_valid_email()
    profile['postal_code'] = get_valid_postal_code()
    profile['postal_address'] = input('Введите почтовый адрес: ')
    profile['additional_info'] = input('Введите дополнительную информацию:\n')
    return profile

def update_business_info(business: dict):
    business['ogrnip'] = get_valid_ogrnip()
    business['inn'] = get_valid_inn()
    business['account_number'] = get_valid_account_number()
    business['bank_name'] = input('Введите название банка: ')
    business['bik'] = get_valid_bik()
    business['correspondent_account'] = get_valid_correspondent_account()
    return business

def update_info_menu(profile: dict, business: dict):
    while True:
        print('ИЗМЕНИТЬ ИНФОРМАЦИЮ')
        print('1 - Личная информация')
        print('2 - Информация о предпринимателе')
        print('0 - Назад')

        option1 = get_menu_option('Введите номер пункта меню: ', [0, 1, 2])
        if option1 == 0:
            break
        elif option1 == 1:
            update_personal_info(profile)
        elif option1 == 2:
            update_business_info(business)

def display_info_menu(profile: dict, business: dict):
    while True:
        print('ВЫВЕСТИ ИНФОРМАЦИЮ')
        print('1 - Личная информация')
        print('2 - Вся информация')
        print('0 - Назад')

        option2 = get_menu_option('Введите номер пункта меню: ', [0, 1, 2])
        if option2 == 0:
            break
        elif option2 == 1:
            general_info_user(profile)
        elif option2 == 2:
            general_info_user(profile)
            business_info_user(business)