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

            