import requests

with open('file1.txt', 'r', encoding='utf-8') as file1:
    url = file1.readline().strip()
request = requests.get(url)
print(len(request.text.splitlines()))
