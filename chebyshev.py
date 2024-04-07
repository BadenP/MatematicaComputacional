import math
import numpy as np
import matplotlib.pyplot as plt


''' 
MATEMÁTICA COMPUTACIONAL (6900/1)
MÉTODO PARA CÁLCULO DO SENO E COSSENO UTILIZANDO POLINÔMIOS DE CHEBYSHEV

Professor Dr. Airton Marco Polidório

Discentes:
Luca Mattosinho Teixeira RA 124316
Paula Fernandes Torres RA 123565 
'''


# Coeficientes de Chebyshev usados para calcular seno e cosseno
# Os polinômios foram calculados utilizando o método multiplicativo de Horner

def cosseno(x):
    y = x**2
    T12 = y*(y*(y*(y*(y*(2048*y - 6144)) + 6912) - 3584) + 840) - 72 + 1
    MONICO12 = T12 / (2 ** 11)
    z = y**2

    # Polinômio econômico para cosseno
    return 1 - y/2 + z/24 - z*y/720 + z*z/40320 - z*z*y/3628800 + z*z*z/479001600 - MONICO12/479001600

def seno(x):
    y = x**2
    T13 = x*((y*(y*(y*(y*(y*(4096*y - 13312)) + 16640) - 9984) + 2912) - 364) + 13)
    MONICO13 = T13 / (2 ** 12)
    z = y**2

    # Polinômio econômico para seno
    return x - (y*x)/6 + (z*x)/120 - (z*y*x)/5040  + (z*z*x)/362880 - (z*z*y*x)/39916800 +(z*z*z*x)/6227020800 - MONICO13/6227020800

def angulo_correspondente(k):

    # Calcular o ângulo correspondente em radianos
    angulo_radianos = k * np.pi / 2

    # Reduzir o ângulo para o intervalo entre 0 e 2π
    angulo_radianos = angulo_radianos % (2 * np.pi)
    angulo_graus = np.degrees(angulo_radianos)

    return angulo_graus

# Reduzir o ângulo para o intervalo entre -π/4 e π/4
def reducao_aditiva(x):
   
    c = np.pi / 2
    xmax = np.pi / 4
    xmin = -np.pi / 4
    k = math.ceil((x - xmax) / c)
    arg = x - (k * c)

    if arg > xmax:
        arg = reducao_aditiva(arg)[0]
    elif arg < xmin:
        arg = reducao_aditiva(arg)[0]

    return arg, k

# Calcular seno e cosseno
def calcular(x):

    arg = reducao_aditiva(x)[0]
    k = reducao_aditiva(x)[1]

    cosarg = cosseno(arg)
    senoarg = seno(arg)

    if angulo_correspondente(k) == 90:
        senx = cosarg
        cosx = -senoarg
    elif angulo_correspondente(k) == 180:
        cosx = -cosarg
        senx = -senoarg
    elif angulo_correspondente(k) == 270:
        senx = -cosarg
        cosx = senoarg
    elif angulo_correspondente(k) == 0:
        cosx = cosarg
        senx = senoarg

    return senx, cosx

# Gerar gráficos de erro e comparação entre seno e cosseno
def gerarResultadosErro():
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    cheb_cos_values = [calcular(angle)[1] for angle in x]
    cheb_sin_values = [calcular(angle)[0] for angle in x]
    math_cos_values = [math.cos(angle) for angle in x]
    math_sin_values = [math.sin(angle) for angle in x]
    cos_error = [abs(cheb - math) for cheb, math in zip(cheb_cos_values, math_cos_values)]
    sin_error = [abs(cheb - math) for cheb, math in zip(cheb_sin_values, math_sin_values)]
    x_degrees = np.degrees(x)
    plt.figure(figsize=(10, 5))
    plt.plot(x_degrees, cos_error, label='Erro Cosseno', color='blue')
    plt.plot(x_degrees, sin_error, label='Erro Seno', color='orange')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Erro')
    plt.legend()
    plt.show()
    x = np.linspace((-2)*np.pi, 2*np.pi, 1000)
    cheb_cos_values = [calcular(angle)[1] for angle in x]
    math_cos_values = [math.cos(angle) for angle in x]
    x_degrees = np.degrees(x)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x_degrees, cheb_cos_values, label='Chebyshev', color='blue')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Cosseno Polinômio Econômico')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x_degrees, math_cos_values, label='Math', color='green')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Cosseno Math')
    plt.legend()
    plt.show()

    x = np.linspace((-2)*np.pi, 2*np.pi, 1000)
    cheb_sin_values = [calcular(angle)[0] for angle in x]
    math_sin_values = [math.sin(angle) for angle in x]
    x_degrees = np.degrees(x)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x_degrees, cheb_sin_values, label='Chebyshev', color='blue')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Seno Polinômio Econômico')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x_degrees, math_sin_values, label='Math', color="green")
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Seno Math')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    gerarResultadosErro()





     