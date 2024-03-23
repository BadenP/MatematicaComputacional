from IEEE754 import Dec2IEEE
def newtonRaphson(num, epsilon):
    xk = 1.0
    k = 1
    while True:
        fx = xk * xk - num.x 
        fxp = xk + xk
        xk_1 = xk - fx / fxp 
        print("#{}\t[xk]: {:.20f}\t[xk+1]: {:.20f}".format(k, xk, xk_1))

        if abs(xk_1 - xk) <= epsilon:
            break

        xk = xk_1
        k += 1
    return xk_1

def main():
    epsilon = 1e-15

    num = Dec2IEEE(3.3) 
    
    resultado = newtonRaphson(num, epsilon=epsilon) #calculates the square root

    print("O valor aproximado para a raíz quadrada de " + str(round(num.x, 3)) + " é "
            + str(resultado) + ".")

main()