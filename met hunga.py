### Hunga - Hunga

def mostrarMatriz(mt, nfilas, ncolumnas):
    print('\n')
    for i in range(nfilas):
        st = ''
        for j in range(ncolumnas):
            st = st + str(mt[i][j]) + '   '
        print(st)
    print('----------------------------------------------------------')

def crearMatriz(mt, nfilas, ncolumnas):
    matriz = []
    for i in range(nfilas):
        aux = []
        for j in range(ncolumnas):
            aux.append( mt[i][j] )
        matriz.append( aux )
    return matriz

def obtenerMenorFila(mt, nfila, ncolumnas):
    ax = mt[nfila][0]
    for j in range(ncolumnas):
        if (ax > mt[nfila][j]):
            ax = mt[nfila][j]
    return ax

def obtenerMenorColumna(mt, nfilas, ncolumna):
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
        ax.append( obtenerMenorFila(mt, i, ncolumnas) )    
    print('2.1.1. Menor Valor a Restar por Fila')
    print(ax)
    for i in range(len(ax)):
        for j in range(ncolumnas):
            mt[i][j] -= ax[i]
    mostrarMatriz(mt, len(mt), len(mt[0]))

    # 2.2 Restar el menor de cada columna a cada elemento de la columna
    print('2.2. Restar menor de Columna a Cada Elemento de la Columna')
    bx = []
    for i in range(ncolumnas):
        bx.append( obtenerMenorColumna(mt, nfilas, i) )
    print('\n2.2.1. Valores Menores a Restar por Columna')
    print(bx)
    for i in range(len(bx)):
        for j in range(nfilas):
            mt[j][i] -= bx[i]

    mostrarMatriz(mt, len(mt), len(mt[0]))
    conf = revisarAsignaciones(mt, nfilas, ncolumnas)
    
    if (conf == True):
        return mt
    else:
        mtb = []
        for i in range(nfilas):
            ax = []
            for j in range(ncolumnas):
                ax.append( mt[i][j] )
            mtb.append(ax)
   
        print('3.1. Mínimo número de Asignación de Líneas \n')
        nano = nfilas
        cont = 1
        while (nano > 0):
            for i in range(nfilas):
                if ( mtb[i].count(0) == nano ):
                    killFila(mtb, ncolumnas, i)
                    print('Numero de Asignación: ' + str(cont))
                    cont += 1
                    mostrarMatriz(mtb, len(mtb), len(mtb))
                if ( cerosColumnas(mtb, nfilas, i) == nano ):
                    killColumn(mtb, nfilas, j)
                    print('Numero de Asignación: ' + str(cont))
                    cont += 1
                    mostrarMatriz(mtb, len(mtb), len(mtb))
            nano -= 1

        minVal = 99999999
        for i in range(nfilas):
            for j in range(ncolumnas):
                if (type(mtb[i][j]) == type(3)):
                    if ( mtb[i][j] < minVal ):
                        minVal = mtb[i][j]
        print('3.2. Mínimo valor de la tabla Resultante: ' + str(minVal))
        print('3.2.1. Tabla Resultante de la Resta del Mínimo Valor')
        for i in range(nfilas):
            for j in range(ncolumnas):
                if (type(mtb[i][j]) == type(3)):
                    mtb[i][j] -= minVal

        mostrarMatriz(mtb, len(mtb), len(mtb[0]))

        print('Tabla obtenida en el Paso 2')
        mostrarMatriz(mt, len(mt), len(mt[0]))
        
        for i in range(nfilas):
            for j in range(ncolumnas):
                if ( type(mtb[i][j]) == type(3) ):
                    mt[i][j] = mtb[i][j]

        print('3.2.2. Combinación de Ambas Tablas')
        mostrarMatriz(mt, len(mt), len(mt[0]))
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
            ax.append( matriz[i][j] )
        mt.append(ax)

    while (True):
        cond = 0
        for i in range(nfilas):
            if (mt[i].count(0) == nano):
                cond = 1
                for j in range(ncolumnas):
                    if ( mt[i][j] == 0 ):
                        killColumn(mt, nfilas, j)
                        killFila(mt, ncolumnas, i)
                        coors.append([i+1,j+1])
                    else:
                        mt[i][j] = '-'
        if (cond == 0):
            nano += 1
        if (nano > ncolumnas):
         break
    print('2.3. Asignación de Líneas')
    print(coors)
    mostrarMatriz(mt, nfilas, ncolumnas)

    if ( ncolumnas == len(coors) ):
        print('Solucion Optima:')
        print(coors)
        return True
    else:
        print('No se obtuvo una solución optima, se procede al Paso 3')
        print(coors)
        print('----------------------------------------------------------')
        return False


def obtenerCoors(matriz, nfilas, ncolumnas):
    mt = []
    coors = []
    nano = 1
    cond = 1

    for i in range(nfilas):
        ax = []
        for j in range(ncolumnas):
            ax.append( matriz[i][j] )
        mt.append(ax)

    while (True):
        cond = 0
        for i in range(nfilas):
            if (mt[i].count(0) == nano):
                cond = 1
                for j in range(ncolumnas):
                    if ( mt[i][j] == 0 ):
                        killColumn(mt, nfilas, j)
                        killFila(mt, ncolumnas, i)
                        coors.append([i+1,j+1])
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
        aux.append( 0 )
    return aux

def pasoUno(mt, nfilas, ncolumnas):
    if ( ncolumnas > nfilas ):
        diff = ncolumnas - nfilas
        aux = crearCeros(ncolumnas)
        
        for i in range( ncolumnas - nfilas ):
            mt.append( aux ) 
                
    if ( ncolumnas < nfilas ): 
        for j in range( nfilas - ncolumnas ):
            for i in range(nfilas):
                mt[i].append( 0 )

if (__name__ == '__main__'):
    rest = [
        [50, 130, 190],
        [130, 100, 150],
        [110, 150, 270],
        [150, 90, 60]
    ]
    
    """
    rest = [
        [8, 7, 9, 8, 6],
        [4, 5, 3, 5, 3],
        [2, 3, 4, 3, 2],
        [7, 6, 8, 6, 7],
        [5, 4, 4, 6, 3],
    ]"""

    f_o = 'max' # min o max, dependiendo del ejercicio
    
    mtBalanceada = crearMatriz(rest, len(rest), len(rest[0]))
    nfilas = len( mtBalanceada )
    ncolumnas = len( mtBalanceada[0] )

    print('Tabla Inicial')
    mostrarMatriz(mtBalanceada, nfilas, ncolumnas)

    if (f_o == 'min'):
        for i in range(nfilas):
            for j in range(ncolumnas):
                mtBalanceada[i][j] = mtBalanceada[i][j]*(-1)

    pasoUno(mtBalanceada, nfilas, ncolumnas)
    
    nfilas = len( mtBalanceada )
    ncolumnas = len( mtBalanceada[0] )
    
    print('Tabla Balanceada')
    mostrarMatriz(mtBalanceada, nfilas, ncolumnas)
    mt = pasoDos(mtBalanceada, nfilas, ncolumnas)
    coors = obtenerCoors(mt, nfilas, ncolumnas)

    mtCoors = crearMatriz(rest, len(rest), len(rest[0]))
    pasoUno(mtCoors, len(rest), len(rest[0]))
    costo = 0;
    costos = []
    for k in coors:
        a = k[0]-1
        b = k[1]-1
        costo += mtCoors[a][b]
        costos.append(mtCoors[a][b])
        print('> El '+str(a+1)+' ocupa el '+ str(b+1))
    
    print('Costos: ')
    print(costos)
    print('Costo Total: ' + str(costo))






