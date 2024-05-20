import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLAYER_SPEEDY = 5
PLAYER_SPEEDX = 5
PLAYER_SPEED0 = 0
class NewGame():
    def __init__(self):
        self.game_over = False
        self.cube_hits = False
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/bg_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over.mp3")
        self.game_over_sound.set_volume(1)
        self.hit_cubes_sound = pygame.mixer.Sound("sounds/hit_cubes.mp3")
        self.hit_cubes_sound.set_volume(0.2)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("GTA VII")
        self.clock = pygame.time.Clock()
        self.cube_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.running = True
        self.cube_player = Cubeplayer(self, GREEN, WIDTH / 2, HEIGHT / 2)
        self.player_group.add(self.cube_player)

        self.cube2 = Cubebots(self, WHITE, WIDTH / 2, HEIGHT / 3, 8, 1)
        self.cube_sprites.add(self.cube2)

        self.cube3 = Cubebots(self, RED, WIDTH / 3, HEIGHT / 4, 5, 5)
        self.cube_sprites.add(self.cube3)
        self.tt = Score(self.screen)
        self.tt2 = CountDown(self.screen)

    def game_cycle(self):





        while self.running == True:
            self.clock.tick(FPS)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


                if pygame.key.get_pressed()[pygame.K_w] == True:
                    self.cube_player.speed_y = -PLAYER_SPEEDY
                elif pygame.key.get_pressed()[pygame.K_s] == True:
                    self.cube_player.speed_y = PLAYER_SPEEDY
                else:
                    self.cube_player.speed_y = PLAYER_SPEED0

                if pygame.key.get_pressed()[pygame.K_d] == True:
                    self.cube_player.speed_x = PLAYER_SPEEDX
                elif pygame.key.get_pressed()[pygame.K_a] == True:
                    self.cube_player.speed_x = -PLAYER_SPEEDX
                else:
                    self.cube_player.speed_x = PLAYER_SPEED0
                if pygame.key.get_pressed()[pygame.K_k] == True:
                    self.game_over = True




            if  self.cube_hits:
                self.hit_cubes_sound.play(0)
                self.cube_hits = False

            if not self.game_over:
                self.tt2.update()

                if self.tt2.score < 0:
                    self.cube_sprites.update()
                    self.player_group.update()

                    self.tt.update()




                self.screen.fill(BLUE)



                if self.game_over == True:
                    pygame.mixer.music.pause()
                    self.game_over_sound.play()


            else:
                self.screen.fill(RED)
            self.cube_sprites.draw(self.screen)
            self.player_group.draw(self.screen)

            self.tt.draw()
            self.tt2.draw()
            pygame.display.flip()



        pygame.quit()


class Cube(pygame.sprite.Sprite):
    def __init__(self, new_game, color, pos_x, pos_y, speed_x=0, speed_y=0):
        self.color = color
        self.new_game = new_game
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.pos_y = pos_y
        self.pos_x = pos_x
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
       pass

class Cubebots(Cube):
    def update(self):


        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speed_x = -self.speed_x

        elif self.rect.left < 0:
            self.rect.left = 0
            self.speed_x = -self.speed_x



        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_y = -self.speed_y



        elif self.rect.top < 0:
            self.rect.top = 0
            self.speed_y = -self.speed_y
        self.check_collision()

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y




    def check_collision(self):
        coll_list = pygame.sprite.spritecollide(self, self.new_game.cube_sprites, dokill=False)
        for sprite in coll_list:
            if sprite == self:
                continue


            top = False
            bottom = False
            left = False
            right = False

            cross_y = 0
            cross_x = 0

            if sprite.rect.bottom >= self.rect.top >= sprite.rect.top:
                top = True
            if sprite.rect.bottom >= self.rect.bottom >= sprite.rect.top:
                bottom = True
            if sprite.rect.right >= self.rect.left >= sprite.rect.left:
                left = True
            if sprite.rect.right >= self.rect.right >= sprite.rect.left:
                right = True

            if top and bottom:
                cross_y = self.rect.height
            elif top:
                cross_y = sprite.rect.bottom-self.rect.top
            elif bottom:
                cross_y = self.rect.bottom-sprite.rect.top

            if left and right:
                cross_x = self.rect.width
            elif top:
                cross_x = sprite.rect.right-self.rect.left
            elif bottom:
                cross_x = self.rect.right-sprite.rect.left

            if cross_x > cross_y:
                self.speed_y = -self.speed_y
            elif cross_x < cross_y:
                self.speed_x = -self.speed_x
            else:
                self.speed_x = -self.speed_x
                self.speed_y = -self.speed_y
            self.new_game.hit_cubes = True

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y





class Cubeplayer(Cube):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speed_x = 0

        elif self.rect.left < 0:
            self.rect.left = 0
            self.speed_x = 0



        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_y = 0



        elif self.rect.top < 0:
            self.rect.top = 0
            self.speed_y = 0
        self.check_collision()

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, self.new_game.cube_sprites) is not None:

            self.new_game.game_over = True

class Score():
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.sec_counter = 0
        self.sc_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.update_counter = 0

    def draw(self):
        sc_font_surface = self.sc_font.render(str(self.score), True, WHITE)
        sc_rect = sc_font_surface.get_rect()
        sc_rect.topleft = (10,0)
        self.screen.blit(sc_font_surface, sc_rect.topleft)
    def update(self):
        self.update_counter+=1
        if self.update_counter == FPS:
            self.update_counter = 0
            self.score += 1


class CountDown():
    def __init__(self, screen):
        self.screen = screen
        self.score = 5
        self.sec_counter = 0
        self.sc_font = pygame.font.SysFont('Comic Sans MS', 100)
        self.update_counter = 0

    def draw(self):
        if self.score >= 0:
            sc_font_surface = self.sc_font.render(str(self.score), True, RED)
            sc_rect = sc_font_surface.get_rect()
            sc_rect.midbottom = ( WIDTH / 2 , HEIGHT / 2)
            self.screen.blit(sc_font_surface, sc_rect.topleft)

    def update(self):
        if self.score >= 0:
            self.update_counter += 1
            if self.update_counter == FPS:
                self.update_counter = 0
                self.score -= 1















if __name__ == "__main__":
    game = NewGame()
    game.game_cycle()