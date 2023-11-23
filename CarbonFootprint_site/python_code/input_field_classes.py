from .support.widgets import CustomDropdownField, CustomStringField
from abc import ABC, abstractmethod

class CustomInput(ABC):

    def __init__(self, name, input_dict, collection_class):

        self.name = name
        self.label = self.name
        self.sub_label = None
        self.init_label()

        self.init_from_dict(input_dict)
        self.collection_class = collection_class

        self.value = 0.
        self.co2_cost = 0.
        self.field = CustomStringField(self.label)

        self.init_field()

    def init_label(self):

        self.label = self.name
        self.sub_label = None

        if "(" in self.name and ")" in self.name:

            label_parts = self.name.split("(")
            self.label = label_parts[0]
            self.sub_label = "(" + label_parts[1]

    @property
    def get_name(self):

        return "{}_{}".format(self.collection_class.main_class.name, self.name)

    @property
    def has_sub_label(self):

        return self.sub_label is not None

    def append_data(self, form):

        try:
            self.value = float(form[self.get_name].data)

        except:
            self.value = 0

        self.evaluate_co2_cost()

    def get_fields_dict(self):

        return {self.get_name: self.field}

    @abstractmethod
    def init_from_dict(self, input_dict):

        pass

    @abstractmethod
    def init_field(self):

        pass

    @abstractmethod
    def evaluate_co2_cost(self):

        pass

class BaseInput(CustomInput):

    def init_from_dict(self, input_dict):

        self.time_base = input_dict.get("time-base", "day")
        self.placeholder = input_dict.get("placeholder", "")

        try:
            self.base_multiplier = float(input_dict.get("base-multiplier", 0.)),

        except:
            self.base_multiplier = 0.

        try:
            self.unit_conv_mult = float(input_dict.get("unit-conversion-multi", 0.)),

        except:
            self.unit_conv_mult = 0.

        self.__check_input()

    def init_field(self):

        self.field = CustomStringField(self.label)

    def __check_input(self):

        if type(self.placeholder) == tuple:
            self.placeholder = str(self.placeholder[0])

        if type(self.base_multiplier) == tuple:
            self.base_multiplier = self.base_multiplier[0]

        if type(self.unit_conv_mult) == tuple:
            self.unit_conv_mult = self.unit_conv_mult[0]

    def evaluate_co2_cost(self):

        self.__check_input()
        self.co2_cost = self.value * self.base_multiplier * self.unit_conv_mult

        if self.time_base == "week":
            self.co2_cost /= 7

        elif self.time_base == "year":
            self.co2_cost /= 356

class DropdownInput(CustomInput):

    def init_from_dict(self, input_dict):

        self.dropdown_list = input_dict["acceptable"]

    def init_field(self):

        if type(self.dropdown_list) == list:

            choices = [(element, element) for element in self.dropdown_list]

        else:

            choices = [(self.dropdown_list[name], name) for name in self.dropdown_list.keys()]

        self.field = CustomDropdownField(

            label=self.label,
            choices=choices

        )

    def evaluate_co2_cost(self):

        self.co2_cost = 0.

def init_input(name, init_dict, superclass):

    input_type = init_dict.get("type", None)

    if input_type is not None and input_type.lower() == "dropdown":

        return DropdownInput(name, init_dict, superclass)

    else:

        return BaseInput(name, init_dict, superclass)
