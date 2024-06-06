x = -123
if x == 0:
    print(0)
else:
    sign = -1 if x < 0 else 1
    x = abs(x)

    reversed_x = 0
    while x != 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    if reversed_x > 2 ** 31 - 1 or reversed_x < -2 ** 31:
        print(0)
    else:
        print(reversed_x * sign)
