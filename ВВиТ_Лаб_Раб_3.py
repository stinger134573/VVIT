#Задание 1: Открытие и чтение файла
def read_txt(type):
    with open('example.txt', 'r') as file:
        if type == 1:
            content = file.read()
            print(content)
        elif type == 2:
            for line in file:
                print(line)
read_txt (int(input('Введите тип ввода: 1-целиком, 2-по строчно ')))

#Задание 2: Запись в файл
def write_to_file(text):
    with open('user_input.txt', 'a') as file:
        file.write(text + "\n")
write_to_file(input('Введите текст, который хотите добавить в файл:'))

#Задание 3: Открытие и чтение файла 2
def read_txt(type):
    try:
        with open('example.txt', 'r') as file:
            if type == 1:
                content = file.read()
                print(content)
            elif type == 2:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print ('Файл не существует.')
read_txt (int(input('Введите тип ввода: 1-целиком, 2-по строчно ')))
