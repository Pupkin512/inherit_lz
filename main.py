import security
def main():
    user = security.Authorization(
        name=input("Введите ваше имя: "),
        surname=input("Введите вашу фамилию: "),
        login=input("Введите ваш логин: "),
        password=input("Введите ваш пароль: "),
        hash_algorithm=input("Алгоритм хеширования(sha512, md5): "))
    print(user.hashing_pass())
    print(user.info())
    print(user.is_employee())

if __name__ == "__main__":
    main()
