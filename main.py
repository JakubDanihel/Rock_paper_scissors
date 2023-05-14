import random
import re

#body of main function of game
#telo hlavnej funkcie hry

respons = ['yes', 'no']

def check_status():
    odpoved = ["yes", "no"]

    #spustenie hry
    #start of the game
    while True:
        try:
            nova_hra = input("Wanna play again? (yes or no): ")

            #Zistenie co pouzil pouzivatel
            #Check user input
            if nova_hra.lower() == "yes":
                return True
            else:
                print("Thanks for playing!")
                exit()
        #zachytenie chyby
        #catch error
        except ValueError as err:
            print(err)

#telo hry
#body of game
def hra():
    play = True

    while play:
        print("Rock, Paper, Scissors")

        #get user input
        #ziskaj uzivatelsky vstup
        pouzivatel = input("Choose your weapon traverse: [R]ock, [P]aper or [S]cissors: ")

        #check if input is valid
        #zisti ci vstup je vhodny
        if not re.match("[SsRrPp]", pouzivatel):
            print("Please use only letter: ")
            print("[R]ock, [P]aper or [S]cissors")
            continue

        print("You chose: ",pouzivatel)
        print("A fine weapon indeed!")

        #Bot si vyberie moznosti s ktorymi bude hrat
        #Choosing the weapon for bot
        moznosti = ['R', 'P', 'S']
        bot_moznosti = random.choice(moznosti)

        print("Lets see if it can beat my choise: ",bot_moznosti)

        #Urcenie vytaza v hre
        #Choosing winconditions
        if bot_moznosti == pouzivatel.upper():
            print("Tie!")
            play = check_status()
        elif bot_moznosti == "R" and pouzivatel.upper() == 'S':
            print("Rock beats scissors. I win!")
            play = check_status()
        elif bot_moznosti == "S" and pouzivatel.upper() == 'P':
            print("Scissors beat paper. I win!")
            play = check_status()
        elif bot_moznosti == "P" and pouzivatel.upper() == "R":
            print("Paper beat scissors. I win!")
            play = check_status()
        else:
            print("You win!")
            play = check_status()



if __name__ == "__main__":
    print("Hello world")
    hra()

