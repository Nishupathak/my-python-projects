import json
import urllib.error
import urllib.parse
import urllib.request

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mostly clear",
    2: "Partly cloudy",
    3: "Cloudy",
    45: "Foggy",
    48: "Foggy",
    51: "Light drizzle",
    53: "Drizzle",
    55: "Heavy drizzle",
    61: "Light rain",
    63: "Rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Thunderstorm with hail",
}


def describe(code):
    return WEATHER_CODES.get(code, "Unknown")


def get_json(url):
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def find_city(name):
    url = GEO_URL + "?name=" + urllib.parse.quote(name) + "&count=1"
    data = get_json(url)
    results = data.get("results")
    if not results:
        return None
    return results[0]


def get_weather(latitude, longitude):
    url = (
        FORECAST_URL
        + "?latitude=" + str(latitude)
        + "&longitude=" + str(longitude)
        + "&current=temperature_2m,apparent_temperature,"
        + "relative_humidity_2m,wind_speed_10m,weather_code"
        + "&daily=weather_code,temperature_2m_max,temperature_2m_min"
        + "&timezone=auto"
    )
    return get_json(url)


def show_weather(city, data):
    place = city["name"]
    if city.get("admin1"):
        place += ", " + city["admin1"]
    if city.get("country"):
        place += ", " + city["country"]

    now = data["current"]
    print()
    print("Weather in", place)
    print("-" * 30)
    print("Now:        ", describe(now["weather_code"]))
    print("Temperature:", now["temperature_2m"], "C")
    print("Feels like: ", now["apparent_temperature"], "C")
    print("Humidity:   ", now["relative_humidity_2m"], "%")
    print("Wind:       ", now["wind_speed_10m"], "km/h")

    daily = data["daily"]
    print()
    print("Next 3 days:")
    for i in range(3):
        print(
            daily["time"][i], "|",
            describe(daily["weather_code"][i]), "|",
            daily["temperature_2m_min"][i], "to",
            daily["temperature_2m_max"][i], "C",
        )


print("Weather App (type q to quit)")

while True:
    name = input("\nCity name: ").strip()
    if name.lower() == "q":
        print("Bye!")
        break
    if name == "":
        print("Please type a city name.")
        continue

    try:
        city = find_city(name)
        if city is None:
            print("I couldn't find that city. Check the spelling.")
            continue
        data = get_weather(city["latitude"], city["longitude"])
        show_weather(city, data)
    except (urllib.error.URLError, TimeoutError):
        print("Can't reach the internet. Check your connection and try again.")
    except (KeyError, json.JSONDecodeError):
        print("The weather server sent something unexpected. Try again later.")