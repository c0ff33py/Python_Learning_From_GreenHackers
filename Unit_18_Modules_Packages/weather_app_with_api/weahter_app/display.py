def show_weather(parsed):
    """Display weahter info nicely"""
    if not parsed:
        print("⚠️ No data to display.")
        return
    
    print(f"\n🌤️ Weather in {parsed['city']}:")
    print(f"Temperature: {parsed['temperature']}C")
    print(f"Description: {parsed['description']}")
    print(f"Hunidity: {parsed['humidity']}%")
    print(f"Wind speed: {parsed['wind_speed']}m/s\n")
    
    
    