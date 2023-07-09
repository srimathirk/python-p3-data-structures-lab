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
    names = [spicy_food["name"] for spicy_food in spicy_foods]
    print(names)
    return(names)

#get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spiciest = [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5 ]
    print(spiciest)
    return(spiciest)

#get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        format_out = "{name} ({cuisine}) | Heat Level: {heat_level}".format(
            name=spicy_food["name"],
            cuisine=spicy_food["cuisine"],
            heat_level="🌶" * spicy_food["heat_level"]
        )
        print(format_out)
    return format_out


#print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food['cuisine'] == cuisine:
            return spicy_food
    

#get_spicy_food_by_cuisine(spicy_foods, "Thai")

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            format_out = "{name} ({cuisine}) | Heat Level: {heat_level}".format(
                name=spicy_food["name"],
                cuisine=spicy_food["cuisine"],
                heat_level="🌶" * spicy_food["heat_level"]
            )
            print(format_out)
    return format_out

#print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat = 0
    
    for spicy_food in spicy_foods:
        total_heat += spicy_food["heat_level"]
    avg_heat_level = total_heat / len(spicy_foods)
    print(avg_heat_level)
    return(avg_heat_level)
#get_average_heat_level(spicy_foods)    

def create_spicy_food(spicy_foods, spicy_food):
    new_food = spicy_food
    spicy_foods.append(new_food)
    print(spicy_foods)
    return(spicy_foods)
#create_spicy_food(spicy_foods, { "name": "Griot", "cuisine": "haitian", "heat_level": 10 })
