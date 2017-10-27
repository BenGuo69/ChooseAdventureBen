import time

def Duke():
    print("You are now Duke, the Top Laner for SKT.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Trundle"
                             "\n2. Poppy")


def Bengi():
    print("You are now Bengi, the Jungler for SKT.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Rengar"
                             "\n2. Jarvan IV")

def Faker():
    print("You are now Faker, the best in the world.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Orianna"
                             "\n2. Ryze")


def Bang():
    print("You are now Bang, the ADC for SKT.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Ezreal"
                             "\n2. Kog'Maw")

def Wolf():
    print("You are now Wolf, the Support for SKT.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Lulu"
                             "\n2. Janna")





def CuVee():
    print("You are now CuVee, the Top Laner for SSG.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Darius"
                             "\n2. Maokai")

def Ambition():
    print("You are now Ambition, the Jungler for SSG.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Nidalee"
                             "\n2. Kha'Zix")

def Crown():
    print("You are now Crown, the Mid Laner for SSG.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Victor"
                             "\n2. Cassiopeia")

def Ruler():
    print("You are now Ruler, the ADC for SSG.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Jhin"
                             "\n2. Caitlyn")

def CoreJJ():
    print("You are now CoreJJ, the Support for SSG.")
    time.sleep(1.75)
    print("Right now, champion select is in progress")
    time.sleep(1.75)
    print("Who do you wish to pick?")
    time.sleep(1.5)
    CHAMP = raw_input("1. Karma"
                             "\n2. Soraka")









def SKT():
    print("Welcome to SKT T1, who has won the last two World Championships.")
    time.sleep(2)
    while True:
        roleselect = raw_input("Now, do you wish to be"
                            "\n1. Duke"
                            "\n2. Bengi"
                            "\n3. Faker"
                            "\n4. Bang"
                            "\n5. Wolf")
        if roleselect in ["1", "Duke", "duke"]:
            Duke()
            break
        elif roleselect in ["2", "Bengi", "bengi"]:
            Bengi()
            break
        elif roleselect in ["3", "Faker", "faker"]:
            Faker()
            break
        elif roleselect in ["4", "Bang", "bang"]:
            Bang()
            break
        elif roleselect in ["5", "Wolf", "wolf"]:
            Wolf()
            break
        else:
            print("That's not a person....")
            time.sleep(1.5)



def SSG():
    print("Welcome to Samsung Galaxy, who has been the underdogs in this season.")
    time.sleep(2)
    while True:
        roleselect = raw_input("Now, do you wish to be"
                            "\n1. CuVee"
                            "\n2. Ambition"
                            "\n3. Crown"
                            "\n4. Ruler"
                            "\n5. CoreJJ")
        if roleselect in ["1", "CuVee", "cuVee", "cuvee", "Cuvee"]:
            CuVee()
            break
        elif roleselect in ["2", "Ambition", "ambition"]:
            Ambition()
            break
        elif roleselect in ["3", "Crown", "crown"]:
            Crown()
            break
        elif roleselect in ["4", "Ruler", "ruler"]:
            Ruler()
            break
        elif roleselect in ["5", "CoreJJ", "corejj", "coreJJ", "Corejj"]:
            CoreJJ()
            break
        else:
            print("That's not a person....")
            time.sleep(1.5)



def main():
    print("Welcome to LoL Esports: World Champions 2016.")
    time.sleep(2)
    print("This year, SKT T1 will face against Samsung Galaxy in Staples Center, Los Angeles.")
    time.sleep(3)
    while True:
        team = raw_input("Which team do you wish to be on?"
                        "\n1. SKT"
                        "\n2. SSG")
        if team in ["1", "SKT", "skt", "Skt"]:
            SKT()
            break
        elif team in ["2", "SSG", "ssg", "Ssg"]:
            SSG()
            break
        else:
            print("That's not a valid team.")
            time.sleep(1.75)

main()