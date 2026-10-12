import requests
import json
def get_weather(city):
    try:
        response = requests.get(
            f"https://wttr.in/{city}",
            params={"format": "j1"},
            timeout=5
    )
        response.raise_for_status()

        data = response.json()
        return {
            "temp": data["current_condition"][0]["temp_C"],
            "desc": data["current_condition"][0]["weatherDesc"][0]["value"],
            "humidity": data["current_condition"][0]["humidity"]
        }

    except requests.exceptions.ConnectionError:
        raise Exception("Failed to connect to the weather service.")
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error occurred: {err}")
    except requests.exceptions.Timeout:
        raise Exception("The request timed out.")
    except requests.exceptions.RequestException as err:
        raise Exception(f"An error occurred: {err}")