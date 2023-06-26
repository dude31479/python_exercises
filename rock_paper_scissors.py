def rpsWinner(player1, player2):
    if player1.lower() == 'rock':
        match(player2):
            case 'paper':
                return 'player two'
            case 'scissors':
                return 'player one'
            case 'rock':
                return 'tie'
    elif player1.lower() == 'paper':
        match(player2):
            case 'scissors':
                return 'player two'
            case 'rock':
                return 'player one'
            case 'paper':
                return 'tie'
    elif player1.lower() == 'scissors':
        match(player2):
            case 'rock':
                return 'player two'
            case 'paper':
                return 'player one'
            case 'scissors':
                return 'tie'
            

assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'

import random
def rock_paper_scissors():
    playing = True
    input("Hello! Let's play rock, paper, scissors!")
    
    while playing:
        player1 = input("Choose 1: Rock, Paper, or Scissors: ")
        player2 = random.choice(['rock', 'paper', 'scissors'])
        print(f"Player two chose {player2}!")
        input()
        winner = rpsWinner(player1, player2)
        if winner == 'tie':
            print("It's a tie!")
        else:
            print(f"{winner} wins!")
        play_again = input("Would you like to play again?")
        if play_again[0].lower() != "y":
            playing = False
    print("Goodbye!")

rock_paper_scissors()