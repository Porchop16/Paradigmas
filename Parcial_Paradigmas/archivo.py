import csv

def lista_clientes(archivo1) :#funcion que lee  un archivo y retorna una lista de Clientes sin duplicados
    with open(archivo1) as archivo :
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['CLIENTE'] not in lista_consulta :
               lista_consulta.append(l['CLIENTE'])
        return lista_consulta

#lee arhivo y lo guarda como un diccionario el cual es asignado a la variable listadic, se retorna la misma
def leer(archivo1) :
    with open(archivo1) as archivo :
         arch_csv = csv.DictReader(archivo)
         listadic = list(arch_csv)
    return listadic

def lista_producto(archivo1): #funcion que lee  un archivo y retorna una lista de Productos sin duplicados
    with open(archivo1) as archivo:
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['PRODUCTO'] not in lista_consulta:
                lista_consulta.append(l['PRODUCTO'])
        return lista_consulta