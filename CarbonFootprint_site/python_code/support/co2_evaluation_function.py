from .constants import get_initializer

initializer_ita = get_initializer()
initializer_eng = get_initializer(return_italian=False)


def evaluate_function(heating_module, function_name):
    if function_name == "evaluate_heating":
        return __evaluate_heating(heating_module, is_italian=False)

    elif function_name == "evaluate_cooling":
        return __evaluate_cooling(heating_module, is_italian=False)

    elif function_name == "calcola_riscaldamento":
        return __evaluate_heating(heating_module, is_italian=True)

    elif function_name == "calcola_condizionamento":
        return __evaluate_cooling(heating_module, is_italian=True)

    else:
        return __evaluate_default(heating_module)

def __evaluate_heating(heating_module, is_italian):
    if is_italian:
        people_count = heating_module.main_class.get_field_value("Residenti")
    else:
        people_count = heating_module.main_class.get_field_value("People Living in the House")

    if people_count == 0:
        people_count = 1

    if is_italian:
        efficiency_multiplier = heating_module.get_field_value("Efficienza energetica") * 55
        device_multiplier = heating_module.get_field_value("Sistema di riscaldamento")
        square_meters = heating_module.get_field_value("Superficie calpestabile")

    else:
        efficiency_multiplier = heating_module.get_field_value("Efficiency class") * 55
        device_multiplier = heating_module.get_field_value("Heating Device")
        square_meters = heating_module.get_field_value("House area")

    return efficiency_multiplier * square_meters * device_multiplier / people_count / 365

def __evaluate_cooling(heating_module, is_italian):

    if is_italian:
        people_count = heating_module.main_class.get_field_value("Residenti")
    else:
        people_count = heating_module.main_class.get_field_value("People Living in the House")

    if people_count == 0:
        people_count = 1

    if is_italian:
        power = heating_module.get_field_value('Potenza')
        activation_time = heating_module.get_field_value('Giornate torride') * heating_module.get_field_value('Ore di utilizzo')
        heat_pump_factor = initializer_ita["CONSUMI DOMESTICI"]["Riscaldamento"]['Sistema di riscaldamento']["acceptable"]["Caldaia"]

    else:
        power = heating_module.get_field_value('Power')
        activation_time = heating_module.get_field_value('Hot days') * heating_module.get_field_value('Hours per day')
        heat_pump_factor = initializer_eng["HOME"]["House Heating"]['Heating Device']["acceptable"]["Heat Pump"]

    return heat_pump_factor * activation_time * power / people_count / 365

def __evaluate_default(heating_module):

    co2_production = 0.
    for input_value in heating_module.input_list:

        if hasattr(input_value, "evaluate_co2_cost"):
            input_value.evaluate_co2_cost()

        co2_production += input_value.co2_cost

    return co2_production
