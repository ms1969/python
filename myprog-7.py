# Задача Иосифа Флавия 🌶️🌶️
# nn человек, пронумерованных числами от 1 до nn, стоят в кругу. Они начинают считаться, каждый kk-й по
# счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
# Напишите программу, определяющую номер человека, который останется в кругу последним.


# Мое решение

n = int(input())
k = int(input())
m = [i for i in range(1, n + 1)]
lposition = 1
while len(m) > 1:
    for i in range(1, k + 1):
        if i == k:
            m.remove(m[lposition - 1])
        else:
            lposition += 1
        if lposition > len(m):
            lposition = 1
print(m[0])

# Лучшее решение

# n = int(input())
# k = int(input())
# res = 0
# for i in range(1, n+1):
#     res = (res + k) % i
# print(res + 1)