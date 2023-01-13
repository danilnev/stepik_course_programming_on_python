classes = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
    '11': [],
}
with open('table.txt', 'r', encoding='utf-8') as table:
    for string in table.readlines():
        array = string.rstrip().split('\t')
        classes[array[0]].append(int(array[2]))
for classs in classes:
    if len(classes[classs]) == 0:
        print(f'{classs} -')
    else:
        print(f'{classs} {sum(classes[classs]) / len(classes[classs])}')
