import random

k = 1000 # int(input())

list_k = []
a = random.randint(-10**6, 10**6)
for _ in range(k):
    while a in list_k:
        a = random.randint(-10**6, 10**6)
    list_k.append(a)

# def f(a):
#     b = []
#     while len(a) > 1:
#         min_it = min(a)
#         max_it = max(a)
#         b.append(max_it - min_it)
#         a.remove(max_it)
#         a.remove(min_it)
#     return b


def f(a):
    a.sort()
    b = []
    cnt = len(a) // 2
    for i in range(cnt):
        b.append(a[-i-1] - a[i])
    return b

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [5, 4, 3, 2, 9, 11, 15]

print(*a)
while len(a) > 1:
    a = f(a) 
    print(*a)
