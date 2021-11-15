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

# class Vector:
#     def __init__(self, *args):
#         self.values = sorted([i for i in args if isinstance(i, int)])
#
#     def __str__(self):
#         if self.values:
#             return f"Вектор{tuple(self.values)}"
#         return "Пустой вектор"
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             x = [i + other for i in self.values]
#             return Vector(*x)
#         if isinstance(other, Vector):
#             if len(self.values) == len(other.values):
#                 x = [self.values[i] + other.values[i] for i in range(len(self.values))]
#                 return Vector(*x)
#             else:
#                 print("Сложение векторов разной длины недопустимо")
#         else:
#             print(f"Вектор нельзя сложить с {other}")
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             self.values = [i * other for i in self.values]
#             return Vector(*self.values)
#         if isinstance(other, Vector):
#             if len(self.values) == len(other.values):
#                 self.values = [self.values[i] * other.values[i] for i in range(len(self.values))]
#                 return Vector(*self.values)
#             else:
#                 print("Умножение векторов разной длины недопустимо")
#         else:
#             print(f"Вектор нельзя умножать с {other}")
#
#
# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
# v2 = Vector(3, 4, 5)
# print(v2)  # печатает "Вектор(3, 4, 5)"
#
# v3 = v1 + v2
#
# print(v3)  # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4)  # печатает "Вектор(9, 11, 13)"
# v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
# v5 + 'hi' # печатает "Вектор нельзя сложить с hi"

# class City:
#     def __init__(self, name):
#         name = name.lower().split()
#         s = ''
#         for i in name:
#             s = s + i[0].upper() + i[1:] + ' '
#         self.name = s[0:-1:]
#
#     def __str__(self):
#         return self.name
#
#     def __bool__(self):
#         return self.name[-1] not in ('a', 'e', 'i', 'o', 'u')
#
# p1 = City('new york')
# print(p1)  # печатает "New York"
# print(bool(p1))  # печатает "True"
# p2 = City('SaN frANCISco')
# print(p2)  # печатает "San Francisco"
# print(p2 == True)  # печатает "False"

# class Quadrilateral:
#     def __init__(self, width, height=None):
#         self.height = height or width
#         self.width = width
#
#     def __str__(self):
#         if self.width == self.height:
#             return f"Куб размером {self.width}х{self.height}"
#         else:
#             return f"Прямоугольник размером {self.width}х{self.height}"
#
#     def __bool__(self):
#         return self.height == self.width
#
#
# q1 = Quadrilateral(10)
# print(q1)  # печатает "Куб размером 10х10"
# print(bool(q1))  # печатает "True"
# q2 = Quadrilateral(3, 5)
# print(q2)  # печатает "Прямоугольник размером 3х5"
# print(q2 == True)  # печатает "False"

# class NewInt(int):
#     def __init__(self, n):
#         self.n = n
#
#     def repeat(self, i=2):
#         return int(str(self.n) * i)
#
#     def to_bin(self):
#         return int(bin(self.n)[2:])
#
#
# a = NewInt(9)
# print(a.repeat())  # печатает число 99
# d = NewInt(a + 5)
# print(d.repeat(3))  # печатает число 141414
# b = NewInt(NewInt(7) * NewInt(5))
# print(b.to_bin()) # печатает 100011 - двоичное представление числа 35
#
# # Кстати, как вы думаете, что вернет данный вызов NewInt() ?

# class Transport:
#     def __init__(self, brand, max_speed, kind=None):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.kind = kind
#
#     def __str__(self):
#         return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"
#
#
# class Car(Transport):
#     def __init__(self, brand, max_speed, mileage, gasoline_residue):
#         super().__init__(brand, max_speed, 'Car')
#         self.mileage = mileage
#         self.__gasoline_residue = gasoline_residue
#
#     def get_gasoline_residue(self):
#         return f"Осталось бензина на {self.__gasoline_residue} км"
#
#     def set_gasoline_residue(self, value):
#         if isinstance(value, int):
#             self.__gasoline_residue = self.__gasoline_residue + value
#             print(f"Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л")
#         else:
#             print('Ошибка заправки автомобиля')
#
#     gasoline = property(fget=get_gasoline_residue, fset=set_gasoline_residue)
#
#
# class Boat(Transport):
#     def __init__(self, brand, max_speed, owners_name):
#         super().__init__(brand, max_speed, 'Boat')
#         self.owners_name = owners_name
#
#     def __str__(self):
#         return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
#
# class Plane(Transport):
#     def __init__(self, brand, max_speed, capacity):
#         super().__init__(brand, max_speed, 'Plane')
#         self.capacity = capacity
#
#     def __str__(self):
#         return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'
#

# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 320 км
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr


class Initialization:
    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print(f"Количество людей должно быть целым числом")
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.capacity
        elif isinstance(other, (MeatEater, Vegetarian)):
            return other.capacity == self.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {self.capacity}"

    def __lt__(self, other):
        if isinstance(other, int):
            return other > self.capacity
        elif isinstance(other, (MeatEater, Vegetarian)):
            return other.capacity > self.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {self.capacity}"

    def __gt__(self, other):
        if isinstance(other, int):
            return other < self.capacity
        elif isinstance(other, (MeatEater, Vegetarian)):
            return other.capacity < self.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {self.capacity}"


v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 25000)  # False
print(100000 < s_first)  # False
print(100 < s_first)  # True
