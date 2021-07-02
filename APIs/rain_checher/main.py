# CAREFULL this script send SMS to your mobile!!
import requests
from twilio.rest import Client

API_key = "f7f95089000e3f18a5ee703de9ca72ad"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = 'AC8e143696579e7ffebacd942a5bfb3661'
auth_token = '9627befcbfa34896f68ce87276365fad'
client = Client(account_sid, auth_token)

weather_params = {
    "lat": 47.752370,
    "lon": 46.402870,
    "appid": API_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 600:
        will_rain = True


if will_rain is True:
    message = client.messages \
        .create(
        body="It's going to rain. Remember bring ☔️ today!! Your Dev with ❤️",
        from_='+19192457336',
        to='+79170891139'
    )
print(message.status)