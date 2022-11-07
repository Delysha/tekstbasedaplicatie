
import time

def start():
    
    time.sleep(1)
    print("Het is een rustige dag, je zit gewoon te reizen in je ruimteschip en rond te kijken door het heelal. Plotseling wordt je gebeld door je moeder, ze vraagt wat je wilt eten als je terug bent op mars. Je verteld haar wat je wilt eten, tot dat je plotseling  in een meteorieten regen vast komt. Je ruimteschip begint helemaal raar te doen en je kan het niet meer besturen. Je staat op een punt dat je niet meer weet wat je moet doen, je kijkt het heelal nog 1 keer aan en denkt bij je zelf zou ik gaan springen of zou ik gewoon kijken of ik hier uit kan komen ? Je denkt uiteindelijk goed na en je zegt tegen je zelf dat je der uit gaat komen je leunt het stuur zo ver naar links dat je der uit komt. Maar helaas zie je dat je ruimteschip helemaal beschadigd is wat moet je nu doen……")

    time.sleep(1)
    question= input("vraag: A. ga naar aarde \nB.blijf waar je bent ")
    if question == "A" or question == "a":
        time.sleep(1)
        print("je gaat nu naar de aarde")
        vraag3()
    elif question == "B"or question == "b" :
        time.sleep(1)
        print("je blijft nu waar je bent.")
        vraag1()
    else:
        time.sleep(1)
        print("antwoord met A of B")
        start()
def vraag1():
 
    time.sleep(1)
    print('Je blijft zitten en probeert rustig te blijven je kijkt naar het heelal en ziet hoe mooi het is. \nJe bedenkt bij je zelf dat dit het moment is dat je dood gaat dus je belt je moeder om haar vaarwel te zeggen en na dat jullie hebben gebeld zie je dat je steeds dichter bij de zon komt dus zeg je vaarwel tegen het heelal en doe je je ogen dicht. \nJe bent dood. ')
    print ("wil je nog een keer?")
    print("(ja of nee)")
    A = input()
    if A == "ja":
        print("good luck")
        start()
    elif A == "nee":
        print(" bye bye")
    else:
        vraag1()
    
    

def vraag2():
    time.sleep(1)
    print("Je bent op aarde in amsterdam en jij en je nieuwe vrienden lopen langs een paar nieuwe mensen jullie kijken elkaar aan en zien dat hun niet bang voor jullie zijn. \nJe kijkt je nieuwe vrienden aan en jullie lopen naar de mensen toe maar je ziet dat ze een raar wezen bij hun hebben het wezen begint naar jullie te grommen. \nJe schrikt je rot en begint terug te grommen de mensen kijken jullie aan en maken een gebaar dat je rustig moet worden en dat hun wezen je niks aan gaat doen.  \nJe begrijpt helaas niet wat ze zeggen maar begrijpt wel dat je rustig kan worden. \nDe mensen aaien het wezen en wijzen je hand aan ze willen dat je het wezen aait maar of jij het wilt is nog de vraag.\nDus ga je het doen of niet….")
    time.sleep(1)
    question2= input ("vraag: A je aait het wezen B \nje staart het wezen alleen aan")
    if question2 == "A"or question2 == "a":
        time.sleep(1)
        print("oke je aait het wezen!")
        vraag10()
    elif question2 == "B" or question2 == "b":
        time.sleep(1)
        print("oke je staart het wezen aan")
        vraag4()
    
    
def vraag3 (): 
    time.sleep(1)
    print ("Je tank is nog half vol dus je probeert te reizen naar de aarde maar tijdens die reis kom je terecht op de maan omdat je tank helemaal leeg is. \nGelukkig weet je dat de maan een bar heeft met andere aliens dus je begint met lopen je loopt helemaal naar de bar genaamd MOONDRINKS 221. \nJe gaat naar binnen en loopt naar een tafel je gaat zitten en kijkt om je heen helaas is er niemand die je kent je zucht want je kan ook niemand meer bereiken met je holografic Phone want die is helemaal kapot gegaan door de meteorieten regen. \nOpeens komt er iemand binnen en hij loopt naar jou toe hij kijkt je heel blij aan want hij weet blijkbaar dat jij naar aarde wilt gaan maar jij weet niet dat hij het weet. \nJe zegt tegen hem dat die mag zitten en jullie beginnen te praten hij vraagt aan je of je hulp nodig hebt om naar de aarde te komen hij heeft namelijk zelf ook wat vrienden die mee willen gaan. \nJe weet het niet zeker maar je gaat alsnog mee met hun. Je loopt met je nieuwe vriend en zijn vrienden naar zijn ruimteschip en gaat er in. \nJullie vliegen naar aarde maar hij wilt dat je naast iemand gaat zitten die best eng is ga je naast die persoon zitten of blijf je uit zijn buurt…")
    time.sleep(1)
    question3= input("vraag:A je gaat naast hem zitten \nB je blijft staan")
    if question3 == "A" or question3 == "a" :
     time.sleep (1)
     print ("oke je zit nu naast hem!")
     vraag8()
    elif question3 == "B" or question3 == "b":
        time.sleep(1)
        print ("je blijft staan")
        vraag11()
    else: 
        time.sleep(1)
        print("antwoord met A of B")
        vraag3()

def vraag4 ():
    time.sleep(1)
    print ("Je staart het wezen alleen maar eng aan en de mensen vinden dat niet zo fijn ze merken ook dat je ogen rood worden alleen jij merkt het niet. \nDe mensen worden bang van je en je maakt een beweging dat er op lijkt dat je ze wilt slaan. \nOp een geven moment voel je een steek in je borst kast. \nJe bloed en ziet dat er een ander mens je heeft neer gestoken blijkbaar waren ze toch bang… \nje voelt je tempratuur zakken en sluit je ogen je gaat dood en dat weet je.Na 1 minuut ben je dood …. ")
    print ("wil je nog een keer?")
    print ("ja of nee?")
    B = input ()
    if B == "ja":
        print ("good luck!")
        start()
    elif B == "nee":
         print ("okay byee")
    else:
        time.sleep(1)
        print("antwoord met A of B")   
        vraag4()

def vraag5 ():
    time.sleep (1)
    print ("Je zegt niks en blijft stil je wilt namelijk niet dat hij het weet. Hij kijkt je boos aan en begint geïrriteerd te praten. \nHij zegt als je nu niks zegt zorg ik er voor dat je een kort leven hebt. \nMaar als je het aan me vertelt dan kunnen we iets regelen dat jij een oke leven hebt en dat er niks ergs gebeurt met jou en je vriendjes. \nJe kijkt hem bang aan maar zegt Oke. Je vertelt het en daarna zeg je ook sorry dat je het eerst niet wouw vertellen. \nMaar je vertelt ook dat je je zelf wouw veranderen naar iemand anders. Zodat je een beter leven kan leven. \nHij lacht en zegt dat als je het meteen had vertelt dat er niks ergs zou gebeuren met je maar nu heb je het zelf erg gemaakt. \nHij kijkt je kwaad aan en roept de mannen in pak om jou op te sluiten en dat hij je vrienden haalt. Je kijkt verdrietig en zegt nogmaals sorry en smeekt om je leven en dat van je vrienden. \nHij zegt nog een keer dat het je eigen schuld is en dat je het had moet vertellen. \n2 dagen later zit je in de gevangenis met je vrienden en zeg je tegen hun dat het je spijt dat hun ook dood gaan. \nZe zeggen dat het oke is en dat het niet jou schuld is omdat jij het niet kon weten dat dit zou gebeuren. Een uur later komen er een paar mannen naar jullie toe met tazers en zeggen ze dat je moet gaan lopen. \nJullie lopen naar een busje en gaan daar in het busje begint te rijden en het duurt ongeveer 4 dagen tot jullie der aan kwamen. \nDe mannen zeggen dat jullie der uit moeten gaan en dat jullie moeten gaan lopen. Je begint te lopen naar een groot diep gat en kijkt de mannen aan je vraagt wat dit is en ze zeggen dat jullie gedeporteerd worden  naar de kern van de aarde. \nJe kijkt verbaast en vraagt wat dat is maar  ze beantwoorden je niet en zeggen dat je moet springen. \nJe smeekt ze nog 1 keer maar ze luisteren niet. Je springt er in en zegt vaarwel tegen de aarde. \n2 jaar later jullie zitten nog steeds in kern van de aarde en komen der ook nooit meer uit. EINDE")
    time.sleep(1)
    print ("wil je nog een keer?")
    time.sleep(1)
    print ("ja of nee?")
    C = input ()
    if C == "ja":
        print ("good luck!")
        start ()
    elif C == "nee":
        print ("okay byee")
    else: 
        time.sleep(1)
        print("antwoord met A of B")
        vraag5()

def vraag6 ():
    time.sleep(1)
    print("Je vertelt dat je een alien bent en dat je hier alleen bent omdat je niet meer naar je thuis planeet kon vluchten ook vertel je dat je bang bent maar dat je graag anderen aliens wilt helpen. \nDe burgermeester lacht en vraagt of je je kan vermommen als hem. Je zegt ja en vraagt meteen hoezo hij dat wilt weten. \nHij vertelt je dat die al een tijdje met pensioen wilt en dat hij het zat is om wereldleider te zijn. \nOok wilt die dat je je verandert naar hem en dat je niemand iets vertelt want hij weet jou geheim. Je zegt oke en veranderd in hem. \nHij lacht weer en zegt bedankt ook vertelt die je dat je hier door sneller aliens kan helpen als je maar der voor zorgt dat niemand der achter komt je. \nJe belooft het en lacht naar hem. Jullie schudden elkaars hand en zeggen vaarwel hij loopt naar een geheimen deur en rent weg. \nNadat hebben jullie elkaar niet meer gesproken.\nTien jaar later> Na tien jaar heb je in totaal 1700 aliens geholpen om zich te nestelen op aarde en heb je ervoor zorgt dat niemand ze pijn kan doen ook weten mensen nu dat aliens bestaan en dat ze niemand pijn doen. \nJe bent nu de leider van de wereld en dit is daarom ook een heel mooi einde EINDE.")
    time.sleep(1)
    print ("wil je nog een keer?")
    time.sleep(1)
    print ("ja of nee?")
    D = input ()
    if D == "ja":
        print ("good luck!")
        start()
    elif D == "nee":
        print ("okay byee")
    else: 
        time.sleep(1)
        print("antwoord met A of B")
        vraag6()

def vraag7 ():
    time.sleep(1)
    print ("Je trekt je vrienden aan hun arm en zegt “tegen ze kom snel we moeten gaan rennen naar het bos” je rent met je vrienden naar het bos en zegt dat jullie je zelf moeten gaan camoufleren je hebt toevallig een apparaat dat je kan veranderen naar het wezen dat je moet zijn op aarde.\nJij en je vrienden veranderen je zelf snel als mensen en proberen rustig langs het leger te lopen om weg te kunnen gaan. \nHet leger kijkt jullie aan en waarschuwt jullie dat er aliens zijn niet vermoedend dat ze eigenlijk tegen de aliens aan het praten zijn. \nJe zegt dat jullie zullen opletten en dat jullie snel moeten gaan. Jij en je vrienden gaan snel naar een plek je ziet een grote plek met raren wezens het zijn groten dieren met zwarten vlekken op hun vacht je ziet een mens en vraagt wat voor wezen het is ze zeggen dat het een koe is \n( ja je kan nu mensen taal spreken omdat je gecamoufleerd bent als mens). Je kijkt de koeien raar aan en aait er 1. \nDe mensen vragen waar je woont en je zegt dat je geen woning hebt en of je bij hun kan slapen met je vrienden ze zeggen ja maar als je wel klusjes doet en dat vindt je oké. \nJullie lopen naar de logeer woning en je ziet opeens een hele knappen jongen hij kijkt je aan het lacht je voelt je raar in je buik en kijkt heel lang naar hem. Hij zwaait naar je en wilt dat je naar hem toe loopt maar ga je dat ook doen…")
    time.sleep(1)
    question7 = input("vraag: A je gaat naar hem toe \nB je loopt door")
    time.sleep(1)
    if question7 == "A" or question7 == "a":
        time.sleep(1)
        print ("je loopt nu naar hem toe.")
        vraag9()
    elif question7 == "B" or question7 == "b":
        time.sleep(1)
        print ("je loopt door")
        vraag21()
    else:
        time.sleep(1)
        print("antwoord met A of B")
        vraag7()
    
def vraag8 ():
    time.sleep(1)
    print("Je zit naast de enge man en zwaait naar hem hij doet niks want hij vraagt zich af wat er rond gaat in je hoofd ook kijkt die je aan alsof je zijn moeder hebt gedood. \nDaarna zegt die met een grote zucht hallo. Jullie staren elkaar voor 10 seconden lang aan zonder iets te zeggen tot dat jij je bedenkt dat je je nog niet hebt voorgesteld. \nJe zegt je naam en daarna vraag je die van hem. Je bedenkt je ook dat je de komende uren naast hem zit dus probeer je aardig te zijn en reageer je heel lief met wat die allemaal zegt. \nNa een uur met hem te praten zie je in dat hij eigenlijk niet zo gemeen is maar juist heel aardig . hij vraagt aan je waarom je eigenlijk naar aarde wilt gaan want je lijkt op een normalen alien die gewoon alles voor elkaar heeft. \nJe wilt het hem vertellen maar bent bang met hoe die zou reageren dus draait je gezicht om en zegt niks. Hij merkt dat je het geen leuk onderwerp vindt en begint te praten over iets anders. \nHij vraagt je nu wat je zou willen doen als je op aarde bent.")
    time.sleep(1)
    question8 = input ("vraag: A.Je gaat proberen te veranderen \n B. je gaat liefde proberen te zoeken \n C.je gaat proberen de wereld te veranderen voor aliens")
    if question8 == "A" or question8 == "b":
        time.sleep(1)
        print ("je vertelt het aan hem")
        vraag12()
    elif question8 == "B" or question8 == "b":
        time.sleep(1)
        print("je vertelt het aan hem")
        vraag14()
    elif question8 == "C" or question8 == "c":
        time.sleep(1)
        print("je vertelt het aan hem")
        vraag19()
    else: 
        time.sleep(1)
        print("antwoord met A, B of C")

def vraag9():
    time.sleep(1)
    print("Je loopt naar hem toe en begint met hem te praten jullie lachen en kijken elkaar diep in de ogen aan. Hij vraagt waar je vandaan komt en jij zegt dat je hier ver vandaan komt want je bent en blijft natuurlijk een alien. \n10 jaar later je hebt hem eindelijk vertelt dat je een alien bent hij vindt dat niet erg (zijn naam is Lucas) Lucas kijkt juist heel blij en lacht naar je. \nHij is namelijk zelf ook een alien maar hij wist niet hoe hij je het moest vertellen jullie kijken elkaar heel blij en gelukkig aan je kust hem en verteld hem dat je hem leuk vindt en dat je dat al sinds het begin dat jullie elkaar kennen al doet. \nHij lacht en zegt dat hij je ook leuk vindt hij vraagt daarom ook of je zijn vriendin wilt zijn. Je zegt ja met een grote glimlach.\nVier jaar later jullie zijn getrouwd en hebben een gezin met een dochter zoon en een hond jullie hebben dus ook een gelukkig einde.")
    time.sleep(1)
    print ("wil je nog een keer?")
    time.sleep(1)
    print("ja of nee?")
    E = input ()
    if E == "ja":
        print ("good luck!")
        start()
    elif E == "nee":
        print ("okay byee")
    else:
        print("antwoord met ja of nee")
        vraag9()
        

def vraag10():
    time.sleep(1)
    print ("Je aait het wezen en de mensen kijken je blij aan ze merken dat je een aardige alien bent en dat je het diertje niks aan gaat doen. \nJe lacht naar de mensen en loopt door met je vrienden maar alsnog wordt je raar aan gekeken door sommige je bent bang dat ze jullie iets aan gaan doen dus je vertelt je vrienden om naar het ruimte schip te gaan. \nJullie lopen der naar toen en zien der mensen met geweren en anderen wapens je bent bang en weet niet wat jullie moeten doen. \nGa je naar je ruimteschip of ren je naar het bos met je nieuwe vrienden….")
    time.sleep(1)
    question10 = input ("vraag: A. je gaat naar het ruimte schip \nB. je rent weg in het bos")
    if question10 == "A" or question10 == "a":
       time.sleep(1)
       print ("je gaat naar het ruimteschip")
       vraag20()
    elif question10 == "B" or question10 == "b":
        time.sleep(1)
        print("je rent weg")
        vraag7()
    else:
        print("antwoord met A of B")
        vraag10()

def vraag11():
    time.sleep(1)
    print ("Je blijft staan maar omdat je bijna gaat vallen moet je alsnog naast iemand gaan zitten je ziet dat er ook plek is naast een andere alien die ziet er wat aardiger uit je gaat naast der zitten. \nZe verteld dat haar naam Emeraldia is en dat ze van Saturnus komt ook vertelt ze dat ze naar aarde komt om liefde te vinden en ze vraagt zich af wat jij wilt doen als je op aarde bent. \nJe begint goed na te de denken en vertelt dat je…. ")
    time.sleep(1)
    question11 = input ("A. de wereld veranderen \nB. liefde vinden \nC je gaat je zelf proberen te veranderen.")
    if question11 == "A" or question11 == "a":
        time.sleep(1)
        print("je vertelt het")
        vraag19()
    elif question11 == "B" or question11 == "b":
        time.sleep(1)
        print("je vertelt het")
        vraag14()
    elif question11 == "C" or question11 == "c":
        time.sleep(1)
        print("je vertelt het")
        vraag12()
    else: 
        print("antwoord met A of B")
        vraag11()

def vraag12():
    time.sleep(1)
    print("Je vertelt dat je je zelf gaat proberen te veranderen om bij de mensen te horen ook vertel je dat je blij bent als het lukt. Hij lacht je uit en zegt dat het niet kan want mensen gaan nooit veranderen en ook nooit om je geven. Je lacht en denkt dat het je wel gaat lukken  en zegt dat hij gewoon vertrouwen in je moet hebben. Hij zegt sorry en jullie praten verder na een tijdje komen jullie aan op aarde en vragen je vrienden waar jij naar toe wilt je hebt keuze uit drie steden naar welke van de 3 ga je……")
    time.sleep(1)
    question12 = input ("A.	Alkmaar \nB.Amsterdam \nC.Rotterdam")
    if question12 == "A" or question12 == "a":
        time.sleep(1)
        print("je gaat daar naar toe")
        vraag15()
    elif question12 == "B" or question12 == "b":
        time.sleep(1)
        print("je gaat daar naar toe")
        vraag2()
    elif question12 == "C" or question12 == "c":
        time.sleep(1)
        print("je gaat daar naar toe")
        vraag18()
    else: 
        print ("antwoord met A of B")
        vraag12()

def vraag13():
    time.sleep(1)
    print("Je rent weg maar merkt dat de mensen in pak achter je aan komen je probeert sneller te rennen maar voor dat je het weet hebben ze je gevangen. Ze zeggen dat ze alleen met je willen praten je kijkt hun verbaast aan en vraagt waarom ze je dan boos aankeken. \nZe lachen en zeggen dat het hun werk gezicht is en dat ze wel serieus moeten kijken om serieus genomen te worden. \nDaarna zeggen ze dat de burgermeester met je wilt praten en dat het dringend is omdat ze ook weten dat jij bij dat ruimteschip was. \nJe zegt oke en gaat met hun mee naar het gemeente huis. Ze zeggen dat je moet wachten tot de burgermeester je roept en je zegt oke. \nNa tien minuten komt de burgermeester en zegt die dat je met hem mee moet komen. Je zegt oke en loopt achter hem aan en gaat zitten in zijn kantoor. \nHij begint meteen met het vragen waarom je in het bos was. Je zegt dat je naar de boerderij aan het lopen was en benieuwd was waarom er zoveel mensen waren. \nDe burgermeester zegt oke en vraagt daarna meteen iets wat jij niet had verwacht dat hij je dat zou gaan vragen. Hij vraagt of je een alien bent. \nJe kijkt verbaast en weet niet wat je moet zeggen. Ga je vertellen dat je een alien bent of niet……")
    time.sleep(1)
    question13 = input ("A.	Je vertelt het \nB.Je liegt en zegt dat je geen alien bent \nC.Je zegt niks ")
    if question13 == "A" or question13 == "a":
        time.sleep(1)
        print("je bent eerlijk")
        vraag6()
    elif question13 == "B" or question13 == "b":
        time.sleep(1)
        print("je begint met liegen")
        vraag16()
    elif question13 == "C" or question13 == "c": 
        time.sleep(1)
        print("je houd je mond")
        vraag5()

def vraag14(): 
    time.sleep(1)
    print("Je verteld dat je liefde wilt zoeken op aarde omdat je nu van je planeet af bent en je ruimteschip niet meer werkt. \nJe weet dat je niet meer kan komen naar je planeet en wilt dus ook niet alleen eindigen hij begrijpt het. Opeens voelen jullie dat jullie door de atmosfeer komen van de aarde jullie merkte niet dat jullie al uren met elkaar aan het praten waren. \nJe gaat bij het raam kijken en ziet hoe mooi de wereld is. 1 van je nieuwe vrienden vraagt of je weet naar welke plek je het beste kan gaan jij zegt Nederland want het is een klein landje net onder de zee spiegel. \nMaar waar in Nederland willen jullie landen ?")
    time.sleep(1)
    question14 = input ("A.Alkmaar B.Amsterdam C. Rotterdam")
    if question14 == "A" or question14 == "a":
        time.sleep(1)
        print ("je gaat daar naar toe")
        vraag15()
    elif question14 == "B" or question14 == "b":
        time.sleep(1)
        print("je gaat daar naar toe")
        vraag2()
    elif question14 == "C" or question14 == "c":
        time.sleep(1)
        print("je gaat daar naar toe")
        vraag18()
    else:
        print ("antwoord met A,B of C")
        vraag14()
    
def vraag15():
    time.sleep(1)
    print("Jullie landen in Alkmaar op een boerderij je bedenkt je dat het handig is als jullie je vermommen als mensen . \nje loopt naar de boer en vraagt hem of jullie hier kunnen wonen omdat jullie geen plek hebben en ook geen familie in de buurt hebben. \nDe boer zeg ja maar dan moet je ook wat klusjes doen  je zegt oké en jullie beginnen met helpen op de boerderij. \nNa een paar weken komen er opeens een paar mannen in pak naar jullie toe. De boer loopt naar hun toe en begint met hun te praten opeens wijst hij naar jou en zegt die dat je naar hem toe moet komen maar hij kijkt beangstigend naar je wat ga je doen ren je weg of ga je naar hem toe… ")
    time.sleep(1)
    question15 = input ("A.je rent weg \nB.je gaat naar hem toe")
    if question15 == "A" or question15 == "a":
        time.sleep(1)
        print ("je rent weg")
        vraag13()
    elif question15 == "B" or question15 == "b":
        time.sleep(1)
        print ("je gaat naar hem")
        vraag17()
    else:
        print ("antwoord met A of B")
        vraag15()

def vraag16():
    time.sleep(1)
    print("Je liegt en zeg dat je geen alien je bent maar de burgermeester weet het al en kijkt je kwaad aan hij zegt dat hij weet dat je liegt en dat je moet stoppen anders hebben het slechten gevolgen. \nJe zegt nog steeds dat je der geen bent en zegt dat je weg wilt. Hij zegt oke en wijst je deur maar voor dat je het weet word je neergestoken door de 2 mannen….. EINDE ")
    time.sleep(1)
    print ("wil je nog een keer?")
    time.sleep(1)
    print("ja of nee?")
    F= input ()
    if  F== "ja":
        print ("good luck!")
        start()
    elif F == "nee":
        print ("okay byee")
    else:
        print("antwoord met ja of nee")
        vraag16()

def vraag17():
    time.sleep(1)
    print("Je loopt naar hem toe en vraagt wat er aan de hand is. De boer zegt tegen je dat de mannen met je willen praten ze kijken je heel boos aan. Je bent bang  maar loopt als nog naar ze toe. \nZe zeggen hoi tegen je en je glimlacht naar ze. Ze vragen of je met hun mee kan komen naar het stadshuis en dat je dan met de burgermeester kan gaan praten. Je twijfelt maar gaat alsnog mee. \nAls je aan komt bij de burgermeester beginnen ze meteen met vragen stellen over wat je allemaal doet in je dagelijks leven. Je verteld ze dat je vooral de boer helpt en dat je ook natuurlijk wat dingetjes voor je zelf doet. \nNa het gesprek met hun komt de burgermeester hij wijst je aan en maakt een handbeweging met dat je naar zijn kantoor moet komen. je loopt met hem mee en vraagt waarom je hier bent. \nHij komt meteen op zaken en vertelt dat hij met je wilt praten over aliens. Je kijkt geschokt en vraagt waarom hij dat wilt. \nHij zegt dat hij denkt dat je een alien bent en zegt dat als je er 1 bent dat je dat met liefde tegen hem mag vertellen want dan zorgt die er voor dat je een goed leven krijgt en dat jij er voor kan zorgen dat alle aliens veilig blijven. \nDus hij vraagt aan je of je een alien bent maar zegt ook meteen dat als je liegt dat hij dat merkt. Dus wat ga je doen ga je het vertellen of lieg je dat je geen alien bent…")
    time.sleep(1)
    question17 = input ("A.je vertelt het \nB. je liegt \nC. je zegt niks")
    if question17 == "A" or question17 == "a":
        time.sleep(1)
        print ("je vertelt het")
        vraag6()
    elif question17 == "B" or question17 == "b":
        time.sleep(1)
        print ("je liegt")
        vraag16()
    elif question17 == "C" or question17 == "C": 
        time.sleep(1)
        print("je zegt niks")
        vraag5()
    else:
        print ("antwoord met A of B")
        vraag17()

def vraag18():
    time.sleep(1)
    print("Jullie gaan naar Rotterdam en landen in een bos. Je vertelt je vrienden dat het handig is om rond te kijken door de stad. \nZe zeggen allemaal oke en jullie beginnen met lopen. Onderweg zien jullie een raar pluizig wezen met een mens naast het wezen. \nHet wezen begint te grommen naar je dus je gromt terug ze zeggen tegen je dat het wezen je niks doet en wijst naar je hand en om te zeggen dat je het kan aaien. ")
    time.sleep(1)
    question18 = input ("A. je aait het wezen \n B. je staart het wezen alleen aan")
    if question18 == "A" or question18 == "a":
        time.sleep(1)
        print ("je aait het wezen")
        vraag10()
    elif question18 == "B" or question18 == "b":
        time.sleep(1)
        print ("je staart het aan")
        vraag4()
    else:
        print ("antwoord met A of B")
        vraag18()

def vraag19():
    time.sleep(1)
    print("Je vertelt dat je de wereld wilt veranderen en de wereld beter wilt maken voor de aliens omdat je weet dat de mens een slecht verleden hebben met aardig zijn. \nZe glimlacht naar je en zegt dat het een mooie idee is en wie weet misschien lukt het je ook. \nJe lacht terug naar der en jullie praten nog wat door na een tijdje merken jullie dat jullie door de atmosfeer gaan en je vrienden vragen aan jou waar jij graag zou willen landen je weet dat er een mooi land genaamd Nederland is maar in welke stad zou je willen landen……")
    time.sleep(1)
    question19 = input ("A. je aait het wezen \n B. je staart het wezen alleen aan")
    if question19 == "A" or question19 == "a":
        time.sleep(1)
        print ("je gaat daar naar toe")
        vraag15()
    elif question19 == "B" or question19 == "b":
        time.sleep(1)
        print ("je gaat daar naar toe")
        vraag2()
    elif question19 == "C" or question19 == "c":
        time.sleep(1)
        print("je gaat daar naar toe")
        vraag18()
    else:
        print ("antwoord met A,B of C")
        vraag19()

def vraag20():
    time.sleep(1)
    print("Je gaat naar het ruimteschip maar voor dat je dat doet verander je je zelf eerst effe snel als een mens. Je zegt tegen je vrienden dat je dat je het beter zelf alleen kan doen en dat hun naar de boerderij moeten rennen die daar in de buurt zit ze zeggen oke en je loopt naar het ruimteschip je vraagt een van de mannen wat er aan de hand is en hij zegt dat je je geen zorgen moet maken alleen wel dat je moet opletten dat er geen aliens zijn want dat zijn gevaarlijke wezens. \nJe kijkt verbaast en zegt dat aliens niet zo erg kunnen zijn en dat ze ook wel aardig kunnen zijn. De mensen lachen je uit en zeggen dat je een goede grap maakte. \nUiteindelijk vertellen ze je dat je weg moet en dat je ze met rust moet laten. Je zegt oke en gaat ook naar de boerderij. Eenmaal aan gekomen bij de boerderij vragen je vrienden wat die mensen wouden. \nJe vertelt het verhaal wat de mensen je vertelde en ze kijken verbaast hoezo zouden ze dat doen en waarom denken ze dat jullie gevaarlijk zijn? Je zegt niks op hun vraag en loopt naar de boer je vraagt of jullie hier mogen wonen als jullie helpen met klusjes. \nDe boer zegt ja en jullie beginnen met helpen. Een paar dagen later komen er 2 mannen in pak naar de boerderij en vragen aan de boer of ze met jou mogen praten ze kijken je een beetje boos aan en je vraagt je af wat er aan de hand is. De boer vraagt of je naar hem toe kan komen je kijkt hem aan en weet niet wat je moet doen. \nGa je naar hem toe of ren je weg…")
    question20 = input ("Aje rent weg \nB je loopt naar hem toe")
    if question20 == "A" or question20 == "a":
        time.sleep(1)
        print ("je rent weg")
        vraag13()
    elif question20 == "B" or question20 == "b":
        time.sleep(1)
        print ("je gaat naar hem toe")
        vraag17()
    else:
        print ("antwoord met A of B")
        vraag20()

def vraag21():
    time.sleep(1)
    print("Je loopt door en doet alsof er niks gebeurt is maar na een paar dagen komt hij naar jou toe hij vraagt wie je bent en je zegt dat je iemand uit een andere stad bent. Maar hij geloofd je niet maar hij vindt je wel heel speciaal hij lacht naar je en kijkt je blij aan hij vraagt of je iets te doen hebt en je zegt nee. \nJullie beginnen met daten en na 10 jaar vraagt hij of je met hem wilt trouwen natuurlijk zeg je ja maar op je bruiloft bedenk je dat je het hem wel moet vertellen dus je loopt naar hem toe. \nHij vraagt wat er aan de hand is en je zegt dat je met hem moet praten over iets heel belangrijks. Je vertelt hem dat je een alien bent hij schrikt en zegt dat het niet waar kan zijn want je lijkt precies op een mens. \nJe zegt dat je je kan vermommen en hij kijkt je boos aan na al die jaren heb je het hem nooit vertelt. Je zegt sorry maar voor dat je het weet wordt je neergestoken door je waren liefde…. EINDE ")
    time.sleep(1)
    print ("wil je nog een keer?")
    time.sleep(1)
    print("ja of nee?")
    G= input ()
    if G == "ja":
        print ("good luck!")
        start()
    elif G == "nee":
        print ("okay byee")
    else:
        print("antwoord met ja of nee")
        vraag21()

start()  



