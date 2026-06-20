from reader import Buscar_usuarios
from sender import Mandar_msg

usuarios = Buscar_usuarios()


if usuarios:
    print("usuarios encontrados: ")
    for user in usuarios:
        print(user)
        Mandar_msg(user['Number'],user['Name'])
