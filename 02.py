with open('input02') as file:
    data = file.read().strip().split('\n')

# Rock - A, X
# Paper - B, Y
# Scissors - C, Z

# Scoring guide:

# Points for choice:
# 1 - Rock
# 2 - Paper
# 3 - Scissors

# Points for outcome:
# 0 - lose
# 3 - draw
# 6 - win

# Part 1
choice = {'X': 1, 'Y': 2, 'Z': 3}
lose = {'A Z', 'B X', 'C Y'}
draw = {'A X', 'B Y', 'C Z'}
win = {'A Y', 'B Z', 'C X'}

total_score = 0

for match in data:
    total_score += choice[match[-1]]
    if match in draw:
        total_score += 3
    elif match in win:
        total_score += 6

print('Part 1: Total Score', total_score)

# Part 2
# X - you need to lose
# Y - you need to draw
# Z - you need to win

lose_win_draw = {'X': 0, 'Y': 3, 'Z': 6}
must_choose_rock = {'A Y', 'B X', 'C Z'}
must_choose_paper = {'A Z', 'B Y', 'C X'}

total_score = 0

for match in data:
    total_score += lose_win_draw[match[-1]]
    if match in must_choose_rock:
        total_score += 1
    elif match in must_choose_paper:
        total_score += 2
    else:
        total_score += 3

print('Part 2: Total Score', total_score)
