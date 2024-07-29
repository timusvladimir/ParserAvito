import requests
from bs4 import BeautifulSoup

# Определите URL страницы поиска на Avito
#search_query = "ноутбук"  # ключевое слово для поиска
#url = f"https://www.avito.ru/rossiya?q={search_query}"
url = f"https://www.avito.ru/all/avtomobili"


# Функция для парсинга страницы и извлечения данных
def parse_avito_page(url):
    # Отправляем GET-запрос на страницу
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешность запроса

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы с объявлениями (например, ссылки на объявления)
    items = soup.find_all('div', class_='iva-item-content')

    # Извлекаем заголовки, ссылки и цены
    results = []
    for item in items:
        title = item.find('h3', class_='title-root').get_text(strip=True) if item.find('h3', class_='title-root') else 'Без названия'
        link = item.find('a', class_='link-link').get('href') if item.find('a', class_='link-link') else None
        price = item.find('span', class_='price-text').get_text(strip=True) if item.find('span', class_='price-text') else 'Цена не указана'

        # Сохраняем данные
        results.append({
            'title': title,
            'link': f"https://www.avito.ru{link}" if link else None,
            'price': price
        })

    return results

# Используем функцию и выводим результаты
results = parse_avito_page(url)
for result in results:
    print(f"Название: {result['title']}")
    print(f"Ссылка: {result['link']}")
    print(f"Цена: {result['price']}")
    print('-' * 40)
