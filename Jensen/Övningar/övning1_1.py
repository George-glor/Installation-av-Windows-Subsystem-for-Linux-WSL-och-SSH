#Skriv ett program som frågar efter kroppstemperatur och avgör om personen har hypotermi (< 35°C), normal temperatur (35–37.5°C), eller feber (> 37.5°C).

		
temperatur = float(input("Ange din kroppstemperatur i °C: "))

if temperatur < 35:
    print("Du har hypotermi.")
elif temperatur >= 35 and temperatur <= 37.5:
    print("Din kroppstemperatur är normal.")
else:
    print("Du har feber.")
