# Yongdong Xi (Dec 3)


total = 0
while True:
    number = input("Give me a number: ")
    if number == '-1':
        break
    else:
        total += int(number)


print('the sum of all number is {0}'. format(total))
