from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('random_forest_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Input order: Time, Amount, V1–V28
        features = [
            float(request.form.get('Time')),
            float(request.form.get('Amount')),
            float(request.form.get('V1')),
            float(request.form.get('V2')),
            float(request.form.get('V3')),
            float(request.form.get('V4')),
            float(request.form.get('V5')),
            float(request.form.get('V6')),
            float(request.form.get('V7')),
            float(request.form.get('V8')),
            float(request.form.get('V9')),
            float(request.form.get('V10')),
            float(request.form.get('V11')),
            float(request.form.get('V12')),
            float(request.form.get('V13')),
            float(request.form.get('V14')),
            float(request.form.get('V15')),
            float(request.form.get('V16')),
            float(request.form.get('V17')),
            float(request.form.get('V18')),
            float(request.form.get('V19')),
            float(request.form.get('V20')),
            float(request.form.get('V21')),
            float(request.form.get('V22')),
            float(request.form.get('V23')),
            float(request.form.get('V24')),
            float(request.form.get('V25')),
            float(request.form.get('V26')),
            float(request.form.get('V27')),
            float(request.form.get('V28'))
        ]

        # Scale and reshape
        input_data = np.array(features).reshape(1, -1)
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)[0]
        result = "❌ Fraudulent Transaction Detected!" if prediction == 1 else "✅ Transaction Looks Safe."

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
