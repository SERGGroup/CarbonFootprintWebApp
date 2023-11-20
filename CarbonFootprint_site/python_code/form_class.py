from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.widgets.core import TextInput


class CustomStringInput(TextInput):

    def __init__(self):
        super().__init__()

    def __call__(self, field, **kwargs):

        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '%s %s' % ("text-input", c)
        kwargs['placeholder'] = '%s' % (field.placeholder)
        return super().__call__(field, **kwargs)


class CustomStringField(StringField):

    widget = CustomStringInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholder = "none"


class RegistrationForm(Form):

    username = CustomStringField('Username', [validators.Length(min=4, max=25)])
    email = CustomStringField('Email Address', [validators.Length(min=6, max=35)])
    password = CustomStringField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = CustomStringField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

