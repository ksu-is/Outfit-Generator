import random

def get_gender_input():
    # Asking the user for their gender.
    print("What's your gender? Options: male, female, nonbinary")
    gender = input("Gender: ").strip().lower()
    return gender

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

def suggest_outfit(gender, weather, outing):
    # Generates an outfit suggestion based on gender, weather, and type of outing
    outfits = {
        "male": {
            "sunny": {
                "casual": ["T-shirt and shorts", "Light polo shirt"],
                "formal": ["Light suit", "Summer blazer with chinos"],
                "workout": ["Tank top and running shorts"],
                "party": ["Floral shirt and chinos", "Bright-colored T-shirt"]
            },
            "rainy": {
                "casual": ["Raincoat and jeans", "Waterproof jacket"],
                "formal": ["Trench coat and formal pants"],
                "workout": ["Water-resistant hoodie and joggers"],
                "party": ["Dark blazer with waterproof pants"]
            },
            "cold": {
                "casual": ["Sweater and jeans", "Hoodie and joggers"],
                "formal": ["Wool suit", "Long coat and scarf"],
                "workout": ["Thermal gear and sweatpants"],
                "party": ["Blazer and warm trousers"]
            },
            "hot": {
                "casual": ["Tank top and shorts", "Short-sleeve shirt"],
                "formal": ["Linen suit", "Light cotton shirt with trousers"],
                "workout": ["Breathable tank top and shorts"],
                "party": ["Short-sleeved shirt and lightweight pants"]
            }
        },
        "female": {
            "sunny": {
                "casual": ["Light sundress", "T-shirt and shorts"],
                "formal": ["Summer dress", "Light blouse and skirt"],
                "workout": ["Tank top and running shorts"],
                "party": ["Floral dress", "Bright-colored jumpsuit"]
            },
            "rainy": {
                "casual": ["Waterproof jacket", "Raincoat with leggings"],
                "formal": ["Trench coat and dress pants"],
                "workout": ["Water-resistant hoodie and leggings"],
                "party": ["Dark dress with a raincoat"]
            },
            "cold": {
                "casual": ["Sweater and jeans", "Hoodie and leggings"],
                "formal": ["Wool coat and dress", "Long trench coat"],
                "workout": ["Thermal top and joggers"],
                "party": ["Sweater dress with tights"]
            },
            "hot": {
                "casual": ["Sleeveless dress", "Tank top and shorts"],
                "formal": ["Light blouse and skirt", "Linen dress"],
                "workout": ["Breathable tank top and shorts"],
                "party": ["Short sundress"]
            }
        },
        "nonbinary": {
            "sunny": {
                "casual": ["T-shirt and shorts", "Light sundress"],
                "formal": ["Light suit", "Summer dress"],
                "workout": ["Tank top and running shorts"],
                "party": ["Floral shirt and chinos", "Bright-colored outfit"]
            },
            "rainy": {
                "casual": ["Raincoat and jeans", "Waterproof jacket"],
                "formal": ["Trench coat and formal pants"],
                "workout": ["Water-resistant hoodie and joggers"],
                "party": ["Dark-colored outfit with a raincoat"]
            },
            "cold": {
                "casual": ["Sweater and jeans", "Hoodie and joggers"],
                "formal": ["Wool suit", "Long coat and scarf"],
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
    }

    if gender in outfits and weather in outfits[gender] and outing in outfits[gender][weather]:
        return random.choice(outfits[gender][weather][outing])
    else:
        return "Sorry, I don't have an outfit suggestion for that combination at this time."

def main():
    # This would be the main function to run the outfit generator.
    print("Welcome to the Outfit Generator!")
    gender = get_gender_input()
    weather = get_weather_input()
    outing = get_outing_input()

    outfit = suggest_outfit(gender, weather, outing)
    print(f"\nBased on your inputs, you should wear: {outfit}")

if __name__ == "__main__":
    main()
