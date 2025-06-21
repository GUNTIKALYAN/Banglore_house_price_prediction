# 🏠 Bangalore House Price Predictor + 🤖 WhatsApp Bot
  
📱 **WhatsApp Bot**: Predict home prices via chat!  
🧠 Powered by ML | 📊 Smart Feature Engineering | ⚙️ Flask Backend

## 📌 Overview

This project predicts the price of residential properties in Bangalore based on various parameters like location, total square feet, BHK, and bathrooms.

You can either use the **web interface** or message the **WhatsApp bot** to get instant predictions!

🔗 **GitHub Repo**: [GUNTIKALYAN/Banglore_house_price_prediction](https://github.com/GUNTIKALYAN/Banglore_house_price_prediction)

---

## 🔥 Why This Project?

Real estate in Bangalore is hyper-localized. A 2BHK in Whitefield might cost drastically different than in Rajajinagar — even with the same specs.

This project:

- 🧠 Predicts house prices using area, BHK, bathrooms, location, and more.
- 🌍 Uses cleaned and filtered data from Bangalore housing listings.
- 🤖 Connects to a **WhatsApp Bot** using Twilio for real-time user interaction.

---

## 🌟 What Makes This Project Unique?

Unlike typical house price prediction apps, this project goes beyond basic ML deployment:

### 🤖 WhatsApp Bot Integration
- Most ML projects stop at a web interface — **this one lets users interact via WhatsApp!**
- Seamless integration using **Twilio API** + **Flask Webhooks**
- You can ask:  
  *"What's the price of a 2 BHK in Indiranagar, 1100 sqft?"*  
  and get an instant reply like:  
  *"Estimated Price: ₹ 95 Lakhs"*
- You can get locations by typing:
  "locations"
---
## 🚀 Features

- ✅ House price prediction using trained ML model
- 🛠️ Cleaned & engineered dataset
- 📁 Modular code with separate model + server logic
- 🤖 Twilio-powered chatbot for price queries
- 🌐 Flask backend with templated frontend (HTML/CSS)
- 📈 JSON-powered prediction interface

---

## 🧠 Model Insights

- **Model Used**: Linear Regression
- **Target**: Price (Lakhs ₹)
- **Data Source**:
  
  ```bash
  https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data
  ```
- **Key Features**:
  - Location
  - Total Sqft
  - Number of BHK
  - Number of Bathrooms

---

## 🗂️ Project Structure
```bash
BHP/
├── model/
│ ├── banglore_home_prices_model.pkl # Trained ML model
│ ├── columns.json # Feature list
│ └── House_price_prediction.ipynb # Notebook for model training
│
├── server/
│ ├── artifacts/ # Prediction artifacts
│ ├── static/ # CSS, JS, assets
│ ├── templates/ # HTML templates
│ └── pycache/ # Auto-generated
│
├── .env # Environment variables
├── .gitignore
├── server.py # Flask API
├── util.py # Utility functions (load model, etc.)
├── whatsapp.py # Twilio WhatsApp bot interface
├── requirements.txt
├── Bengaluru_House_Data.csv # Raw dataset
└── README.md


```
---

## 📲 WhatsApp Bot Demo

This bot lets you send a message like:
"3 BHK in Whitefield, 1200 sqft, 2 bathrooms"
And get a response like: Estimated Price: ₹ 75 Lakhs

Features:
- Accepts flexible text input
- Parses and processes message
- Responds with price prediction instantly


---
## 🧰 Tech Stack

### 💻 Frontend
- **HTML** — Structure the interface
- **CSS** — Style and responsiveness
- **JavaScript** — Input validation, interactivity

### 🧠 Backend & Model
- **Python** — Core logic, model training
- **Flask** — REST API and web server
- **Pandas & NumPy** — Data preprocessing
- **Scikit-learn** — Linear Regression model
- **Jupyter Notebook** — For training and experimentation

### 🤖 Bot Integration
- **Twilio API** — WhatsApp bot messaging
- **Flask Webhook** — Handling WhatsApp requests
- **ngrok** — Tunneling local server to public for bot testing

---

## ⚙️ How to Run Locally

### 🧪 Setup

```bash
git clone git@github.com:GUNTIKALYAN/Banglore_house_price_prediction.git
cd BHP
pip install -r requirements.txt
```

###  Run Flask App

```bash
python server.py
```
### Run WhatsApp Bot (with ngrok)
```bash
ngrok http 5000
python server.py
```
### Data
Source:
```bash
https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data
```
### Author
Gunti Kalyan
Linked-in
```bash
https://www.linkedin.com/in/gunti-kalyan-470b87252/
```
---

## 📜 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project with attribution.

**MIT License © 2025 Kalyan Gunti**

---

## Show some ❤️ by starring this repo and sharing it!
## 🛠️ Contributions, suggestions are always welcome.







