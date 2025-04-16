#Skapa ett program där användaren skriver text istället för ett tal och hantera felet.

try:
    tal = int(input("Ange ett tal: "))
    print(f"Du skrev: {tal}")
except ValueError:
    print("Du måste skriva ett heltal!")
