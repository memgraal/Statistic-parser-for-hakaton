from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys


def parse_statistics_from_url(url: str = "https://asbasket.ru/teams/6807?apiUrl=https%3A%2F%2Fasb.infobasket.su"):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage")  
    options.add_argument("--ignore-certificate-errors")  
    options.add_argument("--incognito")  
    options.add_argument("--disable-gpu") 
    options.add_argument("--disable-software-rasterizer")  
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.accept_insecure_certs = True
    options.add_argument("--log-level=3")

    # Отключение изображений для ускорения загрузки страниц
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    res_dct = {
        "Победы": {"Всего": 0, "Дома": 0, "В гостях": 0, "Серия": 0},
        "Поражения": {"Всего": 0, "Дома": 0, "В гостях": 0, "Серия": 0},
    }

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        # Устанавливаем неявное ожидание
        driver.implicitly_wait(5)  # Устанавливаем ожидание в 5 секунд

        # Вместо каждого вызова WebDriverWait, используем driver.find_element
        wins_total = driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.wins.total']")
        wins_data = {
            "Всего": int(wins_total.text.strip()),
            "Дома": int(driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.wins.home']").text.strip()),
            "В гостях": int(driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.wins.away']").text.strip()),
            "Серия": int(driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.wins.series']").text.strip()),
        }

        losses_total = driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.lost.total']")
        losses_data = {
            "Всего": int(losses_total.text.strip()),
            "Дома": int(driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.lost.home']").text.strip()),
            "В гостях": int(driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.lost.away']").text.strip()),
            "Серия": int(driver.find_element(By.XPATH, "//td[@ng-bind='data.lastSeason.games.lost.series']").text.strip()),
        }

        res_dct["Победы"] = wins_data
        res_dct["Поражения"] = losses_data

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit()

    finally:
        driver.quit()

    return res_dct
