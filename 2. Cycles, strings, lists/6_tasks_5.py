n = int(input())
matrix = [[0 for i in range(n)] for i in range(n)]
x = -1
y = 0
d_row = 1
d_coll = 0
count = 1
while count <= n ** 2:
    if  0 <= (x + d_row) < n and 0 <= (y + d_coll) < n and matrix[y + d_coll][x + d_row] == 0:
        x += d_row
        y += d_coll
        matrix[y][x] = count
        count += 1
    else:
        if d_row == 1:
            d_row = 0
            d_coll = 1
        elif d_row == -1:
            d_row = 0
            d_coll = -1
        elif d_coll == 1:
            d_coll = 0
            d_row = -1
        else:
            d_coll = 0
            d_row = 1
print('\n'.join([' '.join([str(number) for number in row]) for row in matrix]))
