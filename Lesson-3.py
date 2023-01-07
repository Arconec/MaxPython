import random

# k = [1, 5, 3, 8, 9, 2, 5]
k = [random.randint(1, 1000) for i in range(100)]

print(*k)

odd = 0 # нечетное
even = 0 # четное
for i in range(len(k)):
    if i % 2 == 0:
        even += k[i]
    else:
        odd += k[i]
print(even - odd)

odd = 0 # нечетное
even = 0 # четное
counter = 0
for it in k:
    if counter % 2 == 0:
        even += it
        counter += 1
    else:
        odd += it
        counter += 1
print(even - odd)

odd = 0 # нечетное
even = 0 # четное
even = sum(k[::2])
odd = sum(k[1::2])
print(even - odd)

# print(even, odd)
s = 0
p = 1
for it in k:
    s += it * p
    p = -p
print(s)

s = 0
for i in range(len(k)):
    n = (i % 2) * 2 - 1
    s += k[i] * n
print(s)
