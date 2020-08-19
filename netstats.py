#!/usr/bin/python3
import os
import sys
import faulthandler; faulthandler.enable()

from comandos import (
    diametro,
    imprimir_operaciones,
    todos_en_rango,
    navegacion_primer_link,
    conectividad,
    comunidades)
from constantes import (
    LISTA_COMANDOS,
    COMANDO_CAMINO_MINIMO,
    COMANDO_DIAMETRO,
    COMANDO_LISTAR_OPERACIONES,
    COMANDO_RANGO,
    COMANDO_NAVEGACION,
    COMANDO_CONECTIVIDAD,
    COMANDO_COMUNIDADES)
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


def crear_red(datos, grafo):
    crear_vertices(datos, grafo)
    crear_aristas(datos, grafo)


def crear_vertices(datos, grafo):
    for dato in datos:
        for articulo in dato:
            grafo.agregar_vertice(articulo)


def crear_aristas(datos, grafo):
    for dato in datos:
        for articulo in dato[1:]:
            grafo.agregar_arista(dato[0], articulo)


def procesar_archivo(archivo_tsv, grafo):
    datos = cargar_datos_tsv(archivo_tsv)
    crear_red(datos, grafo)


def procesar_comandos(grafo, stdin):
    print("Ingrese un comando:")
    for entrada in stdin:
        entrada = entrada.rstrip()
        comandos = entrada.split(" ", maxsplit=1)
        comando = comandos[0].strip()
        if comando not in LISTA_COMANDOS:
            print(f"El comando {entrada} no existe.")
        if comando == COMANDO_CAMINO_MINIMO:
            print("camino minimo")
        elif comando == COMANDO_DIAMETRO:
            diametro(grafo)
        elif comando == COMANDO_LISTAR_OPERACIONES:
            imprimir_operaciones()
        elif comando == COMANDO_RANGO:
            parametros = comandos[1].split(",")
            todos_en_rango(grafo, parametros[0], int(parametros[1]))
        elif comando == COMANDO_NAVEGACION:
            navegacion_primer_link(grafo, comandos[1])
        elif comando == COMANDO_CONECTIVIDAD:
            conectividad(grafo, comandos[1])
        elif comando == COMANDO_COMUNIDADES:
            comunidades(grafo, comandos[1])



if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    archivo_tsv = sys.argv[1]
    grafo = Grafo(True)
    procesar_archivo(archivo_tsv, grafo)
    procesar_comandos(grafo, sys.stdin)
