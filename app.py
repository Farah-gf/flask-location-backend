from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="location_translator")

province_to_language = {
    "Punjab": "ur",
    "Sindh": "sd",
    "Khyber Pakhtunkhwa": "ps",
    "Balochistan": "ur",
    "Islamabad": "ur"
}

@app.route("/location", methods=["POST"])
def get_location_language():
    data = request.get_json()
    lat = data["latitude"]
    lon = data["longitude"]

    location = geolocator.reverse((lat, lon), language='en')
    address = location.raw.get("address", {})
    province = address.get("state", "Unknown")
    language = province_to_language.get(province, "ur")

    return jsonify({
        "province": province,
        "language": language
    })
