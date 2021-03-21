def arithmetic(num1, num2, math):
    if math == '+':
        return num1 + num2
    elif math == '-':
        return num1 - num2
    elif math == '*':
        return num1 * num2
    elif math == '/':
        return num1 / num2
    else:
        return 'неизвестная операция'


def season(month):
    if (month<3 and month >= 1) or month == 12:
        return 'зима'
    elif month<6 and month >= 3:
        return 'весна'
    elif month<9 and month >= 6:
        return 'лето'
    elif month<12 and month >= 9:
        return 'осень'
    else:
        return 'неверное значение'

# print(season(13))



def bank(a, years):

    result = 0
    for i in range(0, years):
        print(a)
        a = a * 1.1
        result = a
    # b = a
    # a = ((a * 1.1) ** years) / b**(years-1)
    return result

# print(bank(1000, 1))


def is_prime(a):

    for b in range(0, a):

            if b == 1 or b == a or b == 0:
                continue
            if a % b == 0:
                return False

    return True

print(is_prime(37))
