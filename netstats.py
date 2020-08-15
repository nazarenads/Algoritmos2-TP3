import os
import sys

from grafo import Grafo


def cargar_datos_tsv(nombre_tsv):
    if os.path.exists(nombre_tsv):
        datos = []
        with open(nombre_tsv) as archivo:
            for linea in archivo:
                dato = linea.split('\t')
                datos.append(dato)
            return datos
    else:
        raise Exception(f"El archivo {nombre_tsv} no existe")


def crear_red(datos):
    grafo = Grafo(True)
    for dato in datos:
        grafo.agregar_vertice(dato[0])


def procesar_archivo(archivo_tsv):
    datos = cargar_datos_tsv(archivo_tsv)
    crear_red(datos)


if __name__ == '__main__':
    archivo_tsv = sys.argv[1]
    procesar_archivo(archivo_tsv)
