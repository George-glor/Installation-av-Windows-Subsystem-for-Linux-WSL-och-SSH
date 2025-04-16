#Skapa ett program där användaren anger två tal och programmet avgör vilket som är störst.

tal1 = float(input("Ange det första talet: "))
tal2 = float(input("Ange det andra talet: "))

if tal1 > tal2:
    print(f"{tal1} är större än {tal2}.")
elif tal2 > tal1:
    print(f"{tal2} är större än {tal1}.")
else:
    print("Talen är lika stora.")
