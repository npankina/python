import requests
import datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = "AC8e143696579e7ffebacd942a5bfb3661"
TWILIO_AUTH_TOKEN = "9627befcbfa34896f68ce87276365fad"

STOCK_API_KEY = "VHEOBH7CXEM07Z84"
NEWS_API_KEY = "09afd82a95b94ab0b3e3eb04e15b9719"

url_stock = f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}"

response = requests.get(url_stock)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday = data_list[1]
day_before_yesterday_price = float(day_before_yesterday["4. close"])

price_difference = abs(yesterday_closing_price - day_before_yesterday_price)

percent_diff = (price_difference / yesterday_closing_price) * 100


if percent_diff > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API_KEY,
    }
    news_responce = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_responce.json()['articles']

    three_articles = articles[:3]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    news_to_sms = [f"Headline: {item['content']} \n\nBrief: {item['url']}" for item in three_articles]

    for item in news_to_sms:
        message = client.messages \
                    .create(
                         body=item,
                         from_='+19192457336',
                         to='+79170891139'
                     )

    print(f"Messages have already sent. Status from Twilio: {message.status}")
else:
    print('Everything is Ok.')
