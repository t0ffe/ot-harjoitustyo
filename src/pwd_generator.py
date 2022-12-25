import random


def generate_password(length, charset):
    print(charset)
    len_int = int(length)
    password = ""
    for i in range(len_int):
        password += str(random.choice(list(charset)))
    return password
