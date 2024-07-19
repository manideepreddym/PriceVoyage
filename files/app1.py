import streamlit as st
import pickle
import numpy as np
from datetime import datetime, time

# Load the trained model
with open('rf_random.pkl', 'rb') as file:
    model = pickle.load(file)

# Airline and destination mappings
airline_mapping = {
    'Trujet': 0, 'SpiceJet': 1, 'Air Asia': 2, 'IndiGo': 3, 'GoAir': 4,
    'Vistara': 5, 'Vistara Premium economy': 6, 'Air India': 7, 'Multiple carriers': 8,
    'Multiple carriers Premium economy': 9, 'Jet Airways': 10, 'Jet Airways Business': 11
}

destination_mapping = {
    "Banglore": 0, "Kolkata": 1, "Delhi": 2, "Chennai": 3, "Mumbai": 4
}

# Function to make predictions
def predict_price(features):
    return model.predict([features])

# Create a form for user input
with st.form(key='form1'):
    st.header('PriceVoyager: Your Ticket to Savings 🌎')
    st.caption('Best Fare Forward: Your Personal Flight Savings Expert 🔍✅')

    st.subheader('Journey Details')
    journey_date = st.date_input("Journey Date", value=datetime(2024, 1, 1))
    journey_day = journey_date.day
    journey_month = journey_date.month

    st.subheader('Departure Time')
    dep_time = st.time_input("Departure Time", value=time(0, 0))
    dep_hour = dep_time.hour
    dep_minute = dep_time.minute

    st.subheader('Arrival Time')
    arrival_time = st.time_input("Arrival Time", value=time(0, 0))
    arrival_hour = arrival_time.hour
    arrival_minute = arrival_time.minute

    st.subheader('Duration')
    duration_hours = st.number_input("Duration Hours", min_value=0, value=0)
    duration_mins = st.number_input("Duration Minutes", min_value=0, value=0)

    st.subheader('Source and Destination')
    source = st.selectbox("Source", options=["Banglore", "Kolkata", "Delhi", "Chennai", "Mumbai"], index=0)
    destination = st.selectbox("Destination", options=["Banglore", "Kolkata", "Delhi", "Chennai", "Mumbai"], index=0)
    
    st.subheader('Other Details')
    airline = st.selectbox("Airline", options=list(airline_mapping.keys()), index=0)
    total_stops = st.number_input("Total Stops", min_value=0, value=0)

    # Submit button
    submit_button = st.form_submit_button(label='Predict Price')
if submit_button:
    # Check if any crucial fields are zero
    if  dep_minute == 0  or arrival_minute == 0:
        st.warning("Please select proper values for Departure Time, Arrival Time, Duration Hours, and Duration Minutes.")
    elif source == destination:
        st.warning("Source and Destination cannot be the same.")
    else:
        # Map the airline and destination to their encoded values
        airline_encoded = airline_mapping[airline]
        destination_encoded = destination_mapping[destination]

        # Convert source to one-hot encoded values
        sources = ["Banglore", "Kolkata", "Delhi", "Chennai", "Mumbai"]
        source_encoded = [1 if s == source else 0 for s in sources]

        # Prepare feature list
        example_features = [
            airline_encoded, destination_encoded, total_stops, journey_day, journey_month,
            dep_hour, dep_minute, arrival_hour, arrival_minute,
            duration_hours, duration_mins
        ] + source_encoded

        # Ensure the feature list has exactly 16 features
        assert len(example_features) == 16, "Feature count mismatch. Expected 16 features."

        # Predict the price
        predicted_price = predict_price(example_features)
        st.write(f"✈️ The predicted price for {airline} with {total_stops} stop(s) to {destination} from {source} is ₹{predicted_price[0]:,.2f} INR.")
