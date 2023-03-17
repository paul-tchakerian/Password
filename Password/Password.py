
import hashlib
import tkinter as tk
from tkinter import messagebox
import json
from json import *
import string
import secrets

entries = ["",""]
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = string.ascii_letters + string.digits + string.punctuation


psswd_length = '' 
with open("password.json") as file:
    register = load( file)

def GeneratePasswd():
    psswd =''
    for i in range(psswd_length):
        psswd += ''.join(secrets.choice(alphabet))
    
    print(psswd)
    
    while True:
        psswd = ''
        for i in range(psswd_length):
            psswd += ''.join(secrets.choice(alphabet))
    
        if (any(char in special_chars for char in psswd) and
            sum(char.isdigit for char in psswd) >= 3):
                break

        print(psswd)

    

"""Ajout d'un mot de passe dans le fichier json"""
def add_password():          
    global Passwd
    global entries
    user_entry = entries[0].get()
    
    if CheckPasswd():
        password = hashlib.sha256(Passwd.encode()).hexdigest()
    if user_entry in register:
        if password in register[user_entry] ["Hashes 256"]:
            message_label.configure(text= f"Désolé , le mot de passe {user_entry} déjà utilisé", fg="purple")
        else:
            message_label.configure(text= f"Mot de passe incorrect", fg="red")
    

def HashPassword():
    global Passwd
    global entries
    user_entry = entries[0].get()
    PasswdHash = hashlib.sha256(Passwd.encode()).hexdigest()
    
    if CheckPasswd() and user_entry in register and entries[1].get() not in register[user_entry]["Hashes 256"]:
        register[user_entry]["Hashes 256"].append(PasswdHash)
        json_update()
        message_label.configure(text= "Mot de passe ajouté avec succès !", fg="green")
    else:
        message_label.configure(text= "Aucun mot de passe  n'est relié à ce compte", fg="red", bg="black")




def CheckPasswd():
    global Passwd
    conditions = [False] * 4
    message_label.config(text="")
    
    # Vérifie si le mot de passe est valide
    if len(Passwd[0].get()) >= 8:    
        print("Password must be at least 8 characters long")
        
        for char in Passwd[0].get():
            if char.isupper():
                conditions[0] = True
            if char.islower():
                conditions[1] = True
            if char.isdigit():
                conditions[2] = True
            if char in "!@#$%^&*()_+-=":
                conditions[3] = True
            if all(conditions):
                return True
        if not all (conditions):
            message_label.configure(text="Supérieur, inférieur, chiffre et un caractère spécial sont requis", fg="red")
            return False
    else:
        if len(entries) < 8:
            message_label.configure(text="Le mot de passe doit contenir au moins 8 caractères", fg="red")
            return False
        else:
            message_label.configure(text="Mot de passe invalide", fg="red")
            return False

    
def clear_entries():
    entries[0].delete(0, tk.END)
    entries[1].delete(0, tk.END)



def ShowPasswd():
    global Passwd
    password_show = not password_show
    password_entry.configure(show="" if password_show else "*")
    for password in entries:
        password.configure(show="" if password_show else "*")
        
    if user_entry in register:
        mini_win = tk.Toplevel()
        mini_win.geometry("200x200")
        mini_win.title(f"{user_entry}'s passwords list")
        userLabel = tk.Label(mini_win, text=f"{user_entry}", font=("Helvetica", 12))
        userLabel.pack(expand=True, fill="both")


        pass_wd_list = tk.Listbox(mini_win)
        i = 1
        for password in register[user_entry]["Hashes 256"]:
            pass_wd_list.insert(i, password)
            i += 1
        pass_wd_list.pack(expand=True, fill="both")
    else:
        message_label.configure(text="Aucun utilisateur et mot de passe n'est relié à ce compte", fg="red", bg="black")

def clear_json():
    confirmed = messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer tous les mots de passe ?")
    if confirmed:
        try:
            with open("passwords.json", "w") as file:
                file.write("{}")
                messagebox.showinfo("Suppression réussie", "le fichier a été supprimé avec succès")
        except IOError as e:
            messagebox.showwarning("Erreur", f"Une erreur s'est produite lors de l'effacement du fichier :\n{str(e)}")


def json_update():
    with open("password.json", "w") as rg:
        json.dump(register, rg, indent=4, separators=(",", ": "))

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
entries[1] = user_entry

show_current_password = tk.Button(root, text="Show", command=ShowPasswd)
show_current_password.grid(row=0, column=2)

add_button = tk.Button(root, text="Add Password")
add_button.grid(row=0, column=3)

show_button = tk.Button(root, text="Show Passwords", command=ShowPasswd)
show_button.grid(row=2, column=0)

clear_button = tk.Button(root, text="Clear Passwords", command=clear_entries)
clear_button.grid(row=2, column=1)


password_list = tk.Listbox(root, width=100)
password_list.grid(row=1, column=0, columnspan=10, padx=20)


root.mainloop()
