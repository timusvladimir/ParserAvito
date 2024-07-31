from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройки Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Запуск в фоновом режиме
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Путь к вашему драйверу Chrome
webdriver_service = Service('')  # Укажите путь к chromedriver

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL страницы
url = 'https://www.avito.ru/moskva/kvartiry'
driver.get(url)

try:
    # Ожидание загрузки элементов
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.iva-item-content-KZ7eH'))
    )

    # Получение элементов
    items = driver.find_elements(By.CSS_SELECTOR, 'div.iva-item-content-KZ7eH')
    for item in items:
        title_tag = item.find_element(By.CSS_SELECTOR, 'a.link-link-MbQDF')
        title = title_tag.text
        link = title_tag.get_attribute('href')
        print(f"Title: {title}")
        print(f"Link: {link}")
        print('-' * 40)
finally:
    driver.quit()
