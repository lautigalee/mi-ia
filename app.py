from database import crear_tabla


def ejecutar():
    crear_tabla()

    print("TU IA está funcionando.")
    print("Base de datos inicializada.")

while True:
    mensaje = input("Vos: ")

    if mensaje.lower() == "salir":
        break

    print("Recibí:", mensaje)