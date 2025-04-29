import requests

def get_recipe(dish_name):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={dish_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['meals'] is None:
            print(f"Sorry, '{dish_name}' ka recipe nahi mila.")
        else:
            meal = data['meals'][0]  # pehla result uthate hain
            print("\n🍳 Recipe Found!\n")
            print("Dish Name:", meal['strMeal'])
            print("Category:", meal['strCategory'])
            print("Area:", meal['strArea'])
            print("\nInstructions:")
            print(meal['strInstructions'])
            print("\nYouTube Video (optional):", meal['strYoutube'])
    else:
        print("Error: Data nahi laa paaye.")

def cooking_agent():
    print("👩‍🍳 Welcome to Cooking Agent!")
    while True:
        user_input = input("\nKya banana chaahti ho? (type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("👋 Goodbye! Happy Cooking!")
            break
        else:
            get_recipe(user_input)

# Program start
cooking_agent()



