# class Person:
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         if gender not in ["male", 'female']:
#             print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
#             self.gender = 'male'
#         else:
#             self.gender = gender
#
#     def __str__(self):
#         if self.gender == 'male':
#             return f"Гражданин {self.surname} {self.name}"
#         return f"Гражданка {self.surname} {self.name}"
#
# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"

class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if self.values:
            return f"Вектор{tuple(self.values)}"
        return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            self.values = [i + other for i in self.values]
            return Vector(*self.values)
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                self.values = [self.values[i] + other.values[i] for i in range(len(self.values))]
                return Vector(*self.values)
            else:
                print("Сложение векторов разной длины недопустимо")

v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"

v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
# v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
# v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
