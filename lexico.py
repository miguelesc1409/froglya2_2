import ply.lex as lex
import re

import pe
import ts

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'INT','REAL','CAD','LST','PERM',
    'IF','BUT','DURING','DO','DURINDO','FUN','BACK','NULL',
    'IN','OUT','BEGIN','END'
)
tokens = reservada + (
'ASIGNACION_VALORES',
'INCREMENTO',
'DECREMENTO',
'SUMA',
'RESTA',
'MULTIPLICACION1',
'MULTIPLICACION2',
'DIVISION',
'MODULO',
'IGUAL',
'DIFERENTE',
'MAYOR',
'MENOR',
'MAYOR_IGUAL',
'MENOR_IGUAL',
'Y_LOGICO',
'O_LOGICO',
'NEGACION',
'AGRUPACION_EC1',
'AGRUPACION_EC2',
'AGRUPACION_LISTA1',
'AGRUPACION_LISTA2',
'AGRUPACION_BLOQUE_EC1',
'AGRUPACION_BLOQUE_EC2',
'SEPARADOR',
'FIN',
'NOMBRE_PROGRAMA',
'VARIABLE',
'CADENA',
'NUMERO_ENTERO',
'NUMERO_REAL',
'FUNCTION_NAME',
'NOMBRE_VACIO'
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_ASIGNACION_VALORES = r'='
t_INCREMENTO = r'=\+'
t_DECREMENTO = r'=\-'

t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_Y_LOGICO = r'&'
t_O_LOGICO = r'\|'
t_NEGACION = r'\!'
t_AGRUPACION_EC1 = r'[(]'
t_AGRUPACION_EC2 = r'[)]'
t_AGRUPACION_LISTA1 = r'[\[]'
t_AGRUPACION_LISTA2 = r'[\]]'
t_AGRUPACION_BLOQUE_EC1 = r'{'
t_AGRUPACION_BLOQUE_EC2 = r'}'
t_SEPARADOR = r','
t_FIN = r';'
t_VARIABLE = r'\b(?!(?:' + '|'.join(reservada) +r'))[a-z][a-zA-Z0-9_]*'
t_CADENA = r"['][a-zA-Z0-9_\s:]*[']"
t_NUMERO_ENTERO = r'\b[0-9]+\b'
t_NUMERO_REAL = r'\b[0-9]+\b\.\b[0-9]+\b'
t_NOMBRE_VACIO = r'@'

def t_FUNCTION_NAME(t):
    r'[A-Z][a-zA-Z0-9_]*'
    return t

def t_NOMBRE_PROGRAMA(t):
    r'@[A-Z][a-zA-Z0-9_]*'
    return t

def t_SUMA(t):
    r'\+'
    return t

def t_RESTA(t):
    r'-'
    return t

def t_MULTIPLICACION1(t):
    r'\*'
    return t

def t_MULTIPLICACION2(t):
    r'\^'
    return t

def t_DIVISION(t):
    r'/'
    return t

def t_MODULO(t):
    r'%'
    return t

def t_INT(t):
    r'\bint\b'
    return t

def t_REAL(t):
    r'\breal\b'
    return t

def t_CAD(t):
    r'\bcad\b'
    return t

def t_LST(t):
    r'\blst\b'
    return t

def t_PERM(t):
    r'\bperm\b'
    return t

def t_IF(t):
    r'\bif\b'
    return t

def t_BUT(t):
    r'\bbut\b'
    return t

def t_DURING(t):
    r'\bduring\b'
    return t

def t_DO(t):
    r'\bdo\b'
    return t

def t_DURINDO(t):
    r'\bdurindo\b'
    return t


def t_FUN(t):
    r'\bfun\b'
    return t

def t_BACK(t):
    r'\bback\b'
    return t

def t_NULL(t):
    r'\bnull\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_OUT(t):
    r'\bout\b'
    return t

def t_BEGIN(t):
    r'\bbegin\b'
    return t

def t_END(t):
    r'\bend\b'
    return t

t_ignore ='\t'

def t_ignore_COMMENT(t):
    r'\#.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error( t):
    global resultado_lexema
    t.lexer.skip(1)

# Definir los patrones de los tokens
tokenes = [
    ('ENTERO', r'int',0),
    ('REAL', r'real',2),
    ('CADENA', r'str',3),
    ('DEFINICION_LISTA', r'lst',4),
    ('CONSTANTE', r'perm',5),
    ('ASIGNACION_VALORES', r'=',6),
    ('INCREMENTO', r'=\+',7),
    ('DECREMENTO', r'=\-',8),
    ('SUMA', r'\b\+\b',9),
    ('RESTA', r'\b\-\b',10),
    ('MULTIPLICACION1', r'\b\*\b',11),
    ('MULTIPLICACION2', r'\b\^\b',12),
    ('DIVISION', r'\b\/\b',13),
    ('MODULO', r'\b\%\b',14),
    ('SI', r'if',15),
    ('SI_NO', r'but',16),
    ('IGUAL', r'==',17),
    ('DIFERENTE', r'!=',18),
    ('MAYOR', r'>',19),
    ('MENOR', r'<',20),
    ('MAYOR_IGUAL', r'>=',21),
    ('MENOR_IGUAL', r'<=',22),
    ('Y_LOGICO', r'&',23),
    ('O_LOGICO', r'\|',24),
    ('NEGACION', r'\!',25),
    ('MIENTRAS', r'during',26),
    ('AGRUPACIÓN_EC', r'[(]|[)]',27),
    ('AGRUPACIÓN_LISTA', r'[\[]|[\]]',28),
    ('AGRUPACIÓN_COMENTARIOS', r'\#',29),
    ('AGRUPACIÓN_BLOQUE_EC', r'[{]|[}]',31),
    ('MIENTRAS_HAZ', r'do',33),
    ('FUNCION', r'fun',34),
    ('SEPARADOR', r'\b`\b',35),
    ('RETORNO', r'back',36),
    ('NO_RETORNO', r'null',37),
    ('ENTRADA', r'\bin\b',38),
    ('SALIDA', r'out',39),
    ('FIN_INSTRUCCION', r';',40),
    ('NOMBRE_PROGRAMA', r'@',41),
    ('INICIO_PROGRAMA', r'begin',42),
    ('FIN_PROGRAMA', r'end',43),
    ('VARIABLE', r'\b(?!(?:' + '|'.join(reservada) +r'))[a-zA-Z_][a-zA-Z0-9_]*',44),
    ('INICIO_CADENA', r"[']",46),
    ('NUMERO_ENTERO', r'\b[0-9]+\b',48),
    ('NUMERO_REAL', r'\.',49)
]


# Prueba de ingreso
def prueba(data):
    global resultado_lexema
    anterior = ''
    id = 0
    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    pe.pilaerrores.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break

        res = (tok.type, tok.value, tokens.index(str(tok.type)), tok.lineno)
        estado = ('', '', tok.value, '', '', '', '', tok.lineno, '')
        id=id+1
        resultado_lexema.append(res)

        excepciones = ['AGRUPACION_EC1','Y_LOGICO','SEPARADOR','O_LOGICO','ASIGNACION_VALORES','IGUAL','SUMA']

        if tok.type == 'VARIABLE' or tok.type == 'FUNCTION_NAME':
            if anterior not in excepciones:
                ts.tablasimbolos.append(estado)

        anterior = tok.type
    #print(resultado_lexema)

    # Buscar símbolos que no coincidan con ningún patrón
    lineas_codigo = data.split('\n')
    simbolos = re.finditer(r'\S+', data)
    for simbolo in simbolos:
        sep = simbolo.group().split(";")
        sap = simbolo.group().split("{")
        sip = simbolo.group().split("}")

        for i, linea in enumerate(lineas_codigo, start=1):

            if len(sep) > 1:
                if sep[1] != "":
                    if str(simbolo.group()) in linea:
                        pe.pilaerrores.append((401, str(simbolo.group()), i))

                else:
                    if str(simbolo.group()) in linea and not any(
                            re.match(patron, str(simbolo.group())) for _, patron, _ in tokenes):
                        pe.pilaerrores.append((400, str(simbolo.group()), i))

            elif len(sap) > 1:
                if sap[1] != "":
                    if str(simbolo.group()) in linea:
                        pe.pilaerrores.append((401, str(simbolo.group()), i))
                else:
                    if str(simbolo.group()) in linea and not any(
                            re.match(patron, str(simbolo.group())) for _, patron, _ in tokenes):
                        pe.pilaerrores.append((400, str(simbolo.group()), i))
            elif len(sip) > 1:
                if sip[1] != "":
                    if str(simbolo.group()) in linea:
                        pe.pilaerrores.append((401, str(simbolo.group()), i))
                else:
                    if str(simbolo.group()) in linea and not any(
                            re.match(patron, str(simbolo.group())) for _, patron, _ in tokenes):
                        pe.pilaerrores.append((400, str(simbolo.group()), i))
            else:
                if str(simbolo.group()) in linea and not any(
                        re.match(patron, str(simbolo.group())) for _, patron, _ in tokenes):
                    pe.pilaerrores.append((400, str(simbolo.group()), i))

        pe.pilaerrores.sort(key=lambda x: x[2])

    if pe.pilaerrores:
        pe.ban=1
        return 1
    else:
        return 0


 # instanciamos el analizador lexico
analizador = lex.lex()

def analizador_lexico(codigo):
    with open(codigo, "r") as archivo:
        data = archivo.read()

    pruebaz = prueba(data)

    return pruebaz

