name = int(input(" Om du vill heta skobido klicka 1 men om du vill heta Erik klicka 2"))
if name == 1:
   print("du heter skobido")
if name == 2:
   print("du heter Erik")

Morgon = int(input(" Om vakna på morgonen och äta frukost, klicka 1, för att sova vidare och sedan råna en bank, klicka 2."))

if Morgon == 1:
   jobbet = int(input("Du går upp ur sängen och sedan in i köket och äter en frukost som består av citronjucie och du är sedan på jobbet hela dagen om du klickar 1 eller så går du och köper en ferrari om du klickar 2."))
   if jobbet == 1: 
      print("du är på jobbet hela dagen och sedan går du hem och sover.")

   if jobbet == 2:
      print("du går och köper en ferrari och får en fortkörningsböter på vägen hem.")

if Morgon == 2:
    banken = int(input("Du ignorerar väckarklockan och sover till klockan 1 och då får du sparken från ditt jobb och därför bestämmer du dig för att råna en bank, om du vill köpa en läskig helikopter och råna banken med den klicka 1 men om du istället vill köpa en iskanon klicka 2"))
    if banken == 2:
        print("Du går till helikopteräffären och köper den läskigaste helikoptern och landar på taket av banken och tar alla pengarna men du blir attackerad av en dinosaurie om du klickar 1, du blir attackerad av shreck med en rymdkanon om du klickar 2.")

    if banken == 1:
        print("Du använder iskanonen för att frysa ner alla och rånar banken.")




