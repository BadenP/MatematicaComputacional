from IEEE754 import Dec2IEEE

def fracao_da_mantissa(mantissa_binaria):
    decimal = 0.0
    expoente = -1

    for bit in mantissa_binaria:
        if bit == '1':
            decimal += 2**expoente
        expoente -= 1

    return decimal+1

def decimal_para_binario(numero_decimal):
    if numero_decimal == 0:
        return '0'
    
    binario = ''
    while numero_decimal > 0:
        resto = numero_decimal % 2
        binario = str(resto) + binario
        numero_decimal //= 2

    return binario

def newton_raphson_sqrt(number, epsilon=1e-6):
    guess = number << 1  # Initial guess
    while abs(guess * guess - number) > epsilon:
        guess = (guess + number / guess) / 2
    return guess


if __name__ == "__main__":

    num = Dec2IEEE(1.5)
    d = (num.Fbits.f - 2**23)/2 + 2**29
    d = fracao_da_mantissa(decimal_para_binario(d))
    print(d)
