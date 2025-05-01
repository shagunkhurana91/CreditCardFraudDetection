from flask import Flask, render_template, request
import joblib
import numpy as np

# Load model
model = joblib.load("random_forest_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect input features from the form
            features = [float(request.form[f]) for f in ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']]
            final_features = np.array(features).reshape(1, -1)

            # Make prediction
            prediction = model.predict(final_features)[0]

            # Return prediction result
            result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"
            return render_template('index.html', prediction_text=f'Prediction: {result}')
        except Exception as e:
            return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
