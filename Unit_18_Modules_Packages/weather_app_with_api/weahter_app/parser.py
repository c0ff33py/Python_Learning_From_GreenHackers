def parse_weather(data):
    """Parse weater Json and return dict"""
    if not data:
        return None
    
    parsed = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"].title(),
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return parsed
