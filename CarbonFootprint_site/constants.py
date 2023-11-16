import os

MAIN_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(MAIN_DIR, "static", "images")

def get_coefficients(form):

    return {

        # Food and Drink
        'beef_herd': 60 / 7 / 1000,         # kgCO2/kg
        'lumb_mutton': 24 / 7 / 1000,       # kgCO2/kg
        'cheese': 21 / 7 / 1000,            # kgCO2/kg
        'beef_dairy': 21 / 7 / 1000,        # kgCO2/kg
        'chocolate': 19 / 7 / 1000,         # kgCO2/kg
        'coffee': 0.05953,                  # kgCO2/cup
        'prawns_farmed': 12 / 7 / 1000,     # kgCO2/kg
        'pig_meat': 7 / 7 / 1000,           # kgCO2/kg
        'wheat_rye': 1.4 / 7 / 1000,        # kgCO2/kg
        'tomatoes': 1.4 / 7 / 1000,         # kgCO2/kg
        'maize': 1 / 7 / 1000,              # kgCO2/kg
        'peas': 0.9 / 7 / 1000,             # kgCO2/kg
        'soy_milk': 0.9 / 7 / 1000,         # kgCO2/kg
        'poultry_meat': 6 / 7 / 1000,       # kgCO2/kg
        'olive_oil': 6 / 7 / 1000,          # kgCO2/kg
        'fish_farmed': 5 / 7 / 1000,        # kgCO2/kg
        'pasta': 1.9 / 7 / 1000,            # kgCO2/kg
        'bread': 0.731 / 7 / 1000,          # kgCO2/kg
        'eggs': 4.5 / 20 / 7,               # kgCO2/kg (/20 is a conversion factor as an egg is around 50g)
        'rice': 4 / 7 / 1000,               # kgCO2/kg
        'fish_wildcatch': 3 / 7 / 1000,     # kgCO2/kg
        'milk': 3 / 7 / 1000,               # kgCO2/kg
        'cane_sugar': 3 / 7 / 1000,         # kgCO2/kg
        'groundnuts': 2.5 / 7 / 1000,       # kgCO2/kg
        'bananas': 0.7 / 7 / 5,             # kgCO2/kg
        'root_vegetables': 0.4 / 7 / 1000,  # kgCO2/kg
        'apples': 0.4 / 7 / 4,              # kgCO2/kg (/4 is a conversion factor as an apple is around 250g)
        'citrus_fruit': 0.3 / 7 / 4,        # kgCO2/kg
        'nuts': 0.3 / 7 / 1000,             # kgCO2/kg

        # Transportation
        'domestic_flight':  0.255 / 365,
        'mediumcar_petrol': 0.192 / 7 / float(form['passangers_petrol']),
        'mediumcar_diesel': 0.171 / 7 / float(form['passangers_diesel']),
        'short_flight': 0.156 / 365,
        'long_flight': 0.150 / 365,
        'bus': 0.105 / 7,
        'motorcycle': 0.103 / 7,
        'electric_vehicle': 0.128 / 7,
        'national_rail': 0.041 / 7,
        'ferry': 0.019 / 7,
        'eurostar': 0.006 / 7,

        # Home
        'refrigerator': 0.14 / float(form['number_family']),        # kgco2/day
        'food_cooking': 0.05048 / float(form['number_family']),     # kgco2/meal
        'oven': 0.7091 / float(form['number_family']),              # kgco2/meal
        'washing_machine': 0.6283 / float(form['number_family']),   # kgco2/cycle
        'personal_cleaning': 0.6057,                                # kgco2/shower
        'laptop': 100 / 365,                                        # kgCO2/device
        'smartphone': 120 / 365,                                    # kgCO2/device
        'heating': 1 / float(form['number_family']),                # from user it returns directly the number of co2

        # Clothing
        'cotton_shirt': 10.75 / 365,            # kgco2/unit
        'cotton_sweatjacket': 13.42 / 365,      # kgco2/unit
        'acrylic_jacket': 13.67 / 365,          # kgco2/unit
        'woolen_sweater': 13.12 / 365,          # kgco2/unit
        'polyester_shirt': 81.62 / 365,         # kgco2/unit
        'jeans': 90.37 / 365,                   # kgco2/unit

}
