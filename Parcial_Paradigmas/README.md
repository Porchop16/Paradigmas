Parcial Paradigmas

INFORME:
-------------

Se desarrolla modulo de consulta de la aplicaci�n web, m�dulo registraci�n y m�dulo login. 
Al ingresar a la aplicacion se mostrar� una p�gina de bienvenida,  para ingresar al sistema habr� que loguearse, 
si no se encuentra registrado, tiene la opci�n de hacerlo a trav�s de la barra de navegaci�n.                                                                                                                  

Una vez iniciada la aplicaci�n las p�ginas se ir�n generando a partir de las solicitudes que realiza el usuario desde el navegador. 
Por ejemplo  cuando el usuario  ingresa usuario y contrase�a, ser� redirigido a la p�gina de base de datos donde contendra toda la informacion visible 

La aplicaci�n esta compuesta por los siguientes archivos: archivo.py, forms.py, app.py, carpeta template que contiene los distintos archivos .html,  
un archivo csv llamado datos(contiene informaci�n de las ventas) y otro archivo de usuarios
(contiene la informaci�n de los usuarios registrados)

*archivo.py* contine las distitas funciones que manipulan el archivo csv, las mismas ser�n utilizadas en app.py.

*archivo forms.py* se crear�  las distintas clases de los formularios que se usar�n en la aplicaci�n.

*app.py* es donde se incia la aplicaci�n,  aqu� se generan las distintas p�ginas html seg�n las solicitudes que ingrese el usuario, y 
dependiendo de estas solicitudes, se realizar�n validaciones o manejo de datos a trav�s de las distintas consultas. 