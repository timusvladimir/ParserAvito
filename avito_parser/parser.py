# avito_parser/parser.py

from bs4 import BeautifulSoup
from typing import List, Dict


def parse_listing(listing_html: str) -> Dict[str, str]:
    """
    Парсит HTML-контент отдельного объявления и возвращает словарь с данными.

    :param listing_html: HTML-контент объявления.
    :return: Словарь с данными объявления.
    """
    soup = BeautifulSoup(listing_html, 'html.parser')
    title = soup.find('h1', class_='title').get_text(strip=True) if soup.find('h1', class_='title') else 'Нет заголовка'
    price = soup.find('span', class_='price').get_text(strip=True) if soup.find('span', class_='price') else 'Нет цены'
    location = soup.find('span', class_='location').get_text(strip=True) if soup.find('span',
                                                                                      class_='location') else 'Нет местоположения'
    description = soup.find('div', class_='description').get_text(strip=True) if soup.find('div',
                                                                                           class_='description') else 'Нет описания'

    return {
        "title": title,
        "price": price,
        "location": location,
        "description": description
    }


def parse_listings(page_html: str) -> List[Dict[str, str]]:
    """
    Парсит HTML-контент страницы с объявлениями и возвращает список словарей с данными.

    :param page_html: HTML-контент страницы с объявлениями.
    :return: Список словарей с данными объявлений.
    """
    soup = BeautifulSoup(page_html, 'html.parser')
    listings = []
    for listing in soup.find_all('div', class_='listing'):
        listing_url = listing.find('a', class_='listing-link')['href']
        listing_html = fetch_page(BASE_URL + listing_url)
        listing_data = parse_listing(listing_html)
        listings.append(listing_data)
    return listings
