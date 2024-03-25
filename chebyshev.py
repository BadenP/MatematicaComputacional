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
    T0 = 1
    T2 = 2*y - 1
    T4 = y*(8*y-8) + 1
    T6 = y*(y*(32*y - 48) + 18) - 1
    T8 = y*(y*(y*(128*y - 256) + 160) - 32) + 1
    T10 = y*(y*(y*(y*(512*y - 1280) + 1120) - 400) + 50) - 1
    T12 = y*(y*(y*(y*(y*(2048*y - 6144)) + 6912) - 3584) + 840) - 72 + 1
    T14 = y*(y*(y*(y*(y*(y*(8192*y - 28672)) + 39424) - 26880) + 9408) - 1568) + 98 - 1

    T0COS = T0
    T2COS = 1/2 * (T0 + T2)
    T4COS = 1/8 * (3*T0 + 4*T2 + T4)
    T6COS = 1/32 * (10*T0 + 15*T2 + 6*T4 + T6)
    T8COS = 1/128 * (35*T0 + 56*T2 + 28*T4 + 8*T6 + T8)
    T10COS = 1/512 * (126*T0 + 210*T2 + 120*T4 + 45*T6 + 10*T8 + T10)
    T12COS = 1/2048 * (462*T0 + 792*T2 + 495*T4 + 220*T6 + 66*T8 + 12*T10 + T12)
    T14COS = 1/8192 * (1716*T0 + 3003*T2 + 2002*T4 + 1001*T6 + 364*T8 + 91*T10 + 14*T12 + T14)

    #return T0COS - T2COS/2 + T4COS/24 - T6COS/720 + T8COS/40320 - T10COS/3628800 + T12COS/479001600
    MONICO12 = T12 / (2 ** 11)
    MONICO14 = T14 / (2 ** 13)
    z = y**2
    return 1 - y/2 + z/24 - z*y/720 + z*z/40320 - z*z*y/3628800 + z*z*z/479001600 -z*z*z*y/87178291200 - MONICO14/87178291200

def seno(x):
    y = x**2
    T1 = x
    T3 = x*(4*y - 3)
    T5 = x*((y*(16*y - 20)) + 5)
    T7 = x*((y*(y*(64*y - 112)) + 56) - 7)
    T9 = x*((y*(y*(y*(256*y - 576)) + 432) - 120) + 9)
    T11 = x*((y*(y*(y*(y*(1024*y - 2816)) + 2816) - 1232) + 220) - 11)
    T13 = x*((y*(y*(y*(y*(y*(4096*y - 13312)) + 16640) - 9984) + 2912) - 364) + 13)
    T1SENO = T1
    T3SENO = 1/4 * (3*T1 + T3)
    T5SENO = 1/16 * (10*T1 + 5*T3 + T5)
    T7SENO = 1/64 * (35*T1 + 21*T3 + 7*T5 + T7)
    T9SENO = 1/256 * (126*T1 + 84*T3 + 36*T5 + 9*T7 + T9)
    T11SENO = 1/1024 * (462*T1 + 330*T3 + 165*T5 + 55*T7 + 11*T9 + T11)
    T13SENO = 1/4096 * (1716*T1 + 1287*T3 + 715*T5 + 286*T7 + 78*T9 + 13*T11 + T13)

    #return T1SENO - T3SENO/6 + T5SENO/120 - T7SENO/5040 + T9SENO/362880 - T11SENO/39916800
    MONICO11 = T11 / (2 ** 10)
    MONICO13 = T13 / (2 ** 12)
    z = y**2
    return x - (y*x)/6 + (z*x)/120 - (z*y*x)/5040  + (z*z*x)/362880 - (z*z*y*x)/39916800 +(z*z*z*x)/6227020800 - MONICO13/6227020800

def angulo_correspondente(k):
    # Calcular o ângulo correspondente em radianos
    angulo_radianos = k * np.pi / 2

    # Reduzir o ângulo para o intervalo entre 0 e 2π
    angulo_radianos = angulo_radianos % (2 * np.pi)

    # Converter o ângulo para graus
    angulo_graus = np.degrees(angulo_radianos)

    # Retornar o ângulo correspondente
    return angulo_graus

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

    print("arg: ", arg)
    return arg, k


def reducao_aditiva_seno(x):
   
    c = np.pi / 2
    xmax = 3 * np.pi / 4
    xmin = np.pi / 4
    k = math.ceil((x - xmax) / c)
    arg = x - (k * c)

    if arg > xmax:
        arg = reducao_aditiva(arg)[0]
    elif arg < xmin:
        arg = reducao_aditiva(arg)[0]

 
    return arg, k

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
    #plt.subplot(1, 2, 1)
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
    plt.ylabel('Cosseno')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x_degrees, math_cos_values, label='Math', color='orange')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Seno')
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
    plt.ylabel('Cosseno')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x_degrees, math_sin_values, label='Math')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Seno')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    gerarResultadosErro()





     