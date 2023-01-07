def digrate(k):
    a = []
    while k > 0:
        a.append(k%10)
        k //= 10
    return a
    
def f(a, m):
    res = 0
    for it in a:
        if it % 2 == m:
            res += 1
    return res

count = [0, 0]
for i in range(10**6):
    m = i % 2
    count[m] += f(digrate(i), 1 - m)

print(f'Нечетные цифры -- {count[0]}, четные цифры -- {count[1]}')