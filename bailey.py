from math import ceil, log, exp, floor
from IEEE754 import Dec2IEEE
import matplotlib.pyplot as plt

''' 
MATEMÁTICA COMPUTACIONAL (6900/1)
MÉTODO DE BAILEY PARA CÁLCULO DA EXPONENCIAL DE EULER

Professor Dr. Airton Marco Polidório

Discentes:
Luca Mattosinho Teixeira RA 124316
Paula Fernandes Torres RA 123565 
'''

# Constantes dos intervalos para os valores de argumento
ln2 = log(2)
inicio = 400
fim = 700
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

def mantissa_ieee(num: Dec2IEEE):
    bin = decimal_para_binario(num.Fbits.f)
    mantissa = 1 + fracao_da_mantissa(bin)
    return mantissa

# Método de Bailey que calcula a exponencial de Euler 
def bailey(x: Dec2IEEE):
    k1 = int(x.x)
    k2_sinal = x.x - k1
    
    if k1%2:
        res = Dec2IEEE(pow(exp(abs(k1)/2), 2))
    else:
        res = Dec2IEEE(exp(1)*(pow(exp((abs(k1)-1)/2), 2)))
    if k1 < 0:
        res = Dec2IEEE(1/res.x)

    k2 = abs(k2_sinal)
    n = ceil((k2 - (ln2/2))/ln2) 
    
    r = (k2 - (n * ln2)) / 256
    expr = (1 + r * (1 + r * (0.5 + r * (0.16666666666666666 + (0.041666666666666664 * r)))))
    expr256 = Dec2IEEE(pow(expr,256))
    expr256.Fbits.e += n

    if k2_sinal<0:
        expr256.x = 1/expr256.x
        
    expx = expr256.x * res.x

    return expx

# Declaração das listas que armazenam os valores necessários
argumentos = []
corretos = []
aproximados = []
erros = []

# Função que monta as listas com os resultados aproximados e corretos da exponencial de Euler
def calculo_valores():
    for i in range(inicio,fim,passo):
        i /= 100
        num = Dec2IEEE(i)
        num.x = round(num.x, 10)
        aproximado = bailey(num)
        correto = exp(num.x)
        argumentos.append(num.x)
        corretos.append(correto)
        erros.append(abs(correto - aproximado))
        aproximados.append(aproximado)

def grafico_resultados():
    plt.plot(argumentos, corretos, label='Corretos', linestyle='-', color='red')  
    plt.plot(argumentos, aproximados, label='Aproximados', linestyle='-', color='blue')  
    plt.title('Valores obtidos da função exponencial de Euler')
    plt.xlabel('Argumento')
    plt.ylabel('Valores')
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_erros():
    plt.plot(argumentos, erros, label='Erro')
    plt.title('Análise de Erros da Aproximação de Bailey')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    calculo_valores()
    grafico_erros()
    grafico_resultados()
