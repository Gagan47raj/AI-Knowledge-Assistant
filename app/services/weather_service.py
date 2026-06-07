import requests


class WeatherService:

    def get_weather(self):

        url = (
            "https://api.open-meteo.com/"
            "v1/forecast?"
            "latitude=12.97&"
            "longitude=77.59&"
            "current_weather=true"
        )

        response = requests.get(url)

        return response.json()