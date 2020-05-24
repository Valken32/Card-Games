# values for the card games being played so that a loop can start.
bj = 0


# class for the amount of money assigned to players.
class MoneyAmount:
    def __init__(self, funds, bfunds):
        self.funds = funds
        self.bfunds = bfunds

gd = 0
gm = MoneyAmount(float(0), float(0))
print("Welcome to Gorgino's Card Casino, where fun is born!")

difficultyChoice = input(
    "\nThere are three game modes to choose from:\n\nEasy, which gives you 10 grand.\nMedium, which gives you 5 grand\n"
    "Hard, which give you 1 grand.\n\nWhich one will you choose?")

if difficultyChoice.lower().strip() == "easy":
    gm = MoneyAmount(float(1000.00), float(1000.00))
    gd = "easy"
elif difficultyChoice.lower().strip() == "medium":
    gm = MoneyAmount(float(500.00), float(500.00))
    gd = "med"
elif difficultyChoice.lower().strip() == "hard":
    gm = MoneyAmount(float(100.00), float(100.00))
    gd = "hard"

print("Great! Now let's get started, shall we?")

gameChoice = input("Here are the games available to play:\nBlackjack\nWhich one will you choose?")

if gameChoice.lower().strip() == "blackjack":
    bj = 1
else:
    print("Sorry, That game isn't available!")
    bj = 1
while bj == 1:
    import random

    # values

    ace = 1
    jack = 11
    queen = 12
    king = 13
    totalScore = 0
    botTotalScore = 0
    botBetting = 0

    # functions

    def cardconditions():
        if cardNum or botCardNum == 1:
            print("ace")
        elif cardNum or botCardNum == 11:
            print("jack")
        elif cardNum or botCardNum == 12:
            print("queen")
        elif cardNum or botCardNum == 13:
            print("king")
        else:
            print(cardNum)


    def keeptrack():
        print("Bot's score is", botTotalScore)
        print("Your score is", totalScore)


    cardDeck = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]

    betting = input("How much are you betting?")

    try:
        val = float(betting)

        if float(betting) <= gm.funds:
            if gd == "easy":
                botBetting = float(random.randrange(500, 1000))
            if gd == "med":
                botBetting = float(random.randrange(250, 500))
            if gd == "hard":
                botBetting = float(random.randrange(50, 100))

            print("betting:", betting, "\nBot is betting", botBetting)
            bj = 2

            while bj == 2:
                start = input("\nDraw a card? y/n")

                if start.lower().strip() == "y":

                    cardNum = random.choice(cardDeck)
                    botCardNum = random.choice(cardDeck)
                    cardconditions()
                    totalScore = totalScore + cardNum
                    botTotalScore = botTotalScore + botCardNum

                    if totalScore and botTotalScore == 21:
                        keeptrack()
                        pa = input("Tie! Want to play again? Y/N")
                        if pa.lower().strip() == "y":
                            bj = 1
                            continue
                        else:
                            break

                    elif totalScore >= 22:
                        keeptrack()
                        pa = input("You lose! Want to play again? Y/N")
                        if pa.lower().strip() == "y":
                            bj = 1
                            continue
                        else:
                            break

                    elif botTotalScore >= 22:
                        keeptrack()
                        pa = input("You win! Want to play again? Y/N")
                        if pa.lower().strip() == "y":
                            bj = 1
                            continue
                        else:
                            break

                    elif totalScore <= 20:
                        keeptrack()
                        continue

                    elif botTotalScore == 21:
                        keeptrack()
                        pa = input("You lose! Want to play again? Y/N")
                        if pa.lower().strip() == "y":
                            bj = 1
                            continue
                        else:
                            break

                    else:
                        keeptrack()
                        pa = input("You win! Want to play again? Y/N")
                        if pa.lower().strip() == "y":
                            bj = 1
                            continue
                        else:
                            break

                elif start.lower().strip() == "n":
                    cardNum = 0
                    botCardNum = random.choice(cardDeck)
                    cardconditions()
                    botTotalScore = botTotalScore + botCardNum
                    if totalScore > botTotalScore:
                        keeptrack()
                        pa = input("You win! Want to play again? Y/N")
                        if pa.lower().strip() == "y":
                            bj = 1
                            continue
                        else:
                            break
                    else:
                        keeptrack()
                        pa = input("You lose! Want to play again? Y/N")
                        if pa.lower().strip() == "y":
                            bj = 1
                            continue
                        else:
                            break
                else:
                    break

        elif float(betting) > gm.funds:
            print("Not enough funds, try again.")
            continue

    except ValueError:
        print("Only numbers allowed.")
        continue
