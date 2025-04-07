def read_file(filename):
    with open(filename, 'r') as file:
        contenido = file.read()
    return contenido