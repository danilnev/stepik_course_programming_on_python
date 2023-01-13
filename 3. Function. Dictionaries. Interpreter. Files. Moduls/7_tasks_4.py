crds = [0, 0]
num = int(input())
for i in range(num):
    command = input().split()
    if command[0] == 'север':
        crds[1] += int(command[1])
    elif command[0] == 'запад':
        crds[0] -= int(command[1])
    elif command[0] == 'юг':
        crds[1] -= int(command[1])
    else:
        crds[0] += int(command[1])
print(crds[0], crds[1])
