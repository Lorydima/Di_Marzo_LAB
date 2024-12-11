# Matrice

# Libreria per il colore del testo
from colorama import *

# Dichiarazione lista "matrice"
matrice = []

# Funzione inserimento numero matrice
def insert_Number():
    input_number = input(Fore.YELLOW + "Enter the number:" + Fore.RESET)
    for i in range(6):
            matrice.append(input_number)
    print_matrice()

# Funzione stampa matrice con colore rosso
def print_matrice():
    for j in range(5):
        print(Fore.RED + str(matrice) + Fore.RESET)

# Chiama funzione "insert_Number()"
insert_Number()