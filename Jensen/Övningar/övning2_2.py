#Skriv ett gissningsspel där programmet väljer ett tal mellan 1 och 10 och användaren gissar tills det blir rätt.

import random
hemligt_tal = random.randint(1, 10)
gissning = 0

while gissning != hemligt_tal:
    gissning = int(input("Gissa talet (1–10): "))
print("Rätt gissat!")
