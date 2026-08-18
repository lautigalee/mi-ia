from database import guardar_recuerdo as guardar_en_db
from database import buscar_recuerdos as buscar_en_db


def guardar_recuerdo(content, importance):
    guardar_en_db(content, importance)
    
def buscar_recuerdos(termino):
    resultados = buscar_en_db(termino)

    return [recuerdo[0] for recuerdo in resultados]