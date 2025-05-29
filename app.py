import streamlit as st
import requests
from mapbox import Geocoder

# Mapbox token
key = 'pk.eyJ1IjoiYWRpbDk4IiwiYSI6ImNtYjdzODZ1NzBkcXcybHM2OHcwZTZ5NzAifQ.SlPs3gdrGqD7iU3Fk35AFw'
MAPBOX_TOKEN = key

if not MAPBOX_TOKEN:
    st.error("Mapbox token not found! Please set MAPBOX_TOKEN environment variable.")
    st.stop()

# Initialize Mapbox geocoder
geocoder = Geocoder(access_token=MAPBOX_TOKEN)

# Get coordinates from location name
def get_coordinates(location_name):
    response = geocoder.forward(location_name, limit=1)
    if response.status_code == 200:
        data = response.json()
        if data['features']:
            coords = data['features'][0]['center']  # [lon, lat]
            return coords[1], coords[0]
    return None

# Get distance and duration
def get_route_info(coord1, coord2):
    url = f"http://router.project-osrm.org/route/v1/driving/{coord1[1]},{coord1[0]};{coord2[1]},{coord2[0]}?overview=false"
    response = requests.get(url)
    data = response.json()
    if 'routes' in data and data['routes']:
        distance_km = data['routes'][0]['distance'] / 1000
        duration_min = data['routes'][0]['duration'] / 60
        return distance_km, duration_min
    return None, None

# Fuel estimation
def estimate_fuel(distance_km, avg_kmpl):
    return round(distance_km / avg_kmpl, 2)

# Streamlit UI
st.title("Distance, Time & Fuel Estimator 🚗")

loc1 = st.text_input("Enter Location 1:")
loc2 = st.text_input("Enter Location 2:")
user_kmpl = st.number_input("Enter your vehicle's mileage (km/l):", min_value=1.0, max_value=100.0, value=15.0)

if st.button("Calculate"):
    with st.spinner("Getting coordinates..."):
        coord1 = get_coordinates(loc1)
        coord2 = get_coordinates(loc2)

    if coord1 and coord2:
        with st.spinner("Calculating route..."):
            distance, duration = get_route_info(coord1, coord2)
            if distance is not None:
                fuel = estimate_fuel(distance, user_kmpl)
                st.success("Here are the results:")
                st.write(f"📍 **Distance**: {distance:.2f} km")
                st.write(f"⏱️ **Estimated Time**: {duration:.2f} minutes")
                st.write(f"⛽ **Fuel Used**: {fuel:.2f} litres (at {user_kmpl} km/l)")
            else:
                st.error("Failed to retrieve route data.")
    else:
        st.error("Failed to get location coordinates. Please check input names.")
