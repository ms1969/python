# class Lion:
#     def roar(self):
#         print('Rrrrrrr!!!')
#
#
# simba = Lion()
# simba.roar()


# class Counter:
#     def start_from(self, start = 0):
#         self.start = start
#     def increment(self):
#         self.start += 1
#     def display(self):
#         print(f'Текущее значение счетчика = {self.start}')
#     def reset(self):
#         self.start = 0
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display()  # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display()  # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display()  # печатает "Текущее значение счетчика = 0"

# Расстояние между точками

# class Point:
#     def set_coordinates(self,x,y):
#         self.x = x
#         self.y =y
#     def get_distance(self, obj):
#         if isinstance(obj, Point):
#             print(pow((abs(self.x - obj.x)**2 + abs(self.y - obj.y)**2), 0.5))
#         else:
#             print('Передана не точка')
#
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"

# Использование метода init

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.price = price
#         self.model = model
#         self.brand = brand
#         self.laptop_name = self.brand + ' ' + self.model
#
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"

# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.surname = surname
#         self.name = name
#         self.goals = 0
#         self.assist = 0
#
#     def score(self, ngoals=1):
#         self.goals += ngoals
#
#     def make_assist(self, nassist=1):
#         self.assist += nassist
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assist}')
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics()  # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics()  # выводит "Kokorin Alex - голы: 1, передачи: 0"

# class Zebra:
#     def __init__(self):
#         self.s = 'Полоска белая'
#
#     def which_stripe(self):
#         if self.s == 'Полоска белая':
#             print(self.s)
#             self.s = 'Полоска черная'
#         elif self.s == 'Полоска черная':
#             print(self.s)
#             self.s = 'Полоска белая'
#
#
# z1 = Zebra()
# z1.which_stripe()  # печатает "Полоска белая"
# z1.which_stripe()  # печатает "Полоска белая"
# z1.which_stripe()  # печатает "Полоска белая"

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_name(self):
#         return self.last_name + ' ' + self.first_name
#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         else:
#             return False
#
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult()) # выводит "True"

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return (f'{self.name} is {self.age} years old')
#
#     def speak(self, say):
#         return (f'{self.name} says {say}')
#
#
# jack = Dog("Jack", 4)
#
# print(jack.description())  # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof"))  # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow"))  # распечатает 'Jack says Bow Wow'
