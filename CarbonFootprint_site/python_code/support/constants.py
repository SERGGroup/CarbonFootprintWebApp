import os

CODE_DIR = os.path.dirname(os.path.dirname(__file__))

MAIN_DIR = os.path.dirname(CODE_DIR)
IMAGES_DIR = os.path.join(MAIN_DIR, "static", "images")
EXCEL_DIR = os.path.join(MAIN_DIR, "static", "excel-files")

TEST_DIR = os.path.join(os.path.dirname(MAIN_DIR), "test")
PROFILE_DIR = os.path.join(TEST_DIR, "profiler-results")
MONITORING_DIR = os.path.join(TEST_DIR, "monitoring_data")


def get_initializer():

    return {

        "DIET": {

            "Explanation": "Enter below what you eat in a typical week",
            "Protein": {

                'Beef': {

                    "base-multiplier": 68.25,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Beef (dairy herd)': {

                    "base-multiplier": 44.75,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Lumb & Mutton': {

                    "base-multiplier": 24,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Cheese': {

                    "base-multiplier": 21,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Pig': {

                    "base-multiplier": 7.9,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Poultry': {

                    "base-multiplier": 10.4,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Eggs': {

                    "base-multiplier": 4.5,  # kgCO2/kg
                    "placeholder": "[number/week]",
                    "unit-conversion-multi": 1 / 20,    # 20 as an egg is almost 50g
                    "time-base": "week"

                },
                'Fish (farmed)': {

                    "base-multiplier": 5,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Fish (wildcatch)': {

                    "base-multiplier": 3,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Prawns': {

                    "base-multiplier": 12,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },

            },
            "Carbohydrates": {

                'Pasta': {

                    "base-multiplier": 1.12,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Bread': {

                    "base-multiplier": 0.731,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Wheat & Rye': {

                    "base-multiplier": 1.4,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Maize (Corn)': {

                    "base-multiplier": 1,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Rice': {

                    "base-multiplier": 4,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Cane Sugar': {

                    "base-multiplier": 3,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },

            },
            "Vegetables & Others": {

                'Tomatoes': {

                    "base-multiplier": 1.4,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Peas': {

                    "base-multiplier": 0.9,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Root Vegetables': {

                    "base-multiplier": 0.4,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },

                'Apples': {

                    "base-multiplier": 0.4,  # kgCO2/kg
                    "placeholder": "[number/week]",
                    "unit-conversion-multi": 1 / 4,     # The average apple is 250g
                    "time-base": "week"

                },
                'Citrus Fruit': {

                    "base-multiplier": 0.3,  # kgCO2/kg
                    "placeholder": "[number/week]",
                    "unit-conversion-multi": 1 / 4,     # The average fruit is 250g
                    "time-base": "week"

                },
                'Bananas': {

                    "base-multiplier": 0.3,  # kgCO2/kg
                    "placeholder": "[number/week]",
                    "unit-conversion-multi": 1 / 5,     # The average banana is 200g
                    "time-base": "week"

                },

                'Chocolate': {

                    "base-multiplier": 19,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Coffee': {

                    "base-multiplier": 0.05953,  # kgCO2/cup
                    "placeholder": "[cup/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },

                'Olive Oil': {

                    "base-multiplier": 6,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Milk': {

                    "base-multiplier": 3,  # kgCO2/kg
                    "placeholder": "[litre/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Milk (Soy)': {

                    "base-multiplier": 0.9,  # kgCO2/kg
                    "placeholder": "[litre/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Nuts': {

                    "base-multiplier": 0.3,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Groundnuts': {

                    "base-multiplier": 2.5,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },

            },

        },
        "TRANSPORT": {

            "Explanation": "Enter below how many kilometers you travel in a typical week/year",
            "Public transport": {

                'Bus': {

                    "base-multiplier": 0.093,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },
                'Train (Regional)': {

                    "base-multiplier": 0.041,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },
                'Train (International)': {

                    "base-multiplier": 0.006,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },
                'Ferry': {

                    "base-multiplier": 0.19,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },

            },
            "Motorized Individual Traffic": {

                'Motorcycle': {

                    "base-multiplier": 0.0968,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },
                'Car (Electric)': {

                    "base-multiplier": 0.12,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week",

                },
                'Car (Petrol)': {

                    "base-multiplier": 0.269,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },
                'Car (Diesel)': {

                    "base-multiplier": 0.229,  # kgCO2/km
                    "placeholder": "[km/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },

            },
            "Flights": {

                'Domestic':  {

                    "base-multiplier": 0.255,  # kgCO2/km
                    "placeholder": "[km/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Short Haul': {

                    "base-multiplier": 0.156,  # kgCO2/km
                    "placeholder": "[km/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Long Haul': {

                    "base-multiplier": 0.150,  # kgCO2/km
                    "placeholder": "[km/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },

            },

        },
        "HOME": {

            "Explanation": "Enter below some information about your home",
            "General Information": {

                'People Living in the House': {

                    "placeholder": "[Number]"

                },

            },
            "House Heating": {

                "Explanation": 'Insert the efficiency class and the surface area of your house together with the '
                               'heating device installed in you house.',

                "Evaluation-Function": "evaluate_heating",

                'Heating Device': {

                    "type": "dropdown",
                    "acceptable": {

                        "Boiler": 0.273,      # Considering Metane boiler with 75% efficiency -> 0,2733 kg_CO2 / kWh
                        "Heat Pump": 0.114    # Considering COP = 4 and energy mix emission = 0,457 kg_CO2 / kWh

                    }

                },
                'Efficiency class': {

                    "type": "dropdown",
                    "acceptable": {

                        "A4": 0.3,
                        "A3": 0.5,
                        "A2": 0.7,
                        "A1": 0.9,
                        "B": 1.10,
                        "C": 1.35,
                        "D": 1.75,
                        "E": 2.30,
                        "F": 3.05,
                        "G": 3.50

                    },

                },
                'House area': {

                    "placeholder": "[m^2]"

                }

            },
            "House Cooling": {

                "Explanation": "Insert the mean power of your cooling system and the number of day (and hours per "
                               "day) in which you usually use it.",

                "Evaluation-Function": "evaluate_cooling",

                'Power': {

                    "placeholder": "[kW]"

                },
                'Hot days': {

                    "placeholder": "[days/year]"

                },
                'Hours per day': {

                    "placeholder": "[hours/days]"

                }

            },
            "Home Appliances": {

                "Explanation": 'The total impact of the home appliances is divided by the number of person living in '
                               'the house.',

                'Refrigerator': {

                    "base-multiplier": 0.14,  # kgCO2/day
                    "placeholder": "[number]",
                    "unit-conversion-multi": 1,
                    "time-base": "day"

                },
                'Food Cooking': {

                    "base-multiplier": 0.05048,  # kgCO2/meal
                    "placeholder": "[meals/day]",
                    "unit-conversion-multi": 1,
                    "time-base": "day"

                },
                'Oven': {

                    "base-multiplier": 0.7091,  # kgCO2/usage
                    "placeholder": "[usages/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },
                'Washing Machine': {

                    "base-multiplier": 0.6283,  # kgCO2/day
                    "placeholder": "[cycles/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },

            },
            "Other": {

                "Explanation": "The items that make up this section are related to your personal use (not divided by "
                               "the number of people living in the house).",

                'Personal Cleaning': {

                    "base-multiplier": 0.6057,  # shower/week
                    "placeholder": "[shower/week]",
                    "unit-conversion-multi": 1,
                    "time-base": "week"

                },
                'Laptop': {

                    "base-multiplier": 100,  # kgCO2/year
                    "placeholder": "[Number]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Smartphone': {

                    "base-multiplier": 120,  # kgCO2/year
                    "placeholder": "[Number]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },

            }

        },
        "CLOTHES": {

            "Explanation": "Enter below how many clothes you buy in a year",
            "None": {

                'Shirt (Cotton)': {

                    "base-multiplier": 20*0.150,  # kgCO2/unit
                    "placeholder": "[items/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Shirt (Polyester)': {

                    "base-multiplier": 27.2,  # kgCO2/unit
                    "placeholder": "[items/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Jacket (Cotton Sweat)': {

                    "base-multiplier": 20*0.55,  # kgCO2/unit
                    "placeholder": "[items/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Jacket (Acrylic)': {

                    "base-multiplier": 35.7*0.55,  # kgCO2/unit
                    "placeholder": "[items/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Woolen Sweater': {

                    "base-multiplier": 13.12,  # kgCO2/unit
                    "placeholder": "[items/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },
                'Jeans': {

                    "base-multiplier": 33.4,  # kgCO2/unit
                    "placeholder": "[items/year]",
                    "unit-conversion-multi": 1,
                    "time-base": "year"

                },

            }

        }

    }


def get_world_co2_impact():

    return {

        'World': 4690,
        'Asia': 4620,
        'South America': 2500,
        'North America': 10300,
        'Africa': 1000,
        'Europe': 7110,
        'United States': 14860,
        'Germany': 8090,
        'Italy': 5550,
        'France': 4740,

    }
