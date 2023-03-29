from bs4 import BeautifulSoup as BS
import requests 
import json

name_of_month = input("Введите месяц своего рождения: ")
year = input("Введите год своего рождения: ")
#переменные, с помощью которых пользователь вводит данные

url = 'https://ru.wikipedia.org/w/index.php?search='
updated_url = url + year + "+" + name_of_month
#добавляю ключевые слова к списку, чтобы сразу попасть на страницу с нужными результатами
page = requests.get(updated_url)
soup = BS(page.text, "lxml")
s = []
div = soup.find_all("div", class_="mw-search-result-heading")
#переменная, которая берёт названия статей
for name in div:
    print(name.a['title'])
    s.append(name.a['title'])
#функция, которая сохраняет только название без ссылок
l = []
l = (s[0:5])
#добавляю названия в отдельный лист, т.к. мне нужно всего 5
print(l)

e = "Вы родились в " + name_of_month + "е в " + year +" году." + str(l)
#добавляю в отдельную переменную всё что хочу записать в файл 
f = open(r"C:\Users\FTP\Documents\GitHub\125_semenov_marsel\hw python\hw17\wiki.txt", "w")
#указываю полный путь файла, потому что по другому он почему-то не хочет записывать данные, несмотря на то что они находятся в одной папке
f.write(e)
f.close()

    
