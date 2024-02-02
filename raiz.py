from IEEE754 import Dec2IEEE
from math import sqrt
import matplotlib.pyplot as plt

raiz_dois = 1.414213562

x = Dec2IEEE(3.125)
y = Dec2IEEE(5)
a = Dec2IEEE(3.125)

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

def ehPar(n):
    if n&1:
        return False
    return True

def raiz_aproximada(f):
    return (1 + (f/2)) * (1 - (f / (4 + 2 * f)))

def raiz(x):
    y = Dec2IEEE(x)
    expoente = y.Fbits.e - 127
    f = decimal_para_binario(y.Fbits.f)
    f = fracao_da_mantissa(f)
    
    if ehPar(expoente):
        #print("f = ", f)
        #print("raiz = ", raiz_aproximada(f))
        return (2**(expoente>>1)) * raiz_aproximada(f)
    else:
        #print("f = ", f)
        #print("raiz = ", raiz_aproximada(f))
        return 2**((expoente-1)>>1) * raiz_dois * raiz_aproximada(f)

valores_aproximados = []
valores_exatos = []
erros = []

def calculoRaizes():
    indiceLista = 0
    for i in range(0, 501, 5):
        valores_aproximados.append(raiz(i/100))
        valores_exatos.append(sqrt(i/100))
        erros.append(abs(valores_aproximados[indiceLista] - valores_exatos[indiceLista]))
        indiceLista += 1

if __name__ == "__main__":
    calculoRaizes()
    print(valores_aproximados)
    print(valores_exatos)
    print(erros)
    vetLegenda = [i/100 for i in range(0, 501, 5)]
    plt.plot(vetLegenda, erros) 
    plt.title('Análise de Erros da Aproximação da Raiz Quadrada')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.show()