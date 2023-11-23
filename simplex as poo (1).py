import numpy as np
from numpy.linalg import inv, det

def getSizeConds(restrict, cond):
    tm = len(cond)+len(restrict)
    return tm

def getSizeColumns(restrict, cond):
    tm = len(restrict) 
    for i in range(len(cond)):
        if (cond[i] == '<='):
            tm += 1
        if (cond[i] == '>='):
            tm += 2
        if (cond[i] == '='):
            tm += 1 
    return tm

def dosFases(restrict, cond, z):
    pass

def getMatAum(restrict, cond, z):
    matriz = []
    cantVarNormal = len(z)
    cantConds = len(cond)
    
    for i in range(cantVarNormal):
        matriz.append(column('x'+str(i), restrict[i], "normal", z[i],"no basica"))
        
    for i in range(cantConds):
        if (cond[i] == '<='):
            matriz.append(column( 'h'+str(i), np.identity(cantConds)[i], 'holgura',0,'basica' ))
        if (cond[i] == '>='):
            matriz.append(column( 'a'+str(i), np.identity(cantConds)[i], 'artificial',0,'basica'))
            matriz.append(column( 'e'+str(i), np.identity(cantConds)[i]*-1, 'exceso',0,'no basica'))
        if (cond[i] == '='):
            matriz.append(column( 'a'+str(i), np.identity(cantConds)[i], 'artificial',0,'basica'))
    return matriz

def cambiar(m_aum, entra,sale):
    for i in range(cantColumns):
        if m_aum[i].name==entra:
                m_aum[i].base='basica'
        if m_aum[i].name==sale:
                m_aum[i].base='no basica'

def menorIgual(m_aum, z, cr):
    BV = []
    BNV = []
    Cb = []
    BVtoMat = []

    for i in m_aum:
        if (i.base == 'basica'):
            BV.append(i)
            BVtoMat.append(i.arr)
            Cb.append(i.z)
        else:
            BNV.append(i)

    B = np.array(BVtoMat);

    ### Iteraciones
    while(True):
        B_1 = inv(B)
        print('B_1')
        print(B_1)        
        
        print('Cb')
        print(Cb)        
        
        #CbB_1 = np.matmul(Cb, B_1)
        CbB_1 = np.matmul(B_1, Cb)

        print(' CbB_1 ')
        print( CbB_1 )
        
        # Evaluar no Básicas
        names = []
        for i in BNV:
            cmp = np.matmul(CbB_1, i.arr) - i.z
            names.append( [cmp, i.name] )
            print( i.name )
            print( str(CbB_1) + str(i.arr) + '-' + str(i.z) + ' = ' +str(cmp) )

        n = names[0][1]
        cmp = names[0][0]
        condNega = 0
        for i in names:
            if ( i[0] < 0 ):
                condNega = 1
            if (i[0] < cmp):
                n = i[1]
                cmp = i[0]
        print(str(n) + ' ' + str(cmp))

        if (condNega == 0):
            #xb = np.matmul(cr, B_1)
            for i in BV:
                print(i.name)

            B_2 = np.matmul(B_1, Cb)
            sol = np.matmul(cr, B_1)
            #print('Sol Opt')
            #print( B_2 )
            print('Z Opt',sol)
            print( np.matmul(cr, B_2) )
            break
        
        aj = []; 
        for i in BNV:
            if (i.name == n):
                aj = i;
        
        # Prueba de Factibilidad
        print('Factibilidad')
        B_1aj = np.matmul( aj.arr, B_1 )
        print('B_1aj'+str(B_1aj))
        B_1b = np.matmul( cr, B_1 )
        print('B_1b'+str(B_1b))

        pos = 0
        cmp = B_1b[0]/B_1aj[0]
        for i in range( len( B_1b ) ):
            if ( B_1b[i]/B_1aj[i] >= 0 ):
                cmp = B_1b[i]/B_1aj[i]
                pos = i
                break; 

        if (cmp < 0):
            print('Mi loco es puro nega')
            break;

        for i in range( len( B_1b ) ):
            if ( B_1b[i]/B_1aj[i] < cmp and B_1b[i]/B_1aj[i] >= 0):
                cmp = B_1b[i]/B_1aj[i]
                pos = i
        print(cmp)

        # Entra AJ a VNB en la posición 'Pos'
        for i in range ( len(BNV) ):
            if ( BNV[i].name == aj.name ):
                BNV[i], BV[pos] = BV[pos], BNV[i]
                B[pos] = aj.arr
                Cb[pos] = aj.z

        print('B')
        print(B)
        print('B_1')
        print(inv(B))
        
class column:
    def __init__(self, x, arr, typ, z, base):
        self.type = typ
        self.name = x
        self.arr = arr
        self.z = z
        self.base = base
    def __str__(self):
        return str(self.arr)
    def str(self):
        return str(self.arr)

class matt:
    def __init__(self, mat):
        self.matriz = mat
    def __str__(self):
        st = ''
        for i in matriz:
            st += i.str() + i.name + "\n" 
        return st

if ('__main__' == __name__):
    
    z = np.array( [150, 200] )
    cr = np.array( [45, 140, 120, 350] ) 
    restrict = np.array([
	    [1, 5, 0, 6],
	    [1, 0, 4, 10]
    ])
    cond = ['<=', '<=', '<=', '<=']
    
    """
    z = np.array( [60, 30, 20] )
    cr = np.array( [48, 20, 8] ) 
    restrict = np.array([
	    [8, 4, 2],
	    [6, 2, 1.5],
        [1, 1.5, 0.5]
    ])
    cond = ['<=', '<=', '<=']
    """
    cantFilas = len(restrict[0])
    cantColumns = getSizeColumns(restrict, cond)
    matriz = getMatAum(restrict, cond, z)
    #m = matt( matriz )
    #print(m)

    if ('>=' not in cond and '=' not in cond):
        menorIgual(matriz, z, cr);
