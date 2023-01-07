counter = 0
a = 0
for i in range(5, 10000, 3):
    for j in range(10, 10000, 10):
        if i == j and counter < 100:
            a += i
            counter += 1
print(counter, a)
