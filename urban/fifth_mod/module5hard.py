import hashlib
import re
import sys


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = int(age)
        self.password = self.__set_password(password)

    def __hash_password(self, password):
        return hashlib.sha3_256(password.encode()).hexdigest()

    def __is_valid_password(self, password):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W_]).{8,}$"
        return re.match(pattern, password) is not None

    def __set_password(self, password):
        if self.__is_valid_password(password):
            return self.__hash_password(password)
        else:
            print("The password does not meet the security criteria.")
            sys.exit(1)


class Video:
    pass
    # def __init__(self, title, duration, time_now, adult_mode):


class UrTube:
    pass


if __name__ == "__main__":
    try:
        nickname = input("nickname: ")
        password = input("password: ")
        age = input("age: ")

        user = User(nickname, password, age)  # Регистрация пользователя

        print(f"User {user.nickname} is registered. Age: {user.age}")

    except SystemExit:
        print("The program has stopped because the password is incorrect.")
    except ValueError as e:
        print(e)
