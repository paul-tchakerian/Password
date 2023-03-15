import random
import hashlib
from tkinter import messagebox
import json


while True:
    Passwd = input("Enter your password: ")



def GeneratePasswd():
    """Génération de mot de passe aléatoire avec une longueur donnéé en cours..."""
    characters = string.asscii_letters + string.digits + string.punctuation
    Passwd = "".join(random.choice(characters) for i in range(8))
    return Passwd


def add_password(Passwd):
    """Ajout d'un mot de passe dans le fichier json"""
    Passwd = Passwd_entry.get()
    if not check_password(Passwd):
        messagebox.showerror("Syntaxe incorrecte", "Le mot de passe doit contenir au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial")
        return
    PasswdHash = HashPassword(Passwd)


def HashPassword(Passwd):
    PasswdHash = hashlib.sha256(Passwd.encode()).hexdigest()
    
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

    except:
        data = {}

    if PasswdHash in data:
        messagebox.showwarning("Mot de passe déjà utilisé", "Ce mot de passe a déjà été utilisé")
    else:
        messagebox.showinfo("Mot de passe ajouté", "Le mot de passe a été ajouté avec succès")
        data[PasswdHash] = Passwd

    with open("passwords.json", "w") as file:
        json.dump(data, file)

    print("Mot de passe :")
    Passwd_Str = "\n".join([f"{key} : {value}" for key, value in data.items()])
    print(Passwd_Str)
    show()  



def CheckPasswd(Passwd):
    Has_uppercase = False
    Has_lowercase = False
    Has_digit = False
    Has_special = False

    if len(Passwd) < 8:
        return False
        print("Password must be at least 8 characters long")
        for char in Passwd:
            if char.isupper():
                has_uppercase = True
            if char.islower():
                has_lowercase = True
            if char.isdigit():
                has_digit = True
            if char in "!@#$%^&*()_+-=":
                has_special = True
        



    def show():
        on_clear()
        
        with open("passwords.json", "r") as file:
            data = file.read()
            password_list.insert(tk.END, data)
    



def ShowPasswd():
    global password_show
    password_show = not password_show
    password_entry.configure(show="" if password_show else "*")


root = tk.Tk()
root.resizable(False, False)
root.title("Password Manager")
root.geometry("650x300")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1, pady=20)

show_current_password = tk.Button(root, text="Show", command=show_password)
show_current_password.grid(row=0, column=2)

add_button = tk.Button(root, text="Add Password", command=add)
add_button.grid(row=0, column=3)

show_button = tk.Button(root, text="Show Passwords", command=show)
show_button.grid(row=2, column=0)

clear_button = tk.Button(root, text="Clear Passwords", command=on_clear)
clear_button.grid(row=2, column=1)

clear_json = tk.Button(root, text="Deleted all saved password", command=clear_json)
clear_json.grid(row=2, column=4)

password_list = tk.Listbox(root, width=100)
password_list.grid(row=1, column=0, columnspan=10, padx=20)

show()
root.mainloop()