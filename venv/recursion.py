# n = input()
# l = list(map(int, input().split()))
# for i in range(len(l), 0, -1):
#     print(str(l[i-1]), end=' ')

# n = int(input())
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print(str(fibo(n)))

# sum using recursion
# l = list(map(int, input().split()))
# def list_sum_recursive(a):
#     if len(a) == 1:
#         return a[0]
#     else:
#         return a[0] + list_sum_recursive(a[1:])
# print(str(list_sum_recursive(l)))

def flatten(L, New=[]):
    for i in L:
        if type(i) == list:
            flatten(i, New)
        else:
            New.append(i)
    return New

L = list(input().split())
# print(flatten([1, [2, 3, [4]], 5]))
# print(flatten([[[[9]]], [1,2], [[8]]]))
print(flatten(L))