import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😑"

    return jsonify({'sentiment': sentiment, 'score': polarity})

if __name__ == '__main__':
    app.run(debug=True)
