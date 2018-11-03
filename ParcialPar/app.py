#!/usr/bin/env python
import csv
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_script import Manager
from forms import LoginForm, RegistrarForm, ClienteForm, ProductoFrom, MyConsulta
import archivo #importamos el modulo archivo

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'un string que funcione como llave'

@app.route('/')
def index():
    if not 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('basededatos'))

@app.route('/principal')
def principal():
    return render_template('principal.html',username=session.get('username'))

#Creo una base de datos para cuando el usuario se logge
@app.route('/basededatos', methods=['GET', 'POST'])
def basededatos():
    if 'username' in session:
        try:
            with open('datos.csv', 'r') as archivo:
                datalines = csv.reader(archivo)                
                titulos = next(datalines)                                
                return render_template('tabla.html', cabeza=titulos, cuerpo=datalines, username=session.get('username'))
        except FileNotFoundError:
            return 'No se encuentra el csv'
    return render_template('index.html')

#Consultas.
#Estos menus aparecen solo cuando está loggeado.
@app.route('/cliente', methods=['GET', 'POST'])
def cliente():
    if 'username' in session:        
        form_nombre = ClienteForm()    
        try:
            with open('datos.csv') as archivo:
                pass
        except FileNotFoundError:
            return 'No se encuentra el csv'    
        
        if form_nombre.validate_on_submit():            
            with open('datos.csv') as archivo:
                try:
                    filecsv = csv.reader(archivo)
                    infos=[]
                    
                    for linea in filecsv:
                        ubicacion = linea
                        codigo = ubicacion[0]
                        cliente = ubicacion[1]
                        # El Array tupla, tiene los titulos del encabezado
                        if "CODIGO" == codigo:
                            tupla = [ubicacion[0],ubicacion[1],ubicacion[2],ubicacion[3],ubicacion[4]]
                        if form_nombre.parametro.data.lower() in cliente.lower():
                            info = [ubicacion[0],ubicacion[1],ubicacion[2],ubicacion[3],ubicacion[4]]
                            infos.append(info)
                    #Este if se puso para informar que no se encuentran resultados.
                    if len(infos) == 0 :
                        flash('El cliente que busca no se encuentra en nuestra Base de Datos.')
                        return render_template('cliente.html', form=form_nombre, username=session.get('username'))
                    return render_template('tabla.html', form=form_nombre, cabeza=tupla, cuerpo=infos, username=session.get('username'))
                except IndexError:
                    return 'Numero invalido de datos a corroborar.'
        #Se retorna el tabla.html para conformar la respuesta visual.           
        return render_template('cliente.html', form=form_nombre, username=session.get('username'))
    flash('Debe estar logueado para acceder')
    return redirect(url_for('ingresar'))

#Consulta de producto. Similar al de Cliente pero utilizando la posicion del Producto. 
@app.route('/productos', methods=['GET', 'POST'])
def profuctos():
    if 'username' in session:        
        form_nombre = ProductoFrom()    
        try:
            with open('datos.csv') as archivo:
                pass
        except FileNotFoundError:
            return 'No se encuentra el csv'    
        
        if form_nombre.validate_on_submit():            
            with open('datos.csv') as archivo:
                try:
                    filecsv = csv.reader(archivo)
                    infos=[]
                    
                    for linea in filecsv:
                        ubicacion = linea
                        codigo = ubicacion[0]
                        cliente = ubicacion[2]
                        if "CODIGO" == codigo:
                            tupla = [ubicacion[0],ubicacion[1],ubicacion[2],ubicacion[3],ubicacion[4]]
                        if form_nombre.parametro.data.lower() in cliente.lower():
                            info = [ubicacion[0],ubicacion[1],ubicacion[2],ubicacion[3],ubicacion[4]]
                            infos.append(info)
                    if len(infos) == 0 :
                        flash('El cliente que busca no se encuentra en nuestra Base de Datos.')
                        return render_template('cliente.html', form=form_nombre, username=session.get('username'))
                    return render_template('tabla.html', form=form_nombre, cabeza=tupla, cuerpo=infos, username=session.get('username'))
                except IndexError:
                    return 'Numero invalido de datos a corroborar.'           
        return render_template('producto.html', form=form_nombre, username=session.get('username'))
    flash('Debe estar logueado para acceder')
    return redirect(url_for('ingresar'))

#Consulta de Mejor cliente lo hicimos distinto
@app.route("/mejores_clientes", methods = ('GET', 'POST'))
def mejores_clientes():
    if 'username' in session:
        form = MyConsulta()
        if form.validate_on_submit():
            listado = archivo.leer("datos.csv")
            masgasto = []
            consulta = []
            lista_busqueda = archivo.lista_clientes("datos.csv")
            for listcli in lista_busqueda:	#recorre  lista de clientes
                gastoTotal = 0
                for clientes in listado:	# recorre archivo ventas
                # en estos dos recorridos se busca agrupar los datos por cliente
                    if listcli == clientes['CLIENTE']:
                        gasto = float(clientes['CANTIDAD']) * float(clientes['PRECIO'])
                        gastoTotal = gastoTotal + gasto
                        #se calcula cuanto gasto cada cliete
                masgasto.append([listcli, gastoTotal])	#se guarda lista cuanto gasto cada cliente
            cont = 1
            masgasto.sort(key=lambda c: c[1], reverse=True)
            # se ordena la lista masgasto de mayor a menor
            for datos in masgasto: 
                if cont <= form.cantidad.data:
                    consulta.append(datos)
                    cont = cont + 1
            return render_template('mejores_clientes.html', form = form, fc = True, consulta = consulta, msg2 = "IMPORTE")
        return render_template('mejores_clientes.html', form = form)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('ingresar'))

#Consulta de productos mas vendidos.
@app.route("/mas_vendidos", methods = ('GET', 'POST'))
def mas_vendidos():
    if 'username' in session:
        form = MyConsulta()
        if form.validate_on_submit():
            listado = archivo.leer("datos.csv")
            masvendio = []
            consulta = []
            lista_busqueda = archivo.lista_producto("datos.csv")
            for listcli in lista_busqueda: # recorre lista de productos
                cant = 0
                codigo = 0
                for clientes in listado:# reocorre lista de ventas
                    if listcli == clientes['PRODUCTO']:
                         cant = cant + float(clientes['CANTIDAD']) #va acumulando cantidad vendidad
                         codigo = clientes['CODIGO']
                masvendio.append([codigo, listcli,int(cant) ])
    			#agrega en lista datos de codigo,cliente y cant
            cont = 1
            masvendio.sort(key=lambda c: c[2], reverse=True) #ordena de mayor a menor
            for datos in masvendio:
                if cont <= form.cantidad.data:
                    consulta.append(datos)
                    cont = cont + 1
            return render_template('mas_vendidos.html', form = form, fc = True, consulta = consulta, msg2 = "CANTIDAD")
        return render_template('mas_vendidos.html', form = form)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('ingresar'))

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        with open('usuarios') as archivo:
            archivo_csv = csv.reader(archivo)
            registro = next(archivo_csv)
            while registro:
                if formulario.usuario.data == registro[0] and formulario.password.data == registro[1]:
                    flash('Bienvenido')
                    session['username'] = formulario.usuario.data
                    return render_template('ingresado.html')
                registro = next(archivo_csv, None)
            else:
                flash('Revisá nombre de usuario y contraseña')
                return redirect(url_for('ingresar'))
    return render_template('login.html', formulario=formulario)


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    formulario = RegistrarForm()
    if formulario.validate_on_submit():
        if formulario.password.data == formulario.password_check.data:
            with open('usuarios', 'a+') as archivo:
                archivo_csv = csv.writer(archivo)
                registro = [formulario.usuario.data, formulario.password.data]
                archivo_csv.writerow(registro)
            flash('Usuario creado correctamente')
            return redirect(url_for('ingresar'))
        else:
            flash('Las passwords no matchean')
    return render_template('registrar.html', form=formulario)


@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('logged_out.html')
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    manager.run()
