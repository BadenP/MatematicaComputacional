from IEEE754 import Dec2IEEE
from math import log

def cria_lut() -> [[]]:
    lut = []
    n = -1
    while True:
        lut.append([((2**n + 1)), log(2**n)])
        n -= 1
        if ((2**n + 1) == 1):
            break
    print(lut)
    return lut


if __name__ == "__main__":
    lut = cria_lut()
    x = Dec2IEEE(3.6)
