import pygame
import random

import languaje
import objects

class image:
    
    def __init__(self,languaje = 0):
        pygame.init()
        pygame.mixer.init()
        
        screen_info =               pygame.display.Info()
        self.width =                screen_info.current_w
        #self.width = 1000
        self.height =               (self.width*1440)/3440
        # Crea la pantalla de juego global
        self.screen =               pygame.display.set_mode((self.width, self.height),) 
        # Titulo de la ventana
        pygame.display.set_caption("NOLD")  
        # Idioma del juego
        self.language = languaje
        # Imágenes para los menús
        self.house_title =          pygame.image.load("ART/HOUSE_TITLE.png")
        self.house_title =          pygame.transform.scale(self.house_title, (int((self.width*1909)/3440), int((self.height*835)/1440)))  
        self.shine_title =          pygame.image.load("ART/SHINE_TITLE.png")
        self.shine_title =          pygame.transform.scale(self.shine_title, (int((self.width*2249)/3440), int((self.height*2245)/1440)))
        self.title =                pygame.image.load("ART/TITLE.png")
        self.title =                pygame.transform.scale(self.title, (int((self.width*(1529/4))/3440), int((self.height*(572/4))/1440)))
        self.blood_title =          pygame.image.load("ART/BLOOD_TITLE.png")
        self.blood_title =          pygame.transform.scale(self.blood_title, (int((self.width*600)/3440),int((self.height*50)/1440)))      
        self.blood_diffic =         pygame.image.load("ART/BLOOD_DIFFIC.png")
        self.blood_diffic =         pygame.transform.scale(self.blood_diffic, (int((self.width*80)/3440),int((self.height*80)/1440)))     

        self.image = 0
        self.back = pygame.image.load("ART/SCENE_12_BACK.png")
        self.front = pygame.image.load("ART/scene_12_FRONT.png")
            
        # Imagen para el cursor
        self.cursor_sprite = CursorSprite("ART/CURSOR_ARROW.png", ((self.width*0.2)/3440))
        # Tipografía global                
        self.type =                 pygame.font.Font("ART/typeg.ttf", int((self.width*50)/3440))
        # Audios
        self.sound_title =          pygame.mixer.Sound("ART/MENU_SOUND.wav")
        self.sound_click =          pygame.mixer.Sound("ART/CLICK_SOUND.wav")
        # Constantes
        self.turns =                7 # Esto indica el máximo de turnos que rota. En el juego siembre será 7, pero para test puede cambiarse
        # Variables
        self.turn =                 0 # Esto indica el turno actual (1 = Barbara, 2 = Ben, 3 = Harry, 4 = Hellen, 5 = Tom, 6 = Judy, 7 = zombis)
        self.zombiesOnStage =       0 # Esto indica el número de zombis que hay en el escenario
        self.hour =                 0 # Esto indica la hora actual
        self.x_house =              20 # Esto indica la posición x de la casa
        self.y_house =              20 # Esto indica la posición y de la casa
        self.zoom =                 0.9 # Esto indica el zoom de la casa
        self.scene =                0 # Esto indica la escena actual
        self.transparence_all_image=255 # Esto indica la transparencia de todas las imágenes
        self.event_cards=           [] # Aquí se guardan las cartas de eventos
        self.first_inititation =    True # Esto indica si es la primera vez que se inicia la pantalla
        
        self.zombies_cards=         [] # Aquí se guardan las cartas de zombies (se rellena en el reset)
        self.items_cards=           [] # Aquí se guardan las cartas de objetos
        self.items_cards_2=         [] # Aquí se guardan las cartas de objetos durante la preparación de la partida
        self.items_cards_3=         [] # Aquí se guardan las cartas de objetos durante la partida
        
    def Menu(self):
        
        pygame.mouse.set_visible(False)
        
        self.sound_title.play(-1)
        self.sound_title.set_volume(0)
        for i in range(0,100):
            self.sound_title.set_volume(i/100)
            pygame.time.delay(10)
            
        original_rect  = self.house_title.get_rect()
        current_scale = 0.001
        current_rect  = self.screen.get_rect().center
        
        clock = pygame.time.Clock()
        
        bucle = True
        while bucle:
            scaled_house_title = pygame.transform.scale(self.house_title, (int(original_rect.width * current_scale),
                                                              int(original_rect.height * current_scale)))
            current_rect = scaled_house_title.get_rect(center=self.screen.get_rect().center)
            self.screen.fill((0,0,0))
            self.screen.blit(scaled_house_title, current_rect.topleft)
            pygame.display.flip()            
            clock.tick(60)
            current_scale += 0.006
            if current_scale >= 0.5:
                bucle = False
        
        x_title = self.width/2 - self.title.get_width()/2
        y_title = self.height/2 - self.title.get_height()/((self.height*6)/1440)
        
        for i in range(int((self.height*120)/1440)):
            self.screen.fill((0,0,0))
            self.screen.blit(self.title, (x_title,y_title))
            self.screen.blit(scaled_house_title, current_rect.topleft)
            pygame.display.flip()
            y_title -= 3
            pygame.time.delay(10)   
            
        y_title = ((self.height*336.16666666666663)/1440)
        textos = languaje.languaje_menu(self.language)
        
        for a in range(0,255,4):    
            self.screen.fill((0,0,0))
            self.screen.blit(self.title, (x_title,y_title))
            self.screen.blit(scaled_house_title, current_rect.topleft)
            options = self.put_text(textos)
            pygame.display.flip()
            pygame.time.delay(10)
        
        alpha= 0
        into_menu = True
        cursor_group = pygame.sprite.Group()
        cursor_group.add(self.cursor_sprite)
        
        while into_menu:
            position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    position_mouse = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position_mouse = event.pos
                    if position_mouse[0] > self.width/2 - self.title.get_width()/2 and position_mouse[0] < self.width/2 + self.title.get_width()/2:
                        self.sound_click.play()
                        control_position = ((self.height*200)/1440)
                        for possibilities in range(5):
                            if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + ((self.height*50)/1440):
                                
                                if possibilities == 0:
                                    self.ResetValues()
                                    self.playing()               
                                
                                elif possibilities == 1:
                                    self.difficulty_options(scaled_house_title,current_rect,position_mouse)
                                
                                elif possibilities == 2:
                                    self.language += 1
                                    if self.language == 13:
                                        self.language = 0
                                    datas = open("SAVE/lang.txt", "w")
                                    datas.write(str(self.language))
                                    datas.close()
                                    
                                
                                elif possibilities == 3:
                                    self.credits(scaled_house_title,current_rect,position_mouse)
                                
                                elif possibilities == 4:
                                    into_menu = False
                                    break
                            
                            control_position += ((self.height*50)/1440)
            if alpha < 255:
                alpha += 4
                self.shine_title.set_alpha(alpha)
            elif alpha > 255:
                alpha = 255
                self.shine_title.set_alpha(alpha)
            
            self.base_menu(scaled_house_title,current_rect)

            if position_mouse[0] > self.width/2 - self.title.get_width()/2 and position_mouse[0] < self.width/2 + self.title.get_width()/2:
                control_position = ((self.height*200)/1440)
                for possibilities in range(5):
                    if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + ((self.height*50)/1440):
                        self.screen.blit(self.blood_title, (self.width/2 - self.title.get_width()/2 - ((self.width*120)/3440),self.height/2 - options.get_height()/2 + control_position+((self.height*10)/1440)))
                    control_position += ((self.height*50)/1440)
                    
            textos = languaje.languaje_menu(self.language)
            options = self.put_text(textos)
            
            position_mouse = pygame.mouse.get_pos()
            cursor_group.update(position_mouse)
            cursor_group.draw(self.screen)
            pygame.display.flip()
        
        actually_screen = self.screen.copy()
        for a in range(255,0,-2):
            
            self.sound_title.set_volume(a/255)
            actually_screen.set_alpha(a)
            self.screen.fill((0,0,0))
            self.screen.blit(actually_screen, (0,0))
            pygame.display.flip()
            pygame.time.delay(10) 
               
        return False   
    
    def difficulty_options(self,scaled_house_title,current_rect,position_mouse):
        
        datas = open("SAVE/dif.txt", "r")
        difficulty_str = datas.readline()
        difficulty = eval(difficulty_str)
        datas.close()
        
        cursor_group = pygame.sprite.Group()
        cursor_group.add(self.cursor_sprite)        
        into_difficulty = True
        while into_difficulty:
            for event in pygame.event.get():
                            if event.type == pygame.MOUSEMOTION:
                                position_mouse = event.pos
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if position_mouse[0] > ((self.width*1236)/3440) and position_mouse[0] < ((self.width*1400)/3440) and position_mouse[1] > ((self.height*1345)/1440) and position_mouse[1] < ((self.height*1392)/1440):
                                    self.sound_click.play()
                                    datas = open("SAVE/dif.txt", "w")
                                    datas.write(str(difficulty))
                                    datas.close()
                                    into_difficulty = False
                                    break
                                elif position_mouse[0] > ((self.width*2156)/3444) and position_mouse[0] < ((self.width*2200)/3440):
                                    control_position = ((self.height*290)/1440)
                                    
                                    for possibilities in range(7):
                                        if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + ((self.height*50)/1440):
                                            difficulty[possibilities] -= 1
                                            self.sound_click.play()                                            
                                            if difficulty[possibilities] < 0:
                                                difficulty[possibilities] = 0
                                        control_position += ((self.height*45)/1440)
                                elif position_mouse[0] > ((self.width*2284)/3440) and position_mouse[0] < ((self.width*2317)/3440):
                                    control_position = ((self.height*290)/1440)
                                    for possibilities in range(7):
                                        if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + ((self.height*50)/1440):
                                            difficulty[possibilities] += 1
                                            self.sound_click.play()
                                            if possibilities == 2 and difficulty[possibilities] > 30:
                                                difficulty[possibilities] = 30
                                            elif possibilities != 2 and difficulty[possibilities] > 3:
                                                difficulty[possibilities] = 3
                                        control_position += ((self.height*45)/1440)
                                                    
            self.base_menu(scaled_house_title,current_rect)

            if position_mouse[0] > ((self.width*1236)/3440) and position_mouse[0] < ((self.width*1400)/3440) and position_mouse[1] > ((self.height*1345)/1440) and position_mouse[1] < ((self.height*1392)/1440):
                self.screen.blit(self.blood_title, (((self.width*1050)/3440),((self.height*1350)/1440)))
            
            elif position_mouse[0] > ((self.width*2156)/3444) and position_mouse[0] < ((self.width*2200)/3440):
                control_position = ((self.height*290)/1440)
                for possibilities in range(7):
                    if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + ((self.height*50)/1440):
                        self.screen.blit(self.blood_diffic, (((self.width*2150)/3444),self.height/2 - options.get_height()/2 + control_position+((self.height*5)/1440)))
                    control_position += ((self.height*45)/1440)                
            
            elif position_mouse[0] > ((self.width*2284)/3440) and position_mouse[0] < ((self.width*2317)/3440): 
                control_position = ((self.height*290)/1440)
                for possibilities in range(7):
                    if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + ((self.height*50)/1440):
                        self.screen.blit(self.blood_diffic, (((self.width*2278)/3444),self.height/2 - options.get_height()/2 + control_position+((self.height*5)/1440)))
                    control_position += ((self.height*45)/1440) 
                        
            suma = ((self.height*200)/1440)
            textos = languaje.languaje_difficulty(self.language)
            title = 0
            for i in textos:
                options = self.type.render(i, True, (255,100,100))
                if title == 0:
                    x_options = self.width/2 - options.get_width()/2
                else:
                    x_options = self.width/2 - self.house_title.get_width()/4
                y_options = self.height/2 - options.get_height()/2 + suma
                self.screen.blit(options, (x_options, y_options))
                if title >1 and title < 9:
                    surface_to_blit_1 = self.type.render("< ", True, (255,255,255))
                    surface_to_blit_2 = self.type.render(str(difficulty[title-2]), True, (255,255,100))
                    surface_to_blit_3 = self.type.render(" >", True, (255,255,255))
                    self.screen.blit(surface_to_blit_1,(x_options + ((self.width*925)/3440), y_options))
                    self.screen.blit(surface_to_blit_2,(x_options + ((self.width*1000)/3440) - surface_to_blit_2.get_width()/2, y_options))
                    self.screen.blit(surface_to_blit_3,(x_options + ((self.width*1025)/3440), y_options))
                    
                suma += ((self.height*45)/1440)
                title +=1    
                
            position_mouse = pygame.mouse.get_pos()
            cursor_group.update(position_mouse)
            cursor_group.draw(self.screen)
            pygame.display.flip() 
            
        return       
    
    def playing(self):
        self.image = self.screen.copy()
        in_game = True
        while in_game:
            if self.turn == 1:
                possible_paint = self.calculate_paint_house(self.Barbara)
                if possible_paint == True:
                    self.paint_house(self.Barbara)
                self.Barbara.move()
                self.Barbara.define_scene()
            
    def ResetValues(self):
        # Entrega el turno a Barbara
        self.turn =                1
        # Crea las barajas
        datas = open("SAVE/cards_zombies.txt", "r")
        self.zombies_cards_str = datas.readline()
        self.zombies_cards = eval(self.zombies_cards_str)
        datas.close()
        # (1 - 1 zombi, 2 - 2 zombis, 3 - 3 zombis, 4 - 4 zombis, 5 - 5 zombis, 6 - 6 zombis, 7 - fuga)
        datas = open("SAVE/cards_events.txt", "r")
        self.event_cards_str = datas.readline()
        self.event_cards = eval(self.event_cards_str)
        datas.close()
        # (1 - Agresión, 2 - Nuerte, 3 - Pánico, 4 - Pasa una hora, 5 - Serenidad, 6 - zombi, 8 - Zombies en la gasolinera)
        datas = open("SAVE/cards_items.txt", "r")
        self.items_cards_str = datas.readline()
        self.items_cards = eval(self.items_cards_str)
        datas.close()
        # (1 - Botella, 2 - Cartuchos , 3 - clavos, 4 - Cuchillo, 5 - Cuerda, 6 - Escopeta, 7 - Espátula, 8 - Gasolina, 9 - Hacha, 10 - Llave, 11 - Martillo, 12 - Mechero, 13 - Pañuelo, 14 - Pico, 15 - zombi)
        self.items_cards_2=         [] # De momento está vacía
        self.items_cards_3=         [] # De momento está vacía
        # Prepara las barajas
        # Quita de la baraja de items las cartas de zombi y llave y las mete en la baraja 2
        for i in range(len(self.items_cards)-1,-1,-1):
            if self.items_cards[i] == 15 or self.items_cards[i] == 10:
                self.items_cards_2.append(self.items_cards[i])
                self.items_cards.pop(i)
        # Mezcla las cartes de items
        random.shuffle(self.items_cards)
        # Apartamos las 10 primeras cartas de items_cards para ponerlas en items_cards_3
        for i in range(10):
            self.items_cards_3.append(self.items_cards[i])
            self.items_cards.pop(i)
        # Añade a items_cards_3 todas las cartas de items_Cards_2 que estén marcadas como 15 (zombi)
        for i in range(len(self.items_cards_2)-1,-1,-1):
            if self.items_cards_2[i] == 15:
                self.items_cards_3.append(self.items_cards_2[i])
                self.items_cards_2.pop(i)
        # Eliminamos todas las cartas de items_cards que superen la número 37
        not_yet = True
        while not_yet:
            self.items_cards_2.append(self.items_cards[-1])
            self.items_cards.pop(-1)
            if len(self.items_cards) == 37:
                not_yet = False
        # Añadimos la carta de llave a items_Cards:
        self.items_cards.append(self.items_cards_2[0])
        self.items_cards_2.pop(0)
        # Vuelve a mezclar el motón items_cards e items_cards_3
        random.shuffle(self.items_cards_3)
        random.shuffle(self.items_cards)        
        # Mezclamos las cartas de zombies
        random.shuffle(self.zombies_cards)
        # Mezclamos las cartas de eventos
        random.shuffle(self.event_cards)
        
        # Crea los objetos
        # Crea los InsideHouse
        all_objects_atributes = ((5,1,(11,18),5,1,45),
                                 (5,1,(11,18),5,1,45),
                                 (5,1,(11,18),5,1,45),
                                 (5,1,(11,18),5,1,45),
                                 (5,1,(11,18),5,3,45),
                                 (6,1,(11,18),3,2,25),
                                 (6,1,(11,18),3,3,25),
                                 (4,1,(11,18),1,2,8),
                                 (4,1,(11,18),1,1,8),
                                 (4,1,(11,18),1,1,8),
                                 (4,1,(11,18),1,1,8),
                                 (4,1,(11,18),1,1,8),
                                 (1,1,(11,18),3,1,20),
                                 (1,1,(11,18),3,1,20),
                                 (1,1,(11,18),3,2,20),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,1,4),
                                 (3,1,(11,18),0,2,4),
                                 (3,1,(11,18),0,2,4),
                                 (3,1,(11,18),0,2,4),
                                 (3,1,(11,18),0,3,4),
                                 (3,1,(11,18),0,3,4),
                                 (2,1,(11,18),0,1,40),
                                 (2,1,(11,18),0,1,40),
                                 (2,1,(11,18),0,3,40))
        for i in range(15):
            exec("self.InsideHouse"+str(i)+" = objects.InsideHouse()")
            exec("self.InsideHouse"+str(i)+".type ="+str(all_objects_atributes[i][0]))
            exec("self.InsideHouse"+str(i)+".state ="+str(all_objects_atributes[i][1]))
            exec("self.InsideHouse"+str(i)+".location ="+str(all_objects_atributes[i][2]))
            exec("self.InsideHouse"+str(i)+".capacity ="+str(all_objects_atributes[i][3]))
            exec("self.InsideHouse"+str(i)+".floor ="+str(all_objects_atributes[i][4]))
            exec("self.InsideHouse"+str(i)+".wood ="+str(all_objects_atributes[i][5]))
        
        # repasamos todos los objetos
        for i in range (15):
            # Si es un armario, mesa, estantería o baúl...
            if eval("self.InsideHouse"+str(i)+".type") == 1 or eval("self.InsideHouse"+str(i)+".type") == 4 or eval("self.InsideHouse"+str(i)+".type") == 5 or eval("self.InsideHouse"+str(i)+".type") == 6:

                # salvamos el valor de capacity en una variable circunstancial
                e = eval("self.InsideHouse"+str(i)+".capacity")
                # Si type es igual a armario o baúl...
                if eval("self.InsideHouse"+str(i)+".type") == 5 or eval("self.InsideHouse"+str(i)+".type") == 6:
                    # Restamos uno a e
                    e -= 1
                # miramos el valor de capacity. Ese número de veces...
                for a in range(e):
                    # copiamos el último valor de la lista de items_cards y lo añadimos a items
                    eval("self.InsideHouse"+str(i)+".items.append(self.items_cards[-1])")
                    # borramos el último valor de la lista de items_cards
                    self.items_cards.pop(-1)
                    
        # Repasamos una vez más todos los objetos
        for i in range (15):
            # Si es una armario, o baúl...
            if eval("self.InsideHouse"+str(i)+".type") == 5 or eval("self.InsideHouse"+str(i)+".type") == 6:
                # Añadimos a la lista de items el último valor de la lista de items_cards_3
                eval("self.InsideHouse"+str(i)+".items.append(self.items_cards_3[-1])")
                # Borramos el último valor de la lista de items_cards_3
                self.items_cards_3.pop(-1)
        # items 2 e items 3 los juntamos en un único paquete (items 2)
        self.items_cards_2 = self.items_cards_2 + self.items_cards_3
        self.items_cards_3 = []
        
        # Crea las puertas y ventanas
        # Cogemos el valor del archivo dificulty para saber cuantas puertas y ventanas están cerradas
        datas = open("SAVE/dif.txt", "r")
        difficulty_str = datas.readline()
        difficulty = eval(difficulty_str)
        datas.close()
        windoor_difficulty = difficulty[2]
        all_windoor_atributes = ((1,1,(13,11),0,1,20,0,1,2),
                                 (1,1,(14,11),0,1,20,0,2,2),
                                 (1,1,(23,11),0,1,20,0,1,2),
                                 (1,1,(24,11),0,1,20,0,2,2),
                                 (2,1,(16,11),0,1,4,0,1,2),
                                 (2,1,(17,11),0,1,4,0,2,2),
                                 (2,1,(26,11),0,1,4,0,1,2),
                                 (2,1,(27,11),0,1,4,0,2,2),
                                                                  
                                 (2,1,(11,17),0,1,4,0,1,2),
                                 (2,1,(11,18),0,1,4,0,1,2),
                                 (2,1,(11,24),0,1,4,0,1,2),
                                 (2,1,(11,25),0,1,4,0,1,2),
                                 (1,1,(11,28),0,1,20,0,1,2),
                                 (1,1,(11,29),0,1,20,0,1,2),
                                 
                                 (2,1,(31,16),0,1,4,0,2,1),
                                 (2,1,(31,17),0,1,4,0,2,1),
                                 (1,1,(31,24),0,1,20,0,2,1),
                                 (1,1,(31,25),0,1,20,0,2,1),
                                 (2,1,(31,29),0,1,4,0,2,1),
                                 
                                 (2,1,(13,30),0,1,4,0,1,1),
                                 (2,1,(14,30),0,1,4,0,2,1),
                                 (1,1,(21,30),0,1,20,0,1,1),
                                 (1,1,(22,30),0,1,20,0,2,1),
                                 (2,1,(26,30),0,1,4,0,1,1),
                                 (2,1,(27,30),0,1,4,0,2,1),
                                 (2,1,(30,30),0,1,4,0,2,1),
                                 
                                 (2,1,(18,32),0,1,4,0,3,2),
                                 (2,1,(21,33),0,1,4,0,1,1),
                                 (1,1,(22,33),0,1,20,0,2,1),
                                 (1,1,(24,32),0,1,20,0,3,1),
                                 
                                 (1,1,(14,21),0,1,20,0,1,1),
                                 (1,1,(15,21),0,1,20,0,2,1),
                                 (1,1,(16,16),0,1,20,0,3,1),
                                 (1,1,(16,17),0,1,20,0,4,1),
                                 (1,1,(20,17),0,1,20,0,1,2),
                                 (1,1,(21,17),0,1,20,0,2,2),
                                 (1,1,(26,17),0,1,20,0,3,2),
                                 (1,1,(26,18),0,1,20,0,4,2),
                                 (1,1,(27,21),0,1,20,0,1,1),
                                 (1,1,(28,21),0,1,20,0,2,1),
                                 
                                 (1,1,(18,22),1,1,200,0,1,1),
                                 
                                 (2,1,(17,16),0,3,4,0,3,2),
                                 (2,1,(17,17),0,3,4,0,4,2),
                                 (2,1,(17,21),0,3,4,0,3,2),
                                 (2,1,(17,22),0,3,4,0,4,2),
                                 (2,1,(21,15),0,3,4,0,1,2),
                                 (2,1,(22,15),0,3,4,0,2,2),
                                 (2,1,(26,17),0,3,4,0,3,1),
                                 (2,1,(26,18),0,3,4,0,4,1),
                                 (2,1,(26,21),0,3,4,0,3,1),
                                 (2,1,(26,22),0,3,4,0,4,1),
                                 (2,1,(21,24),0,3,4,0,1,1),
                                 (2,1,(25,24),0,3,4,0,2,1))
        
        for i in range(len(all_windoor_atributes)):
            exec("self.windoor"+str(i)+" = objects.WindowDoor()")
            exec("self.windoor"+str(i)+".type ="+str(all_windoor_atributes[i][0]))
            exec("self.windoor"+str(i)+".state ="+str(all_windoor_atributes[i][1]))
            exec("self.windoor"+str(i)+".location ="+str(all_windoor_atributes[i][2]))
            exec("self.windoor"+str(i)+".harder ="+str(all_windoor_atributes[i][3]))
            exec("self.windoor"+str(i)+".floor ="+str(all_windoor_atributes[i][4]))
            exec("self.windoor"+str(i)+".resistence ="+str(all_windoor_atributes[i][5]))
            exec("self.windoor"+str(i)+".wood ="+str(all_windoor_atributes[i][6]))
            exec("self.windoor"+str(i)+".hinge ="+str(all_windoor_atributes[i][7]))
            exec("self.windoor"+str(i)+".open ="+str(all_windoor_atributes[i][8]))
            
        # Cerramos puertas y ventanas que tocan
        for i in range(windoor_difficulty):
            trying = True
            while trying:
                # Cogemos un número aleatorio entre 0 y len(all_windoor_atributes)
                a = random.randint(0,len(all_windoor_atributes)-1)
                # Si la puerta o ventana está abierta y su harder es 0 y su floor es 1 y (su x es 11 o 18 o 29 o 31 o su y es 11 o 30 o 33) 
                if all_windoor_atributes[a][1] == 1 and all_windoor_atributes[a][3] == 0 and all_windoor_atributes[a][4] == 1 and (all_windoor_atributes[a][2][0] == 11 or all_windoor_atributes[a][2][0] == 18 or all_windoor_atributes[a][2][0] == 29 or all_windoor_atributes[a][2][0] == 31 or all_windoor_atributes[a][2][1] == 11 or all_windoor_atributes[a][2][1] == 30 or all_windoor_atributes[a][2][1] == 33):
                    # La cerramos
                    exec("self.windoor"+str(a)+".state = 0")
                    trying = False  
                                  
        # Crea los personajes
        self.Barbara = objects.Characters()
        self.Barbara.creation(1,"Barbara",1,[1,1],11,1)
        
        
        self.zombiesOnStage = 0 # Contador de zombies en el escenario
        self.hour = 20 # Hora actual
        self.turn = 1 # Turno actual
        self.first_inititation = True # Primera iniciación
                       
    def credits(self,scaled_house_title,current_rect,position_mouse):
        cursor_group = pygame.sprite.Group()
        cursor_group.add(self.cursor_sprite)        
        into_credits = True
        while into_credits:
            for event in pygame.event.get():
                            if event.type == pygame.MOUSEMOTION:
                                position_mouse = event.pos
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if position_mouse[0] > ((self.width*1236)/3440) and position_mouse[0] < ((self.width*1400)/3440) and position_mouse[1] > ((self.height*1345)/1440) and position_mouse[1] < ((self.height*1392)/1440):
                                    self.sound_click.play()
                                    into_credits = False
                                    break            
            self.base_menu(scaled_house_title,current_rect)

            if position_mouse[0] > ((self.width*1236)/3440) and position_mouse[0] < ((self.width*1400)/3440) and position_mouse[1] > ((self.height*1345)/1440) and position_mouse[1] < ((self.height*1392)/1440):
                self.screen.blit(self.blood_title, (((self.width*1050)/3440),((self.height*1350)/1440)))

            suma = ((self.height*200)/1440)
            textos = languaje.languaje_cast(self.language)
            title = 0
            for i in textos:
                options = self.type.render(i, True, (255,100,100))
                if title == 0:
                    x_options = self.width/2 - options.get_width()/2
                else:
                    x_options = self.width/2 - self.house_title.get_width()/4
                y_options = self.height/2 - options.get_height()/2 + suma
                self.screen.blit(options, (x_options, y_options))
                suma += ((self.height*45)/1440)
                title +=1    
                
            position_mouse = pygame.mouse.get_pos()
            cursor_group.update(position_mouse)
            cursor_group.draw(self.screen)
            pygame.display.flip()                 
        return        
        
    def base_menu(self,scaled_house_title,current_rect):
        self.screen.fill((0,0,0))
        self.screen.blit(self.shine_title,(self.width / 2 - ((self.width*2249)/3440) / 2, self.height / 2 - ((self.height*2245)/1440) / 2))
        self.screen.blit(self.title, (((self.width*1529)/3440), ((self.height*336.16666666666663)/1440)))
        self.screen.blit(scaled_house_title, current_rect.topleft)
    
    def put_text(self,textos):
        suma = ((self.height*200)/1440)
        for i in textos:
            options = self.type.render(i, True, (255,100,100))
            x_options = self.width/2 - options.get_width()/2
            y_options = self.height/2 - options.get_height()/2 + suma
            self.screen.blit(options, (x_options, y_options))
            suma += (self.height*50)/1440     
        return options
    
    def calculate_paint_house(self,Character):
        if Character.scene != self.scene:
            self.transparence_all_image = 255
            self.image = self.screen.copy()

        x = Character.location[0]
        y = Character.location[1]
        zoom = Character.zoom
        scene = Character.scene
        if scene == 12:
            x+=4
            y+=7
        if scene == 13:
            x-=2
            y-=5        
        # Transformamos la x y la y en valores legibles
        zoom = (self.width*zoom)/3440
        
        if self.zoom > zoom:
            self.zoom -= 0.01
        elif self.zoom < zoom:
            self.zoom += 0.01
        self.zoom = round(self.zoom,2) 
         
        xr = ((self.width*(2033*self.zoom))/3440) + ((x-1)*((self.width*(49*self.zoom))/3440))-((y-1)*((self.width*(49*self.zoom))/3440))
        yr = y*((self.height*(24.5*self.zoom))/1440) + x*((self.height*(24.5*self.zoom))/1440) - ((self.height*(24.5*self.zoom))/1440)
        x = self.width/2 - xr
        y = self.height/2 - yr

        # Escogemos la imagen dependiendo de la escena en la que estamos
        if scene != self.scene:
            self.back = pygame.image.load("ART/SCENE_"+str(scene)+"_BACK.png")
            self.front = pygame.image.load("ART/scene_"+str(scene)+"_FRONT.png")
            self.scene = scene
        if self.y_house - y < 10*self.zoom and self.y_house - y > -10*self.zoom:
            self.y_house = y
        if self.x_house - x < 10*self.zoom and self.x_house - x > -10*self.zoom:
            self.x_house = x 
        if self.x_house > x:
            self.x_house -= ((self.x_house - x))/2
        elif self.x_house < x:
            self.x_house += ((x - self.x_house))/2
        if self.y_house > y:
            self.y_house -= ((self.y_house - y))/2
        elif self.y_house < y:
            self.y_house += ((y - self.y_house))/2
                

                    

        
        # Escalamos todas las imagenes al tamaño de zoom

        self.scene_house_back = pygame.transform.scale(self.back, (int(self.back.get_width() * self.zoom), int(self.back.get_height() * self.zoom)))    
        self.scene_house_front = pygame.transform.scale(self.front, (int(self.front.get_width() * self.zoom), int(self.front.get_height() * self.zoom)))               
        if self.y_house == y and self.x_house == x and self.zoom == zoom and self.transparence_all_image == 0:
            self.first_inititation = False
            return  False
        else:
            return True
               
    def paint_house(self,Character):
        
        # Pintamos el fondo
        self.screen.fill((0,0,0))                

        # Las ponemos en pantalla
        self.screen.blit(self.scene_house_back, (self.x_house,self.y_house))
        self.screen.blit(self.scene_house_front, (self.x_house,self.y_house))
                
        # Pintamos una cruz blanca que tiene como intersección el círculo y que mide 40x40 pixeles
        pygame.draw.line(self.screen, (255,255,255), (int(self.width/2)-(47.6*self.zoom), int(self.height/2)), (int(self.width/2)+(47.6*self.zoom), int(self.height/2)), 2)
        pygame.draw.line(self.screen, (255,255,255), (int(self.width/2), int(self.height/2)-(22*self.zoom)), (int(self.width/2), int(self.height/2)+(22*self.zoom)), 2)
        pygame.draw.line(self.screen, (255,255,255), (int(self.width/2)-(47.6*self.zoom), int(self.height/2)), (int(self.width/2), int(self.height/2)-(22*self.zoom)), 2)
        pygame.draw.line(self.screen, (255,255,255), (int(self.width/2)-(47.6*self.zoom), int(self.height/2)), (int(self.width/2), int(self.height/2)+(22*self.zoom)), 2)
        pygame.draw.line(self.screen, (255,255,255), (int(self.width/2)+(47.6*self.zoom), int(self.height/2)), (int(self.width/2), int(self.height/2)-(22*self.zoom)), 2)
        pygame.draw.line(self.screen, (255,255,255), (int(self.width/2)+(47.6*self.zoom), int(self.height/2)), (int(self.width/2), int(self.height/2)+(22*self.zoom)), 2)
            
        if self.transparence_all_image > 0:
            self.transparence_all_image -= 50
            if self.transparence_all_image < 0:
                self.transparence_all_image = 0
                self.first_inititation = False
            if self.first_inititation == True:
                # Pintamos self.image a su tamaño normal en las posiciones (0,0)
                self.image.set_alpha(self.transparence_all_image)
                self.screen.blit(self.image, (0,0))
            else:    
                # Escalamos la imagen guarada en self.image al tamaño de zoom
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.zoom), int(self.image.get_height() * self.zoom)))
                # Le aplicamos el alfa correspondiente
                self.image.set_alpha(self.transparence_all_image)                
                # Ponemos la imagen en pantalla
                self.screen.blit(self.image, (0,0))
    
                      
        # Actualizamos la pantalla
        pygame.display.flip()
        
        return
                             
    def endImage(self):
        pygame.quit() 
        
class CursorSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, scale_factor):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * scale_factor),
            int(self.image.get_height() * scale_factor)
        ))
        self.rect = self.image.get_rect()

    def update(self, position):
        self.rect.topleft = position