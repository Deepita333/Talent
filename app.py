import spacy
from flask import Flask, request, jsonify, render_template

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Function to make predictions using NLP
def predict_talent_nlp(input_data):
    # Concatenate all user responses into a single string
    concatenated_responses = ' '.join(input_data.values())
    
    # Process the text using spaCy
    doc = nlp(concatenated_responses)
    
    # Extract nouns and proper nouns (potential talents) from the text
    talents = [token.text.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    
    # Define a list of talents to check for
    talent_keywords = ["programming", "cooking", "baking", "pottery", "knitting", "painting", 
                       "dancing", "sculpting", "photography", "graphics designing", "writing"]
    
    # Check if any of the talent keywords are present in the extracted talents
    predicted_talent = "Unknown"
    for talent in talent_keywords:
        if talent in talents:
            predicted_talent = talent
            break

    return predicted_talent

app = Flask(__name__)

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
    prediction = predict_talent_nlp(input_data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
