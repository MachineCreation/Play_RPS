import random

class playClass():

    def __init__(self, comp, player, ties):
        self.comp = comp
        self.player = player
        self.ties = ties

    def play(self, comp, player):
        if comp == player:
            print("You Tied.")
            self.ties += 1
        elif comp == 1 and player == 2:
            print("You win!!")
            self.player += 1
        elif comp == 2 and player == 3:
            print("You win!!")
            self.player += 1
        elif comp == 3 and player == 1:
            print("You win!!")
            self.player += 1
        else:
            print("You lose!!")
            self.comp += 1

    def score(self):
        print("The score is\n"
              f"Computer:   {self.comp}   Player: {self.player}   Ties: {self.ties}")



game = playClass(0, 0, 0)

def RPS():
    while True:
        answer = input("Type Rock, Paper, or Scissors to play.\n"
                       "Type Score to see how badly you are getting punished by a computer\n"
                       "Type Quit to end the game\n")
        comp_choice = random.randint(1,3)
        if answer.lower() == "quit":
            print("Thanks for playing!!!!")
            game.score()
            break
        elif answer.lower() == "score":
            game.score()
        elif answer.lower() == "rock":
            game.play(comp_choice, 1)
        elif answer.lower() == "paper":
            game.play(comp_choice, 2)
        elif answer.lower() == "scissors":
            game.play(comp_choice, 3)
        else:
            print(f"{answer} is not a valid input")

RPS()