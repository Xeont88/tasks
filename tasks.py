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

print(season(13))
