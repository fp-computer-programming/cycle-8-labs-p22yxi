# Yongdong Xi

numin = int(input("Give me a number: "))


def sum(num):
    total = 0
    for x in range(int(num) + 1):
        total += x
    return total


print(sum(numin))
