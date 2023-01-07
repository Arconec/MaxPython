def digrate(k):
    a = []
    while k > 0:
        a.append(k%10)
        k //= 10
    return a

def test_chet(a):
    for it in a:
        if it % 2 == 1:
            return True
    return False
            
def test_nechet(a):
    for it in a:
        if it % 2 == 0:
            return True
    return False

chet = 0
nechet = 0
for i in range(10, 10**3):
    if i % 2 == 0:
        if test_chet(digrate(i)):
            chet += 1
    else:
        if test_nechet(digrate(i)):
            nechet += 1

print(f'Нечетные -- {nechet}, четные -- {chet}')