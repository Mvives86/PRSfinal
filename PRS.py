import random


def game_on():# keeps game going and score

    humanscore = 0
    computerscore = 0
    winner = 0
    score = tools()

    if score == (1, 1):
        print("draw")
    elif score == (1, 2):
        humanscore += 1
        print("You Win!")
    elif score == (1, 3):
        computerscore += 1
        print("You Lose!")
    elif score == (2, 2):
        print("Draw!")
    elif score == (2, 1):
        computerscore += 1
        print("You Lose!")
    elif score == (2, 3):
        humanscore += 1
        print("You Win!")
    elif score == (3, 3):
        print("Draw!")
    elif score == (3, 1):
        humanscore += 1
        print("You Win!")
    elif score == (3, 2):
        computerscore += 1
        print("You Lose!")

    print(humanscore, computerscore)

    if humanscore > 0:
        winner = 99
    elif computerscore > 0:
        winner = 100
    x = input("Do you want to play again? Y/N\n").lower()
    return winner, x




def end():
    print("Thanks for Playing!")


def tools():  # returns the human option and the computers option to input into the game and score
    print("You are about to play Rock, Paper, Scissors!")
    print("Choose your weapon! \n")
    print("1. Paper\n")
    print("2. Rock\n")
    print("3. Scissors\n")
    h = eval(input("Choose '1' '2' or '3':\n "))
    c = random.randint(1, 3)

    if h == 1:
        print("You chose Paper!\n")
    elif h == 2:
        print("You chose Rock!\n")
    elif h == 3:
        print("You chose Scissors!\n")

    if c == 1:
        print("The computer chose Paper!")
    elif c == 2:
        print("The computer chose Rock!")
    elif c == 3:
        print("The computer chose Scissors!")
    return h, c


def main():
    n = 0
    humanscore = 0
    computerscore = 0


    while n < 1:
        print("\n\t1. See the Rules.")
        print("\t2. Play the Game.")
        print("\t3. End Game.")
        n = eval(input("\nPlease select one of the menu options(1-3) from Above: \n"))

    if n == 1:
        print("\n\t\t->RULES OF THE GAME<-")
        print("\n\t\tPaper covers Rock!")
        print("\t\tRock smashes Scissors!")
        print("\t\tScissors cuts Paper!")
        main()

    while n == 2:

        score = game_on()

        if score == (99, 'y'):
            humanscore += 1
            print("You: ", humanscore )
            print("Computer Score: ", computerscore)
            game_on()
        elif score == (99, 'n'):
            humanscore += 1         #This is where I leave off, it incorporates the return values from game_on() 99 = human win and 100 = computer win
            print("Final score\n")
            print("You: ", humanscore)
            print("Computer: ", computerscore)
            print("Score\n")
            end()
        elif score == (100, 'y'):
            computerscore += 1
            print("Computer Score: ", computerscore)
            game_on()
        elif score == (100, 'n'):
            computerscore += 1
            print("Final score\n")
            print("You: ", humanscore)
            print("Computer: ", computerscore)
            end()
        elif score == (0, 'y'):
            game_on()
        elif score == (0, 'n'):
            end()

        print (type(score))


    if n == 3:
        end()
    print("what n in MAIN is returning:", n)


main()
# check