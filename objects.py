import pygame

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
        
class Characters:
    def __init__(self):
        
        self.type = 0 # 1: Jugador, 2: Zombi
        self.name = "Jane Doe"
        self.numberTurn = 0 # Número de turno que le toca al personaje
        self.location = [0,0]   # coordenadas x,y
        self.scene = 0 # Diferentes partes del escenario
        self.zoom = 0 # Tamaño en el que se muestra la imagen para este personaje
        
    def creation(self,type,Name,turn,location,scene,zoom):
        self.type = type
        self.name = Name
        self.numberTurn = turn
        self.location = location
        self.scene = scene
        self.zoom = zoom
        
    def move(self):
        # Localiza que está pasando en el teclado
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.location[0] -= 1
                if event.key == pygame.K_RIGHT:
                    self.location[0] += 1
                if event.key == pygame.K_UP:
                    self.location[1] -= 1
                if event.key == pygame.K_DOWN:
                    self.location[1] += 1
    
    def define_scene(self):
        
        # Abre el archivo save.relation_location_screen.txt la primera linea es la x del personaje, el primer dato de cada linea es la y del personaje, dependiendo de su x y su y, se le asigna el valor intermedio como escena
        with open("SAVE/relation_location_scene.txt","r") as tabla:
            lines = tabla.readlines()
        
        # Crear una matriz (lista de listas) a partir de lines. cada linea tiene sus valors separados por "," y "\n" indica la siguiente linea de la matriz
        matriz = []
        for line in lines:
            matriz.append(line.split(",")) # Separa los valores de cada linea por "," y los agrega a la matriz
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = int(matriz[i][j]) # Convierte los valores de la matriz en enteros

        self.scene = matriz[int(self.location[1])-1][int(self.location[0])-1]
        return
        