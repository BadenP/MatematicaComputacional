import math

# Função para reduzir o argumento do ângulo para o intervalo [-π/2, π/2]
def reduce_angle(angle):
    # Reduzir para o intervalo [-π, π]
    angle = math.fmod(angle, 2 * math.pi)

    # Reduzir para o intervalo [-π/2, π/2]
    if angle > math.pi / 2:
        angle = math.pi - angle
    elif angle < -math.pi / 2:
        angle = -math.pi - angle

    return angle

# Função para calcular seno usando polinômios de Chebyshev
def chebyshev_sine(x, n_terms=10):
    x = reduce_angle(x)
    result = 0.0

    for n in range(n_terms):
        coefficient = (-1) ** n
        term = coefficient * math.sin((2 * n + 1) * x) / math.factorial(2 * n + 1)
        result += term

    return result

# Função para calcular cosseno usando polinômios de Chebyshev
def chebyshev_cosine(x, n_terms=10):
    x = reduce_angle(x)
    result = 0.0

    for n in range(n_terms):
        term = math.cos(n * x)
        result += term

    return result

def T(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return 2 * x * T(n - 1, x) - T(n - 2, x)
    
def P(n, x, A):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return P(n + 1, x, A) - (1/A) * T(n, x)

# Exemplo de uso
angulo = 1.5708  # Em radianos (90 graus)
seno_calculado = chebyshev_sine(angulo)
cosseno_calculado = chebyshev_cosine(angulo)

print(f"Ângulo original: {angulo} rad")
print(f"Seno calculado: {seno_calculado}")
print(f"Cosseno calculado: {cosseno_calculado}")
