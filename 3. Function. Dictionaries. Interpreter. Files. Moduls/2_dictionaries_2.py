def count_words_in_string(string_clone):
    counts_clone = dict()
    words = set(string_clone.lower().split())
    for word in string_clone.lower().split():
        if word not in counts_clone:
            counts_clone[word] = 1
        else:
            counts_clone[word] += 1
    return counts_clone


string = input()
counts = count_words_in_string(string)
print('\n'.join([f'{key} {counts[key]}' for key in counts.keys()]))
