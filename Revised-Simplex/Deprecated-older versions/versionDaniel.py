import numpy as np

numVar = input('Cuantas variables utilizaras?: ')
numRestric = input('Cuantas restricciones utilizaras?: ')
restric = []
restrics = []
indep = []
obj = []
restricsTypes = []
rt = ''

for i in range(0,int(numVar)):
    obj.append(float(input(f'Ingresa la variable X{i+1} de la funcion objetivo: ')))

minmax = input('La funcion objetivo sera de minimizacion o maximizacion? (min, max): ')
if (minmax == 'min'):
    for i in range(0, int(numVar)):
        obj[i] = obj[i] * -1

for i in range(0,int(numRestric)):
    for j in range(0, int(numVar)):
        restric.append(float(input(f'Ingresa la variable X{j+1} de la restriccion {i+1}: ')))

    rt = input(f'Ingresa el tipo de restriccion para la restriccion {i+1} (=, >=, <=): ')
    ind = float(input(f'Ingresa el termino independiente del lado derecho de la restriccion {i+1}: '))
    match rt:
        case '=':
            restricsTypes.append(0)
        case '<=':
            restricsTypes.append(1)
        case '>=':
            restricsTypes.append(1)    #se transforma el >= a <=
            for m in range(0, numVar):
                restric[m] = restric[m] * -1
            ind = ind * -1

    restrics.append(restric)
    indep.append(ind)
    restric = []

# restric = [[1500, 7000, 4000, 3000], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
# indep = [14000, 1, 1, 1, 1]
# obj = [16000, 22000, 12000, 8000]

def simplex(restric, indep, obj, restricsTypes, minmax):
    restricConv = np.array(restric)
    indepConv = np.array(indep)
    objConv = np.array(obj)

    m,n = restricConv.shape    #m=numero de filas (numero de restricciones), n=numero de columnas (numero de variables)
    matrizAu = np.hstack((restricConv, np.eye(m)))   #matriz aumentada
    objAu = np.hstack((objConv, np.zeros(m)))        #vector con los valores de la funcion objetivo (las variables de hogura y artificiales valen cero)

    vars = np.zeros(m + n)  #vector con numero de variables totales
    for i in range(0, m + n):
        vars[i] = i

    basicVars = np.zeros(m) #vector con numero de variables basicas totales (es igual a la cantidad de variables de holgura y artificiales)
    noBasicVars = np.zeros(n) #vector con numero de variables no basicas totales (igual a la cantidad de variables normales)
    for i in range(0, m):
        if i < n:
            noBasicVars[i] = i  #en ambos vectores se guardan las posiciones de las variables
        basicVars[i] = n + i

    numBasic = np.zeros(m) #vector con el valor de las variables basicas

    minNum = np.zeros(n)
    BInv = np.linalg.inv(np.eye(m))



    while True:
        cb = np.dot(numBasic, BInv)


        posCol = 0                                                      #columna pivote
        for i in range(0,n):
            if (noBasicVars[i] < n):
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
        contNeg = 0
        for i in range(0,m):
            if divisores[i] == 0 or (dividendos[i] * divisores[i] < 0) or (dividendos[i] == 0 and divisores[i] < 0):
                newIndep[i] = -1
                contNeg += 1
            else:
                newIndep[i] = dividendos[i] / divisores[i]

        if (contNeg == m):   #si no existe un pivote significa que el problema no tiene solucion
            print('No existe solucion para el sistema')
            break

        posRow = 0                                                      #fila pivote
        for i in range(1,m):
            if ((newIndep[posRow] > newIndep[i]) or newIndep[posRow] < 0) and (newIndep[i] >= 0):
                posRow = i


        noBasicVars[posCol] = basicVars[posRow]                      #sale la vieja variable basica
        basicVars[posRow] = vars[posCol]                             #se almacena la nueva variable basica

        for row in range(0, m):
            for col in range(0, m):
                BInv[row, col] = matrizAu[row,int(basicVars[col])]      #Se crea la nueva matriz B

        BInv = np.linalg.inv(BInv)                                      #Se calcula la matriz B^(-1)

        for i in range(0, m):                                           #Se guarda el valor numerico de las variables basicas
            numBasic[i] = objAu[int(basicVars[i])]


    result = np.dot(BInv, indepConv)    #se calcula el valor de las variables basicas finales
    z = np.dot(cb, indepConv)           #se calcula el valor de la funcion objetivo

    for i in range(0, m):               #se verifica si existe una variable artificial en las variables basicas
        if (restricsTypes[i] == 0):
            if ((i+n) in basicVars):
                print('El problema tiene una solucion no acotda debido a que existe una variable artificial en la solucion')

    print('Variables No Basicas: ', noBasicVars)
    print('Variables Basicas: ', basicVars)
    print('Valores de las variables basicas: ', result)
    print('Valor de la funcion objetivo: ', z)

simplex(restrics, indep, obj, restricsTypes, minmax)