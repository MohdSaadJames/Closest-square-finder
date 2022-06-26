import math

number = int(input("Number to find the closest square: "))
lessapprox = int(math.sqrt(number))
greaterapprox = int(math.sqrt(number)) + 1
if number - lessapprox**2 < greaterapprox**2 - number:
    print(f"{lessapprox**2} is the closest perfect square to {number}.")
else:
    print(f"{greaterapprox**2} is the closest perfect square to {number}.")
