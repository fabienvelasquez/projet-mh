pv_monstre = 50
attack = 8
while pv_monstre > 0:
    pv_monstre = pv_monstre - attack
    print(f"Le monstre à maintenant {pv_monstre} PV!")

if pv_monstre <= 0:
    difference = -pv_monstre
    print(f"Tu lui as infligé {difference} de plus")