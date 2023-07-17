import random

players = {
    "Dad": 8,
    "Max": 5,
    "Arseniy": 4
}
names = list(players)

first = 50
last = 1
turn = first
current = random.randint(0, len(players) - 1)
49
print(players)

while turn > last:
    name = names[current]

    # correct answer of player
    correct = 0
    if turn % players[name] > 0:
        correct = turn

    # get player answer
    ans = correct
    if current > 0:
        ans = int(input(f'({turn}) turn {name}: '))
    else:
        print(f'{name} say: {correct}')

    if ans != correct:
        last += 1
        print(f'Wrong! last index = {last}')

    current = (current + 1) % len(players)
    turn -= 1