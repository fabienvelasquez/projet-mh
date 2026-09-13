#ici, on apprend les variables.

nom_personnage = "Kinta"
niveau = 1
mana = 100.0
cout_mana_feu_1 = 15.0
est_en_vie = True
lancer_sort_feu = mana - cout_mana_feu_1

print(f"""Bonjour {nom_personnage}, tu es niveau {niveau}
et dispose de {mana} point de manas""")

print(lancer_sort_feu)