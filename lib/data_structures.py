spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciestFoods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciestFoods)

def get_average_heat_level(spicy_foods):
    spiciness = [food['heat_level'] for food in spicy_foods]
    return sum(spiciness) / len(spiciness)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print_spiciest_foods(spicy_foods)
print(get_average_heat_level(spicy_foods))

spicy_food = {
    'name': 'Spicy Fried Rice',
    'cuisine': 'Thai',
    'heat_level': 8
}

print(create_spicy_food(spicy_foods, spicy_food))
