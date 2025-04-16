#Skapa en tuppel med tre bilmärken och försök ändra ett av dem. Vad händer?

bilar = ("Volvo", "BMW", "Tesla")
bilar = list(bilar)  
bilar[0] = "Audi"    
bilar = tuple(bilar) 
