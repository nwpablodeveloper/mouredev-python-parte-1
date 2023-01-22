### Modules ####

import my_module
from my_module import sumValues, printValue

print("====================")

my_module.sumValues(3, 5, 7)
my_module.printValue("Hola print")

print("====================")

sumValues(3, 5, 7)
printValue("Hola print")

print("====================")

import math
from math import pi as pi_personalizado

print(math.pi)
print(math.pow(2, 10))
print(pi_personalizado)


print("\n")