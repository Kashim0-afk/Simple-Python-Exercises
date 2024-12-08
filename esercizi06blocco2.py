#Esercizi Misti blocco2 06/12/2024
 
 
 
# Esercizio 1: Numero di caratteri di una parola
parola = input("Inserisci una parola: ")
lunghezza = len(parola)  # Usa la funzione len() per calcolare la lunghezza
print("Il numero di caratteri della parola è:", lunghezza)



# Esercizio 2: Quoziente di due numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
quoziente = numero1 / numero2  # Divisione diretta
print("Il quoziente dei due numeri è:", quoziente)



# Esercizio 3: Alternanza maiuscolo/minuscolo in una parola
parola = input("Inserisci una parola: ")

# Alterna i caratteri in maiuscolo e minuscolo usando slicing
maiuscolo = parola[::2].upper()  # Caratteri con indice pari in maiuscolo
minuscolo = parola[1::2].lower()  # Caratteri con indice dispari in minuscolo

# Combina i caratteri alternati mantenendo l'ordine originale
alternata = ""
alternata += "".join(maiuscolo[i] + minuscolo[i] if i < len(minuscolo) else maiuscolo[i] for i in range(len(maiuscolo)))

print("La parola con caratteri alternati maiuscolo/minuscolo è:", alternata)



# Esercizio 4: Numero di caratteri di una frase
frase = input("Inserisci una frase: ")
lunghezza_frase = len(frase)  # Calcola la lunghezza della frase
print("Il numero di caratteri della frase è:", lunghezza_frase)



# Esercizio 5: Potenza di due numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
potenza = numero1 ** numero2  # Calcola il primo numero elevato al secondo
print("Il risultato della potenza è:", potenza)



# Esercizio 6: Parola con le prime tre lettere maiuscole
parola = input("Inserisci una parola: ")
parola_modificata = parola[:3].upper() + parola[3:].lower()  # Modifica solo le prime tre lettere
print("La parola con le prime tre lettere maiuscole è:", parola_modificata)
