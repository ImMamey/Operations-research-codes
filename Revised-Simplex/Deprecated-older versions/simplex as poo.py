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

def getMatAum(restrict, cond, z):
    matriz = []
    cantVarNormal = len(restrict)
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
        print("",z)
        print("",cr)
        VB=[]
        VNB=[]
        CBV=[]
        CBVB_1=[]
        ENTRA=[]
        SALE=[]
        IND1=[]
        IND2=[]
        SOL=[]
        indice=0
        indice2=0

        for i in range(cantColumns):
                print("m_aum=",m_aum[i].arr)
                if m_aum[i].base=='basica':
                   VB.append(m_aum[i].arr)
                   CBV.append(m_aum[i].z)
                else:
                   VNB.append(m_aum[i].arr)
        for i in range(len(VB)):
                print("VB=",VB[i])
        for i in range(len(VNB)):
                print("VNB=",VNB[i])

        B = np.array(VB)
        B_1 = inv(B)
        CBV = np.array(CBV)
        print("B=",B)
        print("B_1=",B_1)
        print("CBV=",CBV)

        #CBVB_1 Es la variable de los coheficientes de las variables basicas por la matriz de variables basicas
        
        CBVB_1=np.matmul(CBV,B_1)
        print("CBVB_1=",CBVB_1)

        for i in range(cantColumns):
             if m_aum[i].base=='no basica':
                ENTRA.append(np.matmul(CBVB_1,m_aum[i].arr)-m_aum[i].z)
                IND1.append(m_aum[i].name)
                print("entra=",m_aum[i].name)
             else:
                IND2.append(m_aum[i].name)
        max=np.amin(ENTRA)
        if (max>=0): #parada
                print("Se llego al optimo")
                for i in range(cantColumns):
                    print("nombre y tipo ",m_aum[i].name,m_aum[i].base,"m_aum=",m_aum[i].arr)
                SOL=np.matmul(B_1,cr)
                print("Solucion",SOL)
                return
        
        for i in range(len(IND1)):
                if max==ENTRA[i]:
                        indice=i
                
        print("valor",max,"variable que entra=",IND1[indice])

        for i in range(cantColumns):
                if m_aum[i].name==IND1[indice]:
                        B_1a=np.matmul(B_1,m_aum[i].arr)
        B_1b=np.matmul(B_1,cr)

        print("B_1a",B_1a)
        print("B_1b",B_1b)

        for i in range(len(B_1a)):
                SALE.append(B_1b[i]/B_1a[i])
        min=np.amin(SALE)

        if (min<=0): #parada
                print("Error el cociente de B_1b/B_1a dio negativo")
                print(SALE)
                return
        
        for i in range(len(SALE)):
                if min==SALE[i]:
                        indice2=i
        print(indice2)
        for i in range(cantColumns):
            print("nombre y tipo ",m_aum[i].name,m_aum[i].base,"m_aum=",m_aum[i].arr)
        print("valor",min,"variable que sale=",IND2[indice2])
        cambiar(m_aum,IND1[indice],IND2[indice2]);

        
class column:
    def __init__(self, x, arr, typ, z, base):
        self.type = typ
        self.name = x
        self.arr = arr
        self.z = z
        self.base = base

if ('__main__' == __name__):
    z = np.array( [60, 30, 20] )
    cr = np.array( [48, 20, 8] ) 
    restrict = np.array([
	[8, 4, 2],
	[6, 2, 1],
    [2, 1.5, 0.5]
    ])
    cond = ['<=', '<=', '<=']

    cantFilas = len(restrict[0])
    cantColumns = getSizeColumns(restrict, cond)
    matriz = getMatAum(restrict, cond, z)

    if ('>=' not in cond and '=' not in cond):
        menorIgual(matriz, z, cr);
    
    # matriz[0], matriz[2] = matriz[2], matriz[0]
