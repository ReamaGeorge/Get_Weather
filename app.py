from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace these with your actual API keys
WEATHER_API_KEY = 'f5af63d8278b6f3bdb410afa52e33f8e'  # Replace with your OpenWeatherMap API key
IPINFO_API_KEY = '9ae3bc38a22111'  # Replace with your IPinfo token

def get_weather(city):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(weather_url)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        return temperature
    else:
        return None

def get_location(ip):
    ipinfo_url = f"https://ipinfo.io/{ip}?token={IPINFO_API_KEY}"
    response = requests.get(ipinfo_url)
    location_data = response.json()
    if 'city' in location_data:
        city = location_data['city']
        return city
    else:
        return None

@app.route('/api/hello')
def hello():
    visitor_name = request.args.get('visitor_name')
    client_ip = request.remote_addr

    city = get_location(client_ip)
    temperature = get_weather(city)
    
    if city and temperature is not None:
        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
        return jsonify({"client_ip": client_ip, "location": city, "greeting": greeting})
    else:
        return jsonify({"error": "Could not retrieve location or weather information"}), 400

if __name__ == '__main__':
    app.run()
