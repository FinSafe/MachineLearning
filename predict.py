import requests
import json

# Data input yang akan diprediksi
input_data = {
    "instances": [[
        182963970.185,
        'Female',
        49.0,
        'Single',
        'Degrees/Programs',
        'Category 0',
        'Single house',
        80.0,
        3.0,
        1.0,
        'Own or owner-like possession of house and lot',
        'Extended Family',
        4.0,
        1.0,
        1.0,
        1.0,
        2.0,
        4.0
    ]]
}

# Kirim permintaan prediksi ke backend Flask
url = 'http://127.0.0.1:5000/predict'  # Ganti dengan URL backend Flask Anda
response = requests.post(url, json=input_data)

# Cetak hasil prediksi
if response.status_code == 200:
    print("Response JSON:", response.json())  # Debugging line
    predictions = response.json().get('predictions', 'No predictions found')
    print("Predictions:", predictions)
else:
    print("Error:", response.text)