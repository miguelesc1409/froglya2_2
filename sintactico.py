import sys

import ply.yacc as yacc
from lexico import tokens
from lexico import analizador
from arbol import *
from valores import *
import ts
import pe

#:param t:
numreal = ""



# :return:



# valores
global tam

global nreal
global nint
global ncad
global var
global ope

global ban
global tdafund
global pfuna
global tdafun
global retur
global returl
global nomf

global ambit

global peux
global estado

estado = ""

peux = 0

nreal = ""
nint = ""
var = ""
ncad = ""
ope = ""
ambit = "GLOBAL"
block = 0
ban = 0
retur = ""
returl = ""
nomf = ""
tam = 0



precedence = (
    ('right','ASIGNACION_VALORES'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION1', 'DIVISION'),
    ('left', 'MULTIPLICACION2','MODULO')
)
nombres = {}


def p_def_programa(p):
    '''programa : conjunto'''



def p_def_conjunto(p):
    '''
    conjunto : NOMBRE_PROGRAMA conjinstrucciones
    '''

def p_def_conjunto2_error(p):
    '''
    conjunto : NOMBRE_VACIO FUNCTION_NAME conjinstrucciones
    '''

    resultado = (503, p[1], p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

def p_def_conjunto4_error(p):
    '''
    conjunto : NOMBRE_VACIO VARIABLE conjinstrucciones
    '''

    resultado = (503, p[1], p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

def p_def_conjunto3_error(p):
    '''
    conjunto : FUNCTION_NAME conjinstrucciones
    '''

    resultado = (503, p[1], p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

def p_def_conjunto_error(p):
    '''
    conjunto : conjinstrucciones
    '''

    resultado = (503, '','')
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_conjunto1_error(p):
    '''
    conjunto : VARIABLE conjinstrucciones
    '''

    resultado = (503, p[1], p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1


def p_def_conjinstrucciones(p):
    '''conjinstrucciones : BEGIN bloque END'''

def p_def_conjinstrucciones_error(p):
    '''conjinstrucciones : bloque END'''

    resultado = (519, p[2], p.lineno(2)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_conjinstrucciones1_error(p):
    '''conjinstrucciones : VARIABLE bloque END'''

    resultado = (501, p[1], p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_conjinstrucciones2_error(p):
    '''conjinstrucciones : BEGIN bloque'''

    resultado = (520, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_conjinstrucciones4_error(p):
    '''conjinstrucciones : BEGIN retorno bloque'''


def p_def_conjinstrucciones3_error(p):
    '''conjinstrucciones : BEGIN bloque VARIABLE'''

    resultado = (502, p[3], p.lineno(3)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_inifuncion(p):
    '''
    iniciofuncion : FUN tdadef FUNCTION_NAME AGRUPACION_EC1 parametrosfun AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1
    '''
    global ambit
    ambit = p[3]

    global nomf
    nomf = p[3]

def p_def_inifuncion_error(p):
    '''
    iniciofuncion : tdadef FUNCTION_NAME AGRUPACION_EC1 parametrosfun AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1
    '''

    resultado = (508, '', p.lineno(3)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_inifuncion1_error(p):
    '''
    iniciofuncion : VARIABLE tdadef FUNCTION_NAME AGRUPACION_EC1 parametrosfun AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1
    '''


    resultado = (508, p[1], p.lineno(1)-tam-9)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_inifuncion2_error(p):
    '''
    iniciofuncion : FUN tdadef VARIABLE AGRUPACION_EC1 parametrosfun AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1
    '''

    resultado = (511, p[3], p.lineno(3)-tam-9)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_inifuncion3_error(p):
    '''
    iniciofuncion : FUN tdadef FUNCTION_NAME AGRUPACION_EC1 parametrosfun AGRUPACION_EC2
    '''

    resultado = (517, '', p.lineno(3)-tam-9)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_funcion(p):
    '''
    funcion : iniciofuncion bloque finfuncion
    '''

    if peux ==0:
        estado2 = ('34', 'FUNCION_' + tdafund.upper(), nomf, '', pfuna, retur, '', p.lineno(1) - tam - 9, nomf)
        ts.tablasimbolos.append(estado2)



def p_def_finfuncion(p):
    '''
    finfuncion : retorno AGRUPACION_BLOQUE_EC2
    '''

    global ambit
    ambit = 'GLOBAL'

def p_def_finfuncion_error(p):
    '''
    finfuncion : retorno
    '''

    global ambit
    ambit = 'GLOBAL'

    resultado = (518, '', p.lineno(3) - tam - 9)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1


def p_def_retorno(p):
    '''
    retorno : BACK VARIABLE
            | BACK NUMERO_ENTERO
            | BACK NUMERO_REAL
            | BACK CADENA
    '''

    global retur
    if p[2]:
        retur = p[2]

def p_def_retorno_error(p):
    '''
    retorno : VARIABLE
            | NUMERO_ENTERO
            | NUMERO_REAL
            | CADENA
    '''

    if ambit != 'GLOBAL':
        resultado = (509, '', p.lineno(1)-tam+1)
        pe.pilaerrores.append(resultado)
    else:
        resultado = (512, p[1], p.lineno(1)-tam+1)
        pe.pilaerrores.append(resultado)

def p_def_retorno1_error(p):
    '''
    retorno : VARIABLE VARIABLE
            | VARIABLE NUMERO_ENTERO
            | VARIABLE NUMERO_REAL
            | VARIABLE CADENA
    '''

    if ambit!='GLOBAL':
        resultado = (509, p[1], p.lineno(1)-tam+1)
        pe.pilaerrores.append(resultado)
    else:
        resultado = (512, p[1], p.lineno(1)-tam+1)
        pe.pilaerrores.append(resultado)


def p_def_llamadafuncion(p):
    '''llamadafuncion : FUNCTION_NAME AGRUPACION_EC1 parametrosl AGRUPACION_EC2'''
    global nint
    global nreal
    global ncad

    global ban

    nint = p[1]
    nreal = p[1]
    ncad = p[1]

    ban = 1

def p_def_llamadafuncion_error(p):
    '''llamadafuncion : AGRUPACION_EC1 parametrosl AGRUPACION_EC2'''

    resultado = (511, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_llamadafuncion1_error(p):
    '''llamadafuncion : VARIABLE AGRUPACION_EC1 parametrosl AGRUPACION_EC2'''

    resultado = (511, p[1], p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1


def p_def_parametrosfun(p):
    '''
    parametrosfun : tda VARIABLE
                    | parametrosfun SEPARADOR tda VARIABLE
    '''
    global pfuna
    if len(p) == 3:
        pfuna = '(' + tdafun + ')' + p[2]
    elif len(p) == 5:
        pfuna = pfuna + p[2] + '(' + tdafun + ')' + p[4]


def p_def_entrada(p):
    '''
    entrada : VARIABLE
                | NUMERO_ENTERO
                | NUMERO_REAL
                | CADENA
    '''

    global returl
    if p[1]:
        returl = p[1]


def p_def_parametrosl(p):
    '''
    parametrosl : entrada
                | parametrosl SEPARADOR entrada
    '''
    global pfuna

    if len(p)==2:
        pfuna = returl
    elif len(p)==4:
        pfuna = pfuna+p[2]+returl

    ban = 1

def p_def_tda(p):
    '''
    tda : INT
            | REAL
            | CAD
    '''

    global tdafun
    tdafun = p[1]





def p_def_tdadef(p):
    '''
    tdadef :  INT
            | REAL
            | CAD
            | NULL
    '''

    global tdafund
    tdafund = p[1]

def p_def_estructuracontrol(p):
    '''
    estructuracontrol : estructuradesicion
                        | estructuraiteracion1
                        | estructuraiteracion2
    '''

def p_def_estructuraiteracion2(p):
    '''estructuraiteracion2 : DO AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 DURINDO AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2'''

def p_def_estructuraiteracion2_error(p):
    '''estructuraiteracion2 : AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 DURINDO AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2'''
    resultado = (507, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracion21_error(p):
    '''estructuraiteracion2 : VARIABLE AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 DURINDO AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2'''
    resultado = (507, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1



def p_def_estructuraiteracion22_error(p):
    '''estructuraiteracion2 : DO AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2'''
    resultado = (5071, '', p.lineno(4)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracion23_error(p):
    '''estructuraiteracion2 : DO AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 VARIABLE AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2'''
    resultado = (5071, '', p.lineno(5)-tam-9)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracionc1_error(p):
    '''estructuraiteracion2 : DO bloque AGRUPACION_BLOQUE_EC2 DURING AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2'''
    resultado = (517, '', p.lineno(1)-tam-9)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracionc2_error(p):
    '''estructuraiteracion2 : DO AGRUPACION_BLOQUE_EC1 bloque  DURING AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2'''
    resultado = (518, '', p.lineno(2)-tam-9)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracion1(p):
    '''estructuraiteracion1 : DURING AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2'''

def p_def_estructuraiteracion1_error(p):
    '''estructuraiteracion1 : AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2'''
    resultado = (506, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracion12_error(p):
    '''estructuraiteracion1 : VARIABLE AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2'''
    resultado = (506, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracion13_error(p):
    '''estructuraiteracion1 : DURING AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 bloque AGRUPACION_BLOQUE_EC2'''
    resultado = (517, '', p.lineno(4)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuraiteracion14_error(p):
    '''estructuraiteracion1 : DURING AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque'''
    resultado = (517, '', p.lineno(6)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuradesicion(p):
    '''
    estructuradesicion : IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
                            | IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 BUT AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
    '''

def p_def_estructuradesicion_error(p):
    '''
    estructuradesicion : AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
                            | AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 BUT AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
    '''

    resultado = (505, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1


def p_def_estructuradesicion1_error(p):
    '''
    estructuradesicion : VARIABLE AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
                            | VARIABLE AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 BUT AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
    '''

    resultado = (505, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuradesicion2_error(p):
    '''
    estructuradesicion : IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
    '''

    resultado = (516, '', p.lineno(8)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuradesicion3_error(p):
    '''
    estructuradesicion : IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 VARIABLE AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
    '''

    resultado = (516, p[8], p.lineno(9)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuradesicion4_error(p):
    '''
    estructuradesicion : IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 bloque AGRUPACION_BLOQUE_EC2
                            | IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 bloque AGRUPACION_BLOQUE_EC2 BUT AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
    '''

    resultado = (517, '', p.lineno(4)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuradesicion41_error(p):
    '''
    estructuradesicion : IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 BUT bloque AGRUPACION_BLOQUE_EC2
    '''

    resultado = (517, '', p.lineno(8)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuradesicion5_error(p):
    '''
    estructuradesicion : IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque
                            | IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque  BUT AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2
    '''

    resultado = (518, '', p.lineno(5)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_estructuradesicion51_error(p):
    '''
    estructuradesicion : IF AGRUPACION_EC1 parametroscontrol AGRUPACION_EC2 AGRUPACION_BLOQUE_EC1 bloque AGRUPACION_BLOQUE_EC2 BUT AGRUPACION_BLOQUE_EC1 bloque
    '''

    resultado = (518, '', p.lineno(9)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1


def p_def_parametroscontrol(p):
    '''
    parametroscontrol : tdacontrol operadorrel tdacontrol
                        | AGRUPACION_EC1 tdacontrol operadorrel tdacontrol AGRUPACION_EC2
                        | parametroscontrol operadorlog tdacontrol operadorrel tdacontrol
                        | parametroscontrol operadorlog AGRUPACION_EC1 tdacontrol operadorrel tdacontrol AGRUPACION_EC2
    '''

def p_def_tdacontrol(p):
    '''
    tdacontrol : valor
                | VARIABLE
    '''

def p_def_oplog(p):
    '''
    operadorlog : Y_LOGICO
                | O_LOGICO
                | NEGACION
    '''

def p_def_oprel(p):
    '''
    operadorrel : IGUAL
                | DIFERENTE
                | MENOR
                | MAYOR
                | MAYOR_IGUAL
                | MENOR_IGUAL
    '''

def p_def_bloque(p):
    '''
    bloque : final bloque
            | funcion bloque
            | estructuracontrol bloque
            | finvac bloque
            | retorno bloque
            | empty
    '''



# Definición de la gramática
def p_empty(p):
    'empty :'
    pass

def p_finvac(p):
    'finvac : empty FIN'

def p_final(p):
    '''
    final : asignacion FIN
            | salidadatos FIN
            | declaracion FIN
    '''

    if peux == 0:
        for tupla in ts.tablasimbolos:
            nlinea = estado[7]
            if tupla[7] == nlinea:
                indice = ts.tablasimbolos.index(tupla)
                ts.tablasimbolos[indice] = estado

def p_final_error(p):
    '''
        final : asignacion
                | salidadatos
                | declaracion
        '''


    resultado = (504, '', estado[7])
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1


def p_def_salidadatos(p):
    '''salidadatos : OUT expresioncad'''


def p_def_salidadatos_error(p):
    '''salidadatos : VARIABLE expresioncad'''

    resultado = (504, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1


def p_def_asignacion(p):
    '''
    asignacion : asignacionint
                | asignacionreal
                | asignacioncad
                | asignacionvar
    '''

def p_def_asignacionvar(p):
    '''
    asignacionvar :  VARIABLE ASIGNACION_VALORES expresionvar
                    | VARIABLE ASIGNACION_VALORES llamadafuncion
    '''
    global ban
    global estado

    if ban==1:
        estado = ('43', 'VARIABLE', p[1], var, pfuna, '', 'ASIGNACIÓN',p.lineno(1)-tam+1, ambit)
        ban=0
    else:
        estado = ('43', 'VARIABLE', p[1], var, '', '', 'ASIGNACIÓN',p.lineno(1)-tam+1, ambit)

    # ts.tablasimbolos.append(estado)

def p_def_asignacionint(p):
    '''
    asignacionint : VARIABLE ASIGNACION_VALORES expresionint
                    | VARIABLE ASIGNACION_VALORES lecturadatos
    '''

    #with open("valoresint.txt", "r") as archivo:
    #    contenido = archivo.read()
    #print(contenido)
    global estado
    estado = ('40', 'VARIABLE_INT', p[1], nint, '','','ASIGNACIÓN',p.lineno(1)-tam+1,ambit)



    # ts.tablasimbolos.append(estado)

def p_def_asignacionreal(p):
    '''
    asignacionreal : VARIABLE ASIGNACION_VALORES expresionreal
    '''

    #with open("valores.txt", "r") as archivo:
    #    contenido = archivo.read()
    #print(contenido)

    global estado
    estado = ('41', 'VARIABLE_REAL', p[1], nreal,'','', 'ASIGNACIÓN',p.lineno(1)-tam+1,ambit)

    # ts.tablasimbolos.append(estado)

def p_def_asignacioncad(p):
    '''
    asignacioncad : VARIABLE ASIGNACION_VALORES expresioncad
    '''

    global estado
    estado = ('42', 'VARIABLE_CAD', p[1], ncad, '','','ASIGNACIÓN',p.lineno(1)-tam+1,ambit)


    # ts.tablasimbolos.append(estado)


def p_def_operadorasg(p):
    '''
    operadorasg : INCREMENTO
                | DECREMENTO
    '''

def p_def_declaracion(p):
    '''
    declaracion : declaracionint
                    | declaracionreal
                    | declaracioncad
    '''

def p_def_declaracionint(p):
    '''
    declaracionint : INT VARIABLE ASIGNACION_VALORES expresionint
                    | INT VARIABLE ASIGNACION_VALORES expresionvar
                    | INT VARIABLE ASIGNACION_VALORES lecturadatos
                    | INT VARIABLE ASIGNACION_VALORES llamadafuncion
    '''


    global ban
    global estado
    if ban==1:
        estado = ('40', 'VARIABLE_INT', p[2], nint, pfuna,'','DECLARACIÓN',p.lineno(1)-tam+1,ambit)
        ban=0
    else:
        estado = ('40', 'VARIABLE_INT', p[2], nint, '','','DECLARACIÓN',p.lineno(1)-tam+1,ambit)


    #ts.tablasimbolos.append(estado)

def p_def_declaracionint_error(p):
    '''
    declaracionint : VARIABLE VARIABLE ASIGNACION_VALORES expresionint
                    | VARIABLE VARIABLE ASIGNACION_VALORES expresionvar
                    | VARIABLE VARIABLE ASIGNACION_VALORES lecturadatos
                    | VARIABLE VARIABLE ASIGNACION_VALORES llamadafuncion
    '''

    resultado = (515, '',p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)
    global peux
    peux = 1

def p_def_declaracionint1_error(p):
    '''
    declaracionint : INT VARIABLE ASIGNACION_VALORES expresionreal
                    | INT VARIABLE ASIGNACION_VALORES expresioncad
    '''

    resultado = (521, '', p.lineno(1) - tam + 1)
    pe.pilaerrores.append(resultado)
    global peux
    peux = 1

def p_def_declaracionreal(p):
    '''
    declaracionreal : REAL VARIABLE ASIGNACION_VALORES expresionreal
                    | REAL VARIABLE ASIGNACION_VALORES expresionvar
                    | REAL VARIABLE ASIGNACION_VALORES lecturadatos
                    | REAL VARIABLE ASIGNACION_VALORES llamadafuncion
    '''

    global ban
    global estado
    if ban == 1:
        estado = ('41', 'VARIABLE_REAL', p[2], nreal, pfuna,'','DECLARACIÓN',p.lineno(1)-tam+1,ambit)
        ban = 0
    else:
        estado = ('41', 'VARIABLE_REAL', p[2], nreal, '','','DECLARACIÓN',p.lineno(1)-tam+1,ambit)


    #ts.tablasimbolos.append(estado)

def p_def_declaracionreal_error(p):
    '''
    declaracionreal : VARIABLE VARIABLE ASIGNACION_VALORES expresionreal
    '''

    resultado = (515, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_declaracionreal1_error(p):
    '''
    declaracionreal : REAL VARIABLE ASIGNACION_VALORES expresionint
                    | REAL VARIABLE ASIGNACION_VALORES expresioncad
    '''

    resultado = (521, '', p.lineno(1) - tam + 1)
    pe.pilaerrores.append(resultado)
    global peux
    peux = 1

def p_def_declaracioncad(p):
    '''
    declaracioncad : CAD VARIABLE ASIGNACION_VALORES expresioncad
                    | CAD VARIABLE ASIGNACION_VALORES expresionvar
                    | CAD VARIABLE ASIGNACION_VALORES lecturadatos
                    | CAD VARIABLE ASIGNACION_VALORES llamadafuncion
    '''

    global ban
    global estado

    if ban == 1:
        estado = ('42', 'VARIABLE_CAD', p[2], ncad,pfuna,'', 'DECLARACIÓN',p.lineno(1)-tam+1,ambit)
        ban = 0
    else:
        estado = ('42', 'VARIABLE_CAD', p[2], ncad,'','', 'DECLARACIÓN',p.lineno(1)-tam+1,ambit)


    # ts.tablasimbolos.append(estado)

def p_def_declaracioncad_error(p):
    '''
    declaracioncad : VARIABLE  VARIABLE ASIGNACION_VALORES expresioncad
    '''
    resultado = (515, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_declaracioncad1_error(p):
    '''
    declaracioncad : CAD VARIABLE ASIGNACION_VALORES expresionint
                    | CAD VARIABLE ASIGNACION_VALORES expresionreal
    '''

    resultado = (521, '', p.lineno(1) - tam + 1)
    pe.pilaerrores.append(resultado)
    global peux
    peux = 1

def p_def_lecturadatos(p):
    '''lecturadatos : IN expresioncad'''
    global nint
    global nreal
    global ncad

    nint = 'Entrada'
    nreal = 'Entrada'
    ncad = 'Entrada'

def p_def_lecturadatos_error(p):
    '''lecturadatos : VARIABLE expresioncad'''

    resultado = (514, '', p.lineno(1)-tam+1)
    pe.pilaerrores.append(resultado)

    global peux
    peux = 1

def p_def_expresion(p):
    '''
    expresion : expresionint
                | expresionreal
                | expresioncad
                | expresionvar
    '''

def p_def_expresionreal(p):
    '''
    expresionreal : NUMERO_REAL
                    | expresionreal operadorar NUMERO_REAL
                    | expresionreal operadorar VARIABLE
                    | expresionvar operadorar NUMERO_REAL
    '''

    global nreal
    if len(p) == 2:
        nreal = p[1]
    elif len(p) == 3 and p[1]!='(':
        nreal = nreal+ope + p[3]

def p_def_expresionrealpar(p):
    '''
        expresionreal : AGRUPACION_EC1 expresionreal AGRUPACION_EC2
        '''
    global nreal
    nreal = p[1]+nreal+p[3]

def p_def_expresionint(p):
    '''
    expresionint : NUMERO_ENTERO
                    | expresionint operadorar NUMERO_ENTERO
                    | expresionint operadorar VARIABLE
                    | expresionvar operadorar NUMERO_ENTERO
    '''

    global nint

    #print(len(p))

    if len(p) == 2:
        nint = p[1]
    elif len(p) == 4 and p[1]!='(':
        nint = nint +ope+p[3]

def p_def_expresionintpar(p):
    '''
        expresionint : AGRUPACION_EC1 expresionint AGRUPACION_EC2
        '''
    global nint
    nint = p[1]+nint+p[3]

def p_def_expresioncad(p):
    '''
    expresioncad : CADENA
                    | expresioncad SUMA CADENA
                    | expresioncad SUMA VARIABLE
    '''

    global ncad
    if len(p) == 2:
        ncad = p[1]
    elif len(p) == 4:
        ncad = ncad,' + ',p[3]

def p_def_expresionvar(p):
    '''
    expresionvar : VARIABLE
                | expresionvar operadorar VARIABLE
    '''

    global var
    if len(p) == 2:
        var = p[1]
    elif len(p) == 4 and p[1]!='(':
        var = var +ope+p[3]

def p_def_expresionvarpar(p):
    '''
        expresionvar : AGRUPACION_EC1 expresionvar AGRUPACION_EC2
        '''
    global var
    var = p[1] + var + p[3]

def p_def_operadorar(p):
    '''
    operadorar : SUMA
                | RESTA
                | MULTIPLICACION1
                | MULTIPLICACION2
                | DIVISION
                | MODULO
    '''
    global ope
    ope = p[1]


def p_def_valor(p):
    '''
    valor : NUMERO_ENTERO
            | NUMERO_REAL
    '''

    #print(p[1])

    #with open("valores.txt", "w") as archivo:
    #    archivo.write(p[1])

def p_error(p):
    global peux
    peux = 1
    resultado = []

    if p:
        if p.value != 'end':
            # resultado = "Error sintactico de tipo {} en el valor {} en la linea {}".format( str(p.type),str(p.value),str(p.lineno))
            resultado = (500, p.value, (p.lineno - tam + 1))
            # print(resultado)
        else:
            print("REVISIOONCCCCC")
    else:
        resultado = (510, '', '')
        pass

    pe.pilaerrores.append(resultado)

    while True:
        tok = yacc.token()  # Get the next token
        print(tok)
        if (not tok or
                tok.type == 'AGRUPACION_BLOQUE_EC2'
                or
                tok.type == 'AGRUPACION_BLOQUE_EC1'
                or tok.type == 'FIN' or tok.type == 'END'):
            break
    yacc.restart()





# instanciamos el analizador sistactico
parser = yacc.yacc(errorlog=yacc.NullLogger())


def prueba_sintactica(data):
    global tam
    global peux
    peux = 0
    if not pe.pilaerrores:

        t = data.split('\n')
        tam = len(t)

        gram = parser.parse(data)

        if gram:
            pe.pilaerrores.append(str(gram))

        if pe.pilaerrores:
            return 1
        else:
            return 0
    else:
        pe.ban = 1
        return 1

def analizador_sintactico(codigo):
    try:
        with open(codigo, "r") as archivo:
            s = archivo.read()
    except EOFError:
        print(EOFError)
    if not s: print("si")

    # gram = parser.parse(s)
    # print("Resultado ", gram)

    try:
        pruebaz = prueba_sintactica(s)
    except Exception as e:
        print(e.args)

    return pruebaz
