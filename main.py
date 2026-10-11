name = input("Om du vill heta Skobido klicka Ja, men om du vill heta Erik klicka Nej: ")

if name.lower() == "ja":
    print("Du heter Skobido.")
else:
    print("Du heter Erik.")

Morgon = int(input("Om du vill vakna på morgonen och äta frukost, klicka 1." "för att sova vidare så att du får sparken från jobbet och då bestämma dig för att råna en bank, klicka 2." "För att sova hela dagen, klicka 3."))

if Morgon == 1:
    print("Du går up äter frukost och går till jobbet som vanligt.")

    jobbet = int(input("Om du vill vara på jobbet hela dagen, klicka 1." "Om du istället vill gå och köpa en Ferrari, klicka 2:"))

    if jobbet == 1:
        print("Du stannar på jobbet hela dagen men trillar sedan ned i ett hål")
    elif jobbet == 2:
        print("Du får en fortkörningsbot på vägen hem.")
    
elif Morgon == 2:
    print("du sover vidare och får sparken")
    banken = int(input("Du ignorerar väckarklockan och sover till jätte länge och då får du sparken från ditt jobb och därför bestämmer du dig för att råna en bank, om du vill köpa en läskig helikopter och råna banken med den klicka 1 men om du istället vill köpa en iskanon klicka 2"))
    if banken == 1:
        print("Du går till helikopteräffären och köper den bästa helikoptern och landar på taket av banken och tar alla pengarna.")
        
        polisen = int(input("polisen kommer ditt för att fly från polisen klicka 1 annars klicka 2."))
        if polisen == 1:
            print("Du stjäl en bil och kör där ifrån men du blir till slut fångad.")
        else: 
            print("Du försöker inte att fly så därför bjuder polisen dig på munkar.")

    elif banken == 2:
        print("Du inser att iskanonen inte var det bästa saken för att råna en bank.")
        print("Du ger upp och går hem istället.")

if Morgon == 3: 
    print("Du sover hela dagen men vaknar av att ditt hus har flyttats till uganda")
    Uganda = int(input("Ska du försöka ta tillbaka ditt hus till Sverige? Klicka 1. Om du lämnar huset och går tillbaka till Sverige, klicka 2: "))
    if Uganda == 1: 
        print("Du lyckas köpa tillbaka huset, men transportkostnaderna blev för dyra, Så du behöver ha kvar den som en sommarstuga i Uganda.")
    
    elif Uganda == 2: 
        print("Du köper inte tillbaka huset så du går tillbaka till Sverige utan hus.")
 
