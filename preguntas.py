"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


with open("data.csv","r") as file:
 data = file.readlines()
 data = [row.split('\t') for row in data] #\t es el delimitador 
 print(data)
 data2 = [row[1] for row in data]
 print(data2)
    #data = list(reader)
    #print(data)
    #data = [row.split('\t') for row in data]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    with open("data.csv","r") as file:
        data = file.readlines()
    data = [row.split('\t') for row in data] #\t es el delimitador 
    data2 = [row[1] for row in data]
    
    sum = 0 
    for x in data2:
        sum += int(x[0])
    return sum

print(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    with open("data.csv","r") as file:  
     data2 = file.readlines()
    data2 = [row[0] for row in data2]

    dic_result = dict()  

    for letra in data2:                            
        if letra in dic_result.keys():
            dic_result[letra] = dic_result[letra] + 1
        else:
            dic_result[letra] = 1  

    tuplas2 = [(key,valor) for key,valor in dic_result.items()]

    tuplas_2 = sorted(tuplas2)

    return tuplas_2
  
print(pregunta_02())



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv","r") as file:
        data = file.readlines()
    data3 = [[row[0],int(row[2])] for row in data] # encapzular dentro de la misma lista varias columnas

    diccionario = {}

    key = [row[0] for row in data3]

    values = [(row[1]) for row in data3]

    diccionario = list((zip(key,values)))

    dicci = {}

    for i in diccionario:
        if i[0] not in dicci:
            dicci[i[0]] = i[1]
        else:
            dicci[i[0]] += i[1]

    my_list = dicci.items()

    my_list = list(my_list)

    my_list3 = sorted(my_list)

    return my_list3

print(pregunta_03())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv","r") as file:
        data = file.readlines()
    data = [f.replace("\t",";") for f in data]
    data = [f.split(";") for f in data]
    datoscol = list(data)
    fecha = [row[2] for row in datoscol]
    fechacol = [f.split("-") for f in fecha]
    mes = [row[1] for row in fechacol]
#diccimes = set(mes)

    listado = []

    for i in mes:
        listado.append((i,mes.count(i)))
    list4 = sorted(set(listado))
    return list4

print(pregunta_04()) 


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv","r") as file: #estamos leyendo el archivo 
        data = file.readlines() #asi leemos todas las lineas 
    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data] #extraer las primeras dos columnas

    result_dict = {}
    for letra,valor in data:
        valor = int(valor) #para darle una transformación en valores
        if letra in result_dict.keys():                                  #si la letra existe voy a pegar en una lista el valor que estoy viendo nuevo
         result_dict[letra].append(valor)
        else:
            result_dict[letra] = [valor]  #vayamelo agregando, no me haga ninguna operación
                                            #cuando de la vuelta y encuentre la misma letra le va a pegar el valor que vimos allí 
    result_dict = [(key,max(valor),min(valor)) for key,valor in result_dict.items()] #key es la letra y valor es los números que están al frente

    list5 = sorted(result_dict)

    return list5

print(pregunta_05()) 

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv","r") as file: 
        data6 = file.readlines() 
    data6 = [f.replace("\n","") for f in data6]
    data6 = [row.split("\t") for row in data6]
    data6col5 = [row[4] for row in data6]
    data6col5 = [row.split(",") for row in data6col5]

    list6 = []

    for item in data6col5: #Aplanar la lista
        list6 += item

    data6col5 = [row.split(":") for row in list6]

    result6 = {}

    for letra,valor in data6col5:
        valor = int(valor)
        if letra in result6.keys():
            result6[letra].append(valor)  
        else:
            result6[letra] = [valor] 

    result6 = [(key,min(valor),max(valor)) for key,valor in result6.items()]

    list6 = sorted(result6)

    return list6

print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv","r") as file: 
        data7 = file.readlines() 
    
    col7 = [[row[0],int(row[2])] for row in data7] 

    dic_numeros = {}

    for x in col7:
        dic_numeros.setdefault(x[1],[]).append(x[0]) #me va agregando el número [1] y me va dejando vacio para despues agregarlo con las letras [0]

    dicclist = dic_numeros.items()

    dicclist = list(dicclist)

    list7 = sorted(dicclist)

    return list7

print(pregunta_07())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv","r") as file: 
        data8 = file.readlines() 
    col7 = [[row[0],int(row[2])] for row in data8] 

    dic_numeros = {}

    for x in col7:
        dic_numeros.setdefault(x[1],[]).append(x[0]) 
    dicclist = dic_numeros.items()

    dicclist = list(dicclist)

    punto8 = sorted(dicclist)

    dic8 = {}

    for x in punto8:
        dic8.setdefault(x[0],[]).append(sorted(set(x[1]))) 

    dic8 = dic8.items()

    dic8 = list(dic8)

    return dic8

print(pregunta_08())

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv","r") as file: 
        data9 = file.readlines() 
    data9 = [f.replace("\n","") for f in data9]
    data9 = [row.split("\t") for row in data9]
    data9col5 = [row[4] for row in data9]
    data9col5 = [row.split(",") for row in data9col5]

    list9 = []

    for item in data9col5: #aplanar listas
        list9 += item

    data6col5 = [row.split(":") for row in list9]
    col9 = [row[0] for row in data6col5] #para sacar solo la columna de las letras 

    listado = []

    for x in col9:
        listado.append((x,col9.count(x)))

    list9 = dict(sorted(set(listado)))

    return list9

print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv","r") as file: #estamos leyendo el archivo 
        data = file.readlines() #asi leemos todas las lineas
    data = [f.replace("\n","") for f in data]
    data = [row.split("\t") for row in data]

    listatuplas = [((x[0],(len(x[3].split(","))),(len(x[4].split(","))))) for x in data]

    return listatuplas

print(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv","r") as file: 
     data = file.readlines() 
    data = [f.replace("\n","") for f in data]
    data = [f.replace("\t",";") for f in data]
    data12 = [row.split(";") for row in data]

    lst_lista = [[row[0],row[4]] for row in data12] #[row[4] for row in data12]

    lst_nueva = []

    for tpl_tupla in lst_lista:
        int_suma = 0
        lst_comas = tpl_tupla[1].split(",")
        for str_elemento in lst_comas:
                lst_dos_puntos = str_elemento.split(":")
                int_numero = int(lst_dos_puntos[1])
                int_suma += int_numero
        lst_nueva.append((tpl_tupla[0],int_suma))

    dicc12 = {}

    for i in lst_nueva: #documentación misma clave suma de valores https://es.stackoverflow.com/questions/443109/misma-clave-suma-de-valores-en-diccionarios-en-python
        if i[0] not in dicc12: #vaya mire si el elemento de la posición 0 no está en el diccionario
            dicc12[i[0]] = i[1] #para que lo agregue
        else:                 #en caso contrario, si sí está sumele 
            dicc12[i[0]] += i [1]

    result12 = sorted(dicc12.items())

    dicc_final12 = {} #para ordenar nuevamente como diccionario

    for item in result12:
      nueva_clave = item[0]
      nuevo_valor = item[1]
      dicc_final12 [nueva_clave] = nuevo_valor
    
    dicc_final12

    return dicc_final12

print(pregunta_12())

