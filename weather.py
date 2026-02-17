import requests
from plyer import notification

api_key = "93d0fd90fb1452a212af136a62139be3"

city = "Lagos"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send request
response = requests.get(url)
data = response.json()
print(data)

# Extract useful info
temperature = data['main']['temp']
description = data['weather'][0]['description']

notification.notify(
    title=f"Weather in {city}",
    message=f"{temperature}C, {description}",
    timeout=10
)

print(f"Weather in {city}: {temperature} C, {description}")
