import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = "AFUZDK36CSYQAR71"
stock_api_endpoint = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

news_api_key = "7aa3560af7404658a1ebd2b296577b32"
news_api_endpoint = "https://newsapi.org/v2/everything"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
}

account_sid = "AC1abdc7ac82c6feba7a86c37f42d6f192"
auth_token = "71a1122b85cc63c0bc54f63050323cd2"

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

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

