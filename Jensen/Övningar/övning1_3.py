#Skriv en meny där användaren väljer en maträtt och programmet visar vilka ingredienser som behövs.

print("Välj en maträtt:")
print("1. Spaghetti Bolognese")
print("2. Kycklingsallad")
print("3. Vegetarisk lasagne")

val = input("Ange numret på maträtten: ")

if val == "1":
    print("Ingredienser: spaghetti, köttfärs, tomatsås, lök, vitlök, olivolja, salt, peppar.")
elif val == "2":
    print("Ingredienser: kycklingfilé, sallad, tomat, gurka, paprika, olivolja, vinäger.")
elif val == "3":
    print("Ingredienser: lasagneplattor, zucchini, aubergine, tomatsås, ost, lök, vitlök.")
else:
    print("Ogiltigt val.")


