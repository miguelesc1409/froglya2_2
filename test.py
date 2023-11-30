import re

palabras_reservadas = ['ent', 'real', 'cad', 'lst', 'perm',
                           ':x:', ':xx:', "if", "but", ":Y:", ":O:",
                           ":NO:", "during", "do", "fun","back","null",
                           "in","out","begin","end"]

# Definir los patrones de los tokens
tokens = [
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
        ('MAYOR', r'\b>\b',19),
        ('MENOR', r'\b<\b',20),
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
        ('VARIABLE', r'\b(?!(?:' + '|'.join(palabras_reservadas) +r'))[a-zA-Z_][a-zA-Z0-9_]*',44),
        ('INICIO_CADENA', r"[']",46),
        ('NUMERO_ENTERO', r'\b[0-9]+\b',48),
        ('NUMERO_REAL', r'\.',49)
    ]

srrr = "100.5"

sep = srrr.split(";")
print(sep)

if len(sep)>1:
        if sep[1]!="":
                print("nuevo error")
        else:
                for _, patron, _ in tokens:
                        if re.match(patron, srrr):
                                print(patron)
else:
        for _, patron, _ in tokens:
                if re.match(patron, srrr):
                        print(patron)



