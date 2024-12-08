#Esercizio Improved Generator 06/12/2024 



# Input richiesti
anno_nascita = int(input("Inserisci le ultime due cifre del tuo anno di nascita: "))
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
secret_word = input("Inserisci una parola segreta: ")


# Creazione di un codice più complesso
# Regole:
# 1. Anno di nascita moltiplicato per 3
# 2. Alternanza dei caratteri del nome
# 3. Reverse della parola segreta
# 4. Cognome senza le vocali


codice = str(anno_nascita * 3)
codice += nome[::2]  # Caratteri con indice pari
codice += secret_word[::-1]  # Parola segreta al contrario
codice += ''.join([char for char in cognome if char not in 'aeiouAEIOU'])  # Cognome senza vocali


# Stampa il codice generato
print(f"Il tuo codice segreto migliorato è: {codice}")
