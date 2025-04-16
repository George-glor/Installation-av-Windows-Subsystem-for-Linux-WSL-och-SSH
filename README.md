## **1. Villkor i Programmering (If-satser)**  

### **Vad är villkor?**  
Villkor används i programmering för att kontrollera vilka delar av koden som ska köras baserat på vissa regler. I Python används `if`, `elif` och `else` för att skapa villkor.

### **Exempel 1: Enkla Villkor**
```python
x = int(input("Ange ett nummer: "))

if x > 0:
    print("Numret är positivt")
elif x < 0:
    print("Numret är negativt")
else:
    print("Numret är noll")
```

### **Exempel 2: Villkor med flera uttryck**
```python
age = int(input("Ange din ålder: "))

if age >= 18 and age < 65:
    print("Du är vuxen.")
elif age >= 65:
    print("Du är senior.")
else:
    print("Du är ett barn.")
```

### **Övningar**
1. Skriv ett program som frågar efter en persons kroppstemperatur och avgör om de har hypotermi (< 35°C), normal temperatur (35–37,5°C) eller feber (> 37,5°C).
2. Skapa ett program där användaren anger två nummer och programmet avgör vilket som är störst.
3. Skriv en meny där användaren väljer en maträtt och programmet svarar med de nödvändiga ingredienserna.

## **2. Loops i Programmering**

### **Vad är loopar?**  
Loopar används för att upprepa kod flera gånger utan att behöva skriva samma kod om och om igen.

### **For Loop**
```python
for i in range(1, 6):
    print(f"Iteration nummer {i}")
```

### **While Loop**
```python
x = 0
while x < 5:
    print(f"x är {x}")
    x += 1
```

### **Övningar**
1. Skapa en for-loop som skriver ut alla jämna nummer mellan 1 och 20.
2. Skriv ett gissningsspel där programmet väljer ett slumpmässigt nummer mellan 1 och 10, och användaren fortsätter att gissa tills de får rätt.
3. Skapa en while-loop som ber användaren att skriva in ett namn och avslutas när de skriver "exit".

## **3. Listor och Tupler**  

### **Vad är listor och tupler?**  
- Listor används för att lagra flera värden i en ordnad sekvens.  
- Tupler fungerar på samma sätt men kan inte ändras efter att de har skapats.

### **Exempel: Lista**
```python
fruits = ["äpple", "banan", "apelsin"]
fruits.append("druva")  # Lägger till ett element
print(fruits[1])  # Output: banan
```

### **Exempel: Tuple**
```python
colors = ("röd", "grön", "blå")
print(colors[0])  # Output: röd
```

### **Övningar**
1. Skapa en lista med dina fem favoritfilmer och skriv ut dem med en for-loop.
2. Skapa en tuple med tre bilmärken och försök att ändra en. Vad händer?
3. Gör en lista där användaren kan lägga till och ta bort objekt interaktivt.

## **4. Ordböcker och Mängder**  

### **Vad är ordböcker och mängder?**  
- Ordböcker lagrar nyckel-värde-par (t.ex. namn och ålder).
- Mängder är en samling av unika värden.

### **Exempel: Ordbok**
```python
person = {"namn": "Alice", "ålder": 25}
print(person["namn"])  # Output: Alice
person["stad"] = "Stockholm"
```

### **Exempel: Mängd**
```python
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}
```

### **Övningar**
1. Skapa en ordbok där nyckeln är en persons namn och värdet är deras favoritfärg.
2. Skapa två mängder och hitta gemensamma element med hjälp av `.intersection()`.

## **5. Funktioner i Python**  

### **Vad är funktioner?**  
Funktioner gör det möjligt att återanvända kod och hålla våra program organiserade.

### **Exempel**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### **Övningar**
1. Skriv en funktion som räknar antalet vokaler i en sträng.
2. Skapa en funktion som kollar om ett tal är udda eller jämnt.

## **6. Felhantering**  

### **Vad är felhantering?**  
Fel kan hanteras med `try-except`.

### **Exempel**
```python
try:
    number = int(input("Ange ett nummer: "))
    print(10 / number)
except ZeroDivisionError:
    print("Du kan inte dela med noll!")
except ValueError:
    print("Ange ett giltigt heltal!")
```

### **Övningar**
1. Försök att komma åt ett index i en lista som inte finns och hantera felet.
2. Skapa ett program där användaren skriver in text istället för ett nummer och hantera felet.

## **7. Återanvändbar och Modular Kod**  

### **Vad är moduler?**  
Du kan importera funktioner från andra filer.

### **Exempel: Skapa en modul**  
Fil: `mymodule.py`
```python
def square(x):
    return x * x
```

Huvudprogram:
```python
import mymodule
print(mymodule.square(4))  # Output: 16
```

### **Övningar**
1. Skapa en modul som innehåller en funktion som beräknar arean av en cirkel.
2. Importera en inbyggd modul, som `math`, och använd `math.sqrt()`.

### **Utmaning**  
Skriv ett program där användaren kan:  
1. Ange namn och ålder  
2. Få ett välkomstmeddelande baserat på åldern  
3. Få deras favoritnummer upphöjt till två med en funktion  
4. Se felmeddelanden om de anger ogiltiga värden  
