'''
Het programma vraagt om een toetscijfer (float voor kommagetallen!), zorg dat je programma checkt dat het een geldig toetscijfer is! 
(dus bijv. geen 11 of een -1)

Als het een geldig cijfer is print dan `dankjewel`. Als het een ongeldig cijfer, print dan `Dat is geen geldig cijfer...`

Als het cijfer boven de 8 is, print dan `Wow, dat is heel hoog`.
Als het cijfer onder de 8 maar boven de 5.5 is, print dan `Prima, een voldoende!`.
Als het cijfer onder de 5.5 maar boven de 3 is, print dan `Kon slechter maar mag wel beter de volgende keer...`.
Als het cijfer onder de 3 is, print dan `Wat ging hier mis?`.

Als je niet meer weet hoe alles werkt, zoek het dan even op!
'''

toetscijfer = float(input("Geef een cijfer:"))

if toetscijfer < 0 or toetscijfer > 10:
    print ("Dat is geen geldig cijfer")
else:
    print ("dankjewel")

if toetscijfer > 8:
    print ("Wow, dat is heel hoog")
elif toetscijfer < 8 and toetscijfer > 5.5: 
    print ("Prima, een voldoende!")
elif toetscijfer < 5.5 and toetscijfer > 3:
    print ("Kon slechter maar mag wel beter de volgende keer")
elif toetscijfer < 3:
    print ("wat ging hier mis?")

