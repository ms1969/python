import builtins


# n =  int(input())
# i = 0
# sum = 0
# sumsum =0
# while sumsum + sum <= n:
#     i += 1
#     sum = sum + i
#     sumsum +=sum 
#     print(sum, sumsum)
# print(i)

from string import punctuation


def longest_word_in_file(file_name):
    f = open(file_name, encoding='utf-8')
    s = f.read()
    s = s.strip(punctuation)
    print(s)
    l = [i for i in (s.strip(punctuation).split())]
    word = ''
    for i in l:
        if len(word) <= len(i):
            word = i
    return word

longest_word_in_file('//Users/maxmaxm/PycharmProjects/pythonProjectl1/venv/text.txt')





        















    



