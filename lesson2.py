# Home work 2


# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт определения типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно,в программе.
# Попробуйте использовать не только базовые типы, но и вложенные словари, кортежи, списки.
# (Можно ограничиться вложенностью 1 уровня и не обходить содержимое этих вложенных коллекций.)

# my_list = [1, 1.5, "string", True, [555], {"number": 10}, ("World", "Craft", "OpaOpa")]
# print(my_list)
# print(type(my_list))
#
# for number, element in enumerate(my_list):
#     print(number, element, sep=": ")
#     print(type(element))


# 2. Для списка реализовать c, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Исходные списки можете инициализировать прямо в коде,
# но обязательно проверьте работоспособность, для пустого списка, списка из 1 элемента,
# списка с четным количеством элементов и с нечетным.
# (Опционально) Если получится, реализуйте обмен, как функцию.

# a = 100
# b = 200
# c = 300
# x = 0
# my_list = [a, b, c, 500, 1000, 2000, "End"]
# print(my_list)
# for i in range(int(len(my_list) / 2)):
#     my_list[x], my_list[x + 1] = my_list[x + 1], my_list[x]
#     x += 2
# print(my_list)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# month = int(input("Введите месяц от 1 до 12: "))
# winter = [12, 1, 2]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]
#
# if month in winter:
#     print("это зима")
# elif month in spring:
#     print("это весна")
# elif month in summer:
#     print("это лето")
# elif month in autumn:
#     print("это осень")
# else:
#     print("Пусто")
#
# month = int(input("Введите месяц от 1 до 12: "))
#
# my_dict = {"winter": [12, 1, 2],
#            "spring": [3, 4, 5],
#            "summer": [6, 7, 8],
#            "autumn": [9, 10, 11]
#            }
#
# print(my_dict)
#
# print(my_dict["winter"])
#
# if month in my_dict.setdefault("winter"):
#     print("это зима")
# elif month in my_dict.setdefault("spring"):
#     print("это весна")
# elif month in my_dict.setdefault("summer"):
#     print("это лето")
# elif month in my_dict.setdefault("autumn"):
#     print("это осень")
# else:
#     print("Пусто")

