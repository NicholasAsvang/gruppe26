score = 0
print("I dette spillet er du prosjektlederen Erling og du skal løse konflikter i ditt team som jobber med å utvikle et digitalt verktøy for innbyggerne. Du vil bli presentert ulike konfliktsituasjoner, og du må ta valg for å håndtere dem på en konstruktiv måte.")
input()

print("Silje (UX/UI-designer) og Elias (IT-radgiver) er uenige om teknologi og design. Det som startet som en saklig uenighet, har blitt en personkonflikt, og begge trekker støtte fra sine nærmeste i teamet.")
input()
print("Hva vil du gjøre for å løse konflikten? Valg A eller B?")
print("A: Snakke med Silje og Elias hver for seg.")
print("B: Ta det opp i teammøte og la alle komme med sine synspunkter.")

while (True):
    Svar1 = input("Velg A eller B:")
    if Svar1 == "A" or Svar1 == "a":
        print("Du valgte å snakke med Silje og Elias hver for seg. Dette hjalp deg med å forstå deres perspektiver bedre og du fant en løsning som fungerer for begge parter.")
        score += 1
        break
    elif Svar1 == "B" or Svar1 == "b":
        print("Du valgte å ta det opp i teammøte og la alle komme med sine synspunkter. men blir fort møtt av at teamet tar parti for en av dem, og konflikten eskalerer.")
        break
    else:
        print("Ugyldig valg.")
        
input()
print("Samtidig er Hamdi og Hallgeir uenige om hvordan innbyggerne skal få fremmet sine meninger i de digitale folkemøtene: Hamdi vil ha en kontrollert løsning på kommunens eksisterende plattform, mens Hallgeir vil ha et åpent system med rom for spontane innspill.")
input()
print("Hva vil du gjøre for å løse konflikten? Valg A eller B?")
print("A: Kalle inn til felles møte med Hamdi og Hallgeir for å diskutere fordeler og ulemper ved begge løsningene.")
print("B: Vente å se om konflikten løser seg selv over tid.")

while(True):
    Svar2 = input("Velg A eller B:")
    if Svar2 == "A" or Svar2 == "a":
        print("Du setter seg ned med begge og går gjennom hva hver av dem trenger. Hamdi vil ha kontroll og trygghet. Hallgeir vil ha åpenhet og spontane innspill. Målet er å finne en løsning som dekker begge deler, for eksempel en kontrollert plattform med et åpent dialogfelt. De kommer til enighet og konflikten løses.")
        score += 1
        break
    elif Svar2 == "B" or Svar2 == "b":
        print("Du velger å vente og se om konflikten løser seg selv over tid. Dette fører til at konflikten eskalerer, og det blir vanskeligere å finne en løsning senere.")
        break
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")
else:
    print("Ugyldig valg.")
input()

print("Motivasjonen synker, og fristen nærmer seg for å levere et nytt digitalt verktøy for innbyggerne. Teamet er stresset og frustrert, og det er tydelig at samarbeidet ikke fungerer optimalt.")
input()
print("Hva vil du gjøre for å løse konflikten? Valg A eller B?")
print("A: Ta en pause og ha en teambuilding-aktivitet for å styrke samarbeidet.")
print("B: Prioritere fremdrift og leveranser")

while (True):
    Svar3 = input("Velg A eller B:")
    if Svar3 == "A" or Svar3 == "a":
        print("Du velger å ta en pause og ha en teambuilding-aktivitet for å styrke samarbeidet. Dette kan bidra til å bygge tillit og forståelse mellom teammedlemmene, og dermed forbedre samarbeidet.")
        score += 1
        break
    elif Svar3 == "B" or Svar3 == "b":
        print("Du velger å prioritere fremdrift og leveranser fremfor å prioritere gruppens behov. Dette kan føre til at problemet eskalerer ytterligere, og teamet blir mer stresset og frustrert.")
        break
    else:
        print("Ugyldig valg. Vennligst velg A eller B.")
else:
    print("Ugyldig valg. Vennligst velg A eller B.")
input()    
if score == 3:
    print("Gratulerer! Du har håndtert konfliktene på en konstruktiv måte og bidratt til et bedre samarbeid i teamet. Nå er normingen på plass, og prosjektet kan leveres i tide.")
elif score == 2 or score == 1:
    print("Bra jobbet! Du har delvis håndtert noen av konfliktene på en konstruktiv måte, men det er fortsatt rom for forbedring.")
else:
    print("Dessverre løses ingen av konfliktene og projektet må forsinkes. Det er viktig å ta konflikter på alvor og jobbe aktivt for å løse dem for å oppnå et godt samarbeid i teamet.")