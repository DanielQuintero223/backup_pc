#Se define la clase
class Persona:

    """ Todo método tiene como primer parámetro el identificador self que tiene la referencia del objeto que llamó al método,
    y sirve para poder referenciar sus propias caracteristicas, como si fuera un this """
    def inicializar(self,nom):
        """ Si antecedemos el self, indicamos que la variable nombre pertenece al objeto. Por lo 
        tanto, la variable nombre seguira vigente asi se termine de ejecutar la funcion, siendo 
        como una variable global.  """
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()