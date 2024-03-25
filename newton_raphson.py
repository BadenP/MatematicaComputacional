from IEEE754 import Dec2IEEE
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
fim = 100000
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
    if num.x > 0 and num.x <= 1:
        xk = 1
    elif num.x == 0:
        return 0
    else:
        xk = math.log(num.x)
    k = 1
    while True:
        fx = xk * xk - num.x 
        fxp = xk + xk
        xk_1 = xk - fx / fxp 
        print("#{}\t[xk]: {:.20f}\t[xk+1]: {:.20f}".format(k, xk, xk_1))

        if abs(xk_1 - xk) <= epsilon:
            break

        xk = xk_1
        k += 1
    print("-----------------------------------------------------------------------------")

    return xk_1

def calculo_nr():
    epsilon = 1e-8

    for i in range(inicio, fim, passo):
        num = Dec2IEEE(i/100) 
        resultado = newtonRaphson(num, epsilon=epsilon)
        valores_aproximados_nr.append(resultado)
        erros_nr.append(valores_aproximados_nr[i] - valores_exatos[i])
        argumentos_1.append(i/100)

    print("O valor aproximado para a raíz quadrada de " + str(round(num.x, 3)) + " é " + str(resultado) + ".")

if __name__ == "__main__":
    calculo_raizes()
    calculo_nr()
    grafico_erros()
    graficos_resultados()
    grafico_nr()
    #newtonRaphson(Dec2IEEE(999), 1e-8)