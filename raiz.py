from IEEE754 import Dec2IEEE
from math import sqrt
import matplotlib.pyplot as plt

raiz_dois = 1.414213562
inicio = 0
fim = 501
passo = 5

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

def par(n):
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
    
    if par(expoente):
        return (2**(expoente>>1)) * raiz_aproximada(f)
    else:
        return 2**((expoente-1)>>1) * raiz_dois * raiz_aproximada(f)

valores_aproximados = []
valores_exatos = []
erros = []

def calculo_raizes():
    indice_lista = 0
    for i in range(inicio,fim,passo):
        valores_aproximados.append(raiz(i/100))
        valores_exatos.append(sqrt(i/100))
        erros.append(abs(valores_aproximados[indice_lista] - valores_exatos[indice_lista]))
        indice_lista += 1

if __name__ == "__main__":
    calculo_raizes()
    print(valores_aproximados)
    print(valores_exatos)
    print(erros)
    vetLegenda = [i/100 for i in range(inicio,fim,passo)]
    plt.plot(vetLegenda, erros) 
    plt.title('Análise de Erros da Aproximação da Raiz Quadrada')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.show()