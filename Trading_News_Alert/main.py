import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "5LGX8K0MGXWYZSJH"
NEW_API_KEY = "4ed3d049c035494cb97157e1b6b46a3e"


# TODO 1. Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_prise = data_list[0]["4. close"]
print(yesterday_closing_prise)

# TODO 2. Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = data_list[1]["4. close"]
print(day_before_yesterday_closing_price)

# TODO 3. Find the positive difference between 1 and 2
difference = abs(float(yesterday_closing_prise) - float(day_before_yesterday_closing_price))
print(difference)

# TODO 4. Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday
diff_percent = (difference / float(yesterday_closing_prise)) * 100
print(diff_percent)

# TODO 5. If TODO4 percentage is greater than 5 then print("Get News.")
if diff_percent > 1:
    news_params = {
        "apiKey": NEW_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = new_response.json()["articles"]
    print(articles)

# TODO 6. Use Python slice operator to create a list that contains the first 3 articles
three_articles = articles[:3]
print(three_articles)

# TODO 7. Create a new list of the first 3 article's headline and description using list comprehension

formatted_article_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

print(formatted_article_list)

