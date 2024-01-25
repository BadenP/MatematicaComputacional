from IEEE754 import Dec2IEEE
from math import sqrt

raiz_dois = 1.414213562

x = Dec2IEEE(3.125)
y = Dec2IEEE(5)
a = Dec2IEEE(3.125)

def ehPar(n):
    if n&1:
        return False
    return True

def raiz_aproximada(f):
    return (1 + (f/2)) * (1 - (f / (4 + 2 * f)))

def raiz(x):
    y = Dec2IEEE(x)
    expoente = y.Fbits.e - 127
    f = y.Fbits.f - int(y.Fbits.f)
    if ehPar(expoente):
        print("f = ", int(y.Fbits.f))
        print("raiz = ", raiz_aproximada(f))
        return (2**(expoente>>1)) * raiz_aproximada(f)
    else:
        print("f = ", int(y.Fbits.f))
        print("raiz = ", raiz_aproximada(f))
        return 2**((expoente-1)>>1) * raiz_dois * raiz_aproximada(f)

valores_aproximados = []
valores_exatos = []
erros = []

def calculoRaizes():
    for i in range(0,5,0.05):
        valores_aproximados.append(raiz(i))
        valores_exatos.append(raiz(i))

print(raiz(3.6))


