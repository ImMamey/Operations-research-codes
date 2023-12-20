### Hunga - Hunga
from typing import Any
import pandas as pd
from tabulate import tabulate
from deprecated import deprecated


@deprecated(reason="Usar create_and_print_df en vez de este metodo.")
def mostrarMatriz(mt: list[int | Any], nfilas:int, ncolumnas:int)->None:
    #TODO: metodo deprecated, borrarlo una vez que se haya probado el nuevo metodo.
    print('\n')
    for i in range(nfilas):
        st = ''
        for j in range(ncolumnas):
            st = st + str(mt[i][j]) + '   '
        print(st)
    print('\n\n════════════════════════════════\n')


def create_and_print_df(data: list[int | Any]) -> None:
    """
    Crea un data fram de una lista cualquiera y la imprime. Se utiliza tabulate para agregar 'style'

    :param data: list
    :return: None
    """
    # Numero de columnas y filas
    num_columns = len(data[0])
    num_rows = len(data)

    # Guarda los nombres para cada columna y fila. Se utiliza para crear el dataframe
    column_names = ["Columna " + str(i + 1) for i in range(num_columns)]
    row_names = ["Fila " + str(i + 1) for i in range(num_rows)]
    # incializa el dataframe
    df = pd.DataFrame(data, columns=column_names, index=row_names)
    # imprime dataframe con estilo CSS. Se utiliza tabulate.
    print(tabulate(df, headers="keys", tablefmt="double_grid", showindex=True))


def crearMatriz(mt:list[int | Any], nfilas:int, ncolumnas:int)->list[list[int | Any]]:
    """
    Crea una matriz a partir de una lista cualquiera original, usando append.
    :param mt: Matriz original
    :param nfilas: numero de filas
    :param ncolumnas: numero de columnas
    :return:
    """
    matriz = []
    for i in range(nfilas):
        aux = []
        for j in range(ncolumnas):
            aux.append(mt[i][j])
        matriz.append(aux)
    return matriz


def obtenerMenorFila(mt, nfila, ncolumnas)->list[int | Any]:
    """
    Obtiene el menor valor de una fila en especifico
    :param mt: Matriz
    :param nfila: numero de fila
    :param ncolumnas: numero de columna
    :return: Matriz
    """
    ax = mt[nfila][0]
    for j in range(ncolumnas):
        if (ax > mt[nfila][j]):
            ax = mt[nfila][j]
    return ax


def obtenerMenorColumna(mt, nfilas, ncolumna)->list[int | Any]:
    """
    Obtiene el menor valor de una columna en especifico
    :param mt: Matriz original
    :param nfilas: numero de fils
    :param ncolumna: numero de columna
    :return:
    """
    ax = mt[0][ncolumna]
    for j in range(nfilas):
        if (ax > mt[j][ncolumna]):
            ax = mt[j][ncolumna]
    return ax


def pasoDos(mat, nfilas, ncolumnas):
    mt = mat
    ax = []

    # 2.1 Restar el menor de cada fila a cada elemento de la fila
    print('2.1. Restar menor de Fila a Cada Elemento de la Fila')
    for i in range(nfilas):
        ax.append(obtenerMenorFila(mt, i, ncolumnas))
    print('2.1.1. Menor Valor a Restar por Fila')
    print(ax)
    for i in range(len(ax)):
        for j in range(ncolumnas):
            mt[i][j] -= ax[i]
    create_and_print_df(mt)

    # 2.2 Restar el menor de cada columna a cada elemento de la columna
    print('2.2. Restar menor de Columna a Cada Elemento de la Columna')
    bx = []
    for i in range(ncolumnas):
        bx.append(obtenerMenorColumna(mt, nfilas, i))
    print('\n2.2.1. Valores Menores a Restar por Columna')
    print(bx)
    for i in range(len(bx)):
        for j in range(nfilas):
            mt[j][i] -= bx[i]

    create_and_print_df(mt)
    conf = revisarAsignaciones(mt, nfilas, ncolumnas)

    if (conf == True):
        return mt
    else:
        mtb = []
        for i in range(nfilas):
            ax = []
            for j in range(ncolumnas):
                ax.append(mt[i][j])
            mtb.append(ax)

        print('3.1. Mínimo número de Asignación de Líneas \n')
        nano = nfilas
        cont = 1
        while (nano > 0):
            for i in range(nfilas):
                if (mtb[i].count(0) == nano):
                    killFila(mtb, ncolumnas, i)
                    print('Numero de Asignación: ' + str(cont))
                    cont += 1
                    create_and_print_df(mtb)
                if (cerosColumnas(mtb, nfilas, i) == nano):
                    killColumn(mtb, nfilas, j)
                    print('Numero de Asignación: ' + str(cont))
                    cont += 1
                    create_and_print_df(mtb)
            nano -= 1

        minVal = 99999999
        for i in range(nfilas):
            for j in range(ncolumnas):
                if (type(mtb[i][j]) == type(3)):
                    if (mtb[i][j] < minVal):
                        minVal = mtb[i][j]
        print('3.2. Mínimo valor de la tabla Resultante: ' + str(minVal))
        print('3.2.1. Tabla Resultante de la Resta del Mínimo Valor')
        for i in range(nfilas):
            for j in range(ncolumnas):
                if (type(mtb[i][j]) == type(3)):
                    mtb[i][j] -= minVal

        create_and_print_df(mtb)

        print('Tabla obtenida en el Paso 2')
        create_and_print_df(mt)

        for i in range(nfilas):
            for j in range(ncolumnas):
                if (type(mtb[i][j]) == type(3)):
                    mt[i][j] = mtb[i][j]

        print('3.2.2. Combinación de Ambas Tablas')
        create_and_print_df(mt)
        conf = revisarAsignaciones(mt, nfilas, ncolumnas)

        if (conf == True):
            return mt


def cerosColumnas(mt, nfilas, ncolu):
    cont = 0
    for i in range(nfilas):
        if (mt[i][ncolu] == 0):
            cont += 1
    return cont


def revisarAsignaciones(matriz, nfilas, ncolumnas):
    mt = []
    coors = []
    nano = 1
    cond = 1

    for i in range(nfilas):
        ax = []
        for j in range(ncolumnas):
            ax.append(matriz[i][j])
        mt.append(ax)

    while (True):
        cond = 0
        for i in range(nfilas):
            if (mt[i].count(0) == nano):
                cond = 1
                for j in range(ncolumnas):
                    if (mt[i][j] == 0):
                        killColumn(mt, nfilas, j)
                        killFila(mt, ncolumnas, i)
                        coors.append([i + 1, j + 1])
                    else:
                        mt[i][j] = '-'
        if (cond == 0):
            nano += 1
        if (nano > ncolumnas):
            break
    print('2.3. Asignación de Líneas')
    print(coors)
    create_and_print_df(mt)

    if (ncolumnas == len(coors)):
        print('Solucion Optima:')
        print(coors)
        return True
    else:
        print('No se obtuvo una solución optima, se procede al Paso 3')
        print(coors)
        print('\n\n════════════════════════════════\n')
        return False


def obtenerCoors(matriz, nfilas, ncolumnas):
    mt = []
    coors = []
    nano = 1
    cond = 1

    for i in range(nfilas):
        ax = []
        for j in range(ncolumnas):
            ax.append(matriz[i][j])
        mt.append(ax)

    while (True):
        cond = 0
        for i in range(nfilas):
            if (mt[i].count(0) == nano):
                cond = 1
                for j in range(ncolumnas):
                    if (mt[i][j] == 0):
                        killColumn(mt, nfilas, j)
                        killFila(mt, ncolumnas, i)
                        coors.append([i + 1, j + 1])
                    else:
                        mt[i][j] = '-'
        if (cond == 0):
            nano += 1
        if (nano > ncolumnas):
            break
    return coors


def killFila(mt, ncolumnas, nfila):
    for i in range(ncolumnas):
        mt[nfila][i] = '-'


def killColumn(mt, nfilas, ncolumn):
    for i in range(nfilas):
        mt[i][ncolumn] = '|'


def crearCeros(nCant):
    aux = []
    for i in range(nCant):
        aux.append(0)
    return aux


def pasoUno(mt, nfilas, ncolumnas):
    if (ncolumnas > nfilas):
        diff = ncolumnas - nfilas
        aux = crearCeros(ncolumnas)

        for i in range(ncolumnas - nfilas):
            mt.append(aux)

    if (ncolumnas < nfilas):
        for j in range(nfilas - ncolumnas):
            for i in range(nfilas):
                mt[i].append(0)


if (__name__ == '__main__'):
    rest = [
        [50, 130, 190],
        [130, 100, 150],
        [110, 150, 270],
        [150, 90, 60]
    ]


    rest = [
        [8, 7, 9, 8, 6],
        [4, 5, 3, 5, 3],
        [2, 3, 4, 3, 2],
        [7, 6, 8, 6, 7],
        [5, 4, 4, 6, 3],
    ]

    f_o = 'max'  # min o max, dependiendo del ejercicio

    mtBalanceada = crearMatriz(rest, len(rest), len(rest[0]))
    # TODO: verificar usos de estos dos, si solo se usa para imprimir, se puede borrar.
    nfilas = len(mtBalanceada)
    ncolumnas = len(mtBalanceada[0])

    print('Tabla Inicial')
    create_and_print_df(mtBalanceada)

    if (f_o == 'min'):
        for i in range(nfilas):
            for j in range(ncolumnas):
                mtBalanceada[i][j] = mtBalanceada[i][j] * (-1)

    pasoUno(mtBalanceada, nfilas, ncolumnas)
    # TODO: verificar usos de estos dos, si solo se usa para imprimir, se puede borrar.
    nfilas = len(mtBalanceada)
    ncolumnas = len(mtBalanceada[0])

    print('Tabla Balanceada')
    create_and_print_df(mtBalanceada)
    mt = pasoDos(mtBalanceada, nfilas, ncolumnas)
    coors = obtenerCoors(mt, nfilas, ncolumnas)

    mtCoors = crearMatriz(rest, len(rest), len(rest[0]))
    pasoUno(mtCoors, len(rest), len(rest[0]))
    costo = 0;
    costos = []
    for k in coors:
        a = k[0] - 1
        b = k[1] - 1
        costo += mtCoors[a][b]
        costos.append(mtCoors[a][b])
        print('> El ' + str(a + 1) + ' ocupa el ' + str(b + 1))

    print('Costos: ')
    print(costos)
    print('Costo Total: ' + str(costo))






