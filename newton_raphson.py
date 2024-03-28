from IEEE754 import Dec2IEEE, IEEE754
from IEEE754 import struct
import math
from math import sqrt
import matplotlib.pyplot as plt
''' 
MATEMÁTICA COMPUTACIONAL (6900/1)
MÉTODO PARA CÁLCULO DA RAIZ QUADRADA

Professor Dr. Airton Marco Polidório

Discentes:
Luca Mattosinho Teixeira RA 124316
Paula Fernandes Torres RA 123565 
'''

# Constantes para o intervalo dos valores de argumento
raiz_dois = 1.414213562
inicio = 0
fim = 10000
passo = 1

# Função para obter a fração da mantissa
def fracao_da_mantissa(mantissa_binaria):
    decimal = 0.0
    expoente = -1

    for bit in mantissa_binaria:
        if bit == '1':
            decimal += 2**expoente
        expoente -= 1

    return decimal

def decimal_para_binario_32_bits(numero):
    if numero == 0:
        return '0' * 32  # Se o número for zero, retorna uma string de 32 zeros
    binario = ''
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    
    # Adiciona zeros à esquerda para completar 32 bits
    binario = '0' * (32 - len(binario)) + binario
    
    return binario

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

# Função para calcular a raiz quadrada com a aproximação especificada
def raiz_aproximada(f):
    return ((1 - (f / (4 + 2 * f))) * (f/2)) + 1

# Função geral para calcular a raiz quadrada 
def raiz(x):
    y = Dec2IEEE(x)
    expoente = y.Fbits.e - 127
    f = decimal_para_binario(y.Fbits.f)
    f = fracao_da_mantissa(f)
    
    if par(expoente):
        return (2**(expoente>>1)) * raiz_aproximada(f)
    else:
        return 2**((expoente-1)>>1) * raiz_dois * raiz_aproximada(f)

# Listas para armazenar os valores necessários
valores_aproximados_1 = []
valores_aproximados_nr = []
valores_exatos = [sqrt(i/100) for i in range(inicio, fim, passo)]
erros_1 = []
erros_nr = []
argumentos_1 = []

# Função que calcula os resultados para um intervalo de valores de argumento 
def calculo_raizes():
    for i in range(inicio,fim,passo):
        valores_aproximados_1.append(raiz(i/100))
        erros_1.append(abs(valores_aproximados_1[i] - valores_exatos[i]))

def graficos_resultados():
    plt.plot(argumentos_1, valores_exatos, label='Corretos', linestyle='-', color='red')
    plt.plot(argumentos_1, valores_aproximados_nr, label='Aproximados por N-R', color='orange')
    plt.plot(argumentos_1, valores_aproximados_1, label='Aproximados T1', linestyle='-', color='blue') 
    plt.title('Valores obtidos do cálculo da raiz quadrada')
    plt.xlabel('Argumento')
    plt.ylabel('Valores')
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_erros():
    plt.plot(argumentos_1, erros_nr, label='Erros Newton-Raphson', color='red')
    plt.plot(argumentos_1, erros_1, label='Erros primeiro trabalho', color='blue') 
    plt.title('Análise de erros da aproximação da raiz quadrada')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.legend()
    plt.show()

def grafico_nr():
    plt.plot(argumentos_1, erros_nr, label='Erros Newton-Raphson', color='green')
    plt.title('Erros de cálculo do método de Newton-Raphson')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.show()

def newtonRaphson(num, epsilon):
    xk = calcula_estimativa(num)
    if xk == 0:
        return 0
    k = 1
    while True:
        xk_1 = 0.5 * (xk + num.x/xk)
        print("#{}\t[xk]: {:.20f}\t[xk+1]: {:.20f}".format(k, xk, xk_1))

        if abs(xk_1 - xk) <= epsilon:
            break

        xk = xk_1
        k += 1
    print("-----------------------------------------------------------------------------")

    return xk_1

def calcula_estimativa(num):
    a = 1 << 23
    b = 1 << 29
    if num.x > 0 and num.x <= 1:
        return 1
    elif num.x == 0:
        return 0
    else:
       c = IEEE2IntBits(num) - a
       resp = decimal_para_binario_32_bits(int((c>>1) + b))
       resp = BinToDec(resp)
       return resp

def calculo_nr():
    epsilon = 1e-10

    for i in range(inicio, fim, passo):
        num = Dec2IEEE(i/100) 
        resultado = newtonRaphson(num, epsilon=epsilon)
        valores_aproximados_nr.append(resultado)
        erros_nr.append(valores_aproximados_nr[i] - valores_exatos[i])
        argumentos_1.append(i/100)

    print("O valor aproximado para a raíz quadrada de " + str(round(num.x, 3)) + " é " + str(resultado) + ".")

def IEEE2IntBits(ieee: Dec2IEEE):
    x = ieee.Fbits.f | (ieee.Fbits.e << 23) | (ieee.Fbits.s << 31)
    return x

def BinToDec(bin_string):
    if len(bin_string) != 32:
        raise ValueError("A string binária precisa ter 32 bits")
    
    float_bits = struct()
    float_bits.f = int(bin_string[9:], 2)
    float_bits.e = int(bin_string[1:9], 2)
    float_bits.s = int(bin_string[0], 2)
    
    ieee = IEEE754()
    ieee.Fbits = float_bits
    
    return ieee.x

if __name__ == "__main__":
    calculo_raizes()
    calculo_nr()
    grafico_erros()
    graficos_resultados()
    grafico_nr()
    #newtonRaphson(Dec2IEEE(1.5), 1e-8)