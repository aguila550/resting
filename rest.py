from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mysqlcon

#Hola Erick, si esto funciona lloro
dbconect = mysqlcon.connect(host="localhost",user="root", password="",database="restaurante_ing")

mysql = dbconect.cursor()

rest = Flask(__name__)

@rest.route('/')
def index():
 
   return render_template('index.html')

@rest.route('/desayunos', methods = ['GET','POST'])
def desayunos():

   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "chilaquiles"
       precio = 65


       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)


       mysql.execute(sql,Values)
       dbconect.commit()

   return render_template('desayunos.html')

@rest.route('/molletes', methods = ['GET','POST'])
def mollets():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "molletes"
       precio = 45

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('desayunos'))

@rest.route('/sincronizadas', methods = ['GET','POST'])
def sincronizadas():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "sincronizadas"
       precio = 45

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('desayunos'))

@rest.route('/enfrijoladas', methods = ['GET','POST'])
def enfrijoladas():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "enfrijoladas"
       precio = 55

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('desayunos'))

@rest.route('/comida',methods =['GET','POST'] )
def comida():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "Arrachera"
       precio = 60

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return render_template('comida.html')

@rest.route('/pechuga', methods = ['GET','POST'])
def pechuga():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "pechuga de pollo"
       precio = 75

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)


       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('comida'))

@rest.route('/hamburguesa', methods = ['GET','POST'])
def hamburguesa():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "hamburguesa"
       precio = 55


       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)


       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('comida'))

@rest.route('/filete', methods = ['GET','POST'])
def filete():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "filete"
       precio = 115

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('comida'))

@rest.route('/postres', methods = ['GET','POST'])
def postres():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "pay de queso"
       precio = 30

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return render_template('postres.html')

@rest.route('/arroz', methods = ['GET','POST'])
def arroz():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "arroz con leche"
       precio = 45

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('postres'))

@rest.route('/tarta', methods = ['GET','POST'])
def tarta():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "tarta de manzana"
       precio = 45

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('postres'))

@rest.route('/donas', methods = ['GET','POST'])
def donas():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "orden de donas"
       precio = 45

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('postres'))

@rest.route('/bebidas', methods = ['GET', 'POST'])
def bebidas():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "naranjada"
       precio = 45

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()
   return render_template('bebidas.html')

@rest.route('/limonada', methods = ['GET','POST'])
def limonada():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "limonada"
       precio = 45

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('bebidas'))

@rest.route('/cafe', methods = ['GET','POST'])
def cafe():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "cafe americano"
       precio = 35

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('bebidas'))

@rest.route('/frappes', methods = ['GET','POST'])
def frappes():
   if request.method == 'POST':
      
       cantidad = request.form['cantidad']
       nombre = "frappes"
       precio = 55

       sql = "INSERT INTO pedidos(nombre,cantidad,precio) VALUES(%s,%s,%s)"
       Values = (nombre, cantidad, precio)

       mysql.execute(sql,Values)
       dbconect.commit()

   return redirect(url_for('bebidas'))

@rest.route('/carrito', methods = ['GET','POST'])
def carrito():
   sqls= 'SELECT * FROM pedidos'
   mysql.execute(sqls)

   result = mysql.fetchall()
   contenidoTabla2 = []

   for x in result:
       contenidoTabla2.append({'id':x[0],'nombre':x[1],'precio':x[2],'cantidad':x[3]})

   if request.method == 'POST':
      
       getid = request.args.get('id')
       comida = request.form['nombre']
       precio = request.form['precio']
       cantidad = request.form['cantidad']

       dbconect.commit()

       msj = f"Se actualizo el ID: {getid}"
       return render_template('carrito.html', contenidoTabla2=contenidoTabla2,msj=msj)
   else:
       msj= "Tabla de usuarios"

       return render_template('carrito.html', contenidoTabla2=contenidoTabla2,msj=msj)

@rest.route('/crud', methods =['GET','POST'])
def crud():
   if request.method == 'POST':
       Nombre = request.form['Nombre']
       Numero = request.form['Numero']
       Direccion = request.form['Direccion']
       Correo = request.form['Correo']

       sql = "INSERT INTO usuarios(Nombre,Numero,Direccion,Correo) VALUES(%s,%s,%s,%s)"
       values = (Nombre, Numero, Direccion, Correo)

       mysql.execute(sql, values)
       dbconect.commit()

       return "Usuario agregado con exito <a href='/tabla'>tabla</a><a href='/crud'>volver</a>"
   else:
       return render_template('crud.html')

@rest.route('/eliminar', methods = ['GET', 'POST'])
def eliminar():

   getid = request.args.get('id')

   sqldelete = f"DELETE FROM pedidos WHERE id={getid}"

   mysql.execute(sqldelete)
   dbconect.commit()

   msj = "pedido eliminado"
   return redirect(url_for('carrito'))

@rest.route('/eliminarU', methods = ['GET', 'POST'])
def eliminarU():

   getid = request.args.get('id')

   sqldeleteU = f"DELETE FROM usuarios WHERE id={getid}"

   mysql.execute(sqldeleteU)
   dbconect.commit()

   return redirect(url_for('tabla'))
  
@rest.route('/tabla', methods = ['GET','POST'])
def tabla():

   sqls= 'SELECT * FROM usuarios'
   mysql.execute(sqls)

   result = mysql.fetchall()

   contenidoTabla = []

   for x in result:
       contenidoTabla.append({'id':x[0],'Nombre':x[1],'Numero':x[2],'Direccion':x[3],'Correo':x[4]})

   if request.method == 'POST':
      
       getid = request.args.get('id')
       up_Nombre = request.form['Nombre']
       up_telefono = request.form['Numero']
       up_direccion = request.form['Direccion']
       up_correo = request.form['Correo']

       sqlUpdate = 'UPDATE usuarios SET Nombre=%s, Numero=%s, Direccion=%s, Correo=%s WHERE id=%s'
       valuesUpdate = (up_Nombre, up_telefono, up_direccion, up_correo, getid)

       mysql.execute = (sqlUpdate, valuesUpdate)
       dbconect.commit()

       msj = f"Se actualizo el ID: {getid}"
       return render_template('tabla.html', contenidoTabla=contenidoTabla,msj=msj)
   else:
       msj= "Tabla de usuarios"

       return render_template('tabla.html', contenidoTabla=contenidoTabla,msj=msj)
  
@rest.route('/editar', methods=['GET','POST'])
def editar(id):

   up_Nombre = request.form['Nombre']
   up_telefono = request.form['Numero']
   up_direccion = request.form['Direccion']
   up_correo = request.form['Correo']

   if up_Nombre and up_telefono and up_direccion and up_correo:
       cursor = dbconect()
       sql = 'UPDATE usuarios SET Nombre=%s, Numero=%s, Direccion=%s, Correo=%s WHERE id=%s'
       data = valuesUpdate = (up_Nombre, up_telefono, up_direccion, up_correo)

   return render_template('editar.html')

if  __name__ == '__main__':
   rest.run()

##esto solo es comentario basura