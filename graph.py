import pygame

import languaje

class image:
    
    def __init__(self,languaje = 0):
        pygame.init()
        pygame.mixer.init()
        
        screen_info =               pygame.display.Info()
        self.width, self.height =   screen_info.current_w, screen_info.current_h
        self.height =               (self.width*1440)/3440
        self.screen =               pygame.display.set_mode((self.width, self.height),)
        pygame.display.set_caption("NOLD")
        
        # idioma 0 = castellano, 1 = catalán, 2 = inglés, 3 = gallego, 4 = euskera, 5 = francés, 6 = alemán, 7 = italiano, 8 = portugués, 9 = aragonés, 10 = extremeño, 11 = asturiano, 12 = aranés
        self.language = languaje
        
        self.house_title =          pygame.image.load("ART/HOUSE_TITLE.png")
        self.shine_title =          pygame.image.load("ART/SHINE_TITLE.png")
        self.title =                pygame.image.load("ART/TITLE.png")
        self.title =                pygame.transform.scale(self.title, (int(self.title.get_width()/4), int(self.title.get_height()/4)))

        self.cursor =               pygame.image.load("ART/CURSOR_ARROW.png")
        self.cursor =               pygame.transform.scale(self.cursor, (int(self.cursor.get_width()/5), int(self.cursor.get_height()/5)))
        self.blood_title =          pygame.image.load("ART/BLOOD_TITLE.png")
        self.blood_title =          pygame.transform.scale(self.blood_title, (600,50))              
        self.type =                 pygame.font.Font("ART/typeg.ttf", 50)
        
        self.sound_title =          pygame.mixer.Sound("ART/MENU_SOUND.wav")
        self.sound_click =          pygame.mixer.Sound("ART/CLICK_SOUND.wav")
        
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
        y_title = self.height/2 - self.title.get_height()/6
        
        for i in range(120):
            self.screen.fill((0,0,0))
            self.screen.blit(self.title, (x_title,y_title))
            self.screen.blit(scaled_house_title, current_rect.topleft)
            pygame.display.flip()
            y_title -= 3
            pygame.time.delay(10)   
        
        textos = languaje.languaje_menu(self.language)
        
        for a in range(0,255,4):    
            self.screen.fill((0,0,0))
            self.screen.blit(self.title, (x_title,y_title))
            self.screen.blit(scaled_house_title, current_rect.topleft)
            suma = 200
            for i in textos:
                options = self.type.render(i, True, (255,100,100))
                x_options = self.width/2 - options.get_width()/2
                y_options = self.height/2 - options.get_height()/2 + suma
                options.set_alpha(a)
                self.screen.blit(options, (x_options, y_options))
                suma += 50
            pygame.display.flip()
            pygame.time.delay(10)
        
        alpha= 0
        into_menu = True

        while into_menu:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    position_mouse = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position_mouse = event.pos
                    if position_mouse[0] > self.width/2 - self.title.get_width()/2 and position_mouse[0] < self.width/2 + self.title.get_width()/2:
                        self.sound_click.play()
                        control_position = 200
                        for possibilities in range(5):
                            if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + 50:
                                
                                if possibilities == 0:
                                    return 1
                                
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
                                    return 3
                                
                                elif possibilities == 4:
                                    into_menu = False
                                    break
                            
                            control_position += 50
            if alpha < 255:
                alpha += 4
                self.shine_title.set_alpha(alpha)
            elif alpha > 255:
                alpha = 255
                self.shine_title.set_alpha(alpha)
            
            self.base_menu(scaled_house_title,current_rect)

            if position_mouse[0] > self.width/2 - self.title.get_width()/2 and position_mouse[0] < self.width/2 + self.title.get_width()/2:
                control_position = 200
                for possibilities in range(5):
                    if position_mouse[1] > self.height/2 - options.get_height()/2 + control_position and position_mouse[1] < self.height/2 - options.get_height()/2 + control_position + 50:
                        self.screen.blit(self.blood_title, (self.width/2 - self.title.get_width()/2 - 120,self.height/2 - options.get_height()/2 + control_position+10))
                    control_position += 50
           
            suma = 200
            textos = languaje.languaje_menu(self.language)
            for i in textos:
                options = self.type.render(i, True, (255,100,100))
                x_options = self.width/2 - options.get_width()/2
                y_options = self.height/2 - options.get_height()/2 + suma
                self.screen.blit(options, (x_options, y_options))
                suma += 50
            
            self.screen.blit(self.cursor, position_mouse)
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
        
        into_difficulty = True
        while into_difficulty:
            for event in pygame.event.get():
                            if event.type == pygame.MOUSEMOTION:
                                position_mouse = event.pos
                                
            self.base_menu(scaled_house_title,current_rect)
            
            suma = 200
            textos = languaje.languaje_difficulty(self.language)
            count = 0
            for i in textos:
                if count >1 and count < 9:
                    text = (i+" : "+ str(difficulty[count-2]))
                else:
                    text = i
                options = self.type.render(text, True, (255,100,100))
                x_options = self.width/2 - options.get_width()/2
                y_options = self.height/2 - options.get_height()/2 + suma
                self.screen.blit(options, (x_options, y_options))
                suma += 45
                count += 1
                
            self.screen.blit(self.cursor, position_mouse)
            pygame.display.flip() 
            
        return       
    
    def base_menu(self,scaled_house_title,current_rect):
        self.screen.fill((0,0,0))
        self.screen.blit(self.shine_title,(self.width / 2 - 2249 / 2, self.height / 2 - 2245 / 2))
        self.screen.blit(self.title, (1529.0, 336.16666666666663))
        self.screen.blit(scaled_house_title, current_rect.topleft)
                              
    def endImage(self):
        pygame.quit() 
        
   