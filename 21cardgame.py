import random
ace = 1
jack = 11
queen = 12
king = 13
totalScore = 0
botTotalScore = 0
def cardConditions():
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
def keepTrack():
    print("Bot's score is", botTotalScore)
    print("Your score is", totalScore)
while True:
    cardDeck = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]
    answer = input("Draw a card? y/n")
    if answer.lower().strip() == "y":
        cardNum = random.choice(cardDeck)
        botCardNum = random.choice(cardDeck)
        cardConditions()
        totalScore = totalScore + cardNum
        botTotalScore = botTotalScore + botCardNum

        if totalScore and botTotalScore == 21:
            keepTrack()
            pa = input("Tie! Want to play again? Y/N")
            if pa.lower().strip() == "y":
                totalScore = 0
                botTotalScore = 0
                continue
            else:
                totalScore = 0
                botTotalScore = 0
                break

        elif totalScore >= 22:
            keepTrack()
            pa = input("You lose! Want to play again? Y/N")
            if pa.lower().strip() == "y":
                totalScore = 0
                botTotalScore = 0
                continue
            else:
                totalScore = 0
                botTotalScore = 0
                break

        elif botTotalScore >= 22:
            keepTrack()
            pa = input("You win! Want to play again? Y/N")
            if pa.lower().strip() == "y":
                totalScore = 0
                botTotalScore = 0
                continue
            else:
                totalScore = 0
                botTotalScore = 0
                break

        elif totalScore <= 20:
            keepTrack()
            continue

        elif botTotalScore == 21:
            keepTrack()
            pa = input("You lose! Want to play again? Y/N")
            if pa.lower().strip() == "y":
                totalScore = 0
                botTotalScore = 0
                continue
            else:
                totalScore = 0
                botTotalScore = 0
                break

        else:
            keepTrack()
            pa = input("You win! Want to play again? Y/N")
            if pa.lower().strip() == "y":
                totalScore = 0
                botTotalScore = 0
                continue
            else:
                totalScore = 0
                botTotalScore = 0
                break

    elif answer.lower().strip() == "n":
        cardNum = 0
        botCardNum = random.choice(cardDeck)
        cardConditions()
        botTotalScore = botTotalScore + botCardNum
        if totalScore > botTotalScore:
            keepTrack()
            pa = input("You win! Want to play again? Y/N")
            if pa.lower().strip() == "y":
                totalScore = 0
                botTotalScore = 0
                continue
            else:
                totalScore = 0
                botTotalScore = 0
                break
        else:
            keepTrack()
            pa = input("You lose! Want to play again? Y/N")
            if pa.lower().strip() == "y":
                totalScore = 0
                botTotalScore = 0
                continue
            else:
                totalScore = 0
                botTotalScore = 0
                break
    else:
        break