piece_or = 0
while piece_or < 100:
    piece_or = piece_or + 7
    print(f"Pièces ramassées : {piece_or}")

print(f"Objectif atteint avec {piece_or} pièces !")

if piece_or >= 100: 
    difference = piece_or - 100
    print(f"Tu en as même ramassé {difference} de plus que prévu!")

"""
L'énoncé ne demandait pas spécialement la différence, mais j'ai trouvé sympa de l'ajouter
"""