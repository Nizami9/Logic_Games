import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# API_KEY = os.environ.get("OWN_api_key")
API_KEY = "4575bdd40aaca9e075c68d186cc58c2d"
account_sid = 'AC7b6778e2c1246b6ecf7f6f2c2119f882'
auth_token = 'd1fd28d8603d285b1aa580aca0da776c'

weather_params = {
    "lat": 52.150902,
    "lon": 9.951000,
    "appid": API_KEY,
}

response = requests.get(owm_endpoint, params=weather_params)
weather_data = response.json()
print(weather_data)
weather_slice = weather_data["list"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="Aı qız, başına papaq tax, xəstələnəssssssənç hava soyuq olacaq bugün!",
        from_='+12369007006',
        to='+4915209690036'
    )

    print(message.status)



