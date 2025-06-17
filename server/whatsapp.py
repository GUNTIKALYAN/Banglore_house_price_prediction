from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from util import get_location_names, get_estimated_price
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini API URL
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1/models/"
    "gemini-1.5-flash:generateContent"
    f"?key={GEMINI_API_KEY}"
)

# Define Flask Blueprint
whatsapp_route = Blueprint('whatsapp', __name__)

@whatsapp_route.route("/", methods=["POST"])
def bot():
    user_msg = request.values.get("Body", "").strip()
    print("📩 Incoming:", user_msg)

    
    if user_msg.lower() in ["hi", "hello", "hey", "start"]:
        reply = (
            "👋 Welcome! I can help you predict Bangalore house prices.\n\n"
            "📌 Type: `predict <location> <sqft> <bhk> <bath>`\n"
            "💡 Example: `predict Whitefield 1000 2 2`\n"
            "🏙️ Or type `locations` to see valid areas."
        )

    # Show available locations
    elif user_msg.lower() == "locations":
        locations = get_location_names()
        reply = "📍 Available Locations in Bangalore:\n\n" + ", ".join(locations[:20]) + "..."

    # Handle prediction request
    elif user_msg.lower().startswith("predict"):
        try:
            _, location, sqft, bhk, bath = user_msg.split()
            location = location.strip().lower()
            valid_locations = [loc.lower() for loc in get_location_names()]

            if location not in valid_locations:
                reply = (
                    "❌ Invalid location.\n"
                    "Please type `locations` to see valid ones.\n"
                    "Then use: `predict <location> <sqft> <bhk> <bath>`"
                )
            else:
                price = get_estimated_price(location, float(sqft), int(bhk), int(bath))
                reply = f"🏠 Estimated price for {bhk}BHK in {location} of {sqft} sqft with {bath} baths is ₹{round(price, 2)} lakhs."
        except Exception as e:
            reply = (
                "⚠️ Invalid input format.\n"
                "Use: `predict <location> <sqft> <bhk> <bath>`\n"
                "Example: `predict IndiraNagar 1500 3 2`"
            )

    # General fallback to Gemini
    else:
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": user_msg}]
                }
            ]
        }
        try:
            res = requests.post(GEMINI_URL, headers=headers, data=json.dumps(data))
            if res.status_code == 200:
                response_json = res.json()
                reply = response_json["candidates"][0]["content"]["parts"][0]["text"]
            else:
                reply = "⚠️ Gemini API error. Try again later."
        except Exception as e:
            reply = f"❌ Gemini connection error: {e}"

    # Return Twilio-compatible response
    twilio_resp = MessagingResponse()
    twilio_resp.message(reply)
    return str(twilio_resp)
