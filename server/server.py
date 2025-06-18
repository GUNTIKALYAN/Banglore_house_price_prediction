from flask import Flask, request,jsonify,render_template
from flask_cors import CORS
import util
from whatsapp import whatsapp_route
import webbrowser
import threading

app = Flask(__name__)
CORS(app)

app.register_blueprint(whatsapp_route)

@app.route('/')
def home():
    return render_template('app.html')


@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    if total_sqft < 100:
        return jsonify({'error' : 'Total sqft is too low to estimate price.'})
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    response = jsonify({
            'estimated_price': round(estimated_price, 2)  # round for cleaner output
        })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response    
def open_browser():
    webbrowser.open_new("http://localhost:5000/")

if __name__ == "__main__":
    print("Starting Python flask server Fro Home price predition ....")
    util.load_saved_artifacts()
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)