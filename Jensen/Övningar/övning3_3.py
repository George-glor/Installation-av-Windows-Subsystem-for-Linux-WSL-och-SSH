#Skapa en lista där användaren kan lägga till och ta bort objekt interaktivt.

lista = []

while True:
    val = input("Lägg till/ta bort/visa/avsluta: ").lower()
    
    if val == "lägg till":
        objekt = input("Vad vill du lägga till? ")
        lista.append(objekt)
    elif val == "ta bort":
        objekt = input("Vad vill du ta bort? ")
        if objekt in lista:
            lista.remove(objekt)
    elif val == "visa":
        print(lista)
    elif val == "avsluta":
        break
