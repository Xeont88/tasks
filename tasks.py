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

# print(is_prime(37))


# def apple(pupils, apples):
#     a_for_p = 0
#     a_in_b = 0
#
#     return a_for_p, a_in_b


def XOR_cipher(data, key):
    # from itertools import izip, cycle
    import base64

    print(base64.encodestring(data).strip())


# XOR_cipher('hypercube', '1')


# XOR для шифрования/расшифровки
def xor_cipher(str, key):
    encript_str = ""
    i = 0
    for letter in str:
        i += 10
        encript_str += chr(ord(letter) ^ (key+i))
    return encript_str


# strg = "грузите апельсины бочками"
# key = 0
# key_2 = 1
# print("original:\t", strg)
# encr_strg = xor_cipher(strg, key)
# print("encript:\t", encr_strg)
# print("decript:\t", xor_cipher(encr_strg, key))


# str = 'Abrakadabra'
#
# print(str[2])
# print(str[-2])
# print(str[0:5])
# print(str[0:-2])
# print(str[1::2])
# print(str[::-1])


# str = 'asdf jkl; asdf f'
#
# print(str.count(' ') + 1)


s = 'HyperCube'

print(s[(len(s)+1)//2:]+s[:(len(s)+1)//2])

# dabraAbraka
