import time
import webbrowser
import sys



def LegendsNeverDie(x):
    if x in ["1", "Yes", "yes"]:
        print("Alright man heres the money...")
        time.sleep(2)
        print("SIKE YOU AIN't GETTING NOTHING")
    elif x in ["2", "No", "no"]:
        print("Ok bye :)")
    else:
        print("Well I don't know what you just said but...")
        time.sleep(2)
        print("Bye :)")


def YordleCity():
    global after
    print("You are now on your way to Yordle City")
    time.sleep(2)
    print("Walking, you suddenly see Teemo hiding in the bushes, looking afraid")
    time.sleep(2)
    print("You walk towards him to ask what's going on")
    time.sleep(2)
    print("But, a dark mask suddenly appears in front of you and laughs maniacally.")
    time.sleep(2)
    url = "https://vignette.wikia.nocookie.net/vsbattles/images/a/a6/Zed2.png/revision/latest?cb=20161213163019"
    webbrowser.open(url)
    time.sleep(5)
    print("Zed shadow steps behind you and stabs you in the back")
    time.sleep(1)
    print("You turn around helplessly as you bleed out.")
    if itemSelect in ["3", "guardian angel", "Guardian Angel", "Guardian angel"]:
        print("But, because of Guardian Angel, you revived")
        time.sleep(1.5)
        print("Quickly with your leftover " + str(playerGold3) + " gold, you threw it at Zed and ran away." )
        time.sleep(2)
        while True:
            yordle = raw_input("Now, do you choose to "
                               "\n1. Fight Zed "
                               "\n2. Go home")
            if yordle in ["1", "Fight Zed", "fight zed", "Fight zed"]:
                print("You simply walked back to Zed and got killed again.")
                time.sleep(2)
                print("Smart Choice!!! :)")
                time.sleep(2)
                print("The End.")
                break
            elif yordle in ["2", "Go Home", "go home", "Go home"]:
                print("You reached your house and jumped on the bed")
                time.sleep(2)
                print("You think you are safe, but...")
                time.sleep(1.5)
                print("Zed appears behind you...")
                time.sleep(2)
                url = "http://cdn5.theblackandblue.com/wp-content/uploads/2011/07/blood_dripping_off_wall.jpg"
                webbrowser.open(url)
                time.sleep(3)
                print("The End......")
                time.sleep(4)
                after = raw_input("Oh you haven't left? Do you want money?"
                                  "\n1. Yes"
                                  "\n2. No")
                LegendsNeverDie(after)
                break

            else:
                print("That's not a move you can make.")
                time.sleep(1.5)

    else:
        print("Zed outplayed you and you're bad at this champion.")
        time.sleep(1.5)
        print("The End.....")

def Noxus():
    print("After you reached Noxus, you discover a country in war instead of discovering Zed.")
    time.sleep(2.5)
    print("Suddenly, Pantheon's spear stabs you right through the heart.")
    time.sleep(2.5)
    if itemSelect in ["3", "guardian angel", "Guardian Angel", "Guaridan angel"]:
        print("But, because of Guardian Angel, you revived")
        time.sleep(1.5)
        print("Because of your level " + str(playerLevel3) + ", you used your flash ability to get away.")
        time.sleep(2)
        doyou = raw_input("Do you "
                          "\n1. Run away "
                          "\n2. Find Zed")
        while True:
            if doyou in ["run away", "Run Away", "Run away", "1"]:
                print("ZED POPS OUTTA NOWHERE!!!!!!!")
                time.sleep(2)
                zed = "http://i.imgur.com/7zsuZZG.png"
                webbrowser.open(zed)
                time.sleep(5)
                print("You were sliced into pieces by the shuriken. The End.")
                break
            elif doyou in ["find zed", "Find Zed", "Find zed", "2"]:
                print("While roaming around the battlefield, you got killed "
                      "\nby Caitlyn's ultimate, Ace In The Hole.")
                time.sleep(2.5)
                print("The End.")
                break
            else:
                print("That's not a valid option.")
                time.sleep(1.5)
    else:
        print("You watch yourself helplessly bleed out....")
        time.sleep(2)
        print("The End...")

def Demacia():
    print("While on your way there, you see Zed meditating his Shadow Powers on a rock.")
    time.sleep(2)
    print("You creep towards Zed slowly.")
    time.sleep(1.5)
    print("Suddenly, Zed throws out his shadow at you, ready for assult.")
    if itemSelect in ["2", "black cleaver", "Black Cleaver", "Black clever"] and champSelect in ["3", "Irelia", "irelia"]:
        print("Because of the Black Cleaver, you narrowly avoided his shadows and used your Blade Dash "
              "\nto kill Zed. You have avenged your family.")
        time.sleep(4)
        print("The End")

    elif itemSelect in ["1", "Phantom dancer", "Phantom Dancer", "phantom dancer"] and champSelect in ["2", "Jhin", "jhin"]:
        print("Because of the Phantom Dancer that you purchased, you used your ultimate, Curtain's Call, "
              "\nand destroyed Zed once and for all with critical hits.")
        time.sleep(4)
        print("The End")

    elif itemSelect in ["2", "black cleaver", "Black Cleaver", "Black clever"] and champSelect in ["1", "Yasuo", "yasuo"]:
        print("Because of the Black Cleaver that you purchased, you used your ultimate, Last Breath, "
              "\nand sliced Zed to pieces.")
        time.sleep(4)
        print("The End")
    else:
        time.sleep(2)
        print("You dead boi")

    if itemSelect in ["3", "guardian angel", "Guardian Angel", "Guardian angel"]:
        print("He teleports behind you, and slices your body in half.")
        time.sleep(2)
        print("But, because of the purchase of the Guardian Angel, you revived.")
        time.sleep(2)
        while True:
            ok = raw_input("Now, do you try to go for "
                           "\n1. Attack "
                           "\nor "
                           "\n2. Defense")
            if ok in ["Attack", "attack", "1"] and champSelect in ["3", "Irelia", "irelia"]:
                print("With your ultimate, Transcendent Blades, you prick 3 holes in Zed's body..... "
                      "\nHe fades away........ "
                      "\nThe End")
                break
            elif ok in ["Attack", "attack", "1"] and champSelect in ["2", "Jhin", "jhin"]:
                print("You were too slow in reacting. Zed simply kills you again. "
                      "\nThe End.")
                break
            elif ok in ["Defense", "defense", "2"]:
                print("You really can't defend against such a powerful guy, you died.")
                time.sleep(2)
                print("The End......")
                break
            elif ok in ["Attack", "attack", "1"] and champSelect in ["1", "Yasuo", "yasuo"]:
                print("You used Steel Tempest to stab Zed, but he teleports behind you and throws a shuriken. "
                      "\nBut, because of Yasuo's Way of the Wanderer Passive, you blocked the shruiken.")
                time.sleep(3)
                while True:
                    justyasuo = raw_input("You can use "
                                          "\n1. Windwall "
                                          "\n2. Sweeping Blade "
                                          "\nWhich one do you choose?")
                    if justyasuo in ["1", "Windwall", "windwall"]:
                        print("Zed uses his shadows to get past your Windwall, and stabs you in the heart. "
                              "\nTHE END....")
                        break
                    elif justyasuo in ["2", "Sweeping Blade", "sweeping blade", "Sweeping blade"]:
                        print("You go in for the attack, and narrowly dodges Zed's Shadow Slash.")
                        time.sleep(1.5)
                        print("Then, you turn around, and throws your leftover " + str(playerGold3) + " gold at Zed's face.")
                        time.sleep(2)
                        print("Zed dies because of the impact.")
                        time.sleep(1.75)
                        print("CY@")
                        time.sleep(2)
                        url = "https://www.youtube.com/watch?v=4Q46xYqUwZQ"
                        webbrowser.open(url)
                        break

                    else:
                        print("This skill is on cooldown right now.")
                        time.sleep(1.5)
            else:
                print("That's not a valid move.")
                time.sleep(1.5)

def PhantomDancer():
    global playerLevel1
    global playerGold1
    playerLevel = 1
    playerGold1 = 4000
    print("The Phantom Dancer will make you attack faster and sometimes crictle hit Zed.")
    time.sleep(2)
    playerGold1 = playerGold1 - 4000
    playerLevel1 = playerLevel + 1
    print("Gold left:" + str(playerGold1))
    print("Level:" + str(playerLevel1))
    time.sleep(2)
    while True:
        crossroad = raw_input("Now, it's time to find Zed. You come upon a crossroad that leads to either "
                              "\n1. Yordle City "
                              "\n2. Noxus "
                              "\n3. Demacia "
                              "\nWhich do you choose?")
        if crossroad in ["1", "Yordle City", "yordle city", "Yordle city"]:
            YordleCity()
            break
        elif crossroad in ["2", "Noxus", "noxus"]:
            Noxus()
            break
        elif crossroad in ["3", "Demacia", "demacia"]:
            Demacia()
            break
        else:
            print("That's not a valid city.")

def BlackCleaver():
    global playerLevel2
    global playerGold2
    playerLevel2 = 1
    playerGold2 = 4000
    print("The Black Cleaver will increase your defense, and will make it easier to track Zed's shadows.")
    time.sleep(2)
    playerGold2 = playerGold2 - 3800
    playerLevel2 = playerLevel2 + 1
    print("Gold left:" + str(playerGold2))
    print("Level:" + str(playerLevel2))
    time.sleep(2)
    while True:
        crossroad = raw_input("Now, it's time to find Zed. You come upon a crossroad that leads to either "
                              "\n1. Yordle City "
                              "\n2. Noxus "
                              "\n3. Demacia")
        if crossroad in ["1", "Yordle City", "yordle city", "Yordle city"]:
            YordleCity()
            break
        elif crossroad in ["2", "Noxus", "noxus"]:
            Noxus()
            break
        elif crossroad in ["3", "Demacia", "demacia"]:
            Demacia()
            break
        else:
            print("That's not a valid city.")

def GuardianAngel():
    global playerLevel3
    global playerGold3
    playerLevel3 = 1
    playerGold3 = 4000
    print("Excellent Choice! This item will revive you once Zed has defeated you. "
          "\nAlso, Your attacks against zed will hit a lot harder.")
    time.sleep(2)
    playerGold3 = playerGold3 - 3000
    playerLevel3 = playerLevel3 + 2
    print("Gold left:" + str(playerGold3))
    print("Level:" + str(playerLevel3))
    time.sleep(2)
    while True:
        crossroad = raw_input("Now, it's time to find Zed. You come upon a crossroad that leads to either "
                              "\n1. Yordle City "
                              "\n2. Noxus "
                              "\n3. Demacia")
        if crossroad in ["1", "Yordle City", "yordle city", "Yordle city"]:
            YordleCity()
            break
        elif crossroad in ["2", "Noxus", "noxus"]:
            Noxus()
            break
        elif crossroad in ["3", "Demacia", "demacia"]:
            Demacia()
            break
        else:
            print("That's not a valid city.")

def Yasuo():
    global itemSelect
    print("You have chosen Yasuo, The Unforgiven.")
    time.sleep(1.5)
    print("Zed has framed you for killing his father.")
    time.sleep(1.5)
    print("It's time to prove yourself to the Ionians.")
    time.sleep(1.5)
    while True:
        itemSelect = raw_input("Choose your item to assist you in defeating Zed. "
                               "\n1. Phantom Dancer "
                               "\n2. Black Cleaver "
                               "\n3. Guardian Angel")
        if itemSelect in ["1", "phantom dancer", "Phantom Dancer", "Phantom dancer"]:
            PhantomDancer()
            break
        elif itemSelect in ["2", "black cleaver", "Black Cleaver", "Black clever"]:
            BlackCleaver()
            break
        elif itemSelect in ["3", "guardian angel", "Guardian Angel", "Guaridan angel"]:
            GuardianAngel()
            break
        else:
            print("That's not a valid item.")

def Jhin():
    global itemSelect
    print("You have chosen Jhin, The Virtuoso.")
    time.sleep(1.5)
    print("Zed has murdered your entire family.")
    time.sleep(1.5)
    print("It's time to get revenge for your family.")
    time.sleep(1.5)
    while True:
        itemSelect = raw_input("Choose your item to assist you in defeating Zed. "
                               "\n1. Phantom Danc  er "
                               "\n2. Black Cleaver "
                               "\n3. Guardian Angel")
        if itemSelect in ["1", "phantom dancer", "Phantom Dancer", "Phantom dancer"]:
            PhantomDancer()
            break
        elif itemSelect in ["2", "black cleaver", "Black Cleaver", "Black clever"]:
            BlackCleaver()
            break
        elif itemSelect in ["3", "guardian angel", "Guardian Angel", "Guaridan angel"]:
            GuardianAngel()
            break
        else:
            print("That's not a valid item.")

def Irelia():
    global itemSelect
    print("You have chosen Irelia, The Will of The Blades.")
    time.sleep(1.5)
    print("Your father died while trying to protect you from Zed.")
    time.sleep(1.5)
    print("It's time to avenge your father.")
    time.sleep(1.5)
    while True:
        itemSelect = raw_input("Choose your item to assist you in defeating Zed. "
                               "\n1. Phantom Dancer "
                               "\n2. Black Cleaver "
                               "\n3. Guardian Angel")
        if itemSelect in ["1", "phantom dancer", "Phantom Dancer", "Phantom dancer"]:
            PhantomDancer()
            break
        elif itemSelect in ["2", "black cleaver", "Black Cleaver", "Black clever"]:
            BlackCleaver()
            break
        elif itemSelect in ["3", "guardian angel", "Guardian Angel", "Guardian angel"]:
            GuardianAngel()
            break
        else:
            print("That's not a valid item.")

def main():
    global champSelect
    print("This is the story of Ionia's Revenge.")
    time.sleep(1)
    print("The Shadow Master, Zed, has gone rogue and is on a killing spree.")
    time.sleep(2)
    print("You must kill Zed to bring back peace to Ionia.")
    time.sleep(2)
    print("We know Zed has left Ionia and has gone to a nearby city.")
    time.sleep(2)
    while True:
        champSelect = raw_input("Now, choose your champion to fight Zed. "
                                "\n1. Yasuo "
                                "\n2. Jhin "
                                "\n3. Irelia")
        if champSelect in ["1", "Yasuo", "yasuo"]:
            Yasuo()
            break
        elif champSelect in ["2", "Jhin", "jhin"]:
            Jhin()
            break
        elif champSelect in ["3", "Irelia", "irelia"]:
            Irelia()
            break
        else:
            print("That's not a valid champion.")
            time.sleep(1.5)


main()