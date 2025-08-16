from weahter_app import fetch_weeather, parse_weather, show_weather
def main():
    api_key = input("Enter your API key: ")
    city = input("Enter city name: ")
    data = fetch_weeather(city, api_key)
    parsed = parse_weather(data)
    show_weather(parsed)

if __name__ == "__main__":
    main()