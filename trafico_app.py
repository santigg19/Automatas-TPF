import re
import warnings


warnings.simplefilter('always', UserWarning)
regx_aps = re.compile(r'((?:[A-Fa-f\d]{2}-){5}[A-Fa-f\d]{2}:UM)')
regx_clients = re.compile(r'((?:[A-Fa-f\d]{2}-){5}[A-Fa-f\d]{2}$)',
                          re.MULTILINE)
regx_users = re.compile(r'(?<=;)[A-Za-z-.]{1,15}(?=;)')

# Leer archivo de texto y buscar direcciones MAC y usuarios
with open('acts-user1.txt', 'r') as infile:
    text_file = infile.read()
    aps_mac = re.findall(regx_aps, text_file)
    clients_mac = re.findall(regx_clients, text_file)
    users_list = regx_users.findall(text_file, 121)

# Eliminar direcciones MAC y usuarios duplicados
aps_mac = list(set(aps_mac))
print('\n--> Lista de MAC AP:', aps_mac)

clients_mac = list(set(clients_mac))
print('\n--> Lista de MAC Cliente:', clients_mac)

users_list = list(set(users_list))
print('\n--> Lista de Usuarios:', users_list)

# Escribir en archivos de texto las direcciones MAC y usuarios
with open('aps_mac_output.txt', 'w') as outfile:
    outfile.write('-Lista de MAC AP:\n')
    for match in aps_mac:
        outfile.write('%s\n' % match)

with open('clients_mac_output.txt', 'w') as outfile:
    outfile.write('-Lista de MAC Cliente:\n')
    for match in clients_mac:
        outfile.write('%s\n' % match)

with open('users_output.txt', 'w') as outfile:
    outfile.write('-Lista de Usuarios:\n')
    for match in users_list:
        outfile.write('%s\n' % match)

# Crear diccionario que guardará el número de tráfico de c/AP
trafico_dict = dict()
for match in aps_mac:
    trafico_dict[match] = 0

# Determinar rango de fechas para seguimiento del tráfico
regx_date = re.compile(r'((0?[1-9]|[12][0-9]|3[01])\/(0?[1-9]|1[012])\/\d{4})')
while True:
    date_init = input('\n--> Ingrese fecha de inicio en formato dd/mm/yyyy: ')
    if regx_date.match(date_init):
        break
    else:
        warnings.warn('La expresión ingresada no es válida.', stacklevel=2)
while True:
    date_end = input('\n--> Ingrese fecha de finalización en formato '
                     'dd/mm/yyyy: ')
    if regx_date.match(date_end):
        break
    else:
        warnings.warn('La expresión ingresada no es válida.', stacklevel=2)

# Sumar tráfico correspondiente a cada AP
regx_trafico = re.compile(r'(?<=;)(?:[\d]*)(?=;)')
with open('acts-user1.txt', 'r') as infile:
    while True:
        line_file = infile.readline()
        if date_init in line_file or date_end in line_file:
            for match in aps_mac:
                if match in line_file:
                    trafico_dict[match] = trafico_dict[match] + int(
                                          regx_trafico.findall(line_file)[1])\
                                          + int(regx_trafico.findall(line_file)
                                                [2])
        if len(line_file) == 0:
            infile.close
            break
print('\n--> Tráfico de cada AP entre %s y %s:' % (date_init, date_end),
      trafico_dict)
max_trafico = max(trafico_dict, key=trafico_dict.get)
print('\n--> El AP de MAC %s es el que más tráfico (%s octectos) ha tenido.'
      % (max_trafico, trafico_dict[max_trafico]))
