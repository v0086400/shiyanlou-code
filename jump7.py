a = 0
while a <= 99:
    a = a + 1
    if a % 7 == 0 or a % 10 == 7:
        continue
    elif a // 10 == 7:
        continue
    print(a)
