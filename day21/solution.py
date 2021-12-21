
from functools import cache
from itertools import product

def play_game(player_position, dice):
    roll = 0
    for _ in range(3):
        roll += (dice%10)+1
        dice += 1

    position = player_position + roll
    player_position = position%10 if position%10 != 0 else 10
    return player_position, dice

def play_iterative(player1_position, player2_position):
    player1_score = 0
    player2_score = 0

    turn = 1
    dice = 0

    while player1_score < 1000 and player2_score < 1000:
        if turn:
            player1_position, dice = play_game(player1_position, dice)
            player1_score += player1_position
            #print(f"player 1 moves to {player1_position} with score {player1_score} and dice: {dice}")
            turn = 0
        else:
            player2_position, dice = play_game(player2_position, dice)
            player2_score += player2_position
            #print(f"player 2 moves to {player2_position} with score {player2_score} and dice: {dice}")
            turn = 1

    return min(player1_score, player2_score) * dice

print(play_iterative(4,8))
print(play_iterative(1,10))

@cache
def play_recursive(current_score, other_score, current_pos, other_pos, dice):
    if current_score >= 1000:
        return other_score * dice
    if other_score >= 1000:
        return current_score * dice
    
    position = current_pos + sum(list(range((dice%100)+1,(dice%100)+4)))
    dice += 3
    current_pos = position%10 if position%10 != 0 else 10
    current_score += current_pos
    
    return play_recursive(other_score, current_score, other_pos, current_pos, dice)

print(play_recursive(0,0,4,8,0))
print(play_recursive(0,0,1,10,0))
 
dirac_die = [1, 2, 3]
dirac_die = list(product(dirac_die, dirac_die, dirac_die))

@cache
def play_round(current_score, other_score, current_pos, other_pos):
    if current_score >= 21: 
        return 1, 0
    if other_score >= 21: 
        return 0, 1

    score = [0, 0]
    for (d1, d2, d3) in dirac_die:
        new_current_pos = current_pos + d1 + d2 + d3
        new_current_pos = new_current_pos%10 if new_current_pos%10 != 0 else 10
        new_current_score = current_score + new_current_pos
        
        p2_wins, p1_wins = play_round(other_score, new_current_score, other_pos, new_current_pos)
        score[0] += p1_wins 
        score[1] += p2_wins
    return score


print(play_round(0, 0, 1, 10))