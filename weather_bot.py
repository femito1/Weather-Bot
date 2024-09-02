import requests
import time

TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = ''
WEATHER_API_KEY = ''

# This is the URL of the API endpoint for sending messages to Telegram
SEND_MESSAGE_URL = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_BOT_TOKEN)

# This is the URL of the API endpoint for getting weather information
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q=Rome,IT&appid={}'.format(WEATHER_API_KEY)


# This function sends a message to the Telegram chat
def send_message(text):
    # Construct the payload for the API request
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }

    # Send the request
    requests.post(SEND_MESSAGE_URL, json=payload)


# This function gets the current weather from the OpenWeatherMap API
def get_weather():
    # Send a request to the API and get the response
    response = requests.get(WEATHER_URL)

    # Parse the JSON-formatted response
    data = response.json()

    # Extract the relevant information from the response
    temperature_fah = round((data['main']['temp'] - 273.15)*(9/5) + 32)
    temperature_cel = round(data['main']['temp'] - 273.15)
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    rain = 'It is expected to rain today, grab an umbrella.' if 'rain' in data else 'It is not expected to rain today.'

    # Format the message to send
    message = '{} \nTemp of {} degrees Fahrenheit, \n{} Celsius \n{}% humidity. \n{}'.format(
        description, temperature_fah, temperature_cel, humidity, rain)

    return message


# This is the main loop of the program
while True:
    # Get the current time
    current_time = time.localtime()

    # Check if it is between 6:00 and 7:00 in the morning
    if current_time.tm_hour == 19 and 0 <= current_time.tm_min < 60:
        # Get the weather and send a message with the information
        weather = get_weather()
        send_message(weather)

    # Wait for one minute before checking again
    time.sleep(1800)
