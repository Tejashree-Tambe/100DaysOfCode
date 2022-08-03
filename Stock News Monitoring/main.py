import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = "api_key"
stock_api_endpoint = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

news_api_key = "api key"
news_api_endpoint = "https://newsapi.org/v2/everything"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
}

account_sid = "sid"
auth_token = "token"

stock_response = requests.get(stock_api_endpoint, params=stock_parameters)
stock_response.raise_for_status()

data = stock_response.json()

daily_data = data["Time Series (Daily)"]
daily_data_list = [value for key, value in daily_data.items()]

yesterday_close_price = float(daily_data_list[0]["4. close"])
day_before_yesterday_close_price = float(daily_data_list[1]["4. close"])

difference = abs(yesterday_close_price - day_before_yesterday_close_price)
percentage_difference = 100 * (difference / yesterday_close_price)

if percentage_difference > 0:
    news_response = requests.get(news_api_endpoint, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    top_three_news = news_data["articles"][:3]

    articles = [f"Headlines: {article['title']}\nBrief: {article['description']}" for article in top_three_news]

    client = Client(account_sid, auth_token)

    for article in articles:
        message = client.messages \
            .create(
            body=f"TSLA: 🔺{percentage_difference}% {article}",
            from_='+15207292541',
            to='+919930049115'
        )

        print(message.status)


