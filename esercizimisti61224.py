# Esercizi Misti 06/12/2024


# Esercizio 1: Saluto
nome = input("Inserisci il tuo nome: ")
print(f"Ciao, {nome}!")


# Esercizio 2: Somma di due numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
somma = numero1 + numero2
print(f"La somma dei due numeri è: {somma}")


# Esercizio 3: Primi tre caratteri di una parola
parola = input("Inserisci una parola: ")
print(f"I primi tre caratteri della parola sono: {parola[:3]}")


# Esercizio 4: Ultimi cinque caratteri di una frase
frase = input("Inserisci una frase: ")
print(f"Gli ultimi cinque caratteri della frase sono: {frase[-5:]}")


# Esercizio 5: Doppio di un numero
numero = float(input("Inserisci un numero: "))
print(f"Il doppio del numero è: {numero * 2}")


# Esercizio 6: Parola al contrario
parola = input("Inserisci una parola: ")
print(f"La parola al contrario è: {parola[::-1]}")


# Esercizio 7: Differenza tra due numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
differenza = numero1 - numero2
print(f"La differenza tra i due numeri è: {differenza}")


# Esercizio 8: Caratteri con indice pari di una frase
frase = input("Inserisci una frase: ")
print(f"I caratteri con indice pari della frase sono: {frase[::2]}")


# Esercizio 9: Concatenazione di due parole
parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")
print(f"La concatenazione delle due parole è: {parola1 + parola2}")


# Esercizio 10: Quadrato di un numero
numero = int(input("Inserisci un numero intero: "))
print(f"Il quadrato del numero è: {numero ** 2}")


# Esercizio 11: Frase senza i primi tre caratteri
frase = input("Inserisci una frase: ")
print(f"La frase senza i primi tre caratteri è: {frase[3:]}")


# Esercizio 12: Primi dieci caratteri al contrario
frase = input("Inserisci una frase: ")
print(f"I primi dieci caratteri al contrario sono: {frase[:10][::-1]}")


# Esercizio 13: Prodotto di due numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
prodotto = numero1 * numero2
print(f"Il prodotto dei due numeri è: {prodotto}")


# Esercizio 14: Ripetizione di una parola
parola = input("Inserisci una parola: ")
print(f"{parola}-{parola}-{parola}")


# Esercizio 15: Inversione dei caratteri dispari di una frase
frase = input("Inserisci una frase: ")
caratteri_dispari_invertiti = ''.join([frase[i] for i in range(len(frase)) if i % 2 != 0])[::-1]
print(f"I caratteri con indice dispari invertiti sono: {caratteri_dispari_invertiti}")
