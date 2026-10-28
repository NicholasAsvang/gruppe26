#Variabel for poengsum
poeng = 0

#Introduksjon til Storyline
print("Du er prosjektleder Erling som har ansvar for utviklingen av kommunens nye digitale medborgerportal. ")
print("Det har nå gått 6 uker siden du først samlet prosjekt laget ditt , men selvom det var høy motivasjon på begynnelsen har det nå begynnt å komme konflikter i laget.")
input()

#Konflikt mellom Silje og Elias
print ("Silje og Elias er i konflikt om løsningene deres som har nå eskalert fra en sakskonflikt til en personkonflikt.")
print ("Silje mener at Elias sin løsning vil låse brukeropplevelsen og innovasjon, imens Elias mener at Siljes valg er urealistisk og for kostbar")
print ("Det blir stadig mer friksjon i konfliktene og går fort til at de trekker seg til nærme venner i teamet")
input()
print ("Hva skal du gjøre?")
print ("A) Ta individuelle samtaler")
print ("B) Ta det opp i plenum")

while True:
    valg1 = input ("Velg A eller B: ")
    if valg1 == "A" or valg1 == "B":
        break
    print ("Ugyldig svar. Skriv enten A eller B")


if valg1 == "A":
    poeng += 1
    print ("Du har invitert silje og elias til individuelle samtaler for å skjønne deres perspektiver og har klart å dempe konflikten uten at det trakk ned hele laget")
    input()
elif valg1 == "B": 
    print ("Du har valgt å ta det opp i plenum, men siden begge partiene har allerede støttespillere i hver side går det for over til en konflikt der de forsvarer sin egen side uten å komme til en løsning")
    print ("Konflikten blir eskalert og teamet blir fort splittet i 2 lag")
    input()

#Konflik mellom Hamdi og Hallgeir
print ("Hamdi og Hallgeir er uenig om hvordan innbyggerene skal delta i digitale folkemøter")
print ("Hamdi ønsker å ha en kontrollert løsning gjennom eksisterended plattformer i kommunen")
print ("Men Hallgeir ønsker å ha et mer åpent dialogbasert system som lar til for spontant inspill fra innbyggerene")
input()
print ("Hva skal du gjøre?")
print ("A) Kalle inn et felles møte med begge partiene")
print ("B) Vente og se hva som skjer")

while True:
    valg2 = input("Velg A eller B: ")
    if valg2 == "A" or valg2 == "B":
        break
    print("Ugyldig valg. Skriv A eller B")

if valg2 == "A": 
    poeng += 1 
    print("\nDu går gjennom hva begge partiene vil ha systemet som er kontroll for Hamdi og åpenhet og spontant inspill for hallgeir.")
    print("Dere snakker sammen og landet på et kontrollert plattform med åpenthet for innspill/dialogfelt")
elif valg2 == "B":
    print("Du venter og håper at det skal løse av seg selv, men uenigheten bare vokser og stemningen i laget blir større")
input()

#Synkende Motivasjon i laget
print ("Motivasjonen i laget har gradvis synket, mens fristen for prototypen nærmer seg")
print ("Hva skal du prioritere for å fikse problemet")
print ("A) Sette av tid til relasjonsbygging og sosial teamaktivitet")
print ("B) Prioritere fremdrift og leveranser")

while True: 
    valg3 = input ("Velg A eller B: ")
    if valg3 == "A" or valg3 == "B":
        break
    print("Ugyldig svar, skriv A eller B")

if valg3 == "A":
    poeng += 1 
    print("Du setter sammen en felles aktivitet som får teamet til å få motivasjonen tilbake igjen")
elif valg3 == "B":
    print("Du velger å prioritere fremdrift og leveranse, dette kan føre til økt frustrasjon og dårligere samarbeid i teamaet")

print("\nUtfall")

if poeng == 3:
    print ("Du har løst alle konfliktene. Teamet har fått tilbake tillit og stemningen og har gått videre til norming-fasen")
    print ("Prototypen blir levert i tide og samarbeidet er sterkere enn før")
elif poeng >= 1:
    print("Konflikten har blitt delvis løst, men relasjonene mellom laget er fortsatt sårbare.")
else: 
    print ("Prosjektet mister samholdet, konflikten har fått vokse og prototypen må dermed bli forsinket")