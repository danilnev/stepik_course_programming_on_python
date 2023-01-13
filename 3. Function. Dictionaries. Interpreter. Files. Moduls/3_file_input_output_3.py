marks = dict()
with open('something.txt', 'r', encoding='utf-8') as in_file:
    for string in in_file.readlines():
        words = string.strip().split(';')
        marks[words[0]] = [int(num) for num in words[1:]]
with open('something2.txt', 'w') as output:
    output.write('\n'.join([str(sum(marks[people]) / 3) for people in marks]) + '\n')
    output.write(' '.join([str(sum([marks[people][i] for people in marks]) / len(marks)) for i in range(3)]))
