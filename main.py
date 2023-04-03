import re
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

entries = ["", ""]

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)


# fonction pour vérifier si le mot de passe créer par l'utilisateur est conforme au critères demandés.
def password_validation(password):
    # Au moins 8 caractères
    if len(password) < 8:
        return False
    # Au moins une lettre majuscule
    if not re.search(r'[A-Z]', password):
        return False
    # Au moins une lettre minuscule
    if not re.search(r'[a-z]', password):
        return False
    # Au moins un chiffre
    if not re.search(r'\d', password):
        return False
    # Au moins un caractère spécial
    if not re.search(r'[!@#$%^&*]', password):
        return False
    return True

# Demande à l'utilisateur de choisir un mot de passe et vérifie s'il est valide
while True:
    password = input("Ou bien choisissez votre mot de passe : ")
    if password_validation(password):
        print("Mot de passe valide!")
        break
    else:
        print("Mot de passe invalide. Veuillez choisir un mot de passe contenant au moins 8 caractères, une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial (!, @, #, $, %, ^, &, *).")


# Création de condition pour vérifier si le mot de passe est conforme au critères demandés.
def check_entries(password):
    global entries
    conditions = [False]*4
    specialChar = "&é'(-è_çà)=~#}{[|`\^@]+^¨$£%*µ!§:/;.,?<>²°"
    while True:
        # Check if password is valid
        if len(entries[1].get()) >= 8:
            for char in entries[1].get():
                if char.isupper():
                    conditions[0] = True
                if char.islower():
                    conditions[1] = True
                if char.isalnum():
                    conditions[2] = True
                if char in specialChar:
                    conditions[3] = True
                if all(conditions):
                    return True
            if all(conditions) == False:
                print(text="Upper, lower, num, special char needed")
                return False

# Création du boucle pour générer plusieurs mot de passe aléatoire dont un hashé par sha256.
while True :
    if check_entries(password) == True:
        password = input("Voici quelques mot de passe générés aléatoirement pour vous. ")
        print("Mot de passe valide!")
        break
    else:
        print("Mot de passe invalide. Veuillez choisir un mot de passe contenant au moins 8 caractères, une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial (!, @, #, $, %, ^, &, *).")
        break

