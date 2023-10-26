from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org/")
# driver.get("https://store.google.com/de/config/pixel_8?hl=de&selections=eyJwcm9kdWN0RmFtaWx5IjoiY0dsNFpXeGZPQT09In0%3D")

# price_euro = driver.find_element(By.CLASS_NAME, value="XN64g").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_euro}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)
# driver.close()
price = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(price.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "timer": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)



driver.quit()