levelup = 1
for levelup in range(0,5):
    levelup = levelup + 1
    print(f"Niveau {levelup} débloqué !")


if levelup >= 5:
    print(f"Vous pouvez vous rendre dans la forêt sombre")

"""
Correction : je peux simplifier le bloc de code, sans 
forcément avoir besoin d'ajouter "levelup = levelup + 1"
en faisait partir de range(1, 6) plutôt que range(0,5)
"""

for levelup in range(1, 6):  # commence à 1, s'arrête avant 6
    print(f"Niveau {levelup} débloqué !")

if levelup >= 5:
    print("Vous pouvez vous rendre dans la forêt sombre")