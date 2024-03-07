import math
from IEEE754 import Dec2IEEE

def fracao_da_mantissa(mantissa_binaria):
    decimal = 0.0
    expoente = -1

    for bit in mantissa_binaria:
        if bit == '1':
            decimal += 2**expoente
        expoente -= 1

    return decimal

def decimal_para_binario(numero_decimal):
    if numero_decimal == 0:
        return '0'
    
    binario = ''
    while numero_decimal > 0:
        resto = numero_decimal % 2
        binario = str(resto) + binario
        numero_decimal //= 2

    return binario

def mantissa_ieee(num: Dec2IEEE):
    bin = decimal_para_binario(num.Fbits.f)
    mantissa = 1 + fracao_da_mantissa(bin)
    return mantissa

def raiz_quadrada(num: Dec2IEEE, EPSILON):
    expoente = num.Fbits.e - 127
    print("Expoente:", expoente)
    mantissa = mantissa_ieee(num)
    print("Mantissa:", mantissa, "\n")

    is_impar = 0
    k = 1

    if expoente % 2 != 0:
        is_impar = 1
        expoente -= 1

    xk_1 = mantissa * 0.5 

    xk = 0

    while True:
        print("xk:", xk, "xk+1:", xk_1)
        xk = xk_1
        xk_1 = xk - (xk * xk - mantissa) / (xk * 2)
        print("#{}\t[xk]: {:.20f}\t[xk+1]: {:.20f}".format(k, xk, xk_1))
        k += 1

        if abs(xk_1 - xk) <= EPSILON:
            break

    if is_impar:
        return xk_1 * math.sqrt(2)

    return xk_1

# Exemplo de uso
num = Dec2IEEE(3.4)
EPSILON = 1e-15
resultado = raiz_quadrada(num, EPSILON)
print("Resultado:", resultado)
