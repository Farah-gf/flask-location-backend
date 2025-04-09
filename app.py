from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="language_app")

# Map provinces to languages
province_to_language = {
    "Punjab": "Urdu",
    "Sindh": "Sindhi",
    "Khyber Pakhtunkhwa": "Pashto",
    "Balochistan": "Urdu",
    "Islamabad": "Urdu"
}

@app.route('/')
def home():
    return "🌍 Language location API is live!"

@app.route('/location', methods=['POST'])
def get_location_language():
    data = request.get_json()
    lat = data['latitude']
    lon = data['longitude']

    location = geolocator.reverse((lat, lon), language='en')
    address = location.raw.get('address', {})
    state = address.get('state', 'Unknown')
    language = province_to_language.get(state, "Urdu")

    return jsonify({
        "province": state,
        "language": language
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)