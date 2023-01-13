num = int(input())
knowed_words = [input().lower() for i in range(num)]
num = int(input())
all_words = []
for i in range(num):
    string = input().lower().split()
    for word in string:
        if word not in all_words:
            all_words.append(word)
for word in all_words:
    if word not in knowed_words:
        print(word)
