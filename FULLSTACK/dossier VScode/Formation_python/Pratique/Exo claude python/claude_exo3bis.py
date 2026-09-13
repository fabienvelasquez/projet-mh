countdown = 10

while countdown > 0:
    countdown = countdown - 1
    print(countdown)
print(f"Boom ! 💥")

"""
correction : dans ma réponse, j'ai diminuer avant d'afficher, alors qu'il fallait 
faire l'inverse
"""

countdown = 10
while countdown > 0:
    print(countdown)              # d'abord on affiche
    countdown = countdown - 1    # puis on diminue

print("Boom ! 💥")