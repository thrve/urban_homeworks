#!/usr/bin/env python


my_list = ["apple", "pinapple", "orange", "banana", "watermelon"]
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:])
my_list[2] = "mandarin"
print(my_list)

my_dict = {
    "apple": "яблоко",
    "pinapple": "ананас",
    "orange": "апельсин",
    "banana": "банан",
    "watermelon": "арбуз",
}

print("\n")
print(my_dict)
print(my_dict["apple"])
my_dict["apple"] = "Яблоко"
my_dict["melon"] = "дыня"
print(my_dict)
