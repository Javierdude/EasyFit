import requests
import json ##Gives access to JSON library

APP_ID = 'bfa9b5f5'  # Replace with your actual APP_ID
API_KEY = 'a1acb515aba04361427f0598ffaf4476'  # Replace with your actual API_KEY

def get_food_options(food_item):
    url = "https://trackapi.nutritionix.com/v2/search/instant"
    headers = { ##A DICTIONARY containing headers for the request
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }
    params = { ##Holds the information needed to send
        "query": food_item ##Query is basically telling you what food youre asking for
    } ##Food item is the food you're inquiring about.
    response = requests.get(url, headers=headers, params=params) ##Sends the request
    if response.status_code == 200: ##Checks if code is okay (200)
        results = response.json()["branded"] ##Pushes out items that match perameters
        options = [] ##Creates an empty list for parameters
        for result in results: #Loops through each result until all results are done
            options.append({ ##Adds a dictionary with the food name and nix_item_id
                "food_name": result["food_name"],
                "nix_item_id": result["nix_item_id"]
            })
        return options ##Gives you list of options
    else:
        return None ##Returns nothing if nothing is available

def get_detailed_food_options(nix_item_id): ##Takes "nixitemid" as an input and returns food info
    url = "https://trackapi.nutritionix.com/v2/search/item" ##Endpoint url used to get detailed info
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }
    params = { ##Dictionary containing paramters
        "nix_item_id": nix_item_id
    }
    response = requests.get(url, headers=headers, params=params) ##Requests info from url using parameters and headers
    if response.status_code == 200: ##If okay
        return response.json() 
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

def display_nutrition_info(nutrition_info):
    filtered_data = {
        Name: nutrition_info["foods"][0]["food_name"],
        "serving_qty": nutrition_info["foods"][0]["serving_qty"],
        "nf_calories": nutrition_info["foods"][0]["nf_calories"],
        "nf_protein": f"{nutrition_info['foods'][0]['nf_protein']} grams",
        "nf_total_fat": f"{nutrition_info['foods'][0]['nf_total_fat']} grams",
        "nf_total_carbohydrate": f"{nutrition_info['foods'][0]['nf_total_carbohydrate']} grams"

    }
    return filtered_data
    

if __name__ == "__main__":
    food_item = input("Enter a food item: ")
    options = get_food_options(food_item)
    if options:
        print("Choose one of the following options:")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option['food_name']}")
        choice = int(input("Enter the number of the option you want: "))
        if 1 <= choice <= len(options):
            selected_food = options[choice - 1]
            detailed_options = get_detailed_food_options(selected_food['nix_item_id'])
            if "error" not in detailed_options:
                filtered_info = display_nutrition_info(detailed_options)
                print("Detailed report of macros:")
                print(filtered_info)
            else:
                print(detailed_options["error"])
        else:
            print("Invalid choice.")
    else:
        print(f"No options found for '{food_item}'.")
