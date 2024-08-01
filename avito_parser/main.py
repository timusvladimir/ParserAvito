# main.py

from avito_parser.scraper import fetch_page
from avito_parser.parser import parse_listings
from avito_parser.storage import save_to_csv


def main() -> None:
    """
    Основная функция для запуска парсера Avito.
    """
    # URL страницы с объявлениями (пример)
    # url = "https://www.avito.ru/moskva/avtomobili"
    url = "https://www.avito.ru/moskva/avtomobili?radius=0&searchRadius=0"

    # Получаем HTML-контент страницы
    page_html = fetch_page(url)

    # Парсим данные объявлений
    listings = parse_listings(page_html)

    # Сохраняем данные в CSV-файл
    save_to_csv(listings, "avito_listings.csv")
    print("Парсинг завершен. Данные сохранены в 'avito_listings.csv'.")


if __name__ == "__main__":
    main()
