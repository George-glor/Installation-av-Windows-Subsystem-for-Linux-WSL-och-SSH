# Skapa en funktion som kollar om ett tal är udda eller jämnt.



def udda_eller_jämnt(tal):
    if tal % 2 == 0:
        return "Talet är jämnt."
    else:
        return "Talet är udda."

nummer = int(input("Ange ett tal: "))
print(udda_eller_jämnt(nummer))
