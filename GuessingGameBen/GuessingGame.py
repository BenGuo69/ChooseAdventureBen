import random
import time

p1guesses = 0
p2guesses = 0
p1wins = 0
p2wins = 0

def hard2():
    print("Welcome to hard mode.")
    time.sleep(2)
    hard()

def medium2():
    print("Welcome to medium mode.")
    time.sleep(2)
    medium()

def easy2():
    print("Welcome to easy mode.")
    time.sleep(2)
    easy()

def easy():
    global p1guesses, p2guesses, p1wins, p2wins
    num = random.randrange(0, 50)
    print(name1 + ", PLEASE STEP UP TO THE COMPUTER.")
    time.sleep(2)
    print("Remember, you only have 10 guesses!")
    time.sleep(2)
    while True:
        numguess1 = input("Please guess a number from 0 - 50:")
        if numguess1 > num:
            print("Your number is too large, guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 10:
                print("Bummer! You lost because you had 10 guesses!")
                time.sleep(2)
                p1guesses = 0
                p2guesses = 0
                p2wins = p2wins + 1
                time.sleep(2)
                print(name1 + ", you have " + str(p1wins) + " wins.")
                print(name2 + ", you have " + str(p2wins) + " wins.")
                if p2wins == 3:
                    time.sleep(2.5)
                    print("Congradulations, " + name2 + ", you have won!")
                    break
                easy()
                break
        elif numguess1 < num:
            print("Your number is too small, guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 10:
                print("Bummer! You lost because you had 10 guesses!")
                time.sleep(2)
                p1guesses = 0
                p2guesses = 0
                p2wins = p2wins + 1
                print(name1 + ", you have " + str(p1wins) + " wins.")
                print(name2 + ", you have " + str(p2wins) + " wins.")
                if p2wins == 3:
                    time.sleep(2.5)
                    print("Congradulations, " + name2 + ", you have won!")
                    break
                easy()
                break
        else:
            print("Alright, " + name1 + " survived with " + str(p1guesses) + " guesses.")
            time.sleep(1.25)
            num = random.randrange(0, 50)
            print(name2 + ", PLEASE STEP UP TO THE COMPUTER.")
            time.sleep(2)
            print("Remember, you only have 10 guesses!")
            time.sleep(2)
            while True:
                numguess2 = input("Please guess a number from 0 - 50:")
                if numguess2 > num:
                    print("Your number is too large, guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 10:
                        print("Bummer! You lost because you had 10 guesses!")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1wins = p1wins + 1
                        print(name1 + ", you have " + str(p1wins) + " wins.")
                        print(name2 + ", you have " + str(p2wins) + " wins.")
                        if p1wins == 3:
                            time.sleep(2.5)
                            print("Congradulations, " + name1 + ", you have won!")
                            break
                        easy()
                        break
                elif numguess2 < num:
                    print("Your number is too small, guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 10:
                        print("Bummer! You lost because you had 10 guesses!")
                        p1guesses = 0
                        p2guesses = 0
                        time.sleep(2)
                        p1wins = p1wins + 1
                        print(name1 + ", you have " + str(p1wins) + " wins.")
                        print(name2 + ", you have " + str(p2wins) + " wins.")
                        if p1wins == 3:
                            time.sleep(2.5)
                            print("Congradulations, " + name1 + ", you have won!")
                            break
                        easy()
                        break
                else:
                    print("Alright, " + name2 + " survived with " + str(p2guesses) + " guesses.")
                    time.sleep(2)
                    print(name1 + " TOTAL GUESSES: " + str(p1guesses))
                    print(name2 + " TOTAL GUESSES: " + str(p2guesses))
                    time.sleep(2)
                    print("Ok, let's continue.")
                    easy()

def medium():
    global p1guesses, p2guesses, p1wins, p2wins
    num = random.randrange(0, 100)
    print(name1 + ", PLEASE STEP UP TO THE COMPUTER.")
    time.sleep(2)
    print("Remember, you only have 15 guesses!")
    time.sleep(2)
    while True:
        numguess1 = input("Please guess a number from 0 - 100:")
        if numguess1 > num:
            print("Your number is too large, guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 15:
                print("Bummer! You lost because you had 15 guesses!")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2wins = p2wins + 1
                print(name1 + ", you have " + str(p1wins) + " wins.")
                print(name2 + ", you have " + str(p2wins) + " wins.")
                if p2wins == 3:
                    time.sleep(2.5)
                    print("Congradulations, " + name2 + ", you have won!")
                    break
                medium()
                break
        elif numguess1 < num:
            print("Your number is too small, guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 15:
                print("Bummer! You lost because you had 15 guesses!")
                p1guesses = 0
                p2guesses = 0
                time.sleep(2)
                p2wins = p2wins + 1
                print(name1 + ", you have " + str(p1wins) + " wins.")
                print(name2 + ", you have " + str(p2wins) + " wins.")
                if p2wins == 3:
                    time.sleep(2.5)
                    print("Congradulations, " + name2 + ", you have won!")
                    break
                medium()
                break
        else:
            print("Alright, " + name1 + " survived with " + str(p1guesses) + " guesses.")
            time.sleep(1.25)
            num = random.randrange(0, 100)
            print(name2 + ", PLEASE STEP UP TO THE COMPUTER.")
            time.sleep(2)
            print("Remember, you only have 15 guesses!")
            time.sleep(2)
            while True:
                numguess2 = input("Please guess a number from 0 - 100:")
                if numguess2 > num:
                    print("Your number is too large, guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 15:
                        print("Bummer! You lost because you had 15 guesses!")
                        time.sleep(2)
                        p1guesses = 0
                        p2guesses = 0
                        p1wins = p1wins + 1
                        print(name1 + ", you have " + str(p1wins) + " wins.")
                        print(name2 + ", you have " + str(p2wins) + " wins.")
                        if p1wins == 3:
                            time.sleep(2.5)
                            print("Congradulations, " + name1 + ", you have won!")
                            break
                        medium()
                        break
                elif numguess2 < num:
                    print("Your number is too small, guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 15:
                        print("Bummer! You lost because you had 15 guesses!")
                        time.sleep(2)
                        p1guesses = 0
                        p2guesses = 0
                        p1wins = p1wins + 1
                        print(name1 + ", you have " + str(p1wins) + " wins.")
                        print(name2 + ", you have " + str(p2wins) + " wins.")
                        if p1wins == 3:
                            time.sleep(2.5)
                            print("Congradulations, " + name1 + ", you have won!")
                            break
                        medium()
                        break
                else:
                    print("Alright, " + name2 + " survived with " + str(p2guesses) + " guesses.")
                    time.sleep(2)
                    print(name1 + " TOTAL GUESSES: " + str(p1guesses))
                    print(name2 + " TOTAL GUESSES: " + str(p2guesses))
                    time.sleep(2)
                    print("Ok, let's continue.")
                    medium()

def hard():
    global p1guesses, p2guesses, p1wins, p2wins
    num = random.randrange(0, 200)
    print(name1 + ", PLEASE STEP UP TO THE COMPUTER.")
    time.sleep(2)
    print("Remember, you only have 30 guesses!")
    time.sleep(2)
    while True:
        numguess1 = input("Please guess a number from 0 - 200:")
        if numguess1 > num:
            print("Your number is too large, guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 30:
                print("Bummer! You lost because you had 30 guesses!")
                time.sleep(2)
                p1guesses = 0
                p2guesses = 0
                p2wins = p2wins + 1
                print(name1 + ", you have " + str(p1wins) + " wins.")
                print(name2 + ", you have " + str(p2wins) + " wins.")
                if p2wins == 3:
                    time.sleep(2.5)
                    print("Congradulations, " + name2 + ", you have won!")
                    break
                hard()
                break
        elif numguess1 < num:
            print("Your number is too small, guess again.")
            p1guesses = p1guesses + 1
            if p1guesses == 30:
                print("Bummer! You lost because you had 30 guesses!")
                time.sleep(2)
                p1guesses = 0
                p2guesses = 0
                p2wins = p2wins + 1
                print(name1 + ", you have " + str(p1wins) + " wins.")
                print(name2 + ", you have " + str(p2wins) + " wins.")
                if p2wins == 3:
                    time.sleep(2.5)
                    print("Congradulations, " + name2 + ", you have won!")
                    break
                hard()
                break
        else:
            print("Alright, " + name1 + " survived with " + str(p1guesses) + " guesses.")
            time.sleep(1.25)
            num = random.randrange(0, 200)
            print(name2 + ", PLEASE STEP UP TO THE COMPUTER.")
            time.sleep(2)
            print("Remember, you only have 30 guesses!")
            time.sleep(2)
            while True:
                numguess2 = input("Please guess a number from 0 - 200:")
                if numguess2 > num:
                    print("Your number is too large, guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 30:
                        print("Bummer! You lost because you had 30 guesses!")
                        time.sleep(2)
                        p1guesses = 0
                        p2guesses = 0
                        p1wins = p1wins + 1
                        print(name1 + ", you have " + str(p1wins) + " wins.")
                        print(name2 + ", you have " + str(p2wins) + " wins.")
                        if p1wins == 3:
                            time.sleep(2.5)
                            print("Congradulations, " + name1 + ", you have won!")
                            break
                        hard()
                        break
                elif numguess2 < num:
                    print("Your number is too small, guess again.")
                    p2guesses = p2guesses + 1
                    if p2guesses == 30:
                        print("Bummer! You lost because you had 30 guesses!")
                        time.sleep(2)
                        p1guesses = 0
                        p2guesses = 0
                        p1wins = p1wins + 1
                        print(name1 + ", you have " + str(p1wins) + " wins.")
                        print(name2 + ", you have " + str(p2wins) + " wins.")
                        if p1wins == 3:
                            time.sleep(2.5)
                            print("Congradulations, " + name1 + ", you have won!")
                            break
                        hard()
                        break
                else:
                    print("Alright, " + name2 + " survived with " + str(p2guesses) + " guesses.")
                    time.sleep(2)
                    print(name1 + " TOTAL GUESSES: " + str(p1guesses))
                    print(name2 + " TOTAL GUESSES: " + str(p2guesses))
                    time.sleep(2)
                    print("Ok, let's continue.")
                    hard()

def difficulty():
    print("It's time to choose the difficulty, players.")
    time.sleep(1.5)
    print("1. Easy"
          "\n2. Medium"
          "\n3. Hard")
    time.sleep(1.5)
    difficulty = raw_input()
    if difficulty in ["1", "Easy", "easy"]:
        easy2()
    elif difficulty in ["2", "medium", "Medium"]:
        medium2()
    elif difficulty in ["3", "hard", "Hard"]:
        hard2()
    else:
        print("I don't know what you just put, but because of your disrespect, you are going to hard mode..")
        time.sleep(2.5)
        hard2()

def main():
    global name1
    global name2
    print("Welcome to The Fun Guessing Game!")
    time.sleep(1.25)
    print("This game's goal is to guess the correct number that is generated.")
    time.sleep(1.75)
    name1 = raw_input("Enter your name, Player 1:")
    print("Welcome, " + name1 + "!")
    time.sleep(1.25)
    name2 = raw_input("Enter your name, Player 2:")
    print("Welcome, " + name2 + "!")
    time.sleep(1.25)
    print("Be the first to win 3 rounds!!")
    time.sleep(1.5)
    difficulty()

mathgrade = 0
if mathgrade < 1:
    main()
