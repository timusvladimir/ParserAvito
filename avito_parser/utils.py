# avito_parser/utils.py

def save_html(content: str, filename: str) -> None:
    """
    Сохраняет HTML-контент в файл.

    :param content: HTML-контент страницы.
    :param filename: Имя файла для сохранения.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
