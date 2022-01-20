# def summa_n(t):
#     nSumma = 0
#     for i in range(1, t+1):
#         nSumma += i
#     print(f"Я знаю, что сумма чисел от 1 до {t} равна {nSumma}")


# Проверка пароля
# def check_password(p):
#     from string import ascii_uppercase
#     from string import digits
#     symbols = '!@#$%*'
#     bS = False
#     bH = False
#     isDig = 0
#     if len(p) < 10:
#         print('Easy peasy')
#     else:
#         for i in p:
#             if i in ascii_uppercase:
#                 bH = True
#             if i in digits:
#                 isDig += 1
#             if i in symbols:
#               bS = True
#         if bH and bS and isDig >= 3:
#             print('Perfect password')
#         else:
#             print('Easy peasy')


# def count_letters(s):
#     big = [i for i in s if i.isupper()]
#     small = [i for i in s if i.islower()]
#     print(f'Количество заглавных символов: {len(big)}')
#     print(f'Количество строчных символов: {len(small)}')

# def factorial(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr *= i
#     return pr

# def find_duplicate(l):
#     l1 =[]
#     for i in range(len(l)):
#         if l.count(l[i]) > 1 and l[i] not in l1:
#             l1.append(l[i])
#     return(l1)


# def find_duplicate(l):
#     l1 =[]
#     l1 = [l1.append(l[i]) for i in range(len(l)) if ((l.count(l[i]) > 1) and (l[i] not in l1))]
#     return(l1)
#
# print(find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]))

# def first_unique_char(s):
#     l= []
#     for i in s:
#         l.append(i)
#     for i in range(len(l)):
#         if l.count(l[i]) == 1:
#             return i
#     return -1

def format_namelist(l):
    s = ''
    for i in range(len(l)):
        if i < len(l) - 2:
            s = s + l[i]['name'] + ', '
        elif i < len(l) - 1:
            s = s + l[i]['name'] + ' '
        elif i == len(l) - 1 and len(l) > 1:
            s = s + 'и ' + l[i]['name']
        else:
            s = l[i]['name']
    return (s)


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
