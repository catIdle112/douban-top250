import requests
from bs4 import BeautifulSoup
import csv
i=0
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}
titles = []
for start in range(0,250,25):
    url = f"https://movie.douban.com/top250?start={start}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    for item in soup.find_all('div',class_='hd'):
        title=item.find('span',class_='title').get_text()
        titles.append(title)
    with open('douban_top250.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['rank', 'title'])
        writer.writerows([(i + 1, t) for i, t in enumerate(titles)])
print('已生成 douban_top250.csv')