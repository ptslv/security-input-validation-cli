SEPARATOR = '------------------------------------------'

def general_info_user(profile: dict):
    print(SEPARATOR)
    print('Имя: ', profile.get('name', ''))

    age_parameter = profile.get('age', 0)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', profile.get('phone', ''))
    print('E-mail: ', profile.get('email', ''))
    print('Индекс:', profile.get('postal_code', ''))
    print('Почтовый адрес:', profile.get('postal_address', ''))
    print('Дополнительная информация:', profile.get('additional_info', ''))

def business_info_user(business: dict):
    print(SEPARATOR)
    print('ОГРНИП:', business.get('ogrnip', ''))
    print('ИНН:', business.get('inn', ''))
    print('Расчетный счет:', business.get('account_number', ''))
    print('Название банка:', business.get('bank_name', ''))
    print('БИК:', business.get('bik', ''))
    print('Корреспондентский счет:', business.get('correspondent_account', ''))