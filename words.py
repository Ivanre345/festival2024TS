import tkinter as tk



class Poot(tk.Toplevel):
    def __init__(self):


        self.s=0

        self.btn_color='red'
        self.btn_text_color='black'
        self.bg='blue'

        super().__init__()

        self.title("Words")
        self.config(bg=self.bg)
        self.geometry("400x300")
        self.resizable(False, False)

        self.button_click = tk.Button(self, text="Посчитать и отсортировать", width=25, height=1, bg=self.btn_color, fg=self.btn_text_color)
        self.button_click.bind("<Button-1>", self.tap)
        self.button_click.place(relx=0.5, y=250, anchor=tk.CENTER)

        self.lbl_rule1 = tk.Label(self, text="Вводите слова отделяя их пробелами",
                                  fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule1.place(x=20, y=20, anchor=tk.NW)

        self.line_sv = tk.StringVar()
        self.ent_name = tk.Entry(self, textvariable=self.line_sv, fg=self.btn_text_color,
                                 bg="white", width=20)
        self.ent_name.place(x=100, y=140)
        self.line_sv.set("")

        self.mainloop()

    def tap(self, event):
        self.lbl_rule2 = tk.Label(self, text="слов:                      ",fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule2.place(relx=0.5, y=50, anchor=tk.NW)

        self.lbl_rule3 = tk.Label(self, text="слова отсортированные по длинне:                       ",fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule3.place(relx=0.1, y=100, anchor=tk.NW)
        s = ""
        s=self.line_sv.get()

        d=s.count(" ")
        self.line_sv.set("")
        s = s.split(" ")

        s.sort(key=len)


        self.lbl_rule2 = tk.Label(self, text="слов: {}".format(d+1),
                                  fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule2.place(relx=0.5, y=50, anchor=tk.NW)

        self.lbl_rule3 = tk.Label(self, text="слова отсортированные по длинне: {}".format(" ".join(s)),
                                  fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule3.place(relx=0.1, y=100, anchor=tk.NW)
        print(self.line_sv.get())





if __name__ == "__main__":
    phones = Poot()



