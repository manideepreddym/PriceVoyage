## Flight Price Prediction App - PriceVoyager

This repository contains the code for a Streamlit app called PriceVoyager, which predicts flight prices based on various factors.
![image](https://github.com/user-attachments/assets/5b13bd0d-a6b8-427f-87ae-cc0f9d3d35ea)

### Description

PriceVoyager helps users make informed decisions and potentially save money on air travel by predicting flight prices. It utilizes a pre-trained Random Forest model to analyze historical flight data and identify patterns influencing price. 

### Features

* User-friendly interface for entering flight details.
* Predicts flight prices using a trained Random Forest model.
* Displays the predicted price in INR.

### Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/flight-price-prediction-app.git
```

2. **Navigate to the project directory:**

```bash
cd flight-price-prediction-app
```

3. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app:**

```bash
streamlit run app.py
```

### Usage

1. Open http://localhost:8501/ in your web browser.
2. Enter the flight details in the user interface.
3. Click "Predict Price" to get the estimated flight price.

### Project Structure

The project is organized as follows:

* `app.py`: Contains the Streamlit app logic for user interaction, data processing, and prediction.
* `data`: (Optional) May contain the flight data used for training the model.
* `model.pkl`: The saved Random Forest model file used for prediction.
* `requirements.txt`: Lists the required Python libraries.

### Authors

* Manideep Reddy Mandhadi (or your name/team name)

### Disclaimer

The provided Random Forest model is for demonstration purposes only and may not achieve optimal accuracy on unseen data. Consider retraining the model with your own dataset for improved performance.
