import time

def start():
    
    time.sleep(1)
    print("Het is een rustige dag, je zit gewoon te reizen in je ruimteschip en rond te kijken door het heelal. Plotseling wordt je gebeld door je moeder, ze vraagt wat je wilt eten als je terug bent op mars. Je verteld haar wat je wilt eten, tot dat je plotseling  in een meteorieten regen vast komt. Je ruimteschip begint helemaal raar te doen en je kan het niet meer besturen. Je staat op een punt dat je niet meer weet wat je moet doen, je kijkt het heelal nog 1 keer aan en denkt bij je zelf zou ik gaan springen of zou ik gewoon kijken of ik hier uit kan komen ? Je denkt uiteindelijk goed na en je zegt tegen je zelf dat je der uit gaat komen je leunt het stuur zo ver naar links dat je der uit komt. Maar helaas zie je dat je ruimteschip helemaal beschadigd is wat moet je nu doen……")

    time.sleep(1)
    question= input("vraag: A. ga naar aarde \nB.blijf waar je bent ")
    if question == "A":
        time.sleep(1)
        print("je gaat nu naar de aarde")
        vraag3()
    elif question == "B":
        time.sleep(1)
        print("je blijft nu waar je bent.")
        vraag1()
    else:
        time.sleep(1)
        print("antwoord met A of B")
        start()



def vraag1():
 
 time.sleep(1)
 print('je bent dood. \nGAME OVER')
    
    
 


#vraag de vraag en stuur a/b/c terug naar de vragen lijst
def vraag3():
    #de time.sleep(1) is zodat je de tekst 1 seconden wacht met laten zien zodat het er goed uit ziet je kan de 1 veranderen naar een ander getal of weghalen als je het niet mooi vind
    time.sleep(1)
    print("text")
    time.sleep(1)
    while True:
        #de .lower() is zodat als je met hooftletter a/b/c antwoord dat het kleine letter word dus het maakt niet uit of je a of A antwoord
        question3 = input("vraag: ").lower()
        if question3 == "a":
            time.sleep(1)
            print("text")
            break
        elif question3 == "b":
            time.sleep(1)
            print("text")
            break
        elif question3 == "c":
            time.sleep(1)
            print("text")
            break
        else:
            time.sleep(1)
            print("antwoord met A, B of C")
    return question3

#vraag de vraag en stuur a/b/c terug naar de vragen lijst
def vraag4():
    #de time.sleep(1) is zodat je de tekst 1 seconden wacht met laten zien zodat het er goed uit ziet je kan de 1 veranderen naar een ander getal of weghalen als je het niet mooi vind
    time.sleep(1)
    print("text")
    time.sleep(1)
    while True:
        #de .lower() is zodat als je met hooftletter a/b/c antwoord dat het kleine letter word dus het maakt niet uit of je a of A antwoord
        question4 = input("vraag: ").lower()
        if question4 == "a":
            time.sleep(1)
            print("text")
            break
        elif question4 == "b":
            time.sleep(1)
            print("text")
            break
        elif question4 == "c":
            time.sleep(1)
            print("text")
            break
        else:
            time.sleep(1)
            print("antwoord met A, B of C")
    return question4

start()

#als je a antwoord bij vraag 1 word vraag 2 geactiveerd b word vraag 3 geactiveerd en c word vraag 4 geactiveerd
vrg1 = vraag1()
if vrg1 == "a":
    vrg2 = vraag2()
elif vrg1 == "b":
    vrg3 = vraag3()
elif vrg1 == "c":
    vrg4 = vraag4