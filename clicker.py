import tkinter as tk
import tkinter.filedialog as fd

class Poot(tk.Toplevel):
    def __init__(self):


        self.taps=0

        self.btn_color='green'
        self.btn_text_color='black'
        self.bg='white'

        super().__init__()

        self.title("Clicker")
        self.config(bg=self.bg)
        self.geometry("400x300")
        self.resizable(False, False)

        self.button_click=tk.Button(self, text="Нажми", width=20, height=1, bg=self.btn_color, fg=self.btn_text_color)
        self.button_click.bind("<Button-1>", self.tap)
        self.button_click.place(relx=0.5, y=250, anchor=tk.CENTER)

        self.lbl_rule1 = tk.Label(self, text="Нажатий:",
                                  fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule1.place(x=20, y=20, anchor=tk.NW)

        self.lbl_rule2 = tk.Label(self, text=self.taps,
                                  fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule2.place(relx=0.5, y=20, anchor=tk.NW)

        self.mainloop()

    def tap(self, event):
        self.taps+=1

        self.lbl_rule2 = tk.Label(self, text=self.taps,
                                  fg=self.btn_text_color, bg=self.bg)
        self.lbl_rule2.place(relx=0.5, y=20, anchor=tk.NW)


if __name__ == "__main__":
    phones = Poot()



