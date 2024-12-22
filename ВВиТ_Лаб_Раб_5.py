#Задание 1: Базовый класс и методы
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return "Название книги: {}, Автор: {}, Год издания: {}".format(self.title, self.author, self.year)

book1 = Book("Мертвые Души", "Достоевский", 1842)

print (book1.get_info())

#Задание 2: Работа с конструктором
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, set_radius):
        self.radius = set_radius

circle1 = Circle(14)
print("Радиус круга: {}".format(circle1.get_radius()))

circle1.set_radius(int(input("Введите новое значение радиуса круга:")))
print("Радиус круга: {}".format(circle1.get_radius()))