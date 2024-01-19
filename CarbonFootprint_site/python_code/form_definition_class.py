from .support.co2_evaluation_function import get_initializer, evaluate_function
from .support.collection_plotter import CollectionPlotter
from .input_field_classes import init_input
from abc import ABC, abstractmethod
from datetime import datetime
from wtforms import Form


class InputCollection(ABC):

    def __init__(self, name, init_dict, main_class):

        self.co2_cost = 0.

        self.name = name
        self.main_class = main_class
        self.input_list = list()
        self.direct_fields = list()

        self.explanation = init_dict.pop("Explanation", None)
        self.evaluation_function = init_dict.pop("Evaluation-Function", None)
        self.init_general_information(init_dict.pop("General Information", None))
        self.init_from_dict(init_dict)
        self.plotter = CollectionPlotter(self)

    def init_general_information(self, general_information):

        if general_information is not None:
            for info_key in general_information.keys():
                self.direct_fields.append(init_input(info_key, general_information[info_key], self))

    def append_data(self, form):

        for input_value in self.input_list:
            input_value.append_data(form)

        for direct_input in self.direct_fields:
            direct_input.append_data(form)

    def evaluate_co2_cost(self):

        self.co2_cost = evaluate_function(self, self.evaluation_function)
        self.plotter.update()

    def append_db_entry_to(self, db_model):

        for input_value in self.input_list:
            db_model = input_value.append_db_entry_to(db_model)

        for direct_input in self.direct_fields:
            db_model = direct_input.append_db_entry_to(db_model)

        return db_model

    def get_fields_dict(self):

        return_dict = dict()

        for sub_module in self.input_list:
            return_dict.update(sub_module.get_fields_dict())

        for field in self.direct_fields:
            return_dict.update(field.get_fields_dict())

        return return_dict

    def get_db_model_dict(self, db):

        return_dict = dict()

        for sub_module in self.input_list:
            return_dict.update(sub_module.get_db_model_dict(db))

        for field in self.direct_fields:
            return_dict.update(field.get_db_model_dict(db))

        return return_dict

    def get_field_value(self, field_name):

        for curr_list in [self.direct_fields, self.input_list]:

            for field in curr_list:

                if field.name == field_name:

                    try:
                        value = field.value
                        return value

                    except:
                        pass

        return 0.

    @property
    def has_explanation(self):

        return self.explanation is not None

    @property
    def has_direct_fields(self):

        return len(self.direct_fields) > 0

    @abstractmethod
    def init_from_dict(self, init_dict):

        pass

class FormSubModules(InputCollection):

    def init_from_dict(self, init_dict):

        if self.name.lower() == "none":
            self.name = None

        for input_key in init_dict.keys():
            new_field = init_input(input_key, init_dict[input_key], self)
            self.input_list.append(new_field)

    @property
    def has_name(self):

        return self.name is not None

class FormMainModules(InputCollection):

    def init_from_dict(self, init_dict):

        for sub_key in init_dict.keys():

            if type(init_dict[sub_key]) == dict:

                self.input_list.append(FormSubModules(sub_key, init_dict[sub_key], self))

class MainFormClass(InputCollection):

    def init_from_dict(self, init_dict):

        for base_key in init_dict.keys():
            self.input_list.append(FormMainModules(base_key, init_dict[base_key], self))

    def __init__(self):

        init_dict = get_initializer()
        self.return_dict = dict()

        super().__init__("Main", init_dict, None)

        self.form_class = self.__init_form_class()

    def __init_form_class(self):

        class F(Form):
            pass

        fields_dict = self.get_fields_dict()
        for key in fields_dict.keys():
            setattr(F, key, fields_dict[key])

        return F

    def init_db_class(self, db, bind_key):

        class DBModel(db.Model):

            __bind_key__ = bind_key
            id = db.Column(db.Integer, primary_key=True)
            date_created = db.Column(db.DateTime, default=datetime.utcnow)

        db_model_dict = self.get_db_model_dict(db)
        for key in db_model_dict.keys():
            setattr(DBModel, key, db_model_dict[key])

        return DBModel

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