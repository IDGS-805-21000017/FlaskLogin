from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, Length, NumberRange, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[
        DataRequired(message='El usuario es requerido'),
        Length(min=3, max=50, message='El usuario debe tener entre 3 y 50 caracteres')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es requerida'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    submit = SubmitField('Iniciar Sesión')

class RegistroForm(FlaskForm):
    username = StringField('Usuario', validators=[
        DataRequired(message='El usuario es requerido'),
        Length(min=3, max=50, message='El usuario debe tener entre 3 y 50 caracteres')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es requerida'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        DataRequired(message='La confirmación de contraseña es requerida'),
        EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    submit = SubmitField('Registrarse')

class ProductoForm(FlaskForm):
    nombre = StringField('Nombre del Producto', validators=[
        DataRequired(message='El nombre es requerido'),
        Length(min=3, max=100, message='El nombre debe tener entre 3 y 100 caracteres')
    ])
    precio = FloatField('Precio', validators=[
        DataRequired(message='El precio es requerido'),
        NumberRange(min=0, message='El precio debe ser mayor a 0')
    ])
    cantidad = IntegerField('Cantidad', validators=[
        DataRequired(message='La cantidad es requerida'),
        NumberRange(min=0, message='La cantidad debe ser mayor o igual a 0')
    ])
    submit = SubmitField('Registrar Producto')

class PedidoForm(FlaskForm):
    producto_id = HiddenField('ID del Producto', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[
        DataRequired(message='La cantidad es requerida'),
        NumberRange(min=1, message='La cantidad debe ser mayor a 0')
    ])
    submit = SubmitField('Realizar Pedido')
