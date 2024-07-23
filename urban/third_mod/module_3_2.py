#!/usr/bin/env python


import re

mail_pattern = re.compile(r"^\S+@\S+(\.com|\.ru|\.net)$")


def send_email(message: str, recipient: str, sender="university.help@gmail.com"):
    if not re.match(mail_pattern, sender) or not re.match(mail_pattern, recipient):
        print(
            f"It is impossible to send a letter from address {sender} to address {recipient}"
        )
    elif sender == recipient:
        print("You can't send a letter to yourself!")
    elif sender == "university.help@mail.com":
        print(
            f"NON-STANDARD SENDER! The letter was sent from addressi {sender} to address {recipient}."
        )
    else:
        print(
            f"The letter was successfully sent from address {sender} to address {recipient}."
        )


send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")

send_email(
    "Вы видите это сообщение как лучший студент курса!",
    "urban.fan@mail.ru",
    sender="urban.info@gmail.com",
)

send_email(
    "Пожалуйста, исправьте задание",
    "urban.student@mail.ru",
    sender="urban.teacher@mail.ua",
)
send_email(
    "Напоминаю самому себе о вебинаре",
    "urban.teacher@mail.ru",
    sender="urban.teacher@mail.ru",
)
