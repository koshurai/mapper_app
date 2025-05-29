# 🚗 Distance, Time & Fuel Estimator

A Streamlit web application to estimate the **driving distance**, **travel time**, and **fuel consumption** between two user-input locations based on vehicle mileage.

---

## 🧰 Features

- 🔎 **Location Search** using Mapbox Geocoding API
- 🛣️ **Route Calculation** via OSRM (Open Source Routing Machine)
- ⛽ **Fuel Estimation** based on user-entered mileage (km/l)
- 📊 **Real-time Results** displayed on a simple UI
- ✅ **Error Handling** for location errors or API issues

---


## 📂 Technologies Used

| Component       | Technology                    |
|----------------|-------------------------------|
| Frontend       | [Streamlit](https://streamlit.io/) |
| Geocoding API  | [Mapbox](https://docs.mapbox.com/api/search/geocoding/) |
| Routing Engine | [OSRM](http://project-osrm.org/) |
| Hosting        | Local / Streamlit Cloud        |
| Language       | Python                         |

---

## Backend Workflow


User Input ──▶ Geocoder (Mapbox) ──▶ Route Engine (OSRM) ──▶ Fuel Estimation ──▶ Display Results


## 📈 API Rate Limits

### 🔹 Mapbox Geocoding API (Free Tier)

| Metric                | Limit                        |
|-----------------------|------------------------------|
| Monthly Active Users  | 50,000 requests/month        |
| Rate Limit            | 600 requests/minute          |
| Burst Limit           | 300 requests/second          |
| Pricing               | [View Mapbox Pricing](https://www.mapbox.com/pricing/) |



---

### 🔹 OSRM (Public Routing Server)

| Metric         | Limit                                  |
|----------------|-----------------------------------------|
| Request Type   | Public (Demo Server)                    |
| Rate Limit     | No formal SLA or limit guarantees       |
| Notes          | Not intended for production use         |


