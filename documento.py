@Ejemplo_de_desicion

# Inicio programa
begin

# Declaracion de variables numericas
int a = 1;
int b = 10;

# Declaracion de variables de texto
cad c = 'Hola';
cad d = 'Mundo';

# Declaracion de variables booleanas
int ban = 0;
int opc = 1;

# Imprimir datos en la consola
out 'Todas';
out 'Variables'+a+'c'+b+'c'+c+'c'+d+'c'+ban+'c'+opc+'f';
out 'a'+a ;
out 'b'+b ;
out 'c'+c ;
out 'd'+d ;
out 'ban'+ban ;
out 'opc'+opc ;



# Declaracion de estructura de decision
out 'Estructuras de decision' ;

if(a<b|b>=a){
out 'Condicion1' ;
}

if (a < 5){
out 'Condicion2' ;
}

if (a <= b | b > a) {
out 'Condicion3' ;
}

if (a>5 & a<b){
out 'Condicion4' ;
}

# Declaracion de estructura de iteracion
out 'Estructuras' ;
int cont = 0 ;
int fin = 5 ;

during (fin > cont){
cont = 11 ;
out 'Cont'+cont ;
}

# Cierre del programa
end
