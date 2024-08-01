# avito_parser/storage.py

import pandas as pd
from typing import List, Dict

def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    """
    Сохраняет список словарей в CSV-файл.

    :param data: Список словарей с данными объявлений.
    :param filename: Имя CSV-файла для сохранения данных.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
