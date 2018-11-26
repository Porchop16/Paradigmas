Parcial Paradigmas

INFORME:
-------------

Se desarrolla modulo de consulta de la aplicación web, módulo registración y módulo login. 
Al ingresar a la aplicacion se mostrará una página de bienvenida,  para ingresar al sistema habrá que loguearse, 
si no se encuentra registrado, tiene la opción de hacerlo a través de la barra de navegación.                                                                                                                  

Una vez iniciada la aplicación las páginas se irán generando a partir de las solicitudes que realiza el usuario desde el navegador. 
Por ejemplo  cuando el usuario  ingresa usuario y contraseña, será redirigido a la página de base de datos donde contendra toda la informacion visible 

La aplicación esta compuesta por los siguientes archivos: archivo.py, forms.py, app.py, carpeta template que contiene los distintos archivos .html,  
un archivo csv llamado datos(contiene información de las ventas) y otro archivo de usuarios
(contiene la información de los usuarios registrados)

*archivo.py* contine las distitas funciones que manipulan el archivo csv, las mismas serán utilizadas en app.py.

*archivo forms.py* se creará  las distintas clases de los formularios que se usarán en la aplicación.

*app.py* es donde se incia la aplicación,  aquí se generan las distintas páginas html según las solicitudes que ingrese el usuario, y 
dependiendo de estas solicitudes, se realizarán validaciones o manejo de datos a través de las distintas consultas. 