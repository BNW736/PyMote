import pygame as pg

class GameState:
    def starts(self,start):
       
        if start==1:
            pg.init()
            self.width = 800
            self.height = 800
            self.p_size = 50
            self.speed = 5
            self.RED = (255, 0, 0)
        
            # Player starting coordinates
            self.x_p = self.width // 2
            self.y_p = self.height // 2
        
            self.screen = pg.display.set_mode((self.width, self.height))
        elif start == 2:
            pg.quit()
        else :
            print("game has not started")

    def play(self, key):
        pg.event.pump()

        # 3. Move the player based on the key
        if key == 0:
            self.x_p += self.speed
        elif key == 1:
            self.x_p -= self.speed
        elif key == 2:
            self.y_p += self.speed
        elif key == 3:
            self.y_p -= self.speed

        # 4. Boundary checks
        if self.x_p < 0: self.x_p = 0
        if self.y_p < 0: self.y_p = 0
        if self.x_p > self.width - self.p_size: self.x_p = self.width - self.p_size
        if self.y_p > self.height - self.p_size: self.y_p = self.height - self.p_size

    
        self.screen.fill((0, 0, 0))
       
        pg.draw.rect(self.screen, self.RED, (self.x_p, self.y_p, self.p_size, self.p_size))
        pg.display.flip()


my_game = GameState()