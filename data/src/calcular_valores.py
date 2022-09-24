import numpy as np
import argparse


def calcular_extremos(lista_numeros, verbose=1):
    """calcula el valor minimo y maximo de una lista de numeros

    Args:
        lista_numeros (lista):lista de numeros con valores enteros

    Returns:
        tuple: (minimo,maximo)
    """

    min_val = np.min(lista_numeros)
    max_val = np.max(lista_numeros)

    if verbose == 1:
        print('calcular_extremos')
        print('minimo', min)
        print('maximo', max)
    else:
        pass
    return min,max

    print('calcular_extremos')
    print('minimo', min_val)
    print('maximo', max_val)
    return min_val, max_val

def calcular_valores_centrales(lista_numeros, verbose =1):
    """calcula la media y la desviacion estandar de una lista de numeros

    Args:
        lista_numeros (lista): lista de numeros con valores enteros

    Returns:
        tupla: (media, desviacion estandar)
    """

    media   = np.mean(lista_numeros)
    dev_std = np.std(lista_numeros)

    if verbose == 1:
        print('calcular_valores_centrales')
        print('media', media)
        print('desv_std', dev_std)
    else:
        pass
    return media, dev_std

    print('calcular_valores_centrales')
    print('media', media)
    print('desv std', dev_std)
    return media, dev_std

def calcular_suma(lista_numeros, verbose =1):
    '''
    Calcula la suma de una lista de numeros
    Args:
        lista_numeros : lista de numeros
    '''
    resultado = np.sum(lista_numeros)

    if verbose == 1:
        print('calcular_suma')
        print('suma', resultado)
    else:
        pass
    return resultado

    print('calcular_suma')
    print('suma', resultado)
    return resultado

def calcular_valores(lista_numeros, verbose = 1):
    suma             = calcular_suma(lista_numeros, verbose)
    media, dev_std   = calcular_valores_centrales(lista_numeros, verbose)
    min_val, max_val = calcular_extremos(lista_numeros, verbose)
    return suma, media, dev_std, min_val, max_val

def main():
    parser = argparse.ArgumentParser
    parser.add_argument("--verbose", type=int, default=1, help="para decir si imprime informacon")


    args = parser.parse_arg()

    verbose = args.verbose



    lista_numeros = [1, 5, 8, 3, 45, 93]
    suma, media, dev_std, min_val, max_val = calcular_valores(lista_numeros,verbose)
    print(suma, media, dev_std, min_val, max_val)

if __name__ == '_main_':
    main()
# pseudo codigo
# main()
#   datos = get_data(filename)
#   reporte = generate_reporte(datos)
#    save_data(reporte)
import os
from pathlib import Path
import pandas as pd
root_dir = Path(".").resolve()

def get_data(filename):
    data_dir = "raw"
    file_path = os.path.join(root_dir,"data",data_dir,filename)  # Ruta del archivo que necesito 

    datos = pd.read_csv(file_path,sep=";",encoding="latin-1")
    print('get_data')
    print('La tabla contiene', datos.shape[0], 'filas', datos.shape[1], 'columnnas')
    return datos

def generate_reporte(datos):
    # Crear un diccionario vacio
    dict_reporte = dict()

    # look para llenar el diccionario de columnas con valores unicas
    for col in datos.columns:
        valores_unicos=datos[col].unique()
        n_valores=len(valores_unicos)
        dict_reporte[col] = n_valores
    # print('columna',col,n_unicos)}

    reporte = pd.DataFrame.from_dict(dict_reporte, orient='index')
    reporte.rename({0: 'conteo'}, inplace=True,axis=1)   # 1 buscar en la columna, 0 en las filas

    print('generate_report')
    print(reporte.head())
    return reporte


def save_date(reporte,filename):
    # Guardar tabla
    out_name = 'resumen_' + filename # Renombrar ya el archivo de salida
    out_path =  os. path.join(root_dir,"data", "processed", out_name)
    reporte.to_csv(out_path)

def main():

    filename = 'llamadas123_julio_2022.csv'
    datos = get_data(filename)
    reporte = generate_reporte(datos)
    save_date(reporte, filename)

if __name__ == '_main_':
    main()