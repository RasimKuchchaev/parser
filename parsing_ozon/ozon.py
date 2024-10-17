import json
import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait


def get_products_links(item_name="ноутбук"):
    driver = uc.Chrome()
    driver.implicitly_wait(5)

    driver.get("https://www.ozon.ru/")
    time.sleep(2)

    find_input = driver.find_element(By.NAME, "text")
    find_input.clear()
    find_input.send_keys(item_name)
    time.sleep(2)

    find_input.send_keys(Keys.ENTER)
    time.sleep(10)

    driver.close()
    driver.quit()


def main():
    get_products_links()

if __name__ == "__main__":
    main()  