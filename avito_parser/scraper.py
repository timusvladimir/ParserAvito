# avito_parser/scraper.py

import requests
import time
from avito_parser.config import BASE_URL, HEADERS

def fetch_page(url: str) -> str:
    """
    Отправляет HTTP-запрос к указанному URL и возвращает HTML-контент страницы.

    :param url: URL страницы для загрузки.
    :return: HTML-контент страницы.
    """
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Поднимет исключение при ошибках HTTP-запроса
        time.sleep(1)  # Пауза в 1 секунду между запросами
        return response.text
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        return ""
    except requests.exceptions.RequestException as err:
        print(f"Ошибка запроса: {err}")
        return ""
