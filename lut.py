from IEEE754 import Dec2IEEE
from math import log, exp
import matplotlib.pyplot as plt

def cria_lut() -> [[]]:
    lut = []
    n = 1
    while True:
        lut.append([n, ((2**(-n) + 1)), log((2**(-n))+1)])
        n += 1
        if ((2**(-n) + 1) == 1):
            break
    return lut

def algoritmo(x, lut):
    j = 0
    xj = x
    yj = 1
    
    while xj != 0 and j < len(lut):
        # Passo 3: Pesquisar na LUT o maior valor k tal que xj - k >= 0
        linha = lut[j]
        if xj - linha[2] >= 0:
            max_k = linha[2]
            xj = xj - max_k # Fazer xj+1 = xj - max(kLUT) para k <= xj
            yj = yj * linha[1] # Multiplicar o valor yj pelo valor e^k correspondente

        j += 1

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
    print(valores_aproximados)
    print(valores_exatos)
    print(erros)
    vetLegenda = [i/100 for i in range(0, 100,3)]
    plt.plot(vetLegenda, erros) 
    plt.show()