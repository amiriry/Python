import sympy as smp
from sympy import *

n = smp.symbols('n')
print(smp.sin(1/n))
print(smp.limit(smp.sin(1/n**2), n, smp.pi))
