#Задание 1: Написание простых функций
#Задача 1:
def greet(name):
    print ('Привет,', name)
greet(str(input('Введите имя: ')))

#Задача 2:
def square(number):
    print(number**2)
square(int(input('Введите число: ')))

#Задача 3:
def max_of_two(x, y):
    if x==y:
        print('Числа равны')
    else:
        print('Большее число: ',max(x,y))
max_of_two(int(input('Введите первое число: ')), int(input('Введите второе число: ')))


#Задание 2: Работа с аргументами функций
#Задача 1:
def describe_person(name, age=30):
    print('Имя: ', name, 'Возраст: ', age)
describe_person(str(input('Введите имя: ')), int(input('Введите возраст: ')))


#Задание 3: Использование функций для решения алгоритмических задач
#Задача 1:
import math
def is_prime(number_2):
    if number_2<2:
        return False
    for i in range(2,math.ceil(math.sqrt(number_2))+1):
        if number_2%i==0:
            return False
    return True
print(is_prime(int(input('Введите число: '))))
