
# Weather Telegram Bot

This project is a simple Python script that retrieves the current weather information for Rome, Italy, and sends it to a specified Telegram chat every day at a specific time. The weather information includes temperature in both Fahrenheit and Celsius, humidity, a brief weather description, and whether rain is expected.

## Features

- Retrieves current weather data from the OpenWeatherMap API.
- Sends weather information to a specified Telegram chat.
- Automatically checks and sends the weather update at a scheduled time.

## Prerequisites

To run this script, you'll need:

1. **Python 3.x**: Ensure that Python is installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Requests Library**: The script uses the `requests` library to interact with the APIs. You can install it via pip:
   ```bash
   pip install requests
   ```

3. **API Keys**:
   - **OpenWeatherMap API Key**: Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your API key.
   - **Telegram Bot Token**: Create a bot using the [BotFather](https://core.telegram.org/bots#botfather) on Telegram to get your bot token.
   - **Telegram Chat ID**: Obtain the chat ID where you want to send the weather updates.

## Setup

1. **Configure API Keys**: Replace the placeholders in the script with your actual API keys and chat ID.
   ```python
   TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
   TELEGRAM_CHAT_ID = 'your_telegram_chat_id'
   WEATHER_API_KEY = 'your_openweathermap_api_key'
   ```

2. **Run the Script**: Execute the script using Python. It will continuously check the time and send a weather update to your Telegram chat every day at the specified time.

## How It Works

- The script defines two main functions:
  1. `get_weather()`: Fetches the current weather information from the OpenWeatherMap API and formats it into a readable message.
  2. `send_message(text)`: Sends a message to a specified Telegram chat using the Telegram Bot API.

- The main loop in the script runs indefinitely, checking the local time every minute. If the current time matches the specified time window (between 6:00 and 7:00 AM), the script retrieves the weather data and sends it to the Telegram chat.

- The script waits for 30 minutes (`time.sleep(1800)`) before checking again, reducing unnecessary API calls.

## Customization

- **City and Country**: You can change the weather location by modifying the `WEATHER_URL`. Replace `Rome,IT` with your desired city and country code.
  ```python
  WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q=YourCity,YourCountryCode&appid={}'.format(WEATHER_API_KEY)
  ```

- **Time of Notification**: Adjust the hour in the `if` condition within the main loop to change the time when the weather update is sent.

## Troubleshooting

- Ensure that your API keys are correctly configured.
- Check that the `requests` library is installed.
- Ensure that your Telegram bot is set up correctly and that you have the right chat ID.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this script as per the terms of the license. 

---

Feel free to customize the script as needed for your specific use case!
