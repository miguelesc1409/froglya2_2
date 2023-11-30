txt = " "
cont = 0
def incrementarContador():
	global cont
	cont +=1
	return "%d" %cont

class Nodo():
	pass

class Null(Nodo):
	def __init__(self):
		self.type = 'void'

	def imprimir(self,ident):
		print (ident + "nodo nulo")

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

		return id

class programa(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.name = son1

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

	def imprimir(self):
		self.son1.imprimir()

class conjunto(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class conjinstrucciones(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class instrucciones(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class parte(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class funcion(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id


class idfun(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class retorno(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class llamadafuncion(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class parametrosfun(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class entrada(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class parametrosl(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class tda(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class tdadef(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class estructuracontrol(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class estructuraiteracion2(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class estructuraiteracion1(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class estructuradesicion(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class parametroscontrol(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class tdacontrol(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class oplog(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class oprel(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class bloque(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class comentarios(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class salidadatos(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class asignacion(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class asignacionint(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class asignacionreal(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class asignacioncadena(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class incdec(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class operadorasg(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class declaracion(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class declaracionint(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class declaracionreal(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class declaracioncad(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class lecturadatos(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class idvar(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class expresion(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class expresionreal(Nodo):
	def __init__(self, son1, name):
		self.name = name
		self.name = son1

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

	def imprimir(self):
		self.son1.imprimir()


class expresionint(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class expresioncad(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class operadorar(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class cadenacomp(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class cadena(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class textocomp(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class texto(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class valor(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class valorreal(Nodo):
	def __init__(self, son1, son2, son3, name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class valorentero(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id

class indice(Nodo):
	def __init__(self, name):
		self.name = name

	def traducir(self):
		global txt
		id = incrementarContador()
		return id