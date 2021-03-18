class Factura ():
    empresa = ''
    nombre = ''
    descripcion = ''

    def __init__ (self,empresa,nombre,descripcion):
        self.empresa = empresa 
        self.nombre =  nombre
        self.descripcion = descripcion
    def __str__(self):
        return 'empresa:   '+ self.empresa + 'nombre:   ' + self.nombre + 'descripcion:   '+ self.descripcion

    def compra (self):
        return 'cliente comprando'
    def cotizar (self):
        return 'cliente cotizanod'

opcion1 = Factura (empresa= 'NESTLE', nombre= 'FERNANDO', descripcion='MORRALES' )
print(opcion1.compra())
