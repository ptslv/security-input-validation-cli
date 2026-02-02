def get_valid_age():
    while True:
        try:
            age = int(input('Введите возраст: '))
            if age > 0:
                return age
            else:
                print('Возраст должен быть положительным числом.')
        except ValueError:
            print('Пожалуйста, введите число.')

def get_valid_postal_code():
    while True:
        postal_code = input('Введите почтовый индекс: ')
        if postal_code.isdigit() and len(postal_code) == 6:
            return postal_code
        else:
            print('Пожалуйста, введите корректный почтовый индекс (6 цифр).')

def get_valid_phone():
    while True:
        phone = input('Введите номер телефона: ')
        phone_digits = ''.join(filter(str.isdigit, phone))
        if len(phone_digits) == 11 and phone_digits.startswith('7'):
            return phone
        else:
            print('Пожалуйста, введите корректный номер телефона (11 цифр, начиная с 7).')

def get_valid_email():
    while True:
        email = input('Введите адрес электронной почты: ')
        if '@' in email:
            return email
        else:
            print('Пожалуйста, введите корректный адрес электронной почты.')

def get_valid_ogrnip():
    while True:
        ogrnip = input('Введите ОГРНИП: ')
        if ogrnip.isdigit() and len(ogrnip) == 15:
            return ogrnip
        else:
            print('Пожалуйста, введите корректный ОГРНИП (15 цифр).')

def get_valid_inn():
    while True:
        inn = input('Введите ИНН: ')
        if inn.isdigit() and (len(inn) == 10 or len(inn) == 12):
            return inn
        else:
            print('Пожалуйста, введите корректный ИНН (10 или 12 цифр).')

def get_valid_account_number():
    while True:
        account_number = input('Введите расчетный счет: ')
        if account_number.isdigit() and len(account_number) == 20:
            return account_number
        else:
            print('Пожалуйста, введите корректный расчетный счет (20 цифр).')

def get_valid_bik():
    while True:
        bik = input('Введите БИК: ')
        if bik.isdigit() and len(bik) == 9:
            return bik
        else:
            print('Пожалуйста, введите корректный БИК (9 цифр).')

def get_valid_correspondent_account():
    while True:
        correspondent_account = input('Введите корреспондентский счет: ')
        if correspondent_account.isdigit() and len(correspondent_account) == 20:
            return correspondent_account
        else:
            print('Пожалуйста, введите корректный корреспондентский счет (20 цифр).')

def is_valid_age(value: str) -> bool:
    try:
        return int(value) > 0
    except ValueError:
        return False

def is_valid_postal_code(value: str) -> bool:
    return value.isdigit() and len(value) == 6

def is_valid_phone(value: str) -> bool:
    digits = ''.join(c for c in value if c.isdigit())
    return len(digits) == 11 and digits.startswith('7')

def is_valid_email(value: str) -> bool:
    return value.count('@') == 1 and ' ' not in value

def is_valid_ogrnip(value: str) -> bool:
    return value.isdigit() and len(value) == 15

def is_valid_inn(value: str) -> bool:
    return value.isdigit() and (len(value) == 10 or len(value) == 12)

def is_valid_account_number(value: str) -> bool:
    return value.isdigit() and len(value) == 20

def is_valid_bik(value: str) -> bool:
    return value.isdigit() and len(value) == 9

def is_valid_correspondent_account(value: str) -> bool:
    return value.isdigit() and len(value) == 20            