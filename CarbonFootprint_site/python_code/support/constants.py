import os

CODE_DIR = os.path.dirname(os.path.dirname(__file__))

MAIN_DIR = os.path.dirname(CODE_DIR)
IMAGES_DIR = os.path.join(MAIN_DIR, "static", "images")
EXCEL_DIR = os.path.join(MAIN_DIR, "static", "excel-files")
DATABASE_DIR = os.path.join(MAIN_DIR, "static", "databases")

TEST_DIR = os.path.join(os.path.dirname(MAIN_DIR), "test")
PROFILE_DIR = os.path.join(TEST_DIR, "profiler-results")
MONITORING_DIR = os.path.join(TEST_DIR, "monitoring_data")


def get_initializer(return_italian=True):

    ### CHANGE VALUES IN BOTH DICTIONARIES

    if return_italian:
        return {

            "DIETA": {

                "Explanation": "Descrivi il tuo regime alimentare in una settimana tipo",
                "Proteine": {

                    'Carne rossa': {

                        "base-multiplier": 41.87,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Carne bianca': {

                        "base-multiplier": 9.87,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Pesce': {

                        "base-multiplier": 8.4,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Latticini': {

                        "base-multiplier": 23.9,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Uova': {

                        "base-multiplier": 4.7,  # kgCO2/kg
                        "placeholder": "[uova/sett]",
                        "unit-conversion-multi": 1 / 20,  # 20 as an egg is almost 50g
                        "time-base": "week"

                    },

                },
                "Carboidrati": {

                    'Pasta': {

                        "base-multiplier": 1.12,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Riso': {

                        "base-multiplier": 4.45,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Pane': {

                        "base-multiplier": 0.731,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Cereali': {

                        "base-multiplier": 1.57,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Mais': {

                        "base-multiplier": 1.7,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Zucchero': {

                        "base-multiplier": 3.2,  # kgCO2/kg
                        "placeholder": "[cucchiaini/sett]",
                        "unit-conversion-multi": 8 / 1000,
                        "time-base": "week"

                    },

                },
                "Frutta e verdura": {

                    'Pomodori': {

                        "base-multiplier": 2.09,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Legumi': {

                        "base-multiplier": 1.8,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Ortaggi a radice': {

                        "base-multiplier": 0.43,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },

                    'Verdure a foglia': {

                        "base-multiplier": 0.57,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"
                    },

                    'Frutta': {

                        "base-multiplier": 0.82,  # kgCO2/kg
                        "placeholder": "[frutti/sett]",
                        "unit-conversion-multi": 1 / 4,  # The average apple is 250g
                        "time-base": "week"

                    },
                },
                "Altro": {

                    'Cioccolato': {

                        "base-multiplier": 45,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Caffè': {

                        "base-multiplier": 0.05953,  # kgCO2/cup
                        "placeholder": "[tazzine/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },

                    'Olio': {

                        "base-multiplier": 6,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },
                    'Latte': {

                        "base-multiplier": 3.15,  # kgCO2/kg
                        "placeholder": "[litri/sett]",
                        "unit-conversion-multi": 1 / 1040,
                        "time-base": "week"

                    },
                    'Latte di soia': {

                        "base-multiplier": 0.98,  # kgCO2/kg
                        "placeholder": "[litri/sett]",
                        "unit-conversion-multi": 1 / 1040,
                        "time-base": "week"

                    },
                    'Frutta secca': {

                        "base-multiplier": 0.4,  # kgCO2/kg
                        "placeholder": "[g/sett]",
                        "unit-conversion-multi": 1 / 1000,
                        "time-base": "week"

                    },

                },

            },
            "TRASPORTI": {

                "Explanation": "Indica quanti chilometri percorri di solito in una settimana (un anno per i voli)",
                "Mezzi pubblici": {

                    'Autobus': {

                        "base-multiplier": 0.093,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Treno (Regionale)': {

                        "base-multiplier": 0.053,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Treno (Alta velocità)': {

                        "base-multiplier": 0.006,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Traghetto': {

                        "base-multiplier": 0.019,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },

                },
                "Mezzi privati": {

                    'Moto': {

                        "base-multiplier": 0.0968,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Macchina (Elettrica)': {

                        "base-multiplier": 0.12,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week",

                    },
                    'Macchina (Benzina)': {

                        "base-multiplier": 0.269,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Macchina (Diesel)': {

                        "base-multiplier": 0.229,  # kgCO2/km
                        "placeholder": "[km/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },

                },
                "Voli": {

                    'Continentali': {

                        "base-multiplier": 0.156,  # kgCO2/km
                        "placeholder": "[km/anno]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Intercontinentali': {

                        "base-multiplier": 0.15,  # kgCO2/km
                        "placeholder": "[km/anno]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },

                },

            },
            "CONSUMI DOMESTICI": {

                "Explanation": "Descrivi le tue abitudini casalinghe ",
                "General Information": {

                    'Residenti': {

                        "placeholder": "[numero]"

                    },

                },
                "Riscaldamento": {

                    "Explanation": 'Indica la classe di efficienza energetica e la superficie di casa tua insieme alla'
                                   'tipologia di dispositivo per il riscaldamento installato.',

                    "Evaluation-Function": "calcola_riscaldamento",

                    'Sistema di riscaldamento': {

                        "type": "dropdown",
                        "acceptable": {

                            "Caldaia": 0.273,  # Considering Metane boiler with 75% efficiency -> 0,2733 kg_CO2 / kWh
                            "Pompa di calore": 0.114  # Considering COP = 4 and energy mix emission = 0,457 kg_CO2 / kWh

                        }

                    },
                    'Efficienza energetica': {

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
                    'Superficie calpestabile': {

                        "placeholder": "[m^2]"

                    }

                },
                "Condizionatore": {

                    "Explanation": "Inserisci la potenza dichiarata del tuo dispositivo di climatizzazione ed il numero di giorni (e di ore per "
                                   "giorno) per cui sei solito utilizzarlo.",

                    "Evaluation-Function": "calcola_condizionamento",

                    'Potenza': {

                        "placeholder": "[kW]"

                    },
                    'Giornate torride': {

                        "placeholder": "[giornate/anno]"

                    },
                    'Ore di utilizzo': {

                        "placeholder": "[ore/giorno]"

                    }

                },
                "Elettrodomestici": {

                    "Explanation": 'Le emissioni causate dagli elettrodomestici si considerano suddivise per ogni residente'
                                   '.',

                    'Frigorifero': {

                        "base-multiplier": 0.14,  # kgCO2/day
                        "placeholder": "[quantità]",
                        "unit-conversion-multi": 1,
                        "time-base": "day"

                    },
                    'Cucina': {

                        "base-multiplier": 0.05048,  # kgCO2/meal
                        "placeholder": "[pasti/giorno]",
                        "unit-conversion-multi": 1,
                        "time-base": "day"

                    },
                    'Forno': {

                        "base-multiplier": 0.7091,  # kgCO2/usage
                        "placeholder": "[utilizzi/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Lavatrice': {

                        "base-multiplier": 0.6283,  # kgCO2/day
                        "placeholder": "[lavaggi/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },

                },
                "Altro": {

                    "Explanation": " I consumi riportati in questa sezione riguardano attività personali"
                                   ".",

                    'Igiene personale': {

                        "base-multiplier": 0.6057,  # shower/week
                        "placeholder": "[docce/sett]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Laptop': {

                        "base-multiplier": 100,  # kgCO2/year
                        "placeholder": "[quantità]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Smartphone': {

                        "base-multiplier": 120,  # kgCO2/year
                        "placeholder": "[quantità]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },

                }

            },
            "Abbigliamento": {

                "Explanation": "Indica quanti vestiti acquisti in un anno",
                "None": {

                    'Maglie (cotone)': {

                        "base-multiplier": 3,  # kgCO2/unit
                        "placeholder": "[capi/anno]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Maglie sportive': {

                        "base-multiplier": 4.08,  # kgCO2/unit
                        "placeholder": "[capi/anno]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Giacca (sintetico)': {

                        "base-multiplier": 35.7 * 0.55,  # kgCO2/unit
                        "placeholder": "[capi/anno]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Maglione': {

                        "base-multiplier": 13.12,  # kgCO2/unit
                        "placeholder": "[capi/anno]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Jeans': {

                        "base-multiplier": 33.4,  # kgCO2/unit
                        "placeholder": "[capi/anno]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },

                }

            }

        }

    return {

        "DIET":{

        "Explanation":"Enter below what you eat in a typical week",
        "Protein" :{

            'Red meat': {

                "base-multiplier": 41.87,  # kgCO2/kg
                "placeholder": "[g/week]",
                "unit-conversion-multi": 1 / 1000,
                "time-base": "week"
            },
            'White meat': {

                "base-multiplier": 9.87,  # kgCO2/kg
                "placeholder": "[g/week]",
                "unit-conversion-multi": 1 / 1000,
                "time-base": "week"

            },
            'Fish': {

                "base-multiplier": 8.39,  # kgCO2/kg
                "placeholder": "[g/week]",
                "unit-conversion-multi": 1 / 1000,
                "time-base": "week"

            },
            'cheese': {

                "base-multiplier": 23.9,  # kgCO2/kg
                "placeholder": "[g/week]",
                "unit-conversion-multi": 1 / 1000,
                "time-base": "week"

            },
            'Eggs': {

                "base-multiplier": 4.67,  # kgCO2/kg
                "placeholder": "[number/week]",
                "unit-conversion-multi": 1 / 20,  # 20 as an egg is almost 50g
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
                'Rice': {

                    "base-multiplier": 4.45,  # kgCO2/kg
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

                    "base-multiplier": 1.57,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Maize (Corn)': {

                    "base-multiplier": 1.7,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },

                'Sugar': {

                    "base-multiplier": 3.2,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },

            },
            "Fruit & Vegetables": {

                'Tomatoes': {

                    "base-multiplier": 2.09,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Legumes': {

                    "base-multiplier": 1.79,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Root Vegetables': {

                    "base-multiplier": 0.43,  # kgCO2/kg
                    "placeholder": "[g/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },

                'Leaf vegetables': {

                    "base-multiplier": 0.53,  # kgCO2/kg
                    "placeholder": "[number/week]",
                    "unit-conversion-multi": 1 / 4,  # The average apple is 250g
                    "time-base": "week"

                },
                'Fruit': {

                    "base-multiplier": 0.82,  # kgCO2/kg
                    "placeholder": "[number/week]",
                    "unit-conversion-multi": 1 / 4,  # The average fruit is 250g
                    "time-base": "week"

                },
            },
            "Other": {

                'Chocolate': {

                    "base-multiplier": 45,  # kgCO2/kg
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

                    "base-multiplier": 3.15,  # kgCO2/kg
                    "placeholder": "[litre/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Milk (Soy)': {

                    "base-multiplier": 0.98,  # kgCO2/kg
                    "placeholder": "[litre/week]",
                    "unit-conversion-multi": 1 / 1000,
                    "time-base": "week"

                },
                'Dried fruit': {

                    "base-multiplier": 0.43,  # kgCO2/kg
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

                        "base-multiplier": 0.053,  # kgCO2/km
                        "placeholder": "[km/week]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Train (High speed)': {

                        "base-multiplier": 0.006,  # kgCO2/km
                        "placeholder": "[km/week]",
                        "unit-conversion-multi": 1,
                        "time-base": "week"

                    },
                    'Ferry': {

                        "base-multiplier": 0.019,  # kgCO2/km
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

                    'National flights': {

                        "base-multiplier": 0.156,  # kgCO2/km
                        "placeholder": "[km/year]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'International flights': {

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

                            "Boiler": 0.273,  # Considering Metane boiler with 75% efficiency -> 0,2733 kg_CO2 / kWh
                            "Heat Pump": 0.114  # Considering COP = 4 and energy mix emission = 0,457 kg_CO2 / kWh

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

                },
            },
            "CLOTHES": {

                "Explanation": "Enter below how many clothes you buy in a year",
                "None": {

                    'Shirt (Cotton)': {

                        "base-multiplier": 3,  # kgCO2/unit
                        "placeholder": "[items/year]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Shirt (Polyester)': {

                        "base-multiplier": 4.08,  # kgCO2/unit
                        "placeholder": "[items/year]",
                        "unit-conversion-multi": 1,
                        "time-base": "year"

                    },
                    'Jacket (Acrylic)': {

                        "base-multiplier": 35.7 * 0.55,  # kgCO2/unit
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




def get_world_co2_impact(return_italian=True):

    if return_italian:

        return {

            'Mondiale': 4690,
            'Asia': 4620,
            'Sud America': 2500,
            'Nord America': 10300,
            'Africa': 1000,
            'Europa': 7110,
            'Stati uniti': 14860,
            'Germania': 8090,
            'Italia': 5550,
            'Francia': 4740,

        }

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

