import requests

def fetch_weather(location):
    # Approx lat/lon for Nashik
    lat, lon = 20.00, 73.78
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
        response.raise_for_status()
        data = response.json()
        current = data.get("current_weather", {})
        temp = current.get("temperature", "NA")
        windspeed = current.get("windspeed", "NA")
        return f"Current temperature: {temp}°C, Wind speed: {windspeed} km/h"
    except:
        return "Weather information is currently not available."

def get_mandi_price(crop):
    prices = {
        "tomato": "₹20 per kg",
        "onion": "₹15 per kg",
        "potato": "₹10 per kg",
        "wheat": "₹22 per kg",
        "rice": "₹24 per kg",
        "maize": "₹14 per kg",
        "sugarcane": "₹3 per kg",
        "cotton": "₹65 per kg",
    }
    return prices.get(crop.lower(), "No price data available for this crop.")

def best_crop_for_season(season):
    crops_by_season = {
        "kharif": ["rice", "maize", "soybean", "cotton", "sugarcane", "groundnut"],
        "rabi": ["wheat", "barley", "gram", "mustard", "peas"],
        "summer": ["maize", "moong", "watermelon", "gourd"]
    }
    if season in crops_by_season:
        return f"Best crops for {season} season: {', '.join(crops_by_season[season]).title()}"
    return "Please specify Kharif, Rabi, or Summer season."

def pest_management(crop):
    solutions = {
        "tomato": "For tomato leaf curl, use yellow sticky traps and avoid excess nitrogen. For fruit borer, use neem oil spray.",
        "cotton": "For bollworms, install pheromone traps and use recommended biopesticides.",
        "rice": "Manage stem borer by keeping the field flooded and using trichogramma cards.",
    }
    return solutions.get(crop.lower(), "Please specify the crop for pest advice (e.g., tomato, cotton, rice).")

def fertilizer_recommendations(crop):
    recommendations = {
        "wheat": "Recommended NPK is 120:60:40 kg/ha. Apply 2 split doses of nitrogen.",
        "rice": "Recommended NPK is 100:50:50 kg/ha. Use 1/3rd N at sowing, balance in splits.",
        "potato": "Apply 150:60:100 kg/ha NPK; add well-rotted FYM before planting.",
    }
    return recommendations.get(crop.lower(), "For fertilizer advice, specify crop: wheat, rice, potato, etc.")

def soil_preparation(crop):
    guidelines = {
        "sugarcane": "Deep plough the soil and ensure proper drainage. Add FYM and green manure.",
        "cotton": "Conduct summer ploughing, incorporate crop residues and level the field for uniform irrigation.",
        "onion": "Fine tilth soil with adequate organic matter works best."
    }
    return guidelines.get(crop.lower(), "Please specify the crop for soil preparation (e.g., sugarcane, cotton, onion).")

def general_farming_tips():
    return (
        "- Use certified seeds for better yield.\n"
        "- Adopt crop rotation to keep soil healthy.\n"
        "- Monitor weather forecasts to plan irrigation and pesticide sprays.\n"
        "- Take soil tests every 2-3 years.\n"
        "- Practice integrated pest management to reduce chemical use."
    )

def main():
    print("Welcome to AI Agent for Smart Farming Advice")
    print("Supported: Weather, mandi prices (tomato/onion/potato/wheat/rice/maize/sugarcane/cotton), best crops for season, pest management, soil, fertilizers, tips.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Your question: ").strip().lower()
        if query == "exit":
            print("Thank you for using the Smart Farming Advice Agent.")
            break

        if "weather" in query:
            print(fetch_weather("Nashik"))
        elif "mandi price" in query or ("price" in query and any(c in query for c in ["tomato", "onion", "potato", "wheat", "rice", "maize", "sugarcane", "cotton"])):
            for crop in ["tomato", "onion", "potato", "wheat", "rice", "maize", "sugarcane", "cotton"]:
                if crop in query:
                    print(f"Mandi price for {crop}: {get_mandi_price(crop)}")
                    break
            else:
                print("Please specify crop for mandi price: tomato, onion, potato, wheat, rice, maize, sugarcane, cotton.")
        elif "best crop" in query or ("grow" in query and "season" in query):
            if "kharif" in query:
                print(best_crop_for_season("kharif"))
            elif "rabi" in query:
                print(best_crop_for_season("rabi"))
            elif "summer" in query:
                print(best_crop_for_season("summer"))
            else:
                print("Please specify season (kharif, rabi, summer).")
        elif "pest" in query or "disease" in query:
            for crop in ["tomato", "cotton", "rice"]:
                if crop in query:
                    print(pest_management(crop))
                    break
            else:
                print("Specify crop for pest management advice (e.g., pest in tomato).")
        elif "soil" in query and ("prepare" in query or "preparation" in query):
            for crop in ["sugarcane", "cotton", "onion"]:
                if crop in query:
                    print(soil_preparation(crop))
                    break
            else:
                print("Specify which crop for soil preparation tips (e.g., soil preparation for sugarcane).")
        elif "fertilizer" in query or "fertiliser" in query:
            for crop in ["wheat", "rice", "potato"]:
                if crop in query:
                    print(fertilizer_recommendations(crop))
                    break
            else:
                print("Specify crop for fertilizer suggestion (e.g., fertilizer for wheat).")
        elif "farming tip" in query or "advice" in query or "how to improve" in query:
            print(general_farming_tips())
        else:
            print("Sorry, I can help with questions about weather, mandi price, crops for season, pest management, soil, fertilizers, and general tips. Try rephrasing your question.")

if __name__ == "__main__":
    main()


