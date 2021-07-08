import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient



API_KEY = ""
my_latitude =
my_longitude =
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
MY_NUMBER = "+"
parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)

weather_data = response.json()

# print(type(weather_data))

# angela's
# hourly = weather_data["hourly"][0]["weather"][0]["id"]
# weather_slice = weather_data["hourly"][:12]
# for i in weather_slice:
#     code = i["weather"][0]["id"]
#     print(code)
#     if int(code) < 700:
#         print("Bring an umbrella.")

# print(weather_data)



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN


# print(message.sid)
will_rain = False
# mine
# for weather in weather_data:
for hour in weather_data["hourly"][:12]:
    # print(hour)
    for x in hour["weather"]:
        code = x["id"]
        print(code)
        if code < 700:
            will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☔",
        from_='+14014969647',
        to=MY_NUMBER
    )

    print(message.status)





