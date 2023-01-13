all_words = list()
with open('something2.txt', 'r') as in_file:
    for string in in_file.readlines():
        for word in string.split():
            all_words.append(word.lower())
words = set(all_words)
counts = dict()
for word in words:
    counts[word] = all_words.count(word)
max_words = dict()
for key in counts.keys():
    if len(max_words) == 0 or counts[key] > int(max(max_words.values())):
        max_words.clear()
        max_words[key] = counts[key]
    elif counts[key] == int(max(max_words.values())):
        max_words[key] = counts[key]
with open('something.txt', 'w') as output:
    max_word = ''
    for word in max_words.keys():
        if max_word == '' or word < max_word:
            max_word = word
    output.write(f'{max_word} {max_words[max_word]}')
