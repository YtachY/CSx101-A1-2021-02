#!/usr/bin/python3

from decimal import *

psi = input()

psi = float(psi)

result = psi * 0.453592 / pow(2.54, 2)


getcontext().prec = 6
print(Decimal(result).normalize())