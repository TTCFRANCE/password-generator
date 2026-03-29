import string
import random

letters_maj = string.ascii_uppercase
letters_min = string.ascii_lowercase
numbers = string.digits
puntuation = string.punctuation

password_chars = letters_maj + letters_min + numbers + puntuation
while True:
    lenght_password = int(input("Combien de caractères veux tu dans ton mot de passe ? "))

    password = "".join(random.choices(password_chars, k=lenght_password))

    print(password)