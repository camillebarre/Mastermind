#Camille & Yann 2023, all rights reserved.

from random import *

#Déclaration des variables.

color_list = ["red", "blue", "purple", "green", "black", "white"]
attempt_remaining = 10
color_input_list = []
win = False


#Déclaration des fonctions.

def color_test(code_list, color_input_list): #Fonction de test de l'égalité entre la liste des couleur du joueur et celle défini aléatoirement au debut.
	good_placement = 0
	wrong_placement = 0
	list_placement = []
	for i in range(4): #Test égalité couleur par couleur entre les deux liste de couleur utilisateur et défini aléatoirement.
		if color_input_list[i] in code_list and color_input_list[i] != code_list[i]:
			wrong_placement += 1
		elif code_list[i] == color_input_list[i]:
			good_placement += 1
	list_placement.append(good_placement)
	list_placement.append(wrong_placement)
	return list_placement

def random_color_code(): #Fonction de génération aléatoire d'une combinaison de quatres couleurs.
	code_list = []
	for i in range(4):
		code_list.append(color_list[randrange(6)])
	return code_list

#Programme principal.

code_list = random_color_code()
print(code_list)
while attempt_remaining != 0 and win != True:
	if attempt_remaining != 10 or attempt_remaining == 0:
		print("_______________________________________________________________________")
		print("Essaies restants : ", attempt_remaining)
		print("Nombre de couleurs bien placée(s) : ", list_placement[0])
		print("Nombre de couleurs mal placée(s) : ", list_placement[1])

	print("Entrez une couleur parmis ", color_list)

	for i in range(4):
		color_choice = "none"
		while color_choice not in color_list:
			color_choice = input("Couleur :")
		color_input_list.append(color_choice)

	list_placement = color_test(code_list,color_input_list)
	color_input_list.clear()
	if list_placement[0] == 4:
		win = True

	attempt_remaining -= 1

if attempt_remaining == 0:
	print("GAME OVER")
	print("Le bon code était : ", code_list)
else:
	print("Vous avez gagné en ", 10 - attempt_remaining, " éssais.")