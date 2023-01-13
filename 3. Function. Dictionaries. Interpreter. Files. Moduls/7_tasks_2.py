string1 = input()
string2 = input()
table = dict()
reverse_table = dict()
for i in range(len(string1)):
    table[string1[i]] = string2[i]
    reverse_table[string2[i]] = string1[i]
word = input()
code = input()
result_word = ''
result_code = ''
for letter in word:
    result_word += table[letter]
for symbol in code:
    result_code += reverse_table[symbol]
print(result_word)
print(result_code)
