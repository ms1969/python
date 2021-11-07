# Сортировка по второму элементу
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
#
# subject_marks = sorted(subject_marks, key=lambda x: x[1])
# for i in subject_marks:
#     print(i[0], i[1])

# Сортировка по второму элементу по убыванию
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# subject_marks = sorted(subject_marks, key=lambda x: -x[1])
# for i in subject_marks:
#     print(i[0], i[1])

# Двойная сортировка
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# subject_marks = sorted(subject_marks, key=lambda x: (-x[1], x[0]))
# for i in subject_marks:
#     print(i[0], i[1])

# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
# models = sorted(models, key=lambda x: x['color'])
# for i in models:
#     print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")

a = 100
condition = a % 2 == 0
print(condition)



