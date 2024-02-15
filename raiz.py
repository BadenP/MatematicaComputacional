from IEEE754 import Dec2IEEE
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
fim = 1000
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
valores_aproximados = []
valores_exatos = []
erros = []
argumentos = []

# Função que calcula os resultados para um intervalo de valores de argumento 
def calculo_raizes():
    indice_lista = 0
    for i in range(inicio,fim,passo):
        valores_aproximados.append(raiz(i/100))
        valores_exatos.append(sqrt(i/100))
        erros.append(abs(valores_aproximados[indice_lista] - valores_exatos[indice_lista]))
        argumentos.append(i/100)
        indice_lista += 1

def graficos_resultados():
    plt.plot(argumentos, valores_exatos, label='Corretos', linestyle='-', color='red')  
    plt.plot(argumentos, valores_aproximados, label='Aproximados', linestyle='-', color='blue')  
    plt.title('Valores obtidos do cálculo da raiz quadrada')
    plt.xlabel('Argumento')
    plt.ylabel('Valores')
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_erros():
    plt.plot(argumentos, erros) 
    plt.title('Análise de erros da aproximação da raiz quadrada')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.show()

# Chamadas das funções para calcular os valores e gerar os gráficos dos erros e resultados
if __name__ == "__main__":
    calculo_raizes()
    grafico_erros()
    graficos_resultados()
