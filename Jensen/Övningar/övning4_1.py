#Skapa en ordbok där nyckeln är en persons namn och värdet är deras favoritfärg.?

favoritfärger = {
    "Anna": "Blå",
    "Erik": "Grön",
    "Sara": "Röd"
}

for namn, färg in favoritfärger.items():
    print(f"{namn}s favoritfärg är {färg}.")

