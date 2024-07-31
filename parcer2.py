from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Настройки Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Запуск в фоновом режиме
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Путь к вашему драйверу Chrome
webdriver_service = Service('d://Chromedriver')  # Укажите путь к chromedriver

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL страницы
url = 'https://www.ya.ru'
driver.get(url)

print(driver.title)  # Пример вывода заголовка страницы

driver.quit()
