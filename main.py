# #x = int(input())
# #if x < 0:
#  #   print("Решений нет")
# #elif x == 0:
#  #   print("Одно решение")
# #elif x > 0:
# #    print("Два решения")
# #import random
# #x = random.randint(-50,50)
# #y = random.randint(-50,50)
# #print(x)
# #print(y)
# #if x > 0 and y > 0:
# #    print("Лежит в первой четверти")
# #elif x < 0 and y > 0:
# #    print("Лежит в четвёртой четверти")
# #elif x > 0 and y < 0:
# #    print("Лежит во второй четверти")
# #elif x < 0 and y < 0:
# #    print("Лежит в третьей четверти")
# #x = 0
# #while(x < 10000):
#   #  print("Egor")
#  #   x = x+1
# #print(x)
# #for e in range(0,1001,2):
#     #print(e)
# #import random
# #a = []
# #for i in range(0,10):
#    #  a.append(random.randint(-30,30))
# #print(a)
# #for x in a:
#   #  if x > 7:
#       #  print(x)
#
# #b = []
# #c = 0
# #while(c < 10):
# #    b.append(random.randint(-100,100))
#  #   c = c+1
# #print(b)
# #import random
# #print("Угадайте число в диапозоне от 0 до 100")
# #a = random.randint(0,100)
# #b = -1
# #while(b != a):
#    # b = int(input())
#     #if b > a:
#         #print("Меньше")
#     #elif a > b:
#         #print("Больше")
# #print("Вы угадали")
# #a = int(input())
# #print(a-1,a,a+1,sep="<")
#
# #a = int(input())
# #b = int(input())
# #if a < b:
# #    print(a)
# #elif a > b:
# #   print(b)
#
# #a = int(input())
# #b = int(input())
# #print(min(a,b))
#
# #a = str(input())
# #x = 0
# #while(x < 10):
# #    print(a)
# #    x = x+1
#
# #a = int(input())
# #i = 0
# #for i in reversed(range(0,a)):
# #   print("x" * i)
# #for i in(range(0,a)):
# #    print("x" * i)
#
# #a = str(input()).lower()
# #b = str(input()).lower()
# #if a == b:
# #    print('OK')
# #elif a != b:
# #   print('ERROR')
#
# #def pow(x,y):
# #    pow(12,2)
# #    return x**y
# #a = pow
# #print(a)
#
# #def is_palindrom(my_str:str) -> bool:
# #    return my_str == my_str[::-1]
# #print(is_palindrom("abc"))
#
# #def get_factorial(n: int) -> int:
# #    result = 1
# #    for i in range(1,n+1):
# #        result = result * i
# #    return result
#
# #factorial = get_factorial(80)
# #print(factorial)
#
# #import random
# #def add_random(int_list: list) -> list:
# #    for i in range(len(int_list)):
# #        int_list[i] += random.randint(1,10000)
# #    return int_list
# #len_of_list = int(input("ведите кол-во элементов:"))
# #array = []
# #for a in range(len_of_list):
# #    test = int(input())
# #    array.append(test)
# #print(array)
# #array = add_random(array)
# #print(array)
#
# #def get_first_index(my_str: str,char):
# #    return my_str.find(char)
# #print(get_first_index("test","t"))
#
# #test = {1, 2 ,"abc", 1}
# #test.add(9)
# #test2 ={1,2}
# #print(test.union(test2))
# #print(test.difference(test2))
# #print(test.difference(test))
# #print(test)
# #print(test.intersection(test2))
# #print(set([1,2,1]))
#
# #def get_unique_elements(my_list: list) -> list:
# #   my_list = set(my_list)
# #   my_list = list(my_list)
# #   return my_list
# #print(get_unique_elements([1,2,3,4,5,1,2,3,4,5,6,7,8,8,8,8]))
#
# def get_sum(my_dict: dict)
#        return x
# print(get_sum({"Skrillex": 10 ,
#         "Abc": 20}))

# with open("test.txt", "r") as f:
#     lines = f.readlines()
#     for index in range(len(lines)):
#         lines[index] = lines[index].strip()
# print(lines)
#
#
# def write_to_file(name, date: dict):
#     with open(name, "w") as my_file:
#        my_file.write("name")
# write_to_file("test2.txt", {"BAGUVIX": "Бесконечечные жизни",
#                             "FULLCLIP": "Беконечные патроны"})
#
# def read_with_error(name):
#     try:
#          with open(name, "r") as f:
#             print(f.readlines())
#             a = 12/0
#     except ZeroDivisionError:
#         print("Я поделил на ноль")
#     except FileExistsError:
#         print("123")
#def raise_error():
#    raise SyntaxError("Ты забыл точку с запятой")
#def handle_raised_error():
#    try:
#        raise_error()
#    except SyntaxError:
#        print("Я поймал ошибку")
#if __name__ == '__main__':
#    handle_raised_error()


#def append_to_file(name, date: str):
#    with open(name, "a") as f:
#        f.write(date)
#append_to_file("test2.txt", "123")
# def write_and_read(name, date: str):
#     with open(name, "wr") as f:
#         print(f.readlines())
#         f.write(date)
# write_and_read()
# def write_dict(name, date: dict):
#     with open(name, "a") as f:
#         for key, value in date.items():
#             your_str = f"{key}: {value}\n"
#             f.write(your_str)
# write_dict("test2.txt",{"BAGUVIX": "Бесконечечные жизни",
#                         "FULLCLIP": "Беконечные патроны"})
#
# def input_journal(path: str):
#     journal = {}
#     count = int(input("Введите кол-во записей"))
#     for i in range(count):
#         name = input("Введите Имя и Фамилию: ")
#         score = int(input(f"Введите оценку для {name}:"))
#         journal[name] = score
#     with open(path, "w") as file:
#         file.write(str(journal))
# input_journal("test3.txt")

# def update_dict(my_dict: dict, key, value):
#     if key in my_dict.keys() and not isinstance(my_dict[key], list):
#         my_dict[key].append(value)
#     if key in my_dict.keys() and not isinstance(my_dict[key], list):
#         my_dict[key] = [my_dict[key]]
#     if key not in my_dict.keys():
#         my_dict[key] = value
# d = {"1": 1}
# update_dict(d, "1" , "10")
# update_dict(d, "1", "qwerty")
# update_dict(d, 2 ,)

# def NET_IDEI_DLYA_NAZVANYA (name):
#     int_list = []
#     with open(name, "r") as f:
#         line = f.readlines()
#     for line in lines:
#         int_list.append(int(line.strip()))
#         if line[-1] == 0:
#             raise ValueError
# print(NET_IDEI_DLYA_NAZVANYA("test"))

#def union_files(*paths) -> None:
#    result = []
#    for path in paths:
#        with open(path,"r") as file:
#            result.extend(file.readlines())
#    with open("aboba","w") as file:
#        file.write("".join(result))
#def test(*args):
#    print(args)

#def test_kwargs(**kwargs)
#    print(kwargs)
#    print(type(kwargs))

#union_files("test","test2.txt", "aboba")
#test_kwargs(a=1, b=2, c=3)
#from collections import Counter
#def get_frequence_dict(path: str) -> dict:
#    w = []
#    with open(path, "r") as f:
#        data = f.read()
#        return Counter(data.split())
#print(get_frequence_dict("test"))
# Рекурсия
#def factorial(n):
#    if n == 1: return 1
#    return n*factorial(n-1)
#print(factorial(4))

#def get_n(n, count):
#    print(n)
#    if count > 100: return
#    if n % 2 == 0:
#        return get_n(n / 2, count + 1)
#    else:
#        return get_n(3*n+1, count + 1)
#get_n(7, 1)


#class Animal:
#    hp = 100
#    color = "grey"
#
#    def eat(self):
#        pass
#    def noise(self):
#        print("Я люблю играть в бравлстарс!")
#    def fight(self):
#        self.hp -= 10
#class Cat(Animal):
#    hp = 1000
#    def noise(self):
#        print("Мяу!")
#    def fight(self):
#        self.hp -= 1
#    def die(self):
#        print("Я умираю в Мур-Султане")
#class Dog(Animal):
#    hp = 10
#    def noise(self):
#        print("Гав!")
#    def fight(self):
#        self.hp +=1
#dog = Dog()
#cat = Cat()

#    while cat.hp > 10:
#        dog.fight()
#        cat.fight()
#    cat.die()
#    print(f"cat = {cat.hp}", dog)


# import random
# class Person:
#     hp = 100
#     def punch(self):
#         self.hp -= 10
#     def is_healthy(self) -> bool:
#         return self.hp > 0
#
# def main():
#     oleg = Person()
#     random_value = random.randint(1,15)
#     user_value = int(input("Введите число: "))
#     while (random_value != user_value) and (oleg.is_healthy()):
#         print("Ай!")
#         oleg.punch()
#         user_value = int(input("Введите число: "))
#     if oleg.is_healthy():
#         print(f"Олег угадал. Вот его Hp: {oleg.hp}")
#     else:
#         print(f"Олег умер")
# main()
#
# def Fib(n):
#     if n == 1 or n == 2:
#         print(n)
#         return 1
#     else:
#
#         return Fib(n-1)+Fib(n-2)
# print(Fib())

# class Calculator:
#      a = 0
#      b = 0
#      def __init__(self,num1,num2):
#          self.a = num1
#          self.b = num2
#      def get_sum(self):
#          return self.a + self.b
#
# calculator1 = Calculator(40, 10)
# print(calculator1.get_sum())s