import random
import string
def random_password():
    n = int(input("Введите желаемое число символов: "))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(n):
        password += random.choice(alphabet)
    return password
password = random_password()
print(f"Сгенерированный пароль: {password}")
