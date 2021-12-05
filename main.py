# def get_min():
#     mini = float("+inf")
#     value = int(input("Введите число или -1,чтобы выйти "))
#     while value != -1:
#         if value < mini:
#             mini = value
#         value = int(input("Введите число или -1,чтобы выйти "))
#     print("Minimum ", mini)
# get_min()


# def get_max():
#     maxi = float("-inf")
#     value = int(input("Введите число или -1,чтобы выйти "))
#     while value != -1:
#         if value > maxi:
#             maxi = value
#         value = int(input("Введите число или -1,чтобы выйти "))
#     print("Maximum ", maxi)
# get_max()


# def get_sum():
#     sum = 0
#     value = int(input("Введите число или -1 ,чтобы выйти "))
#     while value != -1:
#         sum = sum + value
#         value = int(input("Введите число или -1 ,чтобы выйти "))
#     print(sum)
# get_sum()


# def get_arithmetic_mean():
#     summ = 0
#     count = 0
#     value = int(input("Введите число или -1 ,чтобы выйти "))
#     while value != -1:
#         summ = summ + value
#         count = count+1
#         value = int(input("Введите число или -1 ,чтобы выйти "))
#     arth = summ // count
#     print(arth)
# get_arithmetic_mean()
# import json
# data = {
#     "persons":["Vasya","Vany"],
#     "is_alive": True
# }
# jsondata = json.dumps(data)
# with open("file.json","w") as file:
#     file.write(jsondata)
# with open("file.json", "r") as json_file:
#     data = json_file.read()
#     print(type(data))
#     data_json = json.loads(data)
#     print(type(data_json), data_json)

import json
from pprint import pprint
def database():
    data = {}
    count = 0
    value_of_persons = int(input("Введите количество пользоватей "))
    while value_of_persons != count:
        name = input("Введите имя ")
        age = int(input("Введите возраст"))
        passw = input("Введите пароль ")
        count = count + 1
        data[name] = {"age":age,"password":passw}
    jsondata = json.dumps(data)
    with open("database1.json", "w") as file:
        file.write(jsondata)
database()
def json_print(nameofjson):
    with open(nameofjson, "r") as file1:
        pprint(file1.read())
name_of_json = input("Введите название файла ")
json_print(name_of_json)