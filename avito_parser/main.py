# main.py

from avito_parser.scraper import fetch_page
from avito_parser.parser import parse_listings
from avito_parser.storage import save_to_csv
from avito_parser.utils import save_html


def main() -> None:
    """
    Основная функция для запуска парсера Avito.
    """
    # URL страницы с объявлениями (пример)
    url = "https://www.avito.ru/moskva/avtomobili"

    # Получаем HTML-контент страницы
    page_html = fetch_page(url)

    # Сохраняем HTML-контент в файл
    save_html(page_html, "page.html")
    print("HTML-страница сохранена в 'page.html'.")

    # Парсим данные объявлений
    listings = parse_listings(page_html)

    # Сохраняем данные в CSV-файл
    save_to_csv(listings, "avito_listings.csv")
    print("Парсинг завершен. Данные сохранены в 'avito_listings.csv'.")


if __name__ == "__main__":
    main()
