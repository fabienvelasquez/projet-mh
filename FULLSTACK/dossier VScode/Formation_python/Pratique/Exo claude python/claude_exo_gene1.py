name = input(f"Bonjour étrangé, quel est ton prénom ?")
repas = int(input("Combien fais-tu de repas par jour ?"))
calorie = int(input("Combien de calories par repas ?"))
total_calorie = repas * calorie
print(f"Bonjour {name}, tu vas manger {repas} de {calorie} calories. Cela représente un total de {total_calorie} aujourd'hui !")
if total_calorie >= 2000:
    print(f"Il faudra penser à faire du sport ensuite {name}")
elif total_calorie <= 1200:
    print(f"Seulement {calorie} ? C'est bien trop peu {name}, tu devrais manger un peu plus")
else:
    print(f" C'est très bien ! {calorie} est un chiffre dans la norme {name}, tu peux être fier !")