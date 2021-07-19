import re
regex_aps = re.compile(r'((?:[A-Fa-f\d]{2}-){5}[A-Fa-f\d]{2}:UM)')
regex_clients = re.compile(r'((?:[A-Fa-f\d]{2}-){5}[A-Fa-f\d]{2}$)',
                           re.MULTILINE)
regex_users = re.compile(r'(?<=;)[A-Za-z-.]{1,15}(?=;)')

# Leer archivo de texto y buscar direcciones MAC y usuarios
with open('acts-user1.txt', 'r') as infile:
    text_file = infile.read()
    aps_mac = re.findall(regex_aps, text_file)
    clients_mac = re.findall(regex_clients, text_file)
    users_list = regex_users.findall(text_file, 121)

# Eliminar direcciones MAC y usuarios duplicados
aps_mac = list(set(aps_mac))
print('\n', aps_mac)

clients_mac = list(set(clients_mac))
print('\n', clients_mac)

users_list = list(set(users_list))
print('\n', users_list)

# Escribir en archivos de texto las direcciones MAC y usuarios
with open('aps_mac_output.txt', 'w') as outfile:
    outfile.write('Lista de MAC AP:\n')
    for match in aps_mac:
        outfile.write('%s\n' % match)

with open('clients_mac_output.txt', 'w') as outfile:
    outfile.write('Lista de MAC Cliente:\n')
    for match in clients_mac:
        outfile.write('%s\n' % match)

with open('users_output.txt', 'w') as outfile:
    outfile.write('Lista de Usuarios:\n')
    for match in users_list:
        outfile.write('%s\n' % match)
