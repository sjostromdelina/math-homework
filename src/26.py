def is_divisible(numerator, denominator):
    if numerator % 2 == 0 and denominator % 2 == 0:
        return True
    elif numerator % 2 != 0 and denominator % 2 != 0:
        return True
    else:
        return False

numerator = 123456789
denominator = 1234567890
result = is_divisible(numerator, denominator)
print(result)
