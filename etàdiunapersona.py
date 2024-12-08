#Esercizio Età di una Persona 06/12/2024


# Chiede nome e età all'utente
nome = input("Inserisci il tuo nome: ")
eta = int(input("Inserisci la tua età: "))

# Stampa i dati inseriti
print(f"Ciao {nome}, hai {eta} anni!")

# Calcola l'età in mesi, giorni, minuti, secondi e millisecondi
mesi = eta * 12
giorni = eta * 365
minuti = giorni * 24 * 60
secondi = minuti * 60
millisecondi = secondi * 1000

# Stampa i calcoli
print(f"La tua età in mesi è: {mesi}")
print(f"La tua età in giorni è: {giorni}")
print(f"La tua età in minuti è: {minuti}")
print(f"La tua età in secondi è: {secondi}")
print(f"La tua età in millisecondi è: {millisecondi}")
