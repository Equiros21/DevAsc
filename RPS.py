# Rock Paper Scissors Challenge at https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
import sys
def rps():
    print("\nWelcome to Rock Paper Scissors challenge, select your choice:\n1 - Paper\n2 - Rock\n3 - Scissors"
          "\n\nGood Luck!\n")  # This is the introduction
    player1 = int(input("Player 1: "))
    while (player1 > 3) or (player1 == 0):
        print("Please select a valid choice, try again")
        player1 = int(input("Player 1: "))
    else:
        pass
    player2 = int(input("Player 2: "))
    while (player2 > 3) or (player2 == 0):
        print("Please select a valid choice, try again")
        player2 = int(input("Player 1: "))
    else:
        pass
    if player1 == player2:
        print("Tie! Try again")
        rps()
    elif (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 1):
        print("\nPlayer 1 is the winner!")
        sys.exit()
    else:
        print("\nPlayer 2 is the winner!")
        sys.exit()


rps()
