#Skapa en while-loop som ber användaren skriva in namn och avslutas när de skriver "exit".

namn = ""

print("Skriv in ett namn (eller 'exit' för att avsluta):")

while namn.lower() != "exit":
    namn = input("Namn: ")
    if namn.lower() != "exit":
        print(f"Hej, {namn}!")
        
print("Programmet avslutas. Hejdå!")
