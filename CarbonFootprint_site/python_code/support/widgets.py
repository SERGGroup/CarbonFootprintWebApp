from wtforms import SelectField, StringField
from wtforms.widgets.core import TextInput, Select

class CustomStringInput(TextInput):

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class_'] = '%s %s' % ("text-input input", c)
        return super().__call__(field, **kwargs)

class CustomStringField(StringField):
    widget = CustomStringInput()

class CustomDropdownInput(Select):

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class_'] = '%s %s' % ("select-cls", c)
        return super().__call__(field, **kwargs)

class CustomDropdownField(SelectField):
    widget = CustomDropdownInput()