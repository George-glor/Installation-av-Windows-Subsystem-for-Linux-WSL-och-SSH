# Försök att komma åt ett index i en lista som inte finns och hantera felet.

lista = [1, 2, 3]

try:
    print(lista[5]) # Ni kan testa här att byta värde på indexet
except IndexError:
    print("Indexet finns inte i listan.")

