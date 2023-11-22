import numpy as np

restric = [[-1, 0, 0, 1], [0, 1, -1, 0], [-1, -1, -1, 3], [1, 1, 1, 1]]
indep = [0, 0, 0, 500000]
obj = [0.1, 0.16, 0.13, 0.2]

def simplex(restric, indep, obj):
    restricConv = np.array(restric)
    indepConv = np.array(indep)
    objConv = np.array(obj)

    m,n = restricConv.shape
    matrizAu = np.hstack((restricConv, np.eye(m)))
    objAu = np.hstack((objConv, np.zeros(m)))

    vars = np.zeros(m*2)
    for i in range(0, m*2):
        vars[i] = i
    
    basicVars = np.zeros(m)
    noBasicVars = np.zeros(m)
    for i in range(0, m):
        noBasicVars[i] = i
        basicVars[i] = m + i

    numBasic = np.zeros(m)

    minNum = np.zeros(m)
    BInv = np.linalg.inv(np.eye(m))
    
    while True:
        cb = np.dot(numBasic, BInv)
        print('\n')                                    #Se calcula CbvB^(-1)
        print(BInv)
        print('\n')
        print(cb)
        print('\n')
        print(basicVars)
        print('\n')
        print(noBasicVars)
        print('\n')
        print(minNum)
        print('\n')

        posCol = 0                                                      #columna pivote
        for i in range(0,m):
            if (noBasicVars[i] < m):
                minNum[i] = np.dot(cb, matrizAu[:,int(noBasicVars[i])]) - objConv[i]       #Valores en la fila de Z
            else:
                minNum[i] = np.dot(cb, matrizAu[:,int(noBasicVars[i])])
            
            if i > 0:
                if minNum[posCol] > minNum[i]:                          
                    posCol = i

        neg = False                                                     #si el vector minNum no tiene valores negativos significa que ya estamos en el optimo                                       
        for i in minNum:
            if (i < 0):
                neg = True
                break

        if neg == False:
            break
        
        dividendos = np.dot(BInv, indepConv)                            #se calcula las variables independientes
        divisores = np.dot(BInv, matrizAu[:,posCol])                 #se calcula los divisores de las variables independientes
        newIndep = np.zeros(m)                                        #se divide y se busca el numero positivo mas pequeño
        
        for i in range(0,m):
            if divisores[i] == 0 or (dividendos[i] * divisores[i] < 0) or (dividendos[i] == 0 and divisores[i] < 0):
                newIndep[i] = -1
            else:
                newIndep[i] = dividendos[i] / divisores[i]
        print(newIndep)
        print(dividendos)
        print(divisores)
        posRow = 0                                                      #fila pivote
        for i in range(1,m):
            if ((newIndep[posRow] > newIndep[i]) or newIndep[posRow] < 0) and (newIndep[i] >= 0):
                posRow = i

        print(posCol, posRow)
        noBasicVars[posCol] = basicVars[posRow]
        basicVars[posRow] = vars[posCol]                             #se almacena la nueva variable basica
        
        for row in range(0, m):
            for col in range(0, m):
                BInv[row, col] = matrizAu[row,int(basicVars[col])]      #Se crea la nueva matriz B
        
        BInv = np.linalg.inv(BInv)                                      #Se calcula la matriz B^(-1)
        
        for i in range(0, m):                                           #Se guarda el valor numerico de las variables basicas
            numBasic[i] = objAu[int(basicVars[i])]

    result = np.dot(BInv, indepConv)
    print(result)
    
simplex(restric, indep, obj)