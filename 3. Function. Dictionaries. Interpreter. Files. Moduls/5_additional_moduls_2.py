import requests


url = 'https://stepik.org/media/attachments/course67/3.6.3/'
with open('file1.txt', 'r', encoding='utf-8') as file:
    name = file.readline().strip()
r = requests.get(name)
while True:
    if not r.text.startswith('We'):
        r = requests.get(url + r.text)
    else:
        print(r.text)
        break
