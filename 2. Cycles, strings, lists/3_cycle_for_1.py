coll_from, coll_to, row_from, row_to = int(input()), int(input()), int(input()), int(input())
table = []
rows = [1] + [i for i in range(coll_from, coll_to + 1)]
colls = [i for i in range(row_from, row_to + 1)]
for i in range(len(rows)):
    row = [rows[i]]
    for number in colls:
        row.append(rows[i] * number)
    table.append(row)
table[0][0] = ''
print('\n'.join(['\t'.join([str(number) for number in row]) for row in table]))
