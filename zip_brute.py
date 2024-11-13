import itertools
import pyzipper

def crack_zip(zip_file):
    with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
        for length in range(1, 5):
            combinations = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=length)
            for combination in combinations:
                password = ''.join(combination)
                try:
                    print(f'Пробуем пароль: {password}')
                    extracted_zip.extractall(pwd=password.encode())
                    print(f'Пароль найден: {password}')
                    return
                except RuntimeError as e:
                    if "Bad password" in str(e):
                        continue  # Игнорируем ошибку неверного пароля
                    else:
                        print(f'Ошибка: {e}')
                        return
    print('Пароль не найден.')

# Запрос имени архива у пользователя
zip_file_name = ''
crack_zip(zip_file_name)
