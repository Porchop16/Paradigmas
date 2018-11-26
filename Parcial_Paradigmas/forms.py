from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Length, DataRequired, EqualTo
from wtforms import validators
from wtforms import StringField, SubmitField, PasswordField, IntegerField



class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')

class RegistrarForm(LoginForm):
    password_check = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Registrarse')

class ClienteForm(FlaskForm): #Estas clase sirve para validar campos y tener los parametros
    parametro = StringField('Escriba el Nombre del Cliente que desea buscar: ', validators=[Length(min=3, max=100, message="Debe ingresar como minimo 3 caracteres"),DataRequired(message="Debe escribir valor")])

class ProductoFrom(FlaskForm):#Estas clase sirve para validar campos y tener los parametros
	parametro = StringField('Escriba el Nombre del Producto que desea buscar: ', validators=[Length(min=3, max=100, message="Debe ingresar como minimo 3 caracteres"),DataRequired(message="Debe escribir un valor")])

#se establece los campos que tendra el formulario en la funcion mejores_clientes() y mas_vendidos() el archivo app.py
class MyConsulta(FlaskForm):
    cantidad = IntegerField('Cantidad de items a mostrar', [validators.data_required(message = "Debe ingresar un numero entero")])
    submit = SubmitField("Aceptar")

class CargarVentaForm(FlaskForm):
	codigo = StringField('Escriba el codigo del producto', validators=[Required()])
	cliente = StringField('Escriba el nombre del cliente', validators=[Required()])
	producto = StringField('Escriba el nombre del producto', validators=[Required()])
	cantidad = StringField('Escriba la cantidad', validators=[Required()])
	precio = StringField('Escriba el precio del producto', validators=[Required()])
	enviar = SubmitField('Enviar')
