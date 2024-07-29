# Flight Price Prediction App (PriceVoyager)

## Introduction

**PriceVoyager** is a machine learning application designed to predict flight prices based on various factors. By utilizing a pre-trained Random Forest model, the app provides real-time flight price estimates, helping users make informed decisions and potentially save money on air travel.

**Try it out!** [PriceVoyager](https://pricevoyage-manideep.streamlit.app/)

![Flight Price Prediction App](https://github.com/user-attachments/assets/5b13bd0d-a6b8-427f-87ae-cc0f9d3d35ea)

### Project Overview

PriceVoyager leverages machine learning to analyze historical flight data and identify patterns influencing flight prices. The app features a user-friendly interface that allows users to input flight details and receive predicted prices in INR. It aims to assist travelers and travel agencies by providing insights into future flight costs.

### Expected Outcomes

- **Informed Decisions**: Users can make better booking decisions based on predicted flight prices.
- **Cost Savings**: Potential to save money by booking flights at optimal times.
- **Data-Driven Insights**: Provides insights into factors affecting flight prices.

## Data Collection

### Source

The model uses historical flight data, including features such as:

- **Airline**
- **Source**
- **Destination**
- **Departure Time**
- **Arrival Time**
- **Price**

### Data Description

- **Features**: Information on various aspects of flight bookings.
- **Target**: Flight price in INR.

## Data Preprocessing

### Steps

- **Data Cleaning**: Removing or imputing missing values.
- **Feature Engineering**: Creating new features to improve model performance.
- **Normalization**: Scaling numerical features for better model accuracy.

## Model Development

### Algorithm

- **Random Forest**: Utilized for predicting flight prices based on historical data.

### Evaluation Metrics

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

### Training

- **Train-Test Split**: Data was split into training and testing sets to evaluate model performance.

## Deployment

### Strategy

- **Streamlit**: The app is deployed using Streamlit for real-time predictions.

### Platform

- **Streamlit Cloud**: Accessible via the provided [PriceVoyager link](https://pricevoyage-manideep.streamlit.app/).

### Security

- **Access Control**: The app is publicly accessible but does not handle sensitive data.

## Recommendations & Insights

### Target Audience

- **Travelers**: Individuals booking flights and seeking cost-effective options.
- **Travel Agencies**: Businesses providing value-added services to clients.
- **Data Science Enthusiasts**: Individuals interested in machine learning applications.

### Process

- **User Interaction**: Enter flight details to receive price predictions.
- **Recommendations**: Based on predicted prices and historical trends.

## Challenges

1. **Data Quality**: Handling missing or incomplete data which required extensive cleaning and imputation.
2. **Feature Selection**: Identifying the most relevant features that significantly impact flight prices.
3. **Model Accuracy**: Ensuring the Random Forest model provides accurate predictions and generalizes well to unseen data.

## What We Learned

1. **Importance of Data Quality**: Clean and well-prepared data is crucial for building accurate predictive models.
2. **Feature Engineering**: Effective feature engineering can significantly enhance model performance.
3. **User Interaction**: Building an intuitive and user-friendly interface improves the usability of the app.

## Future Work

1. **Integration with Real-Time Data**: Incorporate live weather and flight data to enhance prediction accuracy.
2. **User Interface Enhancements**: Develop a more interactive and feature-rich web or mobile app.
3. **Advanced Modeling Techniques**: Explore advanced machine learning models and techniques to further improve prediction accuracy.
4. **Extended Functionality**: Add features like price trend analysis, booking recommendations, and alert notifications for price changes.


## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Data Sources**: Historical flight data used for model training.
- **Libraries and Tools**: Python, Streamlit, Scikit-learn, Pandas

## Contact

For any inquiries or further information, please contact [Manideep Reddy](mailto:manideepreddy966@gmail.com).
