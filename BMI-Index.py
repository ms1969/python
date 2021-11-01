name = input("Введите имя: ")
height = input("Введите свой рост в сантиметрах: ")
weight = input("Введите свой вес в килограммах: ")
bmi = 10000 * int(weight) / (int(height) ** 2)
print("Ваш BMI индекс: " + str(int(bmi)))
if bmi > 25: 
    print("У Вас ожирение, предпримите меры!")
elif bmi == 25:
    print("У Вас пограничное соотношение веса к росту!")
else:
    print("У Вас нормальный вес")
print(type(3))



    








