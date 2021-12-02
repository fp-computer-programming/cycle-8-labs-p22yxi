# Yongdong Xi

def sum_to(n):
    total = 0
    a = 0
    while a < int(n):
        a += 1
        total += a
    return total


num = int(input('Give me a integer: '))
print(sum_to(num))
