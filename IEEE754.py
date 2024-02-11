from ctypes import Structure, Union, c_float, c_uint32, c_uint8
import math

class struct (Structure):
    _fields_ = [("f", c_uint32, 23),
                ("e", c_uint32,  8),
                ("s", c_uint32,  1),
               ]

class IEEE754 (Union):
    _fields_ = [("x", c_float),
                ("Fbits", struct)
               ]

def Dec2IEEE(v):  # v deve ser um float
    y = IEEE754()
    y.x = v
    return y

# para usar a estrutura da IEEE fa�a
z = 3.125
num = Dec2IEEE(z)   #campos na IEEE754
#       num.Fbits.s  sinal da mantissa
#       num.Fbits.f  fra��o da mantissa (0.xxxxxx)
#       num.Fbits.e  exponte enviesado por 127
#print(num.Fbits.s)
#print(num.Fbits.f)
#print(num.Fbits.e)
