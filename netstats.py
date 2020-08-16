#!/usr/bin/python3
import os
import sys

from grafo import Grafo


def cargar_datos_tsv(nombre_tsv):
    if os.path.exists(nombre_tsv):
        datos = []
        with open(nombre_tsv) as archivo:
            for linea in archivo:
                linea_sin_espacios = linea.strip()
                dato = linea_sin_espacios.split('\t')
                datos.append(dato)
            return datos
    else:
        raise Exception(f"El archivo {nombre_tsv} no existe")


def crear_red(datos):
    grafo = Grafo(True)
    crear_vertices(datos, grafo)
    crear_aristas(datos, grafo)
    #print(grafo.ver_cantidad_vertices())


def crear_vertices(datos, grafo):
    for dato in datos:
        for articulo in dato:
            grafo.agregar_vertice(articulo)


def crear_aristas(datos, grafo):
    for dato in datos:
        for articulo in dato[1:]:
            grafo.agregar_arista(dato[0], articulo)


def procesar_archivo(archivo_tsv):
    datos = cargar_datos_tsv(archivo_tsv)
    crear_red(datos)


if __name__ == '__main__':
    archivo_tsv = sys.argv[1]
    procesar_archivo(archivo_tsv)
