from math import ceil, log, exp, floor
from IEEE754 import Dec2IEEE
import matplotlib.pyplot as plt

ln2 = log(2)

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

# Objetivo: cálculo de e^x reduzindo o valor do argumento
# e^x = 2^n * (e^r)^256

'''
colocar no relatorio que fazemos uma redução do valor do argumento pq o erro se propaga muito rapido 
com numeros grandes se utilizarmos a serie de taylor. Entao reduzimos o valor do argumento para calcular a serie de taylow
para um valor bem pequeno e calcula e^x de um valor inteiro q ja e facil de calcular ai no final so faz e^argumento = e^X * e^r
'''

def exponencial(x: Dec2IEEE):
    #verificar se x<0
    # verificar x par ou x impar
    k1 = int(x.x)
    k2 = x.x - k1
    
    if k1%2:
        res = Dec2IEEE(pow(exp(k1/2), 2))
    else:
        res = Dec2IEEE(exp(1)*(pow(exp((k1-1)/2), 2)))
    if k1 < 0:
        res = Dec2IEEE(1/res.x)

    n = ceil((k2 - (ln2/2))/ln2) # deixar como constantes
    
    r = (k2 - (n * ln2)) / 256
    #expr = Dec2IEEE(1 + r * (1 + r * (0.5 + r * (0.16666666666666666 + (0.041666666666666664 * r)))))
    expr = (1 + r * (1 + r * (0.5 + r * (0.16666666666666666 + (0.041666666666666664 * r)))))
    #expx = Dec2IEEE(pow(2,n) * pow(expr.x,256)) # soma do expoente com n
    expr256 = Dec2IEEE(pow(expr,256))
    expr256.Fbits.e += n
    expx = expr256.x * res.x
    #ERRO NAO PODE SE PROPAGAR
    #print(expx.Fbits.e)
    #print(res.Fbits.e)

    #res = Dec2IEEE(expx.x * res.x)
    
    return expx

def bailey():
    argumentos = []
    corretos = []
    aproximados = []
    erros = []
    for i in range(70,100,3):
        i /= 10
        num = Dec2IEEE(i)
        num.x = round(num.x, 2)
        aproximado = exponencial(num)
        correto = exp(num.x)
        argumentos.append(num.x)
        corretos.append(correto)
        erros.append(abs(correto - aproximado))
        aproximados.append(aproximado)
    print(f"{'Argumento':<10}{'Valor Correto':<25}{'Erro':<20}{'Valor Aproximado':<20}")
    print("-" * 55)
    for i in range(len(argumentos)):
        print(f"{argumentos[i]:<10}{corretos[i]:<15.8f}{erros[i]:<20.16f}{aproximados[i]:<30.8f}")
    plt.plot(argumentos, erros, label='Erro')
    plt.title('Análise de Erros da Aproximação de Bailey')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    bailey()
    print(exponencial(Dec2IEEE(3.6)))
    print(exp(3.6))