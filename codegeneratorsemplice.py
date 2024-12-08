#Esercizio Code Generator Semplice 06/12/2024 


# Input
anno_nascita = int(input("Inserisci le ultime due cifre del tuo anno di nascita: "))
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
secret_word = input("Inserisci una parola segreta: ")


# Calcolo codice
codice = str(anno_nascita * 2)  # Doppio delle ultime cifre dell'anno di nascita
codice += nome[0] + nome[-1]  # Primo e ultimo carattere del nome
codice += secret_word[0] + secret_word[2]  # Primo e terzo carattere di secret_word
codice += cognome[:4]  # Primi 4 caratteri del cognome


# Stampa il codice generato
print(f"Il tuo codice segreto è: {codice}")
