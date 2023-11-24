import numpy as np
from numpy.linalg import inv, det

"""
    Esta funcion cuenta la cantidad de variables que se requieren en la matriz. En
    otras palabras, la cantidad de columnas totales de la matriz.
"""
def getSizeColumns(restrict, cond):
    # Aqui añades las columnas propias de las restricciones
    tm = len(restrict) 
    for i in range(len(cond)):
        # Si es menor igual, añades una de holgura
        if (cond[i] == '<='):
            tm += 1
        # Si es mayor igual, añades una de exceso y una artificial
        if (cond[i] == '>='):
            tm += 2
        # Si es igual, añades una artificial
        if (cond[i] == '='):
            tm += 1 
    return tm

# Esta funcion produce la matriz aumentada, ordenada en columnas
def getMatAum(restrict, cond, z):
    # Arreglo de objetos 'column'
    matriz = []
    # Cantidad de Variables normales
    cantVarNormal = len(z)
    # Cantidad de Condiciones
    cantConds = len(cond)

    # Primero se generan las columnas de las variables que vienen en las restricciones
    # Cada columna es un objeto 'column'
    # Lleva nombre de la variable, el arreglo de valores, el tipo de variable,
    # La zeta que le corresponde y si es 'basica o no'
    for i in range(cantVarNormal):
        matriz.append(column('x'+str(i), restrict[i], "normal", z[i],"no basica"))

    # Aqui se generan las columnas correspondientes a las condiciones
    # Se basa en la cantidad de condiciones para establecer el tamaño de la matriz identidad
    # El [i] en np.identity(cantConds)[i] permite obtener esa columna exacta de la matriz iden
    # Asi se obtienen las ubicaciones justas de las condiciones
    for i in range(cantConds):
        if (cond[i] == '<='):
            matriz.append(column( 'h'+str(i), np.identity(cantConds)[i], 'holgura', 0,'basica' ))
        if (cond[i] == '>='):
            matriz.append(column( 'a'+str(i), np.identity(cantConds)[i], 'artificial', 0,'basica'))
            matriz.append(column( 'e'+str(i), np.identity(cantConds)[i]*-1, 'exceso', 0,'no basica'))
        if (cond[i] == '='):
            matriz.append(column( 'a'+str(i), np.identity(cantConds)[i], 'artificial', 0,'basica'))
    return matriz

def menorIgual(m_aum, z, cr):
    # Variables Basicas
    BV = []
    # Variables NO Basicas
    BNV = []
    # La tabla llamada Cb en los PDFS 
    Cb = []
    # Esta es para obtener el arreglo de la matriz de las variables basicas sin complicar
    BVtoMat = []

    # Aqui se recorre la matriz aumentada buscando filtrar las basicas y las no basicas
    for i in m_aum:
        if (i.base == 'basica'):
            # Filtramos las Basicas
            BV.append(i)
            # Filtramos los arreglos de las Basicas para facilitar la obtencion de la B
            BVtoMat.append(i.arr)
            # Obtenemos los Coeficientes de las Columnas de las variables basicas
            Cb.append(i.z)
        else:
            # Obtenemos las Variables no Basicas
            BNV.append(i)

    # Se obtiene B
    B = np.array(BVtoMat);

    print('B')
    print(B)

    print('BNV - 0')
    for i in BNV:
        print(i)
        
    print('BV - 0')
    for i in BV:
        print(i)

    print('Z - 0')
    for i in z:
        print(i)

    ### Iteraciones
    while(True):
        # Se obtiene la inversa de B
        B_1 = inv(B)
        # Se obtiene CbB_1
        CbB_1 = np.matmul(B_1, Cb)

        print('B_1')
        print(B_1)        
        print('Cb')
        print(Cb)        
        print(' CbB_1 ')
        print( CbB_1 )
        
        # Evaluar no Básicas
        names = []
        # Se recorren las BNV obteniendo su nombre y el resultado de la evaluación
        for i in BNV:
            cmp = np.matmul(CbB_1, i.arr) - i.z
            names.append( [cmp, i.name] )
            print( i.name )
            print( str(CbB_1) + str(i.arr) + '-' + str(i.z) + ' = ' +str(cmp) )

        # Aqui se va a filtrar quien es el menor. Para ello nos seteamos en el primer
        # Valor y a partir de ahi vamos filtrando. Buscamos obtener su nombre y el valor
        n = names[0][1]
        cmp = names[0][0]
        # Esta var nos permite identificar si hay al menos una negativa
        condNega = 0
        for i in names:
            if ( i[0] < 0 ):
                condNega = 1
            if (i[0] < cmp):
                n = i[1]
                cmp = i[0]
        print(str(n) + ' ' + str(cmp))

        # Si no hay negativos es el optimo
        if (condNega == 0):
            st = '\n'
            # Se imprimen las variables basicas que terminaron en el arreglo
            for i in BV:
                st += i.name + ' '
            print(st)
            
            # Ultimos Calculos
            B_2 = np.matmul(B_1, Cb)
            sol = np.matmul(cr, B_1)
            print('Z Opt',sol)
            print( np.matmul(cr, B_2) )
            break
        # EndIf

        # Se busca aj en BNV mediante el nombre que obtuvimos antes
        aj = []; 
        for i in BNV:
            if (i.name == n):
                aj = i;
        
        # Prueba de Factibilidad
        # Calculos
        print('Factibilidad')
        B_1aj = np.matmul( aj.arr, B_1 )
        print('B_1aj'+str(B_1aj))
        B_1b = np.matmul( cr, B_1 )
        print('B_1b'+str(B_1b))

        # Aqui se busca filtrar para obtener el primer positivo
        # Identifica si son negativos todos
        # Se busca su posicion en BNV y su valor de coeficiente
        pos = 0
        cmp;
        for i in range( len( B_1b ) ):
            if ( B_1aj[i] == 0 ):
                continue
            else:
                cmp = B_1b[i]/B_1aj[i]
            if ( B_1b[i]/B_1aj[i] >= 0 ):
                cmp = B_1b[i]/B_1aj[i]
                pos = i
                break

        if (cmp < 0):
            print('Mi loco es puro nega')
            break

        # Aqui se termina de filtrar al menor positivo
        # Se busca su posicion en BNV y su valor de coeficiente
        for i in range( len( B_1b ) ):
            if ( B_1b[i]/B_1aj[i] < cmp and B_1b[i]/B_1aj[i] >= 0):
                cmp = B_1b[i]/B_1aj[i]
                pos = i

        # Entra AJ a BNV en la posición 'Pos'. Se intercambian columnas
        for i in range ( len(BNV) ):
            if ( BNV[i].name == aj.name ):
                BNV[i], BV[pos] = BV[pos], BNV[i]
                B[pos] = aj.arr
                Cb[pos] = aj.z

        print('B')
        print(B)
        print('B_1')
        print(inv(B))

# Desde cierto punto de vista, nos parecio mejor organizar en columnas en vez de filas
class column:
    def __init__(self, x, arr, typ, z, base):
        # Tipo de Variable
        self.type = typ
        # Nombre de la Variable
        self.name = x
        # Arreglo de Valores
        self.arr = arr
        # La Z que corresponde a la columna, asi no entorpece las operaciones
        self.z = z
        # Si es Basica o No
        self.base = base
    # Esto permite que cuanto hagas print a un objeto column se imprima el arreglo
    def __str__(self):
        return str(self.arr)
    # Esto te permite obtener el string del arreglo sin necesidad de acceder a los atributos
    def str(self):
        return str(self.arr)

def dosFases(matriz, z, cr, cond, columns):
    # Fase 1
    # Ecuaciones sin la de ec Z
    ecs = []
    # Ecuacion de Z
    zec = []

    # Se ordenan las  variables tal que Normales, Exceso, Holgura, Artificial
    ###
    
    # Se obtienen las ecuaciones
    for j in range( len(cond) ):
        ec = []
        for i in range( columns ):
            ec.append( matriz[i].arr[j] )
            if ( i == columns-1 ):
                ec.append( cr[j] )
        ecs.append(ec)

    posArt = []
    # Se obtiene la ecuacion de Z y las posiciones de las artificiales
    for i in range(columns):
        if (matriz[i].type == 'artificial'):
            zec.append(-1)
            posArt.append(i)
        else:
            zec.append(0)
        if ( i == columns-1 ):
            zec.append( 0 )

    # Reduccion de las Artificiales segun su posicion en las ecuaciones
    for i in posArt:
        for j in ecs:
            if ( zec[i] + j[i] == 0 ):
                zec = np.array(zec) + np.array(j)
                break; 
    # Zec*-1
    zec = zec
    cra = []
    emmet = []

    #print(zec)
    for i in range(columns):
        matriz[i].z = zec[i]

    for i in cr:
        cra.append(i)

    for i in matriz:
        if ( i.type == 'normal' ):
            emmet.append(i)
            
    for i in matriz:
        if ( i.type == 'exceso' ):
            emmet.append(i)

    for i in matriz:
        if ( i.type == 'artificial' or i.type == 'holgura' ):
            emmet.append(i)

    zec = []
    for i in range(columns):
        zec.append(emmet[i].z)
        
    menorIgual(emmet, zec, cra )

    
if ('__main__' == __name__):

    """
    z = np.array( [150, 200] )
    cr = np.array( [45, 140, 120, 350] ) 
    restrict = np.array([
	    [1, 5, 0, 6],
	    [1, 0, 4, 10]
    ])
    cond = ['<=', '<=', '<=', '<=']
    """
    
    # Todo lo organizas en columnas menos las Z's
    z = np.array( [1.5, 1] )
    # Columna de Coeficientes
    cr = np.array( [7, 4, 8] )
    # Las restricciones pero en columnas
    restrict = np.array([
	[2, 0, 2],
	[3, 1, 1]
    ])
    # Las condiciones en orden segun las Z's, Cr y las Restricciones
    cond = ['>=', '=', '<=']
    # Obtiene la Matriz Aumentada
    matriz = getMatAum(restrict, cond, z)
    # 'Menu'
    if ('>=' not in cond and '=' not in cond):
        pass
        #menorIgual(matriz, z, cr)
    else:
        dosFases(matriz, z, cr, cond, getSizeColumns(restrict, cond))
