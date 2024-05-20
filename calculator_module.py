import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):

        self.numbers = []
        self.calculate = []
        self.primer = []

        super().__init__()


        self.bg_color_c = tk.StringVar()
        self.bg_color_c.set("white")

        self.font_color_c = tk.StringVar()
        self.font_color_c.set("black")

        self.btn_text_color_c = tk.StringVar()
        self.btn_text_color_c.set("white")

        self.btn_color_c = tk.StringVar()
        self.btn_color_c.set("green")

        self.ent_text_color_c = tk.StringVar()
        self.ent_text_color_c.set("dark green")

        self.ent_color_c = tk.StringVar()
        self.ent_color_c.set("white")


        self.title("Калькулятор")
        self.config(bg=self.bg_color_c.get())
        self.geometry("205x500")
        self.resizable(False, False)

        self.primer = tk.StringVar()
        self.text_res = tk.Entry(self, textvariable=self.primer, bd=5, fg="black", bg="white" )
        self.text_res.place(relx=0, y=0, anchor=tk.NW, width=205, height=250)
        self.text_res.icursor(0)
        self.primer.set("")


        self.buttons()

        self.mainloop()



    def buttons(self):
        self.button1 = tk.Button(self, text="1", width=5, height=2, bg=self.btn_color_c.get(), fg=self.btn_text_color_c.get())
        self.button1.bind("<Button-1>", self.c_1)
        self.button1.place(x=3.5, y=450, anchor=tk.SW)

        self.button2 = tk.Button(self, text="2", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button2.bind("<Button-1>", self.c_2)
        self.button2.place(x=52.5, y=450, anchor=tk.SW)


        self.buttc_3 = tk.Button(self, text="3", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.buttc_3.bind("<Button-1>", self.c_3)
        self.buttc_3.place(x=101.5, y=450, anchor=tk.SW)



        self.button4 = tk.Button(self, text="4", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button4.bind("<Button-1>", self.c_4)
        self.button4.place(x=3.5, y=400, anchor=tk.SW)



        self.button5 = tk.Button(self, text="5", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button5.bind("<Button-1>", self.c_5)
        self.button5.place(x=52.5, y=400, anchor=tk.SW)


        self.button6 = tk.Button(self, text="6", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button6.bind("<Button-1>", self.c_6)
        self.button6.place(x=101.5, y=400, anchor=tk.SW)


        self.button7 = tk.Button(self, text="7", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button7.bind("<Button-1>", self.c_7)
        self.button7.place(x=3.5, y=350, anchor=tk.SW)


        self.button8 = tk.Button(self, text="8", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button8.bind("<Button-1>", self.c_8)
        self.button8.place(x=52.5, y=350, anchor=tk.SW)


        self.button9 = tk.Button(self, text="9", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button9.bind("<Button-1>", self.c_9)
        self.button9.place(x=101.5, y=350, anchor=tk.SW)


        self.button0 = tk.Button(self, text="0", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button0.bind("<Button-1>", self.c_0)
        self.button0.place(x=52.5, y=498.375, anchor=tk.SW)

        self.button_float = tk.Button(self, text=",", width=5, height=2, bg=self.btn_color_c.get(),
                                 fg=self.btn_text_color_c.get())
        self.button_float.bind("<Button-1>", self.c_float)
        self.button_float.place(x=101.5, y=498.375, anchor=tk.SW)

        self.button_plusminus = tk.Button(self, text="+/-", width=5, height=2, bg=self.btn_color_c.get(),
                                      fg=self.btn_text_color_c.get())
        self.button_plusminus.bind("<Button-1>", self.c_plusminus)
        self.button_plusminus.place(x=3.5, y=498.375, anchor=tk.SW)

        self.button_ravno = tk.Button(self, text="=", width=5, height=2, bg=self.btn_color_c.get(),
                                          fg=self.btn_text_color_c.get())
        self.button_ravno.bind("<Button-1>", self.c_ravno)
        self.button_ravno.place(x=154, y=498.375, anchor=tk.SW)

        self.button_plus = tk.Button(self, text="+", width=5, height=2, bg=self.btn_color_c.get(),
                                      fg=self.btn_text_color_c.get())
        self.button_plus.bind("<Button-1>", self.c_plus)
        self.button_plus.place(x=154, rely=0.9, anchor=tk.SW)

        self.button_minus = tk.Button(self, text="-", width=5, height=2, bg=self.btn_color_c.get(),
                                     fg=self.btn_text_color_c.get())
        self.button_minus.bind("<Button-1>", self.c_minus)
        self.button_minus.place(x=154, y=400, anchor=tk.SW)

        self.button_umn = tk.Button(self, text="*", width=5, height=2, bg=self.btn_color_c.get(),
                                      fg=self.btn_text_color_c.get())
        self.button_umn.bind("<Button-1>", self.c_umn)
        self.button_umn.place(x=154, y=350, anchor=tk.SW)

    def c_1(self, event):
        self.text_res.insert("1")

    def c_2(self, event):
        self.text_res.insert("2")

    def c_3(self, event):
        self.text_res.insert("3")

    def c_4(self, event):
        self.text_res.insert("4")

    def c_5(self, event):
        self.text_res.insert("5")

    def c_6(self, event):
        self.text_res.insert("6")

    def c_7(self, event):
        self.text_res.insert("7")

    def c_8(self, event):
        self.text_res.insert("8")

    def c_9(self, event):
        self.text_res.insert("9")
    def c_0(self, event):
        self.text_res.insert("0")

    def c_float(self, event):
        pass

    def c_plusminus(self, event):
        pass

    def c_ravno(self, event):
        pass

    def c_plus(self, event):
        pass

    def c_minus(self, event):
        pass

    def c_umn(self, event):
        pass






if __name__ == "__main__":
    m_c = Calculator()