class WindowDoor:
    def __init__(self):
        
        self.type = 0 # 1: puerta, 2: ventana
        self.state = 0 # 1: cerrada, 2: abierta
        self.location = [0,0] # coordenadas x,y
        self.harder = 0 # 0: Se puede abrir y cerrar desde cualquier lado, 1: Se puede abrir y cerrar solo desde dentro
        self.floor = 0 # 1: Planta baja, 2: Planta alta, 3: Sótano, 4: Gasolinera
        self.resistence = 0 # Cantidad de vida que tiene el objeto
        self.wood = 0 # Puntos de madera que refuerzan el objeto
        self.hinge = 0 # Eje: 1 - horizontal/izquierda 2 - horizontal/derecha 3 - vertical/arriba 4 - vertical/abajo
        self.open = 0 # 1 abre hacia la derecha o hacia abajo, 2 abre hacia la izquierda o hacia arriba
        
class InsideHouse:
    def __init__(self):
        
        self.type = 0 # 1 Mesa, 2 cama, 3 silla, 4 estanteria, 5 armario, 6 baúl
        self.state = 0 # 1: cerrada, 2: abierta
        self.location = [0,0] # coordenadas x,y
        self.wood = 0 # Puntos de madera que vale el objeto (resistencia, pero que se puede acumular)
        self.floor = 0 # 1: Planta baja, 2: Planta alta, 3: Sótano, 4: Gasolinera
        self.capacity = 0 # Capacidad de utensilios que puede contener el objeto
        self.items = [] # Lista de utensilios que contiene el objeto