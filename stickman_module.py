import tkinter as tk
import time

TIME_PAUSE = 0.01

SPEED_X = 1
SPEED_Y = 1
SPEED_0 = 0

STEP_COUNT = 25
JUMP_COUNT = 60

PLAYER_WIGHT = 27
PLAYER_HEIGHT = 30

log = []

no_log = True

class Game(tk.Toplevel):
    def __init__(self):

        super().__init__()

        self.score = 0
        self.lvl = 1




        self.title("Добежать до выхода")
        self.config(bg="white")
        self.geometry("500x500")
        self.resizable(False, False)

        self.canvas_height = 500
        self.canvas_width = 500
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, highlightthickness=0)
        self.canvas.pack()


        self.bg = tk.PhotoImage(file='stickman/background.gif')
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x*100, y*100, image=self.bg, anchor='nw')
                self.update()
                time.sleep(0.05)
        self.sprites=[]
        self.running = True
        self.exit = False

    def openFile(self, event):
        file = open(file="score")

        if file is None:
            if no_log == False: log.append("not_a_file_with_score")
            return

        self.filename = file.name


        s=1
        while True:

            line = file.readline()

            if not line:
                break

            if s == 1:
                self.score = line

            if s == 2:
                self.lvl = line

        file.close()







    def on_closing(self):
        self.running = False
        self.exit = True
        self.destroy()

    def game_cycle(self):
        while True:
            self.update_idletasks()

            for sprite in self.sprites:
                sprite.move()

            self.update()
            time.sleep(TIME_PAUSE)

            if not self.running:
                break

        while True:
            self.update_idletasks()
            self.update()

            if self.exit:
                self.destroy()
                break

    def load_sprites(self):
        platfom1 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform2.png"), 40, 480, 66, 10)
        self.sprites.append(platfom1)



        platform2 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform1.png"), 150, 440, 100, 10)
        self.sprites.append(platform2)
        platform3 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform1.png"), 300, 400, 100, 10)
        self.sprites.append(platform3)
        platform4= PlatformSprite(self, tk.PhotoImage(file="stickman/platform1.png"), 300, 160, 100, 10)
        self.sprites.append(platform4)
        platform5 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform2.png"), 175, 350, 66, 10)
        self.sprites.append(platform5)
        platform6 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform2.png"), 50, 300, 66, 10)
        self.sprites.append(platform6)
        platform7 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform1.png"), 150, 110, 100, 10)
        self.sprites.append(platform7)
        platform8 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform2.png"), 45, 60, 66, 10)
        self.sprites.append(platform8)
        platform9 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform3.png"), 170, 250, 32, 10)
        self.sprites.append(platform9)
        platform10 = PlatformSprite(self, tk.PhotoImage(file="stickman/platform3.png"), 230, 200, 32, 10)
        self.sprites.append(platform10)
        door= PlatformSprite(self, tk.PhotoImage(file="stickman/door.gif"), 45, 31, 27, 30)
        self.sprites.append(door)
        player = StickFigureSprite(self)
        self.sprites.append(player)




    def within_x(self, co1, co2):
        if (co2.x1 < co1.x1 < co2.x2) or (co2.x1 < co1.x2 < co2.x2) or (co1.x1 < co2.x1 < co1.x2) or (co1.x1 < co2.x2 < co1.x2):
            return True
        else:
            return False

    def within_y(self, co1, co2):
        if (co2.y1 < co1.y1 < co2.y2) or (co2.y1 < co1.y2 < co2.y2) or (co1.y1 < co2.y1 < co1.y2) or (co1.y1 < co2.y2 < co1.y2):
            return True
        else:
            return False

    def collided_left(self, x, co1, co2):
        if self.within_y(co1, co2):
            x_calc = co1.x1 - x
            if co2.x2 >= x_calc >= co2.x1:
                return True
        return False


    def collided_right(self, x, co1, co2):
        if self.within_y(co1, co2):
            x_calc = co1.x2 + x
            if co2.x1 <= x_calc >= co2.x2:
                return True
        return False


    def collided_top(self, y, co1, co2):
        if self.within_x(co1, co2):
            y_calc = co1.y1 - y
            if co2.y2 >= y_calc >= co2.y1:
                return True
        return False

    def collided_bottom(self, y, co1, co2):
        if self.within_x(co1, co2):
            y_calc = co1.y2 + y
            if co2.y1 <= y_calc <= co2.y2:
                return True
        return False


    def win_game(self):

        self.score += 100

        self.canvas.create_text(250, 250, fill="darkblue", font="Ravie 50 italic bold", text=f"You WIN!!!  \nscore = {self.score}")
        self.running = False





class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def coords(self):


        return self.coordinates

    def move(self):
        pass

class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, wight, height):
        super().__init__(game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
        self.coordinates = Coords(x, y, x + wight, y + height)

class DoorSprite(Sprite):
    def __init__(self, game,photo_image, x, y, wight, height):
        super().__init__(game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
        self.coordinates = Coords(x, y, x + wight, y + height)
        self.endgame = True


class StickFigureSprite(Sprite):
    def __init__(self,game):

        super().__init__(game)
        self.images_left = [tk.PhotoImage(file="stickman/figure-L1.gif"),
                            tk.PhotoImage(file="stickman/figure-L2.gif"),
                            tk.PhotoImage(file="stickman/figure-L3.gif")]

        self.images_right = [tk.PhotoImage(file="stickman/figure-R1.gif"),
                             tk.PhotoImage(file="stickman/figure-R2.gif"),
                             tk.PhotoImage(file="stickman/figure-R3.gif")]

        self.image = game.canvas.create_image(200,470,image=self.images_right[0],anchor='nw')

        self.speed_x = SPEED_0
        self.speed_y = SPEED_0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.step_count = 0
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-a>',self.turn_left)
        game.canvas.bind_all('<KeyPress-d>',self.turn_right)
        game.canvas.bind_all('<space>',self.jump)

    def turn_left(self,event):
        self.speed_x = -SPEED_X
        self.step_count = 0



    def turn_right(self,event):
        self.speed_x = SPEED_X
        self.step_count = 0


    def jump(self,event):
        if self.speed_y == SPEED_0:

            self.speed_y = -SPEED_Y
            self.jump_count = 0
    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + PLAYER_HEIGHT

        self.coordinates.y2 = xy[1] + PLAYER_WIGHT

        return self.coordinates

    def animate(self):
        if self.speed_x != SPEED_0 and self.speed_y == SPEED_0 and self.step_count == 0:
            self.current_image += self.current_image_add
            if self.current_image >= 2:
                self.current_image_add = -1

            if self.current_image <= 0:
                self.current_image_add = 1

        if self.speed_x < SPEED_0:

            if self.speed_y != SPEED_0:
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])

            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])

        elif self.speed_x > SPEED_0:

            if self.speed_y != SPEED_0:
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])

            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])

    def move(self):
        self.animate()

        if self.speed_x:
            self.step_count += 1

            if self.step_count == STEP_COUNT:
                self.speed_x = SPEED_0



        if self.speed_y < SPEED_0:
            self.jump_count += 1

            if self.jump_count > JUMP_COUNT:
                self.speed_y = SPEED_Y
        elif self.speed_y > SPEED_0:
            self.jump_count -= 1

        else:
            self.speed_y = SPEED_Y

        co = self.coords()

        left = True
        right = True
        top = True
        bottom = True

        if self.speed_y > SPEED_0 and co.y2 >= self.game.canvas_height:
            self.speed_y = SPEED_0
            bottom = False

        elif self.speed_y < SPEED_0 and co.y1 <= 0:
            self.speed_y = SPEED_0
            top=False

        if self.speed_x > SPEED_0 and co.x2 >= self.game.canvas_width:
            self.speed_x = SPEED_0
            right = False

        elif self.speed_x < SPEED_0 and co.x1 <= 0:
            self.speed_x = SPEED_0
            left = False


        for sprite in self.game.sprites:
            if sprite is self:
                continue

            sprites_co = sprite.coords()

            if left and self.speed_x < SPEED_0 and self.game.collided_left(self.speed_x, co, sprites_co):
                self.speed_x = sprites_co.x2 - co.x1
                if self.speed_x >= SPEED_0:
                    self.speed_x = SPEED_0
                    left = False
                    if sprite.endgame:
                        self.game.win_game()

            if right and self.speed_x > SPEED_0 and self.game.collided_right(self.speed_x, co, sprites_co):
                self.speed_x = sprites_co.x1 - co.x2
                if self.speed_x <= SPEED_0:
                    self.speed_x = SPEED_0
                    right = False
                    if sprite.endgame:
                        self.game.win_game()

            if top and self.speed_y < SPEED_0 and self.game.collided_top(self.speed_y, co, sprites_co):
                self.speed_y = sprites_co.y2 - co.y1
                if self.speed_y >= SPEED_0:
                    self.speed_y = SPEED_Y
                    top = False
                    if sprite.endgame:
                        self.game.win_game()

            if bottom and self.speed_y > SPEED_0 and self.game.collided_bottom(self.speed_y, co, sprites_co):
                self.speed_y = sprites_co.y1 - co.y2
                if self.speed_y <= SPEED_0:
                    self.speed_y = SPEED_0
                    bottom = False
                    if sprite.endgame:
                        self.game.win_game()
        self.game.canvas.move(self.image, self.speed_x, self.speed_y)






if __name__ == "__main__":
    stickman = Game()
    stickman.load_sprites()
    stickman.game_cycle()

