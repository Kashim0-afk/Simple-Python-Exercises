#Esercizi vari 9/12/2024


# Esercizio: Cicli (14_cicli)
x, y = 0, 10
while x != y:
    print(f"x = {x}, y = {y}")
    if x == y:
        print("x e y sono uguali")
    else:
        print("x e y sono diversi")
    x += 1
    y -= 1
print(f"x = {x}, y = {y}")
print("x e y sono uguali. Esecuzione terminata.")




# Esercizio: Fibonacci (15_fibonacci)
n = int(input("Inserisci n per la successione di Fibonacci: "))
a, b = 1, 1
print(a, b, end=" ")
for _ in range(n - 2):
    a, b = b, a + b
    print(b, end=" ")
print()




# Esercizio: Consonante o vocale (16_consonante_vocale)
lettera = input("Inserisci una lettera: ").lower()
if lettera in "aeiou":
    print(f"{lettera} è una vocale.")
elif lettera.isalpha():
    print(f"{lettera} è una consonante.")
else:
    print(f"{lettera} non è una lettera valida.")




# Esercizio: Controllo utente e password (18_controllo_utente_password)
email_salvata = "test@example.com".strip().lower()
password_salvata = "password123".strip()
email_utente = input("Inserisci la tua email: ").strip().lower()
password_utente = input("Inserisci la tua password: ").strip()
if email_utente == email_salvata and password_utente == password_salvata:
    print("Benvenuto nel programma")
else:
    print("Email o password errate")




# Esercizio: Password sicura (19_password_sicura)
import re
while True:
    password = input("Inserisci una password: ")
    if (len(password) > 8 and
        len(re.findall(r'\d', password)) >= 2 and
        len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) >= 1 and
        any(c.isupper() for c in password)):
        print("Password accettata!")
        break
    else:
        print("Password non valida, riprova.")





# Esercizio: Frase palindroma (20_frase_palindroma)
frase = input("Inserisci una frase: ").replace(" ", "").lower()
if frase == frase[::-1]:
    print("La frase è palindroma!")
else:
    print("La frase non è palindroma!")





# Esercizio: Rettangolo di asterischi (21_rettangolo_asterischi)
b = int(input("Inserisci la base numerica: "))
a = int(input("Inserisci l'altezza numerica: "))
print("Rettangolo pieno:")
for i in range(a):
    print("*" * b)
print("Rettangolo vuoto:")
for i in range(a):
    if i == 0 or i == a - 1:
        print("*" * b)
    else:
        print("*" + " " * (b - 2) + "*")





# Esercizio EXTRA: Generatore di numeri primi (extra_esercizi_loop)
n = int(input("Inserisci un numero per generare numeri primi fino a n: "))
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()





# Esercizio EXTRA: Simulatore sistema bancario (extra_esercizi_loop_2)
balance = 0
while True:
    print("\n1. Controlla saldo\n2. Deposita\n3. Preleva\n4. Esci")
    scelta = input("Scegli un'opzione: ")
    if scelta == "1":
        print(f"Saldo attuale: {balance}€")
    elif scelta == "2":
        deposito = int(input("Quanto vuoi depositare? "))
        balance += deposito
        print("Deposito effettuato.")
    elif scelta == "3":
        prelievo = int(input("Quanto vuoi prelevare? "))
        if prelievo <= balance:
            balance -= prelievo
            print("Prelievo effettuato.")
        else:
            print("Saldo insufficiente.")
    elif scelta == "4":
        print("Grazie per aver usato il sistema bancario.")
        break
    else:
        print("Opzione non valida.")
