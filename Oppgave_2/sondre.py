poeng = 0

#---------------Introduksjon---------------
print("\033[1m" + "Velkommen til scenario spill" + "\033[0m")
print("Du får tre konflikter du må løse.\nHver konflikt har to alternativer som du svarer på med å skrive A eller B")
print("\x1B[3mKlikk enter for å fortsette \x1B[23m")
input()

#---------------Konflikt 1---------------
print("\033[1m" + "Case 1" + "\033[0m")
print(
"Forestill deg at du er prosjektleder Erling. Deg og teamet ditt skal utvikle kommunens nye digitale medborgerportal.\nEtter 6 uker siden det første møtet, har det nå begynt å oppstå konflikter\n\nSilje og Elias er uenige med løsningene deres. Konflikten har nå eskalert seg fra en sakskonflikt til en personkonflikt.\nKonflikten eskaleres og begge av dem går til andre lagspillere for støtte")
print("\x1B[3mKlikk enter for å fortsette \x1B[23m")
input()

print ("\033[1m" + "Hva vil du gjøre" + "\033[0m")
print ("A) Snakke med dem en og en\nB) Ta det opp med hele laget")

valg_1 = input("Velg A eller B: ").lower()
if valg_1 != "a" and valg_1 != "b":
    print("\033[1;31mSVAR BARE MED A ELLER B. SPILLET AVSLUTTES\033[0m")
    exit()

if valg_1 == "a":
    poeng += 1
    print ("\nDu snakker med Silje og Elias i samtaler hver for seg.\nEtter å ha fått begge perspektiv fant dere en løsning, og dermed dempet konflikten")
    print("\x1B[3mKlikk enter for å fortsette \x1B[23m")
    input()
if valg_1 == "b":
    print ("\nDu valgte å ta det opp med hele teamet. \nSiden begge partene har allerede støttespillere kommer dere ikke fram til noe.\nKonflikten har nå splittet teamet i 2 lag")
    print("\x1B[3mKlikk enter for å fortsette \x1B[23m")
    input()

#---------------Konflikt 2---------------
print("\033[1m" + "Case 2" + "\033[0m")
print ("Hamdi og Hallgeir er uenige om hvordan innbyggerens skal få sin mening fram i de digitale folkemøtene. \nHamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.\nHallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill")
print("\x1B[3mKlikk enter for å fortsette \x1B[23m")
input()
print ("\033[1m" + "Hva vil du gjøre" + "\033[0m")
print ("A) Kall de inn til felles møte\nB) Ikke gjøre noe")

valg_2 = input("Velg A eller B: ").lower()
if valg_2 != "a" and valg_2 != "b":
    print("\033[1;31mSVAR BARE MED A ELLER B. SPILLET AVSLUTTES\033[0m")
    exit()

if valg_2 == "a":
    poeng += 1
    print("\nDu kaller de inn til fellesmøte.\nDere går gjennom hva hver av dem trenger.\nDere kommer fram til en kontrollert plattform med et åpent dialogfelt.")
if valg_2 == "b":
    print("\nDu gjør ingenting og håper det går over.\nLaget splitter seg mer.")
print("\x1B[3mKlikk enter for å fortsette \x1B[23m")
input()

#---------------Konflikt 3---------------
print("\033[1m" + "Case 3" + "\033[0m")
print ("Motivasjonen i laget synker, og deadlinen nærmer seg")
print("\x1B[3mKlikk enter for å fortsette \x1B[23m")
input()

print ("\033[1m" + "Hva vil du gjøre" + "\033[0m")
print ("A) Sett av tid til relasjonsbygging og en sosial teamaktivite.\nB) Prioritere fremdrift og leveranser")

valg_3 = input("Velg A eller B: ").lower()
if valg_3 != "a" and valg_3 != "b":
    print("\033[1;31mSVAR BARE MED A ELLER B. SPILLET AVSLUTTES\033[0m")
    exit()

if valg_3 == "a":
    poeng += 1
    print("Du setter av tid for en sosial teamaktivitet.\nTeamet får motivasjonen tilbake igjen")
if valg_3 == "b":
    print("Du prioriterer fremdrift og leveranse.\nDette fører til ingen endringer i motivasjonen")

#---------------Utfall---------------
print("\033[1m" + "\nUTFALL:" + "\033[0m")

if poeng == 3:
    print("\033[1;32mGRATULERER\033[0m")
    print("\033[32mDu har løst alle konfliktene.\nTeamet holdt seg sterkt gjennom alle fasene.\nPrototypen ble levert i tide.\033[0m")
if poeng == 1 or poeng == 2:
    print("\033[1;33mDELVIS KORREKT\033[0m")
    print("\033[33mDu har løst nesten alle konfliktene.\nTeamet holdt seg delvis sammen gjennom alle fasene.\nDet er usikkert på om prototypen ble levert i tide.\033[0m")
if poeng == 0:
    print("\033[1;31mKUNNE IKKE TATT MER FEIL!\033[0m")
    print("\033[31mDu har ikke løst NOEN av konfliktene.\nTeamet holdt seg svakt gjennom alle fasene.\nPrototypen ble IKKE levert i tide.\033[0m")