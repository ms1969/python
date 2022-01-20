# def file_read(file_name):
#     file = open(file_name, encoding='utf-8')
#     print(file.read())
#     file.close()
# file_read('text.txt')

# n = int(input())
# def create_file_with_numbers(n):
#     file = open(f'range_{n}', 'w')
#     for i in range(1,n+1):
#         file.writelines(str(i) +'\n')
#
# create_file_with_numbers(n)

# нахождение самого длинного слова в файле с очисткой от спецсимволов
# from string import punctuation
#
#
# def longest_word_in_file(file_name):
#     f = open(file_name, encoding='utf-8')
#     s = f.read()
#     for i in punctuation:
#         s = s.replace(i, '')
#     l = s.split()
#     maxl = 0
#     for i in range(len(l)):
#         if len(l[maxl]) <= len(l[i]):
#             maxl = i
#     return l[maxl]
#
#
# print(longest_word_in_file('text.txt'))

def numbersfile(file_name):
    f = open(file_name, encoding='utf-8')
    l = [i for i in f.read().split() if len(i) == 3]
    f.seek(0)
    l1 = [int(i) for i in f.read().split() if len(i) == 2]
    f.close()
    # print (str(len(l))+','+str(sum(l1)))
    return f'{len(l)},{sum(l1)}'
    # return str(len(l))+','+str(sum(l1))



print(numbersfile('numbers.txt'))
