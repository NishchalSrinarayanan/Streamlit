import requests
import streamlit as st

# Function to get weather data using a zip code
def get_weather_by_zip(zip_code):
    # Define the URL for the geocoding API request
    geocode_url = f"https://geocode.maps.co/search?q={zip_code}&api_key={st.secrets[geocode]}"

    # Send a GET request to the geocoding API
    geocode_response = requests.get(geocode_url)

    # Check if the request was successful
    if geocode_response.status_code == 200:
        # Parse the JSON response data
        geocode_data = geocode_response.json()

        if geocode_data:
            # Extract latitude and longitude from the first result
            lat = geocode_data[0]['lat']
            lon = geocode_data[0]['lon']

            # OpenWeatherMap API URL and API key
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={st.secrets[openweathermap]}"

            # Send a GET request to the specified URL
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response data
                data = response.json()

                # Access the temperature field and convert it from Kelvin to Celsius
                temperature_kelvin = data["main"]["temp"]
                temperature_celsius = temperature_kelvin - 273.15

                feels_like_kelvin = data["main"]["feels_like"]
                feels_like_celsius = feels_like_kelvin - 273.15
                city_name = data['name']

                # Display the results in Streamlit
                st.write(f"In {city_name}:")
                st.write(f"The current temperature is {temperature_celsius:.2f} degrees Celsius.")
                st.write(f"But it feels like it is {feels_like_celsius:.2f} degrees Celsius")

# Streamlit app title
st.title("Weather Checker")

# User input for zip code
zip_code = st.text_input("Enter zip code:")

# Check if zip_code is provided
if zip_code:
    # Call the function to get weather data
    get_weather_by_zip(zip_code)
