
import tkinter as tk
from tkinter import messagebox
import random
import string
import json
from hashlib import sha256

# créer une instance de la classe sha256
h = sha256()
# ensuite, on peut mettre à jour l'objet hashage avec la méthode de MàJ update()
h.update(b'tryhashthischar')
# utilisez la méthode hexdigest() pour obtenir le condensé de la chaîne transmise à la méthode update() :
hash = h.hexdigest()
# Enfin, on peut afficher le résultat
print(hash)

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

upper, lower, nums, syms = True, True, True, True

all = string.ascii_letters + string.digits + string.punctuation

if upper:
    all += string.ascii_uppercase
if lower:
    all += string.ascii_lowercase
if nums:
    all += string.digits
if syms:
    all += string.punctuation

length = 18
amount = 10

seed = "M1sterP4uL"
random.seed(seed) 

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)



# Création du boucle pour cééer un nom d'utilisateur et un mot de passe soi même pour qu'il soit enregistré dans un fichier json.
menu = ""
while menu != '1' or menu != '2':
    menu = input("Souhaitez-vous enregistrer un nouveau mot de passe ou voir vos anciens  ? ")
    
    if menu == '1':
        user_entry = input("Entrez votre nom d'utilisateur: ")
        password_entry = input("Entrez votre mot de passe: ")
        psswd_dict = {user_entry}
        with open("SecurePasswdData.json", "a") as write_file:
            data = json.load(write_file)  

        print(data)
    if menu != '2':
        with open("SecurePasswdData.json", "w") as write_file:
            data = json.load(write_file)

        print(data)
        
    if menu == '3':
        exit() 


# ----------------------------SAVE PASSWORD------------------------------- #
def save():
    user_entry = user_entry.get()
    password_entry = password_entry.get()
    if len (user_entry) == 0 or len(password_entry) == 0:
        print(title="Error", message="Veuillez remplir tous les champs.")
    else:
        confirmation_mssg = messagebox.askokcancel(title="Confirmation", message="Votre mot de passe est valide. Il peut donc être pris en compte.\n")


# ----------------------------UI SETUP------------------------------- #

root = tk.Tk()
root.resizable(False, False)
root.title("Password Manager")
root.geometry("650x300")

RegisterFrame = tk.Frame(root)
RegisterFrame.grid(row=0, column=0, padx=25, pady=25)


home_label = tk.LabelFrame(RegisterFrame, text="Password Manager", font=("Arial", 20))
home_label.grid(row=0, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0)

user_entry = tk.Entry(root)
user_entry.grid(row=1, column=1, pady=10, padx=10)

message_label = tk.Label(root, text="", font=("Arial", 10))
message_label.grid(row=1, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1, pady=10, padx=10)

confirmation_messg = tk.Label(root)
confirmation_messg.grid(row=2, column=0, columnspan=2, pady=10)

show_current_password = tk.Button(root, text="Show")
show_current_password.grid(row=0, column=2)

add_button = tk.Button(root, text="Add", command=save())
add_button.grid(row=0, column=3)

show_button = tk.Button(root, text="Show Passwords")
show_button.grid(row=2, column=0)

clear_button = tk.Button(root, text="Clear Passwords")
clear_button.grid(row=2, column=1)


password_list = tk.Listbox(root, width=100)
password_list.grid(row=1, column=0, columnspan=10, padx=20)


root.mainloop()