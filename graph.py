import pygame

import languaje

class image:
    
    def __init__(self,languaje = 0):
        pygame.init()
        pygame.mixer.init()
        
        screen_info =               pygame.display.Info()
        self.width =                screen_info.current_w
        
        # self.width = 1000
        self.height =               (self.width*1440)/3440
        
        self.screen =               pygame.display.set_mode((self.width, self.height),)
        pygame.display.set_caption("NOLD")
        
        self.language = languaje
        
        self.house_title =          pygame.image.load("ART/HOUSE_TITLE.png")
        self.house_title =          pygame.transform.scale(self.house_title, (int((self.width*1909)/3440), int((self.height*835)/1440)))  
        self.shine_title =          pygame.image.load("ART/SHINE_TITLE.png")
        self.shine_title =          pygame.transform.scale(self.shine_title, (int((self.width*2249)/3440), int((self.height*2245)/1440)))
        self.title =                pygame.image.load("ART/TITLE.png")
        self.title =                pygame.transform.scale(self.title, (int((self.width*(1529/4))/3440), int((self.height*(572/4))/1440)))
        
        self.cursor_sprite = CursorSprite("ART/CURSOR_ARROW.png", ((self.width*0.2)/3440))

        self.blood_title =          pygame.image.load("ART/BLOOD_TITLE.png")
        self.blood_title =          pygame.transform.scale(self.blood_title, (int((self.width*600)/3440),int((self.height*50)/1440)))      
        self.blood_diffic =         pygame.image.load("ART/BLOOD_DIFFIC.png")
        self.blood_diffic =         pygame.transform.scale(self.blood_diffic, (int((self.width*80)/3440),int((self.height*80)/1440)))
                
        self.type =                 pygame.font.Font("ART/typeg.ttf", int((self.width*50)/3440))
        
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
                                            if possibilities == 2 and difficulty[possibilities] > 28:
                                                difficulty[possibilities] = 28
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