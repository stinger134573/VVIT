# Задача 1:
for i in range (1,int(input('Введите число: '))+1):
    print(i)
# Задача 2:
a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
if a==b:
    print('Числа равны')
else:
    print('Большее число: ',max(a,b))
