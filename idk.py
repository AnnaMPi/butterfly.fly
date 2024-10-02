import requests
from bs4 import BeautifulSoup

url = 'https://learnpython.com/blog/python-libraries/#:~:text=Learn%20about%20the%20most%20popular%20Python%20libraries%20for%20data'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')
# results = s.find(class_ = 'mv-ad-box')
filetitle = s.find_all('h3')
# print(filetitle[0].text)
for title in filetitle:
    print(title.text)