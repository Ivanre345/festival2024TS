import tkinter as tk
from tkinter import Spinbox
from tkinter import filedialog
from PIL import Image


class Collage(tk.Toplevel):
    def __init__(self):
        self.x_p = 100
        self.fotos = {}
        self.y_p = 0
        self.btns = []
        self.photos = []
        self.n = 1
        self.f = 0
        self.collage_size = (100, 100)
        super().__init__()
        self.bg_color_c = "Blue"
        self.title("Создать коллаж")
        self.geometry("500x500")
        self.config(bg=self.bg_color_c)
        self.resizable(False, False)
        self.button = tk.Button(self, text="Выбрать фото", width=10, height=5, command=self.open, bg="Gray")
        self.button.place(x=0, y=0)

        self.button2 = tk.Button(self, text="Сохранить", width=10, height=5, command=self.create_collage, bg="Gray")
        self.button2.place(x=400, y=400)
        self.var1 = tk.IntVar()
        self.var1.set(1080)
        self.spin1 = Spinbox(self, from_=100, to=1080, width=5, textvariable=self.var1)
        self.spin1.grid(column=5, row=10)
        self.spin1.place(relx=0.001, y=490, anchor=tk.SW)
        self.lbl_rule1 = tk.Label(self, text="Ширина:",
                                  fg="Black", bg=self.bg_color_c)
        self.lbl_rule1.place(y=430, relx=0.001, anchor=tk.SW)
        self.lbl_rule2 = tk.Label(self, text="Высота:",
                                  fg="Black", bg=self.bg_color_c)
        self.lbl_rule2.place(y=470, relx=0.001, anchor=tk.SW)
        self.var2 = tk.IntVar()
        self.var2.set(1920)
        self.spin2 = Spinbox(self, from_=100, to=1920, width=5, textvariable=self.var2)
        self.spin2.grid(column=5, row=10)
        self.spin2.place(relx= 0.001, y=450, anchor=tk.SW)


        self.mainloop()






    def open(self):

        file_path = filedialog.askopenfile(title="Выберите фотографию")







        if file_path:
            self.photos.append(file_path.name)

            if self.f < len(self.photos):
                tk.Button(self, text="фото" + str(self.n), bg="#FFF",font=("Times New Roman", 15),command=self.foto_show).place(x=self.x_p, y=self.y_p,width=115,height=79)
                self.x_p += 150
                self.fotos["фото"+str(self.n)] = file_path.name

                if self.x_p >500:
                    self.x_p = 0
                    self.y_p+= 100
                self.f+=1
                self.n+=1


    def foto_show(self, event):
        self.fotos[event.widget.cget('text')].show()

    def create_collage(self):
        # op = []
        # for i in range(len(self.photos)):
        #     t = Image.open(self.photos[i])
        #
        #     op.append([t.height, t.width])
        #



        collage_size = (self.var2.get(),self.var1.get())
        images = self.photos
        collage = Image.new('RGB', collage_size)

        image_width, image_height = collage_size[0] // len(images), collage_size[1]

        x_offset = 0
        for img_path in images:
            img = Image.open(img_path)
            img = img.resize((image_width, image_height))

            collage.paste(img, (x_offset, 0))
            x_offset += image_width

        collage.save(f"collage{self.n}.png")
        collage.show()






if __name__ == "__main__":
    s = Collage()