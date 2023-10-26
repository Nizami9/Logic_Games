import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.de/-/en/Google-Pixel-Pro-Smartphone-Telephoto/dp/B0BDJ55SSD/ref=sr_1_1?keywords=google+pixel+8+pro&qid=1698315988&refinements=p_89%3AGoogle%2Cp_72%3A419118031%2Cp_n_feature_thirty-four_browse-bin%3A81335049031&rnid=44358855031&s=telephone&sr=1-1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("€")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 700
MY_EMAIL = "nizami.suleymanoff@gmail.com"
MY_PASSWORD = "kijggvfdxcasxlrf"
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )