import random
# k = 1000 # int(input())

# list_k = []
# while len(list_k) < k:
#     a = random.randint(-10**6, 10**6)
#     if a not in list_k:
#         list_k.append(a)

# a = list_k

def f(a):
    b = []
    while len(a) > 1:
        b.append(max(a) - min(a))
        i1 = a.index(max(a))
        a.pop(i1)
        i1 = a.index(min(a))
        a.pop(i1)
    return b



# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [5, 4, 3, 2, 9, 11, 15]

final = f(a)
print(final)
while len(final) != 1:
    final = f(final) 
    print(final)
