from tkinter import *
import customtkinter
from random import *

#Déclaration des variables.
root = customtkinter.CTk()
# avaible color list 
color_list = ["red", "blue", "purple", "green", "black", "white"]
attempt_remaining = 10
# number of row and columns
row = 11
col= 4

button= []
button_counter=0
good_placement_labels= []
wrong_placement_labels = []

code_list = []
for i in range(4):
	code_list.append(color_list[randrange(6)])

for i in range(row):
    for x in range(col):
        # creation of a button that run button_color_loop when clicked
        button.append(customtkinter.CTkButton(root, text=" ",fg_color="blue",hover_color="blue",  command=lambda button_index=button_counter: button_color_loop(button[button_index])))
        # place buttons on a grid
        button[button_counter].grid(row= i, column =x+2, padx= 2, pady = 5)
        button_counter += 1
	
for i in range(4):
	button[i].configure(fg_color="grey", text="?", text_color= "black")


def button_color_loop(Button):
    # change the color of the button depending of his actual color
    Button.configure(hover_color =color_list[color_list.index(Button.cget("hover_color"))-len(color_list)+1], fg_color=color_list[color_list.index(Button.cget("fg_color"))-len(color_list)+1])

def color_test(code_list, color_input_list): #Fonction de test de l'égalité entre la liste des couleur du joueur et celle défini aléatoirement au debut.
	good_placement = 0
	wrong_placement = 0
	color_tested=[]
	for i in range(4): #Test égalité couleur par couleur entre les deux liste de couleur utilisateur et défini aléatoirement.
		if code_list[i] == color_input_list[i]:
			good_placement += 1
			print("b")
		elif color_input_list[i] in code_list:
			wrong_placement += 1
			print(i)
	if good_placement == 4:
		print("win")
		exit()
	good_placement_text="there is ",good_placement, " good placement"
	good_placement_labels.append(customtkinter.CTkLabel(root, text=good_placement_text))
	good_placement_labels[10-attempt_remaining].grid(row = attempt_remaining, column=0)
	wrong_placement_text="there is ",wrong_placement, " wrong placement"
	wrong_placement_labels.append(customtkinter.CTkLabel(root, text=wrong_placement_text, padx = 50))
	wrong_placement_labels[10-attempt_remaining].grid(row = attempt_remaining, column=1)
	next_try()

def activate_line(line):
	for i in range(44):
		button[i].configure(state="disabled")
	for i in range(4):
	    button[line*4+i].configure(state="normal")


def next_try():
	global attempt_remaining
	attempt_remaining = attempt_remaining-1
	submit_button.grid(row=attempt_remaining)
	activate_line(attempt_remaining)
	



submit_button= customtkinter.CTkButton(root, text="Submit", command= lambda: color_test(code_list, [button[attempt_remaining*4].cget("fg_color"),button[attempt_remaining*4+1].cget("fg_color"),button[attempt_remaining*4+2].cget("fg_color"),button[attempt_remaining*4+3].cget("fg_color")]))
submit_button.grid(row=10,column=7, padx = 20)
print(code_list)
activate_line(10)
root.mainloop()


