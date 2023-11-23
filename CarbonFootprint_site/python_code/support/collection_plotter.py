import numpy as np

from .constants import get_world_co2_impact
from copy import deepcopy

WORLD_IMPACT = get_world_co2_impact()

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
        self.comparison_value_organized = list()
        self.overall_yearly_ton_impact = 0

    def update(self):

        self.labels = list()
        self.output_list = list()

        input_list = self.collection.input_list

        if len(input_list) == 1:

            if hasattr(input_list[0], "input_list"):

                input_list = input_list[0].input_list

        for main_modules in input_list:

            self.labels.append(main_modules.name.title())
            self.output_list.append(main_modules.co2_cost * 365)

        self.comparison_dict.update({

            "You": self.collection.co2_cost * 365

        })

        self.comparison_dict = dict(sorted(self.comparison_dict.items(), key=lambda x:x[1]))
        self.comparison_labels = list(self.comparison_dict.keys())
        self.comparison_values = list(self.comparison_dict.values())

        you_position = self.comparison_labels.index("You")
        new_list = deepcopy(self.comparison_values)
        new_list[you_position] = 0

        self.comparison_value_organized = {'Total': new_list}
        for i in range(len(self.output_list)):

            new_list = np.zeros(len(self.comparison_values))
            new_list[you_position] = self.output_list[i]
            self.comparison_value_organized.update({self.labels[i]: list(new_list)})

        self.overall_yearly_ton_impact = round(self.collection.co2_cost * 365 / 1000 * 100) / 100

        self.id = hash(self.collection)
        self.comparison_id = hash(self)
