import Phone_book_module
import clicker
import collage
import main
import stickman_module
import DEV_ii
import words
import poisk
from Phone_book_module import *



class Hubofmyproject(tk.Tk):
    def __init__(self):
        super().__init__()

        self.appsopen = False
        self.devopen = False

        self.python_image = tk.PhotoImage(file="LOGOS/back_ground1.png")

        self.title("Хаб")
        self.config(bg="white")
        self.geometry("900x600")
        self.resizable(False, False)

        self.mycanvas = tk.Canvas(self, width=900, height=600, highlightthickness=0)
        self.mycanvas.create_image(0, 0, anchor=tk.NW, image=self.python_image)
        self.mycanvas.pack()

        self.button_image = tk.PhotoImage(file="LOGOS/кнопка.png")
        self.hub_button = tk.Button(image=self.button_image, highlightthickness=-1, bd=-1)
        self.hub_button.bind("<Button-1>", self.apps)
        self.mycanvas.create_window(450, 300, anchor=tk.CENTER, window=self.hub_button)

        self.button_image_INFO = tk.PhotoImage(file="LOGOS/Info_logo.png")
        self.DEV_button = tk.Button(image=self.button_image_INFO, highlightthickness=-1, bd=-1)
        self.DEV_button.bind("<Button-1>", self.DEV)
        self.mycanvas.create_window(650, 300, anchor=tk.CENTER, window=self.DEV_button)




        self.mainloop()

    def apps(self, event):
        if self.appsopen == False:
            self.appsopen = True

            self.appsw = tk.Toplevel()
            self.appsw.config(bg="white")
            self.appsw.title("Приложения")
            self.appsw.geometry("400x400")
            self.appsw.resizable(False, False)

            self.appscanvas = tk.Canvas(self.appsw, width=400, height=400, highlightthickness=0)
            self.appscanvas.create_image(0, 0, anchor=tk.NW, image=self.python_image)
            self.appscanvas.pack()

            self.appsw.protocol("WM_DELETE_WINDOW", self.on_closing_appsw)

            self.button_image_PHONE_BOOK = tk.PhotoImage(file="LOGOS/кнопка_PHONE_BOOK.png")
            self.button_PHONE_BOOK = tk.Button(self.appsw, image=self.button_image_PHONE_BOOK, highlightthickness=0,
                                               bd=0)
            self.button_PHONE_BOOK.bind("<Button-1>", self.phone_book)
            self.appscanvas.create_window(1, 1, anchor=tk.NW, window=self.button_PHONE_BOOK, width=100, height=100)

            self.button_image_STICKMAN = tk.PhotoImage(file="LOGOS/button_STICKMAN.png")
            self.button_STICKMAN = tk.Button(self.appsw, image=self.button_image_STICKMAN, highlightthickness=0, bd=0)
            self.button_STICKMAN.bind("<Button-1>", self.stickman)
            self.appscanvas.create_window(100, 1, anchor=tk.NW, window=self.button_STICKMAN, width=100, height=100)

            self.button_image_COLLAGE = tk.PhotoImage(file="LOGOS/collage_logo.png")
            self.button_COLLAGE = tk.Button(self.appsw, image=self.button_image_COLLAGE, highlightthickness=0, bd=0)
            self.button_COLLAGE.bind("<Button-1>", self.collage)
            self.appscanvas.create_window(200, 1, anchor=tk.NW, window=self.button_COLLAGE, width=100, height=100)

            self.button_image_WORDS = tk.PhotoImage(file="LOGOS/collage_logo.png")
            self.button_WORDS = tk.Button(self.appsw, image=self.button_image_WORDS, highlightthickness=0, bd=0)
            self.button_WORDS.bind("<Button-1>", self.words)
            self.appscanvas.create_window(300, 1, anchor=tk.NW, window=self.button_WORDS, width=100, height=100)

            self.button_image_CLICKER = tk.PhotoImage(file="LOGOS/collage_logo.png")
            self.button_CLICKER = tk.Button(self.appsw, image=self.button_image_CLICKER, highlightthickness=0, bd=0)
            self.button_CLICKER.bind("<Button-1>", self.clicker)
            self.appscanvas.create_window(1, 101, anchor=tk.NW, window=self.button_CLICKER, width=100, height=100)

            self.button_image_CUBES = tk.PhotoImage(file="LOGOS/CUBES_LOGO.png")
            self.button_CUBES = tk.Button(self.appsw, image=self.button_image_CUBES, highlightthickness=0, bd=0)
            self.button_CUBES.bind("<Button-1>", self.cubes)
            self.appscanvas.create_window(100, 101, anchor=tk.NW, window=self.button_CUBES, width=100, height=100)

            self.button_image_GOOGLE = tk.PhotoImage(file="LOGOS/GOOGLE.png")
            self.button_GOOGLE = tk.Button(self.appsw, image=self.button_image_GOOGLE, highlightthickness=0, bd=0)
            self.button_GOOGLE.bind("<Button-1>", self.google)
            self.appscanvas.create_window(200, 101, anchor=tk.NW, window=self.button_GOOGLE, width=100, height=100)

            self.button_image_GOOGLE = tk.PhotoImage(file="LOGOS/GOOGLE.png")
            self.button_GOOGLE = tk.Button(self.appsw, image=self.button_image_GOOGLE, highlightthickness=0, bd=0)
            self.button_GOOGLE.bind("<Button-1>", self.google)
            self.appscanvas.create_window(200, 101, anchor=tk.NW, window=self.button_GOOGLE, width=100, height=100)

            self.appsw.mainloop()

    def on_closing_appsw(self):
        self.appsopen = False
        self.appsw.destroy()

    def phone_book(self, event):
        phonebook_APP = Phone_book_module.PhoneBook()

    def stickman(self, event):
        stickman_APP = stickman_module.Game()

        stickman_APP.load_sprites()
        stickman_APP.game_cycle()

    def collage(self, event):
        collage_APP = collage.Collage()

    def words(self, event):
        words_APP = words.Poot()

    def clicker(self, event):
        clicker_APP = clicker.Poot()

    def cubes(self, event):
        cubes_APP = main.NewGame()
        cubes_APP.game_cycle()

    def google(self, event):
        googlest = poisk.Search
        googlest.search(googlest)

    def DEV(self, event):
        if self.devopen == False:
            self.devopen = True
            self.appdw = tk.Toplevel()
            self.appdw.config(bg="white")
            self.appdw.title("Информация")
            self.appdw.geometry("200x100")
            self.appdw.resizable(False, False)

            self.appdw.protocol("WM_DELETE_WINDOW", self.on_closing_appdw)

            self.button_image_DEV = tk.PhotoImage(file="LOGOS/DEVEL.png")
            self.buttondevinI = tk.Button(self.appdw, image=self.button_image_DEV, highlightthickness=0, bd=0, command=self.DEV_git)
            self.buttondevinI.place(x=0, y=0, anchor=tk.NW)
            self.AUTHORS_logo = tk.PhotoImage(file="LOGOS/Authors_logo.png")
            self.buttonauthorsinI = tk.Button(self.appdw,image=self.AUTHORS_logo, highlightthickness=0, bd=0,command=self.autors)
            self.buttonauthorsinI.place(x=100, y=0, anchor=tk.NW)


    def DEV_git(self):
        dev_ii = DEV_ii.Git()
        dev_ii.search()
    def on_closing_appdw(self):
        self.devopen = False
        self.appdw.destroy()
    def autors(self):
        pass



if __name__ == "__main__":
    window1 = Hubofmyproject()
