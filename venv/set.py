# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*sorted(a & b))

# import string
#
# a = set(input())
# print(a)
# b = set(string.ascii_letters + string.digits)
# c = a - b
# print(c)

# lst = [2,2,2,2,2,3,3,3,3,3,34]
# rsl = set([x for x in lst if lst.count(x) > 1])
# print (*rsl)



# Мое решение
# ls = [['Дили', 'navalny'], ['Дили', 'realdonaldtrump'], ['Били', 'navalny'], ['Вили', 'realdonaldtrump'],
#       ['Вили', 'realdonaldtrump'], ['Били', 'joebiden'], ['Дили', 'joebiden']]
# ls = [i.split(sep=':') for i in iter(input, 'конец')]
# # ls1 = [i[0] for i in ls]
# ls1 = ['Дили', 'Били', 'Вили']
# ls1 = [[i, set()] for i in list(set(ls1))]
# for i in ls:
#     for n in range(len(ls1)):
#         if i[0] == ls1[n][0]:
#             set = ls1[n][1]
#             set.add(i[1])
#             ls1[n][1] = set
# ls1 = [[len(i[1]), i[0]] for i in ls1]
# ls1.sort()
# for i in range(len(ls1) - 1, -1, -1):
#     print(f'''Количество уникальных комментаторов у {ls1[i][1]} -''', ls1[i][0])

#Второе не мое решение
# d = {'Дили' : set(), 'Вили' : set(),  'Били' : set()}
# for s in iter(input, 'конец'):
#     a, b = s.split(': ')
#     d[a].add(b)
# for x in d:
#     d[x] = len(d[x])
# for y, x in sorted(d.items(), key=lambda x: -x[1]):
#     print(f'Количество уникальных комментаторов у {y} - {x}')

#Еще одно не мое, но лучшее решение
# ducks = {'Дили': set(), 'Били': set(), 'Вили': set()}
# for name, comment in (s.split(': ') for s in iter(input, 'конец')):
#     ducks[name].add(comment)
#
# for name, value in sorted(ducks.items(), key=lambda x: -len(x[1])):
#     print(f'Количество уникальных комментаторов у {name} - {len(value)}')

# Мальчик с сайта объявлений
# s = set(input())
# if len(s) % 2 == 0:
#     print('CHAT WITH HER!')
# else:
#     print('IGNORE HIM!')

# Цветные подковы
# s = set(map(int, input().split()))
# print(4 - len(s))

# Неповторяющиеся цифры в годах
# year = int(input())
# while True:
#     year += 1
#     if len(set(str(year))) == 4:
#         break
# print(year)
#s = ('{a, b, c}')
# s = input()
# if s == '{}':
#     print(0)
# else:
#     s = s[1:-1:]
#     s = s.split(', ')
#     set = set(list(s))
#     print(len(set))
n = int(input())
s = input()
s = 'TheQuickBrownFoxJumpsOverTheLazyDog'
#
s = s.upper()
set = set(s)
print(set)
print(len(set))
if 26 == set(s):
    print('YES')
else:
    print('NO')