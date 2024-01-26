from math import ceil, log, exp
from IEEE754 import Dec2IEEE
import matplotlib.pyplot as plt

ln2 = log(2)

# Objetivo: cálculo de e^x reduzindo o valor do argumento
# e^x = 2^n * (e^r)^256

def exponencial(x):
    #verificar se x<0
    # verificar x par ou x impar
    n = ceil((x - (ln2/2))/ln2) # deixar como constantes
    r = (x - (n * ln2)) / 256
    expr = 1 + r * (1 + r * (0.5 + r * (0.16666666666666666 + (0.041666666666666664 * r))))
    expx = pow(2,n) * pow(expr,256) # soma do expoente com n
    return expx

argumentos = []
corretos = []
aproximados = []
erros = []

for i in range(0,100,3):
    i /= 10
    arg = round(i, 2)
    aproximado = exponencial(arg)
    correto = exp(arg)
    argumentos.append(arg)
    corretos.append(correto)
    erros.append(abs(correto - aproximado))
    aproximados.append(aproximado)

# Criando a tabela
print(f"{'Argumento':<10}{'Valor Correto':<15}{'Erro':<10}{'Valor Aproximado':<20}")
print("-" * 55)
for i in range(len(argumentos)):
    print(f"{argumentos[i]:<10}{corretos[i]:<15.8f}{erros[i]:<20.16f}{aproximados[i]:<30.8f}")

# Plotando o gráfico
plt.plot(argumentos, erros, label='Erro')
plt.title('Análise de Erros da Aproximação de Balley')
plt.xlabel('Argumento')
plt.ylabel('Erro')
plt.legend()
plt.grid(True)
plt.show()