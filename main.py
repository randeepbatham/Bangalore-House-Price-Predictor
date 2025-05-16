from flask import Flask, request, render_template

import utils

app = Flask(__name__)

utils.load_artifacts() #calling function
locations = utils.getLocationNames()

# print(locations)

@app.route('/')
def home():
    # return render_template('index.html', locations=locations)
    return render_template('index.html', locations = locations)

@app.route('/predict', methods=['POST'])
def predict_Prices():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Replace this with your actual prediction logic
    # For now, return a dummy value:
    # estimated_price = 75.5  # Replace this with: getEstimatedPrice(location, total_sqft, bhk, bath)
    estimated_price = utils.getEstimatedPrice(location, total_sqft, bhk, bath)

    return str(round(estimated_price, 2))

    # data = request.get_json()
    #
    # total_sqft = float(data['total_sqft'])
    # location = data['location']
    # bhk = int(data['bhk'])
    # bath = int(data['bath'])
    #
    # estimated_price = getEstimatedPrice(location,total_sqft, bhk, bath)
    #
    # response = jsonify({
    #     'estimated_price': estimated_price
    # })

if __name__ == "__main__":
    app.run(debug=True, port=5001)
