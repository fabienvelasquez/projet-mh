"""
Dans cet exo, on utilise la boucle for de 1 à 30 en changeant certains chiffre par des textes
 si ceux-ci sont divisibles par 3, 5 et 15, en utilisant le modulo %

schema bloc : "variable" % 3 == 0
"""

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
            print("Fizz")
    else:
        print(i)