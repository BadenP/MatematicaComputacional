from IEEE754 import Dec2IEEE
from math import log, exp
import matplotlib.pyplot as plt

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

def algoritmo(x, lut):
    k1 = int(x)
    k2 = x - k1
    
    if k1%2:
        res = Dec2IEEE(pow(exp(k1/2), 2))
    else:
        res = Dec2IEEE(exp(1)*(pow(exp((k1-1)/2), 2)))
    if k1 < 0:
        res = Dec2IEEE(1/res.x)

    j = 0
    xj = k2
    yj = 1
    tl = len(lut)
    while xj != 0 and j < tl:
        # Passo 3: Pesquisar na LUT o maior valor k tal que xj - k >= 0
        linha = lut[j]
       # if xj - linha[2] >= 0:
        if xj >= linha[2]:
            max_k = linha[2]
            xj = xj - max_k # Fazer xj+1 = xj - max(kLUT) para k <= xj
            yj = yj * linha[1] # trocar por shift
            #print(xj,   yj)            

        j += 1
    
    yj = (1 + xj) * yj

    yj *= res.x
    # O resultado aproximado é armazenado em y1
    return yj

valores_aproximados = []
valores_exatos = []
erros = []

def calculoLUT():
    lut = cria_lut()
    
    for i in range(0,100,3):
        i /= 100
        x = i
        resultado_aproximado = algoritmo(x, lut)
        valores_aproximados.append(resultado_aproximado)
        valores_exatos.append(exp(x))
        erros.append(abs(exp(x)-resultado_aproximado))


if __name__ == "__main__":
    calculoLUT()
    #print(valores_aproximados)
    #print(valores_exatos)
    #print(erros)
    vetLegenda = [i/100 for i in range(0,100,3)]
    plt.plot(vetLegenda, erros) 
    plt.title('Análise de Erros da Aproximação com LUT')
    plt.xlabel('Argumento')
    plt.ylabel('Erro')
    plt.show()