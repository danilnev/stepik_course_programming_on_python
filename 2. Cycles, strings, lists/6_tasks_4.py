matrix = []
string = input()
colls = 0
while string != 'end':
    matrix.append([int(number) for number in string.split()])
    string = input()
    colls += 1
result_matrix = [[[] for i in range(len(matrix[0]))] for i in range(colls)]
for i in range(colls):
    for j in range(len(matrix[i])):
        nums = [matrix[i - 1][j], 0, matrix[i][j - 1], 0]
        if i == colls - 1:
            nums[1] = matrix[0][j]
        else:
            nums[1] = matrix[i + 1][j]
        if j == len(matrix[i]) - 1:
            nums[3] = matrix[i][0]
        else:
            nums[3] = matrix[i][j + 1]
        result_matrix[i][j] = sum(nums)
print('\n'.join([' '.join([str(number) for number in row]) for row in result_matrix]))
