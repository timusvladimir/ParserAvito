import requests
from bs4 import BeautifulSoup
import time

# Функция для получения страницы
def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Функция для парсинга страницы
def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    ads = []

    # Найти все объявления
    for item in soup.find_all('div', class_='iva-item-content-KZ7eH'):
        title_tag = item.find('a', class_='link-link-MbQDF')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag.get('href')
            ads.append({
                'title': title,
                'link': f'https://www.avito.ru{link}'
            })

    return ads

# Основная функция
def main():
    url = 'https://www.avito.ru/moskva/kvartiry?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyt1JKTixJzMlPV7KuBQQAAP__dhSE3CMAAAA'
    html = get_page(url)
    if html:
        ads = parse_page(html)
        for ad in ads:
            print(f"Title: {ad['title']}")
            print(f"Link: {ad['link']}")
            print('-' * 40)
    else:
        print("Failed to retrieve the page.")

    # Задержка перед следующим запросом (если делаете несколько запросов)
    time.sleep(5)

if __name__ == '__main__':
    main()
