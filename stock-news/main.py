import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient



STOCK = "TSLA"
COMPANY_NAME = "+Tesla Inc"
ALPHAVANTAGE_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
MY_NUMBER = "+"
bigger = 0
smaller = 0

today = datetime.now().date()
yesterday = today - timedelta(days=1)
the_other_day = today - timedelta(days=2)



alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

news_parameters = {
    "q": COMPANY_NAME,
    "from": today,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
    # "page": 3
}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then
# print("Get News").



alpha_response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)

alpha_data = alpha_response.json()
# print(alpha_data)

price_yesterday = alpha_data["Time Series (Daily)"][f"{yesterday}"]["4. close"]
price_the_other_day = alpha_data["Time Series (Daily)"][f"{the_other_day}"]["4. close"]

is_there_change = False
diff = abs((float(price_yesterday) - float(price_the_other_day))) / float(price_yesterday)*100

# diff = 6

if diff > 5:
    is_there_change = True




# for key, value in alpha_data["Time Series (daily)"].items():
#     closing_values = value["4. close"]
#     print(closing_values)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_data = news_response.json()["articles"]
articles = news_data[:3]
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]
# print(formatted_articles)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to
# your phone number.


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

if is_there_change:
    if price_yesterday > price_the_other_day:
        emoji = "🔺"
    else:
        emoji = "🔻"

    # config for pythonanywhere
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    # config for local implementation
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    for sms in formatted_articles:
        message = client.messages \
            .create(
            body=f"{STOCK}: {emoji}{diff}%\n{sms}",
            from_='+14014969647',
            to=MY_NUMBER
        )

        print(message.status)