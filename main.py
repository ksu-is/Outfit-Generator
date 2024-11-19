import random

def get_weather_input():
# Asking the user for input based on weather
    print("What's the weather like? Options: sunny, rainy, cold, hot")
    weather = input("Weather: ").strip().lower()
    return weather

def get_outing_input():
# Asking the user for the type of outing.
    print("Where are you going? Options: casual, formal, workout, party")
    outing = input("Outing: ").strip().lower()
    return outing

def suggest_outfit(weather, outing):
# Generates an outfit suggestion based on weather and type of outing
    outfits = {
        "sunny": {
            "casual": ["T-shirt and shorts", "Light sundress"],
            "formal": ["Light suit", "Summer dress"],
            "workout": ["Tank top and running shorts"],
            "party": ["Floral shirt and chinos", "Bright-colored dress"]
        },
        "rainy": {
            "casual": ["Raincoat and jeans", "Waterproof jacket"],
            "formal": ["Trench coat and formal pants"],
            "workout": ["Water resistant hoodie and leggings"],
            "party": ["Dark colored outfit with a raincoat"]
        },
        "cold": {
            "casual": ["Sweater and jeans", "Hoodie and joggers"],
            "formal": ["Wool suit", "Long coat and dress"],
            "workout": ["Thermal gear and sweatpants"],
            "party": ["Sweater dress with tights", "Blazer and warm trousers"]
        },
        "hot": {
            "casual": ["Tank top and shorts", "Sleeveless dress"],
            "formal": ["Linen suit", "Light blouse and skirt"],
            "workout": ["Breathable tank top and shorts"],
            "party": ["Short-sleeved shirt and lightweight pants"]
        }
    }

    if weather in outfits and outing in outfits[weather]:
        return random.choice(outfits[weather][outing])
    else:
        return "Sorry, I don't have an outfit suggestion for that combination at this time."

def main():
# This would be the main function to run the outfit generator.
    print("Welcome to the Outfit Generator!")
    weather = get_weather_input()
    outing = get_outing_input()

    outfit = suggest_outfit(weather, outing)
    print(f"\nBased on the weather and outing, you should wear: {outfit}")

if __name__ == "__main__":
    main()
