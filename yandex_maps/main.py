from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
# browser.get("https://yandex.ru/maps/")
browser.get("https://yandex.ru/maps/?ll=65.037141%2C53.365361&z=3.8")
browser.maximize_window()
time.sleep(5)

# Country, city
input_content = browser.find_element(By.XPATH, '//input[@class="input__control _bold"]')
input_content.send_keys("Москва")
input_content.send_keys(Keys.ENTER)
time.sleep(5)

# what to look for
input_content = browser.find_element(By.XPATH, '//input[@class="input__control _bold"]')
browser.find_elements(By.XPATH, '//div[@class="small-search-form-view__button"]')[-1].click()
time.sleep(2)
input_content.send_keys("Элеватор")
input_content.send_keys(Keys.ENTER)
time.sleep(5)

# scroll_element = browser.find_element(By.XPATH, '//div[@class="add-business-view"]')
# scroll_element.location_once_scrolled_into_view


while True:
    scroll_element = browser.find_element(By.XPATH, '//ul[@class="search-list-view__list"]').find_elements(By.XPATH,'//li[@class="search-snippet-view"]')
    scroll_element[-1].location_once_scrolled_into_view
    time.sleep(2)
    print(len(scroll_element))

    try:
        if browser.find_element(By.XPATH, '//div[@class="add-business-view"]'):
            print("break")
            break
    except:
        print("except")

data = browser.page_source
print(data)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(data)

with open("index.html", encoding="utf-8") as file:
    src = file.read()

url_address = []

soup = BeautifulSoup(src, "lxml")
url_data = soup.find("ul").find_all("li")
for item in url_data:
    url = "https://yandex.ru" + item.find("a").get("href")
    # name = item.find("a").get("aria-label")
    url_address.append(url)

print(url_address)

# ---------------------------------------------------------------------------------------
start_time = time.time()
# ---------------------------------------------------------------------------------------


browser.get(url_address[0])
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="search-placemark-view _position_right"]')))

name = browser.find_element(By.TAG_NAME, "h1").text.strip()

photo = []
photos = browser.find_element(By.XPATH, '//div[@class="carousel _old-browsers-workaround _theme_black orgpage-photos-view__carousel"]').find_elements(By.CLASS_NAME, "img-with-alt")
for item in photos:
    photo.append(item.get_attribute("src"))

full_address = browser.find_element(By.CLASS_NAME, "card-feature-view__main-content").find_element(By.TAG_NAME, "meta").get_attribute("content").strip()

phone = []
phones = browser.find_elements(By.CLASS_NAME, "orgpage-phones-view__phone-number")
for item in phones:
    phone.append(item.text.strip())

sait_org = browser.find_element(By.CLASS_NAME, "business-urls-view__link").get_attribute("href")

social_link = []
social_links = browser.find_element(By.CLASS_NAME, "business-contacts-view__social-button").find_elements(By.TAG_NAME, "a")
for item in social_links:
    social_link.append(item.get_attribute("href").strip())

coordinates = browser.find_element(By.XPATH, '//div[@class="search-placemark-view _position_right"]').get_attribute("data-coordinates")

print(name)
print(photo)
print(full_address)
print(phone)
print(sait_org)
print(social_link)
print(coordinates)

# ---------------------------------------------------------------------------------------
print("--- %s seconds ---" % (time.time() - start_time))
# ---------------------------------------------------------------------------------------
#  --- 10.677242517471313 seconds ---
#  --- 3.095665216445923 seconds ---

# time.sleep(10)
