from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('res.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    MONTH = request.form['month']
    DAY = request.form['day']
    DEPARTURE_DELAY = request.form['dep_delay']
    DISTANCE = request.form['distance']
    DIVERTED = request.form['diverted']
    CANCELLED = request.form['cancelled']
    AIR_SYSTEM_DELAY= request.form['air_sys_delay']
    SECURITY_DELAY= request.form['security_delay']
    AIRLINE_DELAY = request.form['airline_delay']
    LATE_AIRCRAFT_DELAY = request.form['late_aircraft_delay']
    WEATHER_DELAY = request.form['weather_delay']
    route= request.form['route']

    total = [[int(MONTH), int(DAY), int(DEPARTURE_DELAY),int(DISTANCE), int(DIVERTED), int(CANCELLED),int(AIR_SYSTEM_DELAY), int(SECURITY_DELAY), int(AIRLINE_DELAY), int(LATE_AIRCRAFT_DELAY), int(WEATHER_DELAY), int(route)]]
    y_pred = model.predict(total)
    if y_pred==1:
        msg='Your flight will be delayed'
    else:
        msg='Your flight will be on time'
    return render_template("index.html", showcase = msg)


if __name__ == '__main__':
    app.run(debug=True)