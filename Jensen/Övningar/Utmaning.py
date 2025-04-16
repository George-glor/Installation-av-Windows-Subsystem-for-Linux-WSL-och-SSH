def kvadrera(tal):
    return tal * tal

try:
    namn = input("Ange ditt namn: ")
    ålder = int(input("Ange din ålder: "))

    if ålder < 18:
        print(f"Hej {namn}, du är minderårig.")
    elif ålder < 65:
        print(f"Hej {namn}, du är vuxen.")
    else:
        print(f"Hej {namn}, du är senior.")

    favoritnummer = int(input("Ange ditt favoritnummer: "))
    print(f"Ditt favoritnummer i kvadrat är: {kvadrera(favoritnummer)}")

except ValueError:
    print("Fel: Du måste ange ett giltigt heltal.")
