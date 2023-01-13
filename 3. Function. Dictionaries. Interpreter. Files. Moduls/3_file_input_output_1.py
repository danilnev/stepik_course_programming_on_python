with open('something2.txt', 'r') as input_file:
    input_string = input_file.readline().strip()
output_string = ''
print(input_string)
array = list()
i = 0
letter = True
while i != len(input_string):
    symbol = input_string[i]
    if letter and symbol.isdigit():
        array[-1].append(symbol)
    elif letter:
        array.append(symbol)
        letter = False
    else:
        array.append([symbol])
        letter = True
    i += 1
print(array)
for i in range(0, len(array) - 1, 2):
    output_string += array[i] * int(''.join(array[i + 1]))
print(output_string)
with open('something.txt', 'w') as file:
    file.write(output_string)
