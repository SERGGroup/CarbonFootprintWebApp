from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.widgets.core import TextInput
from .constants import get_initializer


class CustomStringInput(TextInput):

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class_'] = '%s %s' % ("text-input input", c)
        return super().__call__(field, **kwargs)


class CustomStringField(StringField):
    widget = CustomStringInput()


class CustomInput:

    def __init__(self, name, input_dict, super_class):

        self.name = name
        self.__init_from_dict(input_dict)
        self.super_class = super_class

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

        return "{}_{}".format(self.super_class.main_class.name, self.name)

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


class FormSubModules:

    def __init__(self, name, init_dict, main_class):

        self.name = name
        self.co2_cost = 0.

        if self.name.lower() == "none":
            self.name = None

        self.input_list = list()
        self.main_class = main_class

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

    def append_data(self, form):

        for input_value in self.input_list:
            input_value.append_data(form)

    def overall_co2_cost(self):

        self.co2_cost = 0.
        for input_value in self.input_list:
            self.co2_cost += input_value.co2_cost


class FormMainModules:

    def __init__(self, name, init_dict):

        self.name = name
        self.input_list = list()
        self.explanation = init_dict.get("Explanation")
        self.co2_cost = 0.

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

    def append_data(self, form):

        for sub_modules in self.input_list:
            sub_modules.append_data(form)

    def overall_co2_cost(self):

        self.co2_cost = 0.
        for input_value in self.input_list:
            self.co2_cost += input_value.co2_cost


class MainFormClass:

    def __init__(self):

        init_dict = get_initializer()
        self.input_list = list()
        self.return_dict = dict()
        self.co2_cost = 0.

        for base_key in init_dict.keys():
            self.input_list.append(FormMainModules(base_key, init_dict[base_key]))
            self.return_dict.update(self.input_list[-1].get_fields_dict())

        self.form_class = self.__init_form_class()

    def __init_form_class(self):

        class F(Form):
            pass

        for key in self.return_dict.keys():
            setattr(F, key, self.return_dict[key])

        return F

    def evaluate_results(self, curr_form):

        self.co2_cost = 0.

        for main_modules in self.input_list:

            main_modules.append_data(curr_form)
            main_modules.overall_co2_cost()
            self.co2_cost += main_modules.co2_cost
