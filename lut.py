from IEEE754 import Dec2IEEE
from math import log, exp
import matplotlib.pyplot as plt

''' 
MATEMÁTICA COMPUTACIONAL (6900/1)
ALGORITMO BASEADO EM LUT PARA CÁLCULO DA EXPONENCIAL DE EULER

Professor Dr. Airton Marco Polidório

Discentes:
Luca Mattosinho Teixeira RA 124316
Paula Fernandes Torres RA 123565 
'''

# Intervalos para os valores de argumento
inicio = 0
fim = 100
passo = 1

# Função que gera a LUT com nice numbers
def cria_lut() -> [[]]:
    lut = []
    n = 1
    while True:
        nice_number = 2**(-n) + 1
        lut.append([n, nice_number, log(nice_number)])
        n += 1
        if nice_number == 1:
            break
    return lut

# Algoritmo aproximativo que calcula a exponencial de Euler 
def algoritmo(x, lut):
    k1 = int(x)
    k2 = x - k1
    
    if k1%2:
        res = Dec2IEEE(pow(exp(abs(k1)/2), 2))
    else:
        res = Dec2IEEE(exp(1)*(pow(exp((abs(k1)-1)/2), 2)))
    if k1 < 0:
        res = Dec2IEEE(1/res.x)

    j = 0
    xj = abs(k2)
    yj = 1
    tl = len(lut)
    while xj != 0 and j < tl:
        # Pesquisar na LUT o maior valor k tal que xj - k >= 0
        linha = lut[j]
        if xj >= linha[2]:
            max_k = linha[2]
            xj = xj - max_k 
            yj = yj * linha[1] 

        j += 1
    
    # Recuperação do resíduo
    yj = (1 + xj) * yj

    if k2<0:
        yj = 1/yj

    # O resultado aproximado é armazenado em yj
    yj *= res.x
    return yj

# Declaração das listas que armazenam os valores necessários
valores_aproximados = []
valores_exatos = []
erros = []
argumentos = []

# Função que monta as listas com os resultados aproximados e corretos da exponencial de Euler
def calculo_valores():
    lut = cria_lut()

    for i in range(inicio,fim,passo):
        i /= 100
        x = i
        resultado_aproximado = algoritmo(x, lut)
        valores_aproximados.append(resultado_aproximado)
        valores_exatos.append(exp(x))
        erros.append(abs(exp(x)-resultado_aproximado))
        argumentos.append(x)

def grafico_resultados():
    plt.plot(argumentos, valores_exatos, label='Exp(x)', linestyle='-', color='red')  
    plt.plot(argumentos, valores_aproximados, label='Aproximados', linestyle='-', color='blue')  
    plt.title('Valores obtidos da função exponencial de Euler com LUT')
    plt.xlabel('Argumento')
    plt.ylabel('Valores')
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_erros():
    plt.plot(argumentos, erros) 
    plt.title('Análise de erros da função exponencial de Euler com LUT')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.show()

# Chamadas das funções para calcular os valores e gerar os gráficos dos erros e resultados
if __name__ == "__main__":
    calculo_valores()
    grafico_erros()
    grafico_resultados()