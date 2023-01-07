import random

def f(a):
    b = list()
    a.sort()
    cnt = len(a) // 2
    for i in range(cnt):
        b.append(a[-i-1] - a[i])
    return b

k = 1000 # int(input())

b = set()
while len(b) < k:
    b.add(random.randint(-10**6, 10**6))

a = list(b)

print(*a)
while len(a) > 1:
    a = f(a) 
    print(*a)