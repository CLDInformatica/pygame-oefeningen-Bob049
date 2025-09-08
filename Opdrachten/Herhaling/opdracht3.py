'''
Gegeven is een lijst met games. Doe het volgende:

  - Voeg Super  BroMarios toe aan de lijst
  - Vraag de gebruiker om een **getal** tussen de 0 en de 5
  - Print de game die op deze plek in de lijst staat
  - Vraag de gebruiker om een game met een input
  - Voeg deze game toe aan de lijst
  - Print de lijst met games
'''

games = ["Minecraft", "Rust", "GTA V", "Hayday", "Clash of clans"]

games.append ("Super Mario Bros")

getal = int(input("kies een getal tussen 0 en de 5"))

print (games.[getal])