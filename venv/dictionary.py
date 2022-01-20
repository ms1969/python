# n = int(input())
# d = {}
# for i in range(1, n+1):
#     d.setdefault(i, i ** 2)
# print(d)

# from string import ascii_lowercase
#
# d = {i: ascii_lowercase[i - 1] for i in range(1, len(ascii_lowercase) + 1)}
# for para in range(1, len(d)+1):
#     print(d.get(para), para)
# print(ascii_lowercase)

# from string import ascii_lowercase
# alphabet = {i: ascii_lowercase[i - 1] for i in range(1, len(ascii_lowercase) + 1)}
# for para in range(1, len(alphabet)+1):
#    print(alphabet.get(para), para)

# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# for key, value in d2.items():
#     d1[key] = value
# rez = d1
# print(rez)

# n = (int(input()))
# d = {}
# for i in range(1, n + 1):
#     site = input()
#     j = 0
#     while site in d:
#         j += 1
#         if site +str(j) in d:
#             continue
#         d.setdefault(site + str(j))
#         print(site + str(j))
#         break
#     else:
#         d.setdefault(site)
#         print('OK')
# print(d)
s = ''
d = {}

# while s != 'конец':
#     s = input()
#     if s != 'конец':
#         ls = s.split(sep=':')
#         d[ls[0]] = int(ls[1])
# for key, value in sorted(d.items(), key=lambda j: j[1], reverse=True):
#     # print(list(i)[0])
#     print(key)

d = {}
for s in iter(input, 'конец'):
    ls = s.split(sep=',')
    if ls[0] in d:
        d[ls[0]] += [int(ls[1])]
    else:
        d[ls[0]] = [int(ls[1])]
d1 = {}
for key, value in d.items():
    d1[key] = sum(value)/len(value)
for key, value in sorted(d1.items(), key=lambda j: (-j[1], j[0])):
    print(key, value)






