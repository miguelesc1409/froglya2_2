import pe
import ts
import re

tabla_prueba = [('40', 'VARIABLE_INT', 'agua', '55', '', '', 'DECLARACIÓN', 'GLOBAL'),
                ('41', 'VARIABLE_REAL', 'fuego', '51.5', '', '', 'DECLARACIÓN', 'GLOBAL'),
                ('40', 'VARIABLE_INT', 'agua', '(55*5)/0', '', '', 'ASIGNACIÓN', 'GLOBAL'),
                ('40', 'VARIABLE_INT', 'fuego', '(55*5)/0/2', '', '', 'ASIGNACIÓN', 'GLOBAL'),
('40', 'VARIABLE_INT', 'fuego', '(55*5)', '', '', 'ASIGNACIÓN', 'GLOBAL'),
                ('40', 'VARIABLE_INT', 'tierra', '58', '', '', 'ASIGNACIÓN', 'GLOBAL'),
                ('40', 'VARIABLE_INT', 'aire', '77', '', '', 'ASIGNACIÓN', 'Elementos'),
                ('40', 'VARIABLE_INT', 'plasma', '51', '', '', 'ASIGNACIÓN', 'Elementos'),
                ('34', 'FUNCION_INT', 'Elementos', '', '(int)aire,(real)plasma', 'plasma', '', 'Elementos'),
                ('43', 'VARIABLE', 'aire', 'agua', '', '', 'ASIGNACIÓN', 'GLOBAL')]

global ban
ban =0

def indexartabla(tabla):
    tabla_prueba_con_indice = [(str(i + 1),) + tupla for i, tupla in enumerate(tabla)]
    return tabla_prueba_con_indice

def extraerfuncion(tabla):
    nuevatab = []

    for tupla in tabla:
        if tupla[2] != 'FUNCION_INT' and tupla[2] != 'FUNCION_REAL' and tupla[2] != 'FUNCION_CAD':
            nuevatab.append(tupla)

    return nuevatab
# 1ra prueba semantica
def ambitos(tabla,codigo):
    ambitoss = []
    alcance = []

    tabla = extraerfuncion(tabla)

    for i in range(0, len(tabla)):
        ambitoss.append(tabla[i][9])
    ambitoss = list(set(ambitoss))

    matriz = []  # Declarar matriz fuera del bucle
    matrizprincipal = []

    for ambito in ambitoss:
        alcance = []
        for tupla in tabla:
            if ambito == tupla[9]:
                alcance.append((tupla[0], tupla[3], tupla[7],ambito))
        if ambito=='GLOBAL':
            matrizprincipal.append(alcance)
        else:
            matriz.append(alcance)

    listas=[]
    for elemento in matrizprincipal:
        for lista in elemento:
            listas.append(lista[1])

    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j][1] in listas:
                repite=matriz[i][j][1]
                for mat in matrizprincipal:
                    for mmd in mat:
                        if repite == mmd[1]:
                            if mmd[2] != 'DECLARACIÓN':
                                lineas_codigo = codigo.split('\n')
                                nlinea = 0
                                for r, linea in enumerate(lineas_codigo, start=1):


                                    if repite in linea:
                                        #print(repite, ' in ', linea)
                                        nlinea = r
                                pe.pilaerrores.append((602,repite,nlinea))


def def_anteriormente(tabla,codigo):
    declaraciones_globales = {}
    funciones = {}

    for registro in tabla:
        if registro[7] == 'DECLARACIÓN' and registro[9] == 'GLOBAL':
            declaraciones_globales[registro[3]] = registro[1]
        elif registro[2] == 'FUNCION_INT':
            parametros = registro[5].split(',')
            funciones[registro[3]] = parametros

    for registro in tabla:
        if registro[7] == 'ASIGNACIÓN' and registro[9] == 'GLOBAL':
            variable = registro[3]
            if variable not in declaraciones_globales:
                primer_uso = None
                for i, reg in enumerate(tabla):
                    if reg[3] == variable and reg[7] == 'ASIGNACIÓN':
                        primer_uso = reg[1]
                        var = reg[3]
                        val = reg[4]
                        break
                if primer_uso:
                    lineas_codigo = codigo.split('\n')
                    nlinea = 0

                    for r, linea in enumerate(lineas_codigo, start=1):

                        if var in linea and val in linea:
                            nlinea = r

                    pe.pilaerrores.append((601, variable, nlinea))
                    #print(f"La variable '{variable}' se utiliza en '{registro[1]}' sin haber sido declarada previamente. Primer uso en '{primer_uso}'.")

        elif registro[7] == 'ASIGNACIÓN' and registro[7] != 'GLOBAL':
            variable = registro[3]
            var = registro[3]
            val = registro[4]
            nlinea = registro[8]

            pe.pilaerrores.append((601,variable,nlinea))
                #print(f"La variable '{variable}' se utiliza en '{registro[0]}' sin haber sido declarada previamente como parámetro de la función '{registro[9]}'.")

def valor_acorde(tabla,codigo):
    tabla2 = extraerfuncion(tabla)
    variables = {}  # Diccionario para almacenar los valores de las variables

    exepciones = ['(',')','*','/','-','+']

    for fila in tabla:
        _, _, tipo, variable, valor, *_ = fila


        if tipo.startswith('VARIABLE'):

            if valor:
                try:
                    pila_semantica = re.split(r'([()+*/-])', valor)
                    var = variable
                    val = valor
                    tipodec = ''
                    # Obtener variable declarada
                    for registro in tabla:
                        if registro[7] == 'DECLARACIÓN' and registro[3] == var:
                            tipodec = registro[2]

                    if tipodec == 'VARIABLE_INT':
                        for digito in pila_semantica:

                            if '.' in digito:
                                lineas_codigo = codigo.split('\n')
                                nlinea = 0

                                for r, linea in enumerate(lineas_codigo, start=1):
                                    if var in linea and val in linea:
                                        nlinea = r
                                pe.pilaerrores.append((600, variable+' = '+valor+'\n\t Se esperaba entero', nlinea))

                    elif tipodec == 'VARIABLE_REAL':
                        for digito in pila_semantica:

                            if not '.' in digito and digito not in exepciones:
                                lineas_codigo = codigo.split('\n')
                                nlinea = 0

                                for r, linea in enumerate(lineas_codigo, start=1):
                                    if var in linea and val in linea:
                                        nlinea = r
                                pe.pilaerrores.append((600,  variable+' = '+valor+'\n\t Se esperaba flotante', nlinea))

                    elif tipodec == 'VARIABLE_CAD':
                        for digito in pila_semantica:
                            if not "'" in digito:
                                lineas_codigo = codigo.split('\n')
                                nlinea = 0

                                for r, linea in enumerate(lineas_codigo, start=1):
                                    if var in linea and val in linea:
                                        nlinea = r
                                pe.pilaerrores.append((600,  variable+' = '+valor+'\n\t Se esperaba cadena', nlinea))

                except:
                    pe.pilaerrores.append((600, variable, ''))




def analizador_semantico(tabla_prueba,codigo):
    try:
        with open(codigo, "r") as archivo:
            s = archivo.read()
    except EOFError:
        print(EOFError)
    if not s: print("si")


    tabla = indexartabla(tabla_prueba)

    def_anteriormente(tabla, s)
    valor_acorde(tabla, s)
    ambitos(tabla,s)


    if pe.pilaerrores:
        return 1
    else:
        return 0

try:
    with open("elementos.fg", "r") as archivo:
        s = archivo.read()
except EOFError:
    print(EOFError)
if not s: print("si")

