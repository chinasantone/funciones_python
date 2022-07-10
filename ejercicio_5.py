# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada
def generar_invitados():
    print ('ingrese el nombre del primer invitado')
    invitado_1 = str(input())
    print ('ingrese el nombre del segundo invitado')
    invitado_2 = str (input())
    print ('ingrese el nombre del tercer invitado')
    invitado_3 = str (input())
    lista_invitados = [invitado_1, invitado_2, invitado_3]
    return lista_invitados
# --------------------------------

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada
def ordenar(numeros):
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados
# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"

    # lista_invitados = generar_invitados()
    lista_invitados = generar_invitados()
    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    # lista_invidatos_ordenada = ordenar(lista_invitados)
    lista_invitados_ordenada = ordenar (lista_invitados)
    # Imprimir en pantalla "lista_invidatos_ordenada":
    print ('lista de invitados ordenada:', lista_invitados_ordenada)
    print("terminamos")

