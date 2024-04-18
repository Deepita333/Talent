from flask import Flask, request, jsonify, render_template

app = Flask(__name__)



import joblib

def load_model():
    # Load your trained model here
    model = joblib.load('trained_model_updated.pkl')  # Replace 'model.pkl' with the path to your saved model file
    return model



model = load_model()

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'q1': request.form['q1'],
        'q2': request.form['q2'],
        'q3': request.form['q3'],
        'q4': request.form['q4'],
        'q5': request.form['q5'],
        'q6': request.form['q6'],
        'q7': request.form['q7'],
        'q8': request.form['q8'],
        'q9': request.form['q9'],
        'q10': request.form['q10']
    }
    # Preprocess input data if necessary
    prediction = predict_talent(input_data)
    return jsonify({'prediction': prediction})

# Function to make predictions
def predict_talent(input_data):
    # Concatenate all user responses into a single string
    concatenated_responses = ' '.join(input_data.values())

    # Define a list of talents to check for in the concatenated responses
    talents = ["programming", "cooking", "baking", "pottery", "knitting", "painting", 
               "dancing", "sculpting", "photography", "graphics designing", "writing"]

    # Iterate over the list of talents and check if any of them are mentioned in the responses
    predicted_talent = "Unknown"
    for talent in talents:
        if talent in concatenated_responses.lower():
            predicted_talent = talent
            break

    return predicted_talent


if __name__ == '__main__':
    app.run(debug=True)
