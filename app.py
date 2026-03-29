from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL = "https://api.thingspeak.com/channels/3317840/feeds.json?api_key=W3QGRO9AKU3HTEIB&results=5"

@app.route("/")
def home():
    return "AQI Backend Running"

@app.route("/data")
def get_data():
    try:
        response = requests.get(URL)
        data = response.json()

        latest = data["feeds"][-1]

        temp = float(latest["field1"])
        hum = float(latest["field2"])

        aqi = (temp * 2) + (hum * 0.5)

        return jsonify({
            "temperature": temp,
            "humidity": hum,
            "predicted_aqi": aqi
        })

    except Exception as e:
        return str(e)

@app.route("/aqi")
def get_aqi():
    try:
        response = requests.get(URL)
        data = response.json()

        latest = data["feeds"][-1]

        temp = float(latest["field1"])
        hum = float(latest["field2"])

        aqi = (temp * 2) + (hum * 0.5)

        return jsonify({
            "aqi": aqi
        })

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()
