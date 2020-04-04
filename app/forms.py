from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, InputRequired
from wtforms.widgets import html5, html_params, HTMLString

class ButtonWidget(object):
    """
    Renders a multi-line text area.
    `rows` and `cols` ought to be passed as keyword args when rendering.
    """
    input_type = 'button'

    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()

        return HTMLString('<button {params}>{label}</button>'.format(
            params=self.html_params(name=field.name, **kwargs),
            label=field.label.text)
        )


class ButtonField(StringField):
    widget = ButtonWidget()

class LoginForm(FlaskForm):
    """User Login Form."""
    email = StringField('Email', validators=[
        Email('Please enter a valid email address.'),
        DataRequired('Please enter a valid email address.')
    ])
    password = PasswordField('Password', validators=[DataRequired('Uhh, your password tho?')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    """User Register Form."""
    email = StringField('Email', validators=[
        Email('Please enter a valid email address.'),
        DataRequired('Please enter a valid email address.')
    ])
    username = StringField('Username', validators=[DataRequired('Enter a fake name or something.')])
    password = PasswordField('Password', validators=[
        DataRequired('Please enter a password.'),
        Length(min=8, message='Please select a stronger password'),
        EqualTo('password_confirm', message='Password must match')
    ])
    password_confirm = PasswordField('Confirm your Password')

    donate = ButtonField('Donar')
    supply = ButtonField('Transportar')
    apply = ButtonField('Solicitar')

    address = StringField('Direccion', validators=[ DataRequired('Por favor, introduzca una direccion postal valida')])

    usertype_radiobutton = RadioField('Seleccione su rol', choices=[('Donante','Donante'),('Repartidor','Repartidor'),('Solicitante','Solicitante')])

    
    submit = SubmitField('Register')
