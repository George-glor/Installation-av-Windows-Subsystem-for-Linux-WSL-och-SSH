#Skriv en funktion som räknar antalet vokaler i en sträng.


def räkna_vokaler(text):
    vokaler = "aeiouyåäöAEIOUYÅÄÖ"
    return sum(1 for bokstav in text if bokstav in vokaler)

mening = input("Skriv en mening: ")
print(f"Antal vokaler: {räkna_vokaler(mening)}")



