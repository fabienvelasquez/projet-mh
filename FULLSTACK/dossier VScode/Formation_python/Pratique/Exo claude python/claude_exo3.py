pv_monstre = 50
degats_attaque = 12
nombre_attack = 0
for attack in range(1,5):
    pv_monstre = pv_monstre - degats_attaque
    nombre_attack = nombre_attack + 1
    print(f"Attaque n°{attack}, il reste {pv_monstre} PV au monstre")

while pv_monstre > 0:
    pv_monstre = pv_monstre - degats_attaque
    nombre_attack = nombre_attack + 1

if pv_monstre <= 0:
    print(f"Le monstre est vaincu en {nombre_attack} attaques !")
    print("Victoire!")

#correction, il ne fallait utiliser que While dans l'énoncé

pv_monstre = 50
degats_attaque = 12
nombre_attack = 0

while pv_monstre > 0:
    pv_monstre = pv_monstre - degats_attaque
    nombre_attack = nombre_attack + 1
    print(f"Attaque n°{nombre_attack}, il reste {pv_monstre} PV au monstre")

print(f"Le monstre est vaincu en {nombre_attack} attaques !")