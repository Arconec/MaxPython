''' Функция считает кол-во четных цифр в нечетном числе и наоборот '''
def f(n):
    res = 0
    m = 1 - n % 2
    b = n
    while b > 0:
        if b % 2 == m:
            res += 1
        b //= 10        
    return res

count = [0, 0]
for i in range(10**6):
    m = i % 2
    count[m] += f(i)

print(f'Нечетные цифры -- {count[0]}, четные цифры -- {count[1]}')