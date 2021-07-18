import pandas as pd
import random
import math
#import re
import os



# Funcion que guarda los usuarios del archivo en una lista
def get_users():
    excel_file_path = 'texto.xlsx'      # Ubicacion del archivo, como estan en la misma carpeta es solo el nombre
    df = pd.read_excel(excel_file_path) # Lo leo

    # Me fijo que cumpla la condicion de la re, lo hago lista y luego elimino los elementos repetidos
    lista_usuarios = list(dict.fromkeys(df['Usuario'].str.replace(r'[^A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$', "").tolist()))
    cantidad_users = len(lista_usuarios)
    os.system('cls')
    print(f'Hay {cantidad_users} usuarios:\n')
    print(lista_usuarios)

    random_user = random.choice(lista_usuarios)
    print(f'\nUsuario random: {random_user}\nIndice del usuario: {lista_usuarios.index(random_user)}') # Muestro uno random y su indice


def get_MAC_AP():
    # Nombre del archivo 
    excel_file_path = 'texto.xlsx'
    # Lo leo y lo cargo en un DataFrame
    df = pd.read_excel(excel_file_path)
    # En ese df con re busco las que cumplen cierta condicion y las remplazo con un string vacio, despues se hace una lista y elimino duplicados
    lista_MAC_AP = list(dict.fromkeys(df['MAC AP'].str.replace(r'(^[0-9A-F]{1,2})' + '\:([0-9A-F]{1,2})'*5 + '$', "").tolist()))

    # Si el elemento de la lista es un nan, lo saco de lista
    for element in lista_MAC_AP:
        if type(element) == int or type(element) == float:
            if math.isnan(element):
                lista_MAC_AP.remove(element)

    os.system('cls')
    cantidad_MAC_AP = len(lista_MAC_AP)
    print(f'Se han encontrado {cantidad_MAC_AP} MAC AP:\n')
    print(lista_MAC_AP)
    # Muestro uno random
    random_MAC = random.choice(lista_MAC_AP)
    print(f'\nMAC AP random: {random_MAC}\nIndice de la MAC: {lista_MAC_AP.index(random_MAC)}') # Muestro uno random y su indice


def get_mac_Cliente():
    # Esta funcion trabaja de la misma manera que la anterior (get_MAC_AP())

    excel_file_path = 'texto.xlsx'
    df = pd.read_excel(excel_file_path)
    lista_MAC_Cliente = list(dict.fromkeys(df['MAC Cliente'].str.replace(r'^[a-fA-F0-9:]{17}|[a-fA-F0-9]{12}$', "").tolist()))
    os.system('cls')

    cantidad_MAC_Cliente = len(lista_MAC_Cliente)
    print(f'Se han encontrado {cantidad_MAC_Cliente} MAC Cliente:\n')
    random_MAC = random.choice(lista_MAC_Cliente)
    print(f'MAC Cliente random: {random_MAC}\nIndice de la MAC: {lista_MAC_Cliente.index(random_MAC)}') # Muestro uno random y su indice


"""
PARTE ESPECIFICA DE NUESTRO GRUPO.
Enunciado:
Seguimiento del tráfico de AP (Access point), para determinar cuál es el AC, que más tráfico
(Input Octects + Output Octects) ha tenido en un período de tiempo (rango de fechas). 
"""


def get_trafico():
    excel_file_path = 'fechas.xlsx'
    df = pd.read_excel(excel_file_path)
    contador = 0

    # No cuento las filas en la que no hay datos especificos
    for row in df['Inicio de Conexion']:
        if row == '\\N':
            df = df.drop([contador])
        contador += 1

    # Especificamos entre que fechas (con hora) queremos buscar
    fecha_1 = '28/08/2019 10:06'
    fecha_2 = '28/08/2019 10:25'

    rango = df[(df['Inicio de Conexion'] > fecha_1) & (df['Inicio de Conexion'] < fecha_2)]
    rango['Octets'] = rango['Input Octects'] + rango['Output Octects']  # Nueva columna llamada Octets que seria nuestro trafico
    val = rango['Octets'].max() # Valor maximo de trafico
    os.system('cls')
    mac_con_mayor_trafico = rango[rango['Octets'] == val]['MAC AP']
    print(f'La direccion MAC AP con el mayor trafico ({val}) entre {fecha_1} y {fecha_2} es la: {mac_con_mayor_trafico.iloc[0]}\n')


if __name__ == '__main__':
    seleccion = -1
    while seleccion < 5 :
        print('\n1 - Usuarios\n2 - MAC AP\n3 - MAC Cliente\n4 - Trafico\n5 - Salir\n')
        seleccion = int(input('Ingrese que funcion desea usar: '))
        if seleccion == 1:
            get_users()
        elif seleccion == 2:
            get_MAC_AP()
        elif seleccion == 3:
            get_mac_Cliente()
        elif seleccion == 4:
            get_trafico()
        else:
            print('Terminado')
            seleccion = 5
    
