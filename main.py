name = input("Om du vill heta skobido klicka Ja men om du vill heta Erik klicka Nej.")
if name.lower() == "ja":
   print("du heter skobido")
else:
   print("du heter Erik")

Morgon = int(input("Om vakna på morgonen och äta frukost, klicka 1, för att sova vidare och sedan råna en bank, klicka 2, för att sova hela dagen klicka 3."))

if Morgon == 1:
   print("Du går up äter frukost och går till jobbet som vanligt.")
   jobbet = int(input("Om du vill vara på jobbet hela dagen klicka 1 men om du klickar 2 så går du och köper en ferrari."))
   
if jobbet == 1:
   print("Du stannar på jobbet hela dagen men trillar sedan ned i ett hål.")
   if jobbet == 2:
      print("Du får en fortkörningsböter på vägen hem.")
   
   if Morgon == 2:
    banken = int(input("Du ignorerar väckarklockan och sover till klockan 1 och då får du sparken från ditt jobb och därför bestämmer du dig för att råna en bank, om du vill köpa en läskig helikopter och råna banken med den klicka 1 men om du istället vill köpa en iskanon klicka 2"))
    if banken == 2:
        print("Du går till helikopteräffären och köper den bästa helikoptern och landar på taket av banken och tar alla pengarna.")

    if banken == 1:
        polisen = int(input("polisen kommer ditt för att fly från polisen klicka 1 annars klicka 2."))
    if polisen == 1:
       print("Du stjäl en bil och kör där ifrån men du blir till slut fångad.")
    else: 
       print("Polisen bjuder dig på munkar.")
if Morgon == 3: 
   print("du sover hela dagen men vaknar av att ditt hus har flyttats till uganda.")
   
        

