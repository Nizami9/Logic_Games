from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_option)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, value="Teahouse")
# # all_portals.click()
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# driver.quit()

name = driver.find_element(By.NAME, value='fName')
name.send_keys("Nizami")
lastname = driver.find_element(By.NAME, value='lName')
lastname.send_keys("Suleymanov")
mail = driver.find_element(By.NAME, value='email')
mail.send_keys("Nizami@gmail.com")
btn = driver.find_element(By.CSS_SELECTOR, value='form button')
btn.click()

