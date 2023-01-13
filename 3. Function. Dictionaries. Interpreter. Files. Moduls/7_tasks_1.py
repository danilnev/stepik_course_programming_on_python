table = dict()
games = []
num = int(input())
for i in range(num):
    string = input().split(';')
    command1, command2 = string[0], string[2]
    games.append(string)
    if command1 not in table:
        table[command1] = [0] * 5
    if command2 not in table:
        table[command2] = [0] * 5
for game in games:
    value1 = int(game[1])
    value2 = int(game[3])
    command1 = game[0]
    command2 = game[2]
    table[command1][0] += 1
    table[command2][0] += 1
    if value1 > value2:
        table[command1][1] += 1
        table[command2][-2] += 1
        table[command1][-1] += 3
    elif value2 > value1:
        table[command2][1] += 1
        table[command1][-2] += 1
        table[command2][-1] += 3
    else:
        table[command1][2] += 1
        table[command2][2] += 1
        table[command1][-1] += 1
        table[command2][-1] += 1
for command in table:
    print(f'{command}:{" ".join([str(value) for value in table[command]])}')
