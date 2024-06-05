from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import base64
import io

app = Flask(__name__)

model = tf.keras.models.load_model('model/model.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['image']
    header, encoded = data.split(",", 1)
    img_data = base64.b64decode(encoded)
    img = Image.open(io.BytesIO(img_data)).convert('L')

    img = img.resize((28, 28))
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1)

    img = img / 255.0
    prediction = model.predict(img)

    top3_indices = np.argsort(-prediction[0])[:3]
    top3_probabilities = prediction[0][top3_indices]

    results = []
    for idx, prob in zip(top3_indices, top3_probabilities):
        letter = chr(idx + ord('A'))
        results.append({'letter': letter, 'percent': round(prob * 100, 2)})

    return jsonify({'prediction': results})

if __name__ == '__main__':
    app.run(debug=True)
