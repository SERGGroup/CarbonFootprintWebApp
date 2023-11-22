from wtforms import Form, BooleanField, StringField, PasswordField, validators
from .constants import get_initializer, get_world_co2_impact
from wtforms.widgets.core import TextInput
from abc import ABC, abstractmethod

WORLD_IMPACT = get_world_co2_impact()

class CustomStringInput(TextInput):

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class_'] = '%s %s' % ("text-input input", c)
        return super().__call__(field, **kwargs)


class CustomStringField(StringField):
    widget = CustomStringInput()


class CollectionPlotter:

    def __init__(self, collection):

        self.collection = collection

        self.id = hash(collection)
        self.comparison_id = hash(self)

        self.labels = list()
        self.output_list = list()
        self.comparison_dict = WORLD_IMPACT
        self.comparison_labels = list()
        self.comparison_values = list()

    def update(self):

        self.labels = list()
        self.output_list = list()

        input_list = self.collection.input_list

        if len(input_list) == 1:

            if hasattr(input_list[0], "input_list"):

                input_list = input_list[0].input_list

        for main_modules in input_list:

            self.labels.append(main_modules.name)
            self.output_list.append(main_modules.co2_cost)

        self.comparison_dict.update({

            "You": self.collection.co2_cost

        })

        self.comparison_dict = dict(sorted(self.comparison_dict.items(), key=lambda x:x[1]))
        self.comparison_labels = list(self.comparison_dict.keys())
        self.comparison_values = list(self.comparison_dict.values())

        self.id = hash(self.collection)
        self.comparison_id = hash(self)


class CustomInput:

    def __init__(self, name, input_dict, collection_class):

        self.name = name
        self.__init_from_dict(input_dict)
        self.collection_class = collection_class

        self.value = 0.
        self.co2_cost = 0.
        self.field = CustomStringField(self.label)

    def __init_from_dict(self, input_dict):

        self.label = self.name
        self.sub_label = None
        if "(" in self.name and ")" in self.name:
            label_parts = self.name.split("(")
            self.label = label_parts[0]
            self.sub_label = "(" + label_parts[1]

        self.base_multiplier = float(input_dict["base-multiplier"]),
        self.placeholder = input_dict["placeholder"],

        if type(self.placeholder) == tuple:
            self.placeholder = str(self.placeholder[0])

        self.unit_conv_mult = float(input_dict["unit-conversion-multi"]),
        self.time_base = input_dict["time-base"]

        self.__check_input()

    def __check_input(self):

        if type(self.base_multiplier) == tuple:
            self.base_multiplier = self.base_multiplier[0]

        if type(self.unit_conv_mult) == tuple:
            self.unit_conv_mult = self.unit_conv_mult[0]

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

        self.__evaluate_co2_cost()

    def __evaluate_co2_cost(self):

        self.__check_input()
        self.co2_cost = self.value * self.base_multiplier * self.unit_conv_mult

        if self.time_base == "week":
            self.co2_cost /= 7

        elif self.time_base == "year":
            self.co2_cost /= 356


class InputCollection(ABC):

    def __init__(self, name, init_dict, main_class):

        self.co2_cost = 0.

        self.name = name
        self.main_class = main_class
        self.input_list = list()

        self.init_from_dict(init_dict)
        self.plotter = CollectionPlotter(self)

    @abstractmethod
    def init_from_dict(self, init_dict):

        pass

    def append_data(self, form):

        for input_value in self.input_list:
            input_value.append_data(form)

    def evaluate_co2_cost(self):

        self.co2_cost = 0.
        for input_value in self.input_list:

            if hasattr(input_value, "evaluate_co2_cost"):
                input_value.evaluate_co2_cost()

            self.co2_cost += input_value.co2_cost

        self.plotter.update()


class FormSubModules(InputCollection):

    def init_from_dict(self, init_dict):

        if self.name.lower() == "none":
            self.name = None

        for input_key in init_dict.keys():
            new_field = CustomInput(input_key, init_dict[input_key], self)
            self.input_list.append(new_field)

    @property
    def has_name(self):

        return self.name is not None

    def get_fields_dict(self):

        return_dict = dict()
        for input_value in self.input_list:
            return_dict.update({

                input_value.get_name: input_value.field

            })

        return return_dict


class FormMainModules(InputCollection):

    def init_from_dict(self, init_dict):

        self.explanation = init_dict.get("Explanation")

        for sub_key in init_dict.keys():

            if type(init_dict[sub_key]) == dict:

                self.input_list.append(FormSubModules(sub_key, init_dict[sub_key], self))

    def get_fields_dict(self):

        return_dict = dict()
        for sub_module in self.input_list:
            return_dict.update(sub_module.get_fields_dict())

        return return_dict

    @property
    def has_explanation(self):

        return self.explanation is not None


class MainFormClass(InputCollection):

    def init_from_dict(self, init_dict):

        self.return_dict = dict()

        for base_key in init_dict.keys():
            self.input_list.append(FormMainModules(base_key, init_dict[base_key], self))
            self.return_dict.update(self.input_list[-1].get_fields_dict())

    def __init__(self):

        init_dict = get_initializer()
        self.return_dict = dict()

        super().__init__("Main", init_dict, None)

        self.form_class = self.__init_form_class()

    def __init_form_class(self):

        class F(Form):
            pass

        for key in self.return_dict.keys():
            setattr(F, key, self.return_dict[key])

        return F

    def evaluate_results(self, curr_form):

        for main_modules in self.input_list:

            main_modules.append_data(curr_form)

        self.evaluate_co2_cost()

    @property
    def labels(self):

        labels = list()
        for main_modules in self.input_list:

            labels.append(main_modules.name)

        return labels

    @property
    def output_list(self):

        output_list = list()
        for main_modules in self.input_list:

            output_list.append(main_modules.co2_cost)

        return output_list