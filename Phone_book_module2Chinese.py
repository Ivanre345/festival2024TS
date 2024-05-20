import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.filedialog as fd


# from PIL import ImageTk, Image


class PhoneBook(tk.Tk):
    def __init__(self):
        self.phone_book = []


        self.tel = "телефон"
        self.fam = "фамилия"
        self.im9 = "имя"
        self.ot4 = "отчество"

        self.town = "город"
        self.street = "улица"
        self.house = "дом"
        self.kw = "квартира"

        self.ui = 0

        self.newwopto = False
        self.delitto = False

        self.filename = ""

        self.rester = ""

        super().__init__()

        self.bg_color = tk.StringVar()
        self.bg_color.set("bisque")

        self.font_color = tk.StringVar()
        self.font_color.set("black")

        self.btn_text_color = tk.StringVar()
        self.btn_text_color.set("white")

        self.btn_color = tk.StringVar()
        self.btn_color.set("green")

        self.ent_text_color = tk.StringVar()
        self.ent_text_color.set("dark green")

        self.ent_color = tk.StringVar()
        self.ent_color.set("white")



        self.title("Телофонная книга")
        self.config(bg=self.bg_color.get())
        self.geometry("1000x710")
        self.resizable(False, False)

        # Надписи
        # Первая надпись
        self.lbl_rule1 = tk.Label(self, text="搜索可以通过电话号码、全名或任意组合进行。",
                                  fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_rule1.place(x=20, y=20, anchor=tk.NW)

        self.lbl_rule2 = tk.Label(self, text="如果不需要参数，请将其留空。",
                                  fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_rule2.place(x=20, y=40, anchor=tk.NW)

        # "Фамилия"
        self.lbl_fam = tk.Label(self, text="姓", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_fam.place(x=20, y=110, anchor=tk.NW)
      # Имя
        self.lbl_name = tk.Label(self, text="姓名", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_name.place(x=20, y=140, anchor=tk.NW)

        # Отчество
        self.lbl_ot4 = tk.Label(self, text="Nothing", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_ot4.place(x=20, y=170, anchor=tk.NW)

        # Телефон

        self.lbl_tel = tk.Label(self, text="电话号码", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_tel.place(x=20, y=200, anchor=tk.NW)

        # город
        self.lbl_town = tk.Label(self, text="城市", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_town.place(x=20, y=230, anchor=tk.NW)

        # Улица
        self.lbl_street = tk.Label(self, text="街道 ", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_street.place(x=20, y=260, anchor=tk.NW)

        # "Дом
        self.lbl_home = tk.Label(self, text="房子", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_home.place(x=20, y=290, anchor=tk.NW)

        # "Квартира
        self.lbl_appartament = tk.Label(self, text="公寓", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_appartament.place(x=20, y=320, anchor=tk.NW)

        # кнопки

        # Кнопка Загрузить файл
        self.btn_file = tk.Button(self, text="上传文件", width=20, height=1, bg=self.btn_color.get(),
                                  fg=self.btn_text_color.get())
        self.btn_file.bind("<Button-1>", self.openFile)
        self.btn_file.place(relx=0.10, y=690, anchor=tk.CENTER)

        # Кнопка Очистка ввода

        self.btn_clear_inp = tk.Button(self, text="清除输入", width=20, height=1, bg=self.btn_color.get(),
                                       fg=self.btn_text_color.get())
        self.btn_clear_inp.bind("<Button-1>", self.clear_inputs)
        self.btn_clear_inp.place(relx=0.27, y=690, anchor=tk.CENTER)

        # Кнопка Очистить результат

        self.btn_clear_res = tk.Button(self, text="结果清晰", width=20, height=1, bg=self.btn_color.get(),
                                       fg=self.btn_text_color.get())
        self.btn_clear_res.bind("<Button-1>", self.clear_res)
        self.btn_clear_res.place(relx=0.44, y=690, anchor=tk.CENTER)

        # Кнопка создать

        self.btn_new = tk.Button(self, text="创建联系人", width=20, height=1, bg=self.btn_color.get(),
                                 fg=self.btn_text_color.get(), state=tk.DISABLED)
        self.btn_new.bind("<Button-1>", self.neww)
        self.btn_new.place(relx=0.44, y=650, anchor=tk.CENTER)

        # Кнопка удалить

        self.btn_delete = tk.Button(self, text="删除", width=20, height=1, bg=self.btn_color.get(),
                                    fg=self.btn_text_color.get(), state=tk.DISABLED)
        self.btn_delete.bind("<Button-1>", self.deletew)
        self.btn_delete.place(relx=0.27, y=650, anchor=tk.CENTER)

        # Кнопка Поиск

        self.btn_find = tk.Button(self, text="搜索", width=10, height=1, bg=self.btn_color.get(),
                                  fg=self.btn_text_color.get(), font=50, state=tk.DISABLED)
        self.btn_find.bind("<Button-1>", self.find_records)
        self.btn_find.place(relx=0.27, y=400, anchor=tk.CENTER)

        # Кнопка настройки

        # f2=Image.open("img.png")
        # f2=f2.resize((30,30),Image.ANTIALIAS)
        # f=ImageTk.PhotoImage(f2)
        self.btn_opt = tk.Button(self, text="设置", compound=tk.LEFT, width=20, height=1, bg=self.btn_color.get(),
                                 fg=self.btn_text_color.get())
        self.btn_opt.bind("<Button-1>", self.optionswind)
        self.btn_opt.place(relx=0.10, y=650, anchor=tk.CENTER)

        # Строки ввода:
        # Фамилия
        self.fname_sv = tk.StringVar()
        self.ent_fam = tk.Entry(self, textvariable=self.fname_sv, fg=self.ent_text_color.get(), bg=self.ent_color.get(),
                                width=20)
        self.ent_fam.place(x=100, y=110)
        self.fname_sv.set("")

        # Имя
        self.lname_sv = tk.StringVar()
        self.ent_name = tk.Entry(self, textvariable=self.lname_sv, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_name.place(x=100, y=140)
        self.lname_sv.set("")

        # Отчество
        self.sname_sv = tk.StringVar()
        self.ent_ot4 = tk.Entry(self, textvariable=self.sname_sv, fg=self.ent_text_color.get(), bg=self.ent_color.get(),
                                width=20)
        self.ent_ot4.place(x=100, y=170)
        self.sname_sv.set("")

        # Телефон

        self.number_sv = tk.StringVar()
        self.ent_tel = tk.Entry(self, textvariable=self.number_sv, fg=self.ent_text_color.get(),
                                bg=self.ent_color.get(), width=20)
        self.ent_tel.place(x=100, y=200)
        self.number_sv.set("")

        # Город
        self.town_sv = tk.StringVar()
        self.ent_town = tk.Entry(self, textvariable=self.town_sv, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_town.place(x=100, y=230)
        self.town_sv.set("")

        # Улица
        self.street_sv = tk.StringVar()
        self.ent_street = tk.Entry(self, textvariable=self.street_sv, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_street.place(x=100, y=260)
        self.street_sv.set("улица ")

        # Дом
        self.home_sv = tk.StringVar()
        self.ent_home = tk.Entry(self, textvariable=self.home_sv, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_home.place(x=100, y=290)
        self.home_sv.set("")

        # Город
        self.appartament_sv = tk.StringVar()
        self.ent_appartament = tk.Entry(self, textvariable=self.appartament_sv, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_appartament.place(x=100, y=320)
        self.appartament_sv.set("")


        # gg

        columns = ("phone_number", "secondname", "name", "patronymic")
        self.text_res = ttk.Treeview(columns=columns, show="headings", height=43)
        self.text_res.pack(fill=tk.BOTH, expand=1)
        self.text_res.place(relx=0.99, y=0, anchor=tk.NE)

        # определяем заголовки
        self.text_res.heading(column="phone_number", text="Телефон", anchor=tk.NW)
        self.text_res.heading(column="secondname", text="Фамилия", anchor=tk.NW)
        self.text_res.heading(column="name", text="Имя", anchor=tk.NW)
        self.text_res.heading(column="patronymic", text="Отчество", anchor=tk.NW)

        self.text_res.column("#1", width=112, minwidth=112, stretch=False, anchor=tk.NW)
        self.text_res.column("#2", width=112, minwidth=112, stretch=False, anchor=tk.NW)
        self.text_res.column("#3", width=112, minwidth=112, stretch=False, anchor=tk.NW)
        self.text_res.column("#4", width=112, minwidth=112, stretch=False, anchor=tk.NW)

        self.text_res.bind("<<TreeviewSelect>>", self.on_select)

        # self.scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=self.text_res.yview)
        # self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # self.scrollbar.place(relx=1, y=0)
        # self.text_res.configure(yscrollcommand=self.scrollbar.set)
        # self.scrollbar.grid(row=1, column=1, sticky="ns")






        self.mainloop()

    def on_select(self, event):

        if not self.text_res.selection():
            return

        selected_item= self.text_res.selection()[0]

        values= self.text_res.item(selected_item, option="values",)

        if "улица" in values:
            values=" ".join(values)
            values=values.split(" ")

            values.remove("улица")



        self.rezult_window = tk.Toplevel()
        self.rezult_window.config(bg="white")
        self.rezult_window.title("Инфа")
        self.rezult_window.geometry("800x50")
        self.rezult_window.resizable(False, False)

        self.full_text=tk.Label(self.rezult_window, text=" ".join(values),
                                  fg=self.font_color.get(), bg=self.bg_color.get())

        self.lbl_rule1.place(x=0, y=0, anchor=tk.NW)

        columns2 = ("phone_number", "secondname", "name", "patronymic", "town", "street", "home", "appartament")
        self.text_res2 = ttk.Treeview(master=self.rezult_window, columns=columns2, show="headings", height=43)
        self.text_res2.pack(fill=tk.BOTH, expand=1)
        self.text_res2.place(relx=0, y=0, anchor=tk.NW)

        # определяем заголовки
        self.text_res2.heading(column="phone_number", text="Телефон", anchor=tk.NW)
        self.text_res2.heading(column="secondname", text="Фамилия", anchor=tk.NW)
        self.text_res2.heading(column="name", text="Имя", anchor=tk.NW)
        self.text_res2.heading(column="patronymic", text="Отчество", anchor=tk.NW)

        self.text_res2.heading(column="town", text="Город", anchor=tk.NW)
        self.text_res2.heading(column="street", text="Улица", anchor=tk.NW)
        self.text_res2.heading(column="home", text="Дом", anchor=tk.NW)
        self.text_res2.heading(column="appartament", text="Квартира", anchor=tk.NW)


        self.text_res2.column("#1", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res2.column("#2", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res2.column("#3", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res2.column("#4", width=100, minwidth=100, stretch=False, anchor=tk.NW)

        self.text_res2.column("#5", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res2.column("#6", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res2.column("#7", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res2.column("#8", width=100, minwidth=100, stretch=False, anchor=tk.NW)


        self.text_res2.insert("", tk.END, values=values)

        self.rezult_window.mainloop()


    def openFile(self, event):
        file = fd.askopenfile(mode="r")


        if file is None:
            return
        self.filename = file.name

        for line in file:
            line_spis = line.rstrip("/n").split(" ")
            phone_line = {self.tel: line_spis[0], self.fam: line_spis[1], self.im9: line_spis[2], self.ot4: line_spis[3], self.town: line_spis[4],
                    self.street: line_spis[5] +" "+ line_spis[6], self.house: line_spis[7], self.kw: line_spis[8][0:-1]}
            self.phone_book.append(phone_line)

        file.close()

        self.btn_find.config(state=tk.NORMAL)
        self.btn_new.config(state=tk.NORMAL)
        self.btn_delete.config(state=tk.NORMAL)

        print(self.phone_book)

    def clear_res(self, event):
        self.text_res.delete(*self.text_res.get_children())


    def neww(self, event):
        self.newwopto = True
        self.newwind = tk.Toplevel()
        self.newwind.title("Создать контакт")
        self.newwind.config(bg=self.bg_color.get())
        self.newwind.geometry("400x400")
        self.newwind.resizable(False, False)

        # Телефон

        self.number_svw = tk.StringVar()
        self.ent_telw = tk.Entry(self.newwind, textvariable=self.number_svw, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_telw.place(x=100, y=20)
        self.number_svw.set("")

        self.fname_svw = tk.StringVar()
        self.ent_famw = tk.Entry(self.newwind, textvariable=self.fname_svw, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_famw.place(x=100, y=60)
        self.fname_svw.set("")

        # Имя
        self.lname_svw = tk.StringVar()
        self.ent_namew = tk.Entry(self.newwind, textvariable=self.lname_svw, fg=self.ent_text_color.get(),
                                   bg=self.ent_color.get(), width=20)
        self.ent_namew.place(x=100, y=100)
        self.lname_svw.set("")

        # Отчество
        self.sname_svw = tk.StringVar()
        self.ent_ot4w = tk.Entry(self.newwind, textvariable=self.sname_svw, fg=self.ent_text_color.get(),
                                 bg=self.ent_color.get(), width=20)
        self.ent_ot4w.place(x=100, y=140)
        self.sname_svw.set("")

        # город
        self.town_svw = tk.StringVar()
        self.ent_townw = tk.Entry(self.newwind, textvariable=self.town_svw, fg=self.ent_text_color.get(),
                                  bg=self.ent_color.get(), width=20)
        self.ent_townw.place(x=100, y=180)
        self.town_svw.set("")

        # улица
        self.street_svw = tk.StringVar()
        self.ent_streetw = tk.Entry(self.newwind, textvariable=self.street_svw, fg=self.ent_text_color.get(),
                                  bg=self.ent_color.get(), width=20)
        self.ent_streetw.place(x=100, y=220)
        self.street_svw.set("улица ")

        # Дом
        self.home_svw = tk.StringVar()
        self.ent_homew = tk.Entry(self.newwind, textvariable=self.home_svw, fg=self.ent_text_color.get(),
                                    bg=self.ent_color.get(), width=20)
        self.ent_homew.place(x=100, y=260)
        self.home_svw.set("")

        # Квартира
        self.appartament_svw = tk.StringVar()
        self.ent_appartamentw = tk.Entry(self.newwind, textvariable=self.appartament_svw, fg=self.ent_text_color.get(),
                                  bg=self.ent_color.get(), width=20)
        self.ent_appartamentw.place(x=100, y=300)
        self.appartament_svw.set("")

        # Телефон

        self.lbl_telw = tk.Label(self.newwind, text="电话号码", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_telw.place(x=20, y=20, anchor=tk.NW)

        # "Фамилия"
        self.lbl_famw = tk.Label(self.newwind, text="姓", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_famw.place(x=20, y=60, anchor=tk.NW)



        # Имя
        self.lbl_namew = tk.Label(self.newwind, text="姓名", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_namew.place(x=20, y=100, anchor=tk.NW)

        # Отчество
        self.lbl_ot4w = tk.Label(self.newwind, text="Nothing", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_ot4w.place(x=20, y=140, anchor=tk.NW)



        # "город"
        self.lbl_townw = tk.Label(self.newwind, text="城市", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_townw.place(x=20, y=180, anchor=tk.NW)

        # "улица"
        self.lbl_streetw = tk.Label(self.newwind, text="街道", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_streetw.place(x=20, y=220, anchor=tk.NW)

        # "дом"
        self.lbl_homew = tk.Label(self.newwind, text="房子", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_homew.place(x=20, y=260, anchor=tk.NW)

        # "вартира"
        self.lbl_appartamentw = tk.Label(self.newwind, text="公寓", fg=self.font_color.get(), bg=self.bg_color.get())
        self.lbl_appartamentw.place(x=20, y=300, anchor=tk.NW)

        self.btn_made = tk.Button(self.newwind, text="创造", width=20, height=1, bg=self.btn_color.get(),
                                  fg=self.btn_text_color.get())
        self.btn_made.bind("<Button-1>", self.madenew)
        self.btn_made.place(relx=0.27, y=350, anchor=tk.CENTER)

        self.newwind.protocol("WM_DELETE_WINDOW", self.on_closing_newwind)

    def on_closing_newwind(self):
        self.newwind.destroy()
        self.newwopto = False

    def newwopt(self):
        if self.newwopto == True:
            self.newwind.configure(bg=self.bg_color.get())

            self.ent_famw.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
            self.ent_namew.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
            self.ent_ot4w.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
            self.ent_telw.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
            self.ent_townw.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
            self.ent_streetw.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
            self.ent_homew.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
            self.ent_appartamentw.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())

            self.lbl_namew.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_famw.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_ot4w.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_telw.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_townw.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_streetw.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_homew.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_appartamentw.configure(bg=self.bg_color.get(), fg=self.font_color.get())

            self.btn_made.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())

    def madenew(self, event):
        self.phone_book.append({self.tel: self.number_svw.get(),
                                self.fam: self.fname_svw.get(),
                                self.im9: self.lname_svw.get(),
                                self.ot4: self.sname_svw.get(),
                                self.town: self.town_svw.get(),
                                self.street: self.street_svw.get(),
                                self.house: self.home_svw.get(),
                                self.kw: self.appartament_svw.get()})

        n = open(self.filename, "a")
        n.write("{} {} {} {}\n".format(self.number_svw.get(),
                                       self.fname_svw.get(),
                                       self.lname_svw.get(),
                                       self.sname_svw.get(),
                                       self.town_svw.get(),
                                       self.street_svw.get(),
                                       self.home_svw.get(),
                                       self.appartament_svw.get()))
        n.close()
        self.newwopto = False
        self.newwind.destroy()

    def deletew(self, event):
        self.delitto = True
        self.deletewin = tk.Toplevel()
        self.deletewin.title("Удалить контакт")
        self.deletewin.config(bg=self.bg_color.get())
        self.deletewin.geometry("950x800")
        self.deletewin.resizable(False, False)

        self.lbl_rulesdel = tk.Label(self.deletewin, text="查找联系人并", fg=self.font_color.get(),
                                     bg=self.bg_color.get())
        self.lbl_rulesdel.place(relx=0, y=5, anchor=tk.NW)

        self.lbl_rulesdel2 = tk.Label(self.deletewin, text="突出显示它", fg=self.font_color.get(),
                                      bg=self.bg_color.get())
        self.lbl_rulesdel2.place(relx=0, y=35, anchor=tk.NW)

        columns3 = ("phone_number", "secondname", "name", "patronymic", "town", "street", "home", "appartament")
        self.text_res3 = ttk.Treeview(master=self.deletewin, columns=columns3, show="headings", height=43)
        self.text_res3.pack(fill=tk.BOTH, expand=1)
        self.text_res3.place(relx=0.99, y=0, anchor=tk.NE)

        # определяем заголовки
        self.text_res3.heading(column="phone_number", text="Телефон", anchor=tk.NW)
        self.text_res3.heading(column="secondname", text="Фамилия", anchor=tk.NW)
        self.text_res3.heading(column="name", text="Имя", anchor=tk.NW)
        self.text_res3.heading(column="patronymic", text="Отчество", anchor=tk.NW)

        self.text_res3.heading(column="town", text="Город", anchor=tk.NW)
        self.text_res3.heading(column="street", text="Улица", anchor=tk.NW)
        self.text_res3.heading(column="home", text="Дом", anchor=tk.NW)
        self.text_res3.heading(column="appartament", text="Квартира", anchor=tk.NW)

        self.text_res3.column("#1", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res3.column("#2", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res3.column("#3", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res3.column("#4", width=100, minwidth=100, stretch=False, anchor=tk.NW)

        self.text_res3.column("#5", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res3.column("#6", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res3.column("#7", width=100, minwidth=100, stretch=False, anchor=tk.NW)
        self.text_res3.column("#8", width=100, minwidth=100, stretch=False, anchor=tk.NW)

        self.text_res3.bind("<<TreeviewSelect>>", self.delt)



        yo = 0
        while yo <= len(self.phone_book) - 1:
            self.rester = [i for i in list(self.phone_book[yo].values())]
            d=self.rester[5].split(" ")
            d.remove("улица")
            d="".join(d)
            self.rester[5]=d

            self.text_res3.insert("", tk.END, values=self.rester)


            yo += 1

        self.deletewin.protocol("WM_DELETE_WINDOW", self.on_closing_deletewin)

    def on_closing_deletewin(self):
        self.deletewin.destroy()
        self.delitto = False




    def delt(self, event):
        # selection = self.text_resd.tag_ranges(tk.SEL)
        # numst = str(selection[0])
        # numst = numst.split(".")
        # numst = int(numst[0])
        # print(numst - numst * 2)
        # print(self.phone_book[numst - numst * 2])
        #
        # self.phone_book.pop(numst - numst * 2)



        if not self.text_res3.selection():
            return

        selected_item= self.text_res3.selection()[0]

        values= self.text_res3.item(selected_item, option="values",)

        for i in self.phone_book:
            if i.values() == values:
                self.phone_book.remove(i)

        n = open(self.filename, "w")
        n.truncate(0)

        for i in range(len(self.phone_book)):
            n.write(f"{self.phone_book[i][self.tel]} "
                    f"{self.phone_book[i][self.fam]} "
                    f"{self.phone_book[i][self.im9]} "
                    f"{self.phone_book[i][self.ot4]} "
                    f"{self.phone_book[i][self.town]} "
                    f"{self.phone_book[i][self.street]} "
                    f"{self.phone_book[i][self.house]} "
                    f"{self.phone_book[i][self.kw]}\n")

        n.close()

        self.delitto=False
        self.deletewin.destroy()

    def newdel(self):
        if self.delitto == True:
            self.deletewin.configure(bg=self.bg_color.get())

            self.lbl_rulesdel.configure(bg=self.bg_color.get(), fg=self.font_color.get())
            self.lbl_rulesdel2.configure(bg=self.bg_color.get(), fg=self.font_color.get())


    def clear_inputs(self, event):
        self.fname_sv.set("")
        self.lname_sv.set("")
        self.sname_sv.set("")
        self.number_sv.set("")
        self.town_sv.set("")
        self.street_sv.set("улица ")
        self.home_sv.set("")
        self.appartament_sv.set("")

    def find_records(self, event):
        find_records = []
        find_records2 = []
        find_records3 = []
        find_records4 = []
        find_records5 = []
        find_records6 = []
        find_records7 = []
        self.find_records8 = []

        if self.fname_sv.get() != "":
            for e in range(len(self.phone_book)):
                e -= 1
                if self.phone_book[e]["фамилия"] == self.fname_sv.get():
                    find_records=self.phone_book
        else:
            find_records = self.phone_book

        if self.number_sv.get() != "":
            for e in range(len(find_records)):
                e -= 1
                if self.number_sv.get() in find_records[e]["телефон"]:
                    find_records2.append(find_records[e])
        else:
            find_records2=find_records


        if self.lname_sv.get() != "":
            for e in range(len(find_records2)):
                e -= 1
                if find_records2[e]["имя"] == self.lname_sv.get():
                    find_records3.append(find_records2[e])
        else:
            find_records3=find_records2

        if self.sname_sv.get() != "":
            for e in range(len(find_records3)):
                e -= 1
                if find_records3[e]["отчество"] == self.sname_sv.get():
                    find_records4.append(find_records3[e])
        else:
            find_records4=find_records3


        if self.town_sv.get() != "":
            for e in range(len(find_records4)):
                e -= 1
                if find_records4[e]["город"] == self.town_sv.get():
                    find_records5.append(find_records4[e])
        else:
            find_records5 = find_records4

        if self.street_sv.get() == "улица ":

            find_records6 = find_records5

        else:

            for e in range(len(find_records5)):
                e -= 1
                if find_records5[e]["улица"] == self.street_sv.get():
                    find_records6.append(find_records5[e])



        if self.home_sv.get() != "":
            for e in range(len(find_records6)):
                e -= 1
                if find_records6[e]["дом"] == self.home_sv.get():
                    find_records7.append(find_records6[e])
        else:
            find_records7 = find_records6

        if self.appartament_sv.get() != "":
            for e in range(len(find_records7)):
                e -= 1
                if find_records7[e]["квартира"] == self.appartament_sv.get():
                    self.find_records8.append(find_records7[e])
        else:
            self.find_records8 = find_records7

        yo=0
        while yo <= len(self.find_records8)-1:

            # self.text_res.insert("1.0", " ".join([i for i in list(self.find_records8[yo].values())]) + '\n')
            self.text_res.insert("", tk.END, values= str(" ".join([i for i in list(self.find_records8[yo].values())]) + '\n'))
            self.rester=" ".join([i for i in list(self.find_records8[yo].values())]) + '\n'
            yo += 1
        print(self.find_records8)




        return self.find_records8

    def cconfig(self):
        self.configure(bg=self.bg_color.get())

        self.lbl_rule1.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_rule2.configure(bg=self.bg_color.get(), fg=self.font_color.get())

        self.lbl_name.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_fam.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_ot4.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_tel.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_town.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_street.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_home.configure(bg=self.bg_color.get(), fg=self.font_color.get())
        self.lbl_appartament.configure(bg=self.bg_color.get(), fg=self.font_color.get())

        self.btn_find.configure(bg=self.btn_color.get(), fg=self.btn_text_color.get())
        self.btn_file.configure(bg=self.btn_color.get(), fg=self.btn_text_color.get())
        self.btn_clear_inp.configure(bg=self.btn_color.get(), fg=self.btn_text_color.get())
        self.btn_clear_res.configure(bg=self.btn_color.get(), fg=self.btn_text_color.get())
        self.btn_opt.configure(bg=self.btn_color.get(), fg=self.btn_text_color.get())
        self.btn_new.configure(bg=self.btn_color.get(), fg=self.btn_text_color.get())
        self.btn_delete.configure(bg=self.btn_color.get(), fg=self.btn_text_color.get())

        self.ent_fam.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
        self.ent_name.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
        self.ent_ot4.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
        self.ent_tel.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
        self.ent_town.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
        self.ent_street.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
        self.ent_home.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())
        self.ent_appartament.configure(bg=self.ent_color.get(), fg=self.ent_text_color.get())



    def primme(self, event):
        self.cconfig()
        self.newwopt()
        self.newdel()

    def cansel(self, event):
        self.options.destroy()
        self.ui = 0

    def ok(self, event):
        self.options.destroy()
        self.ui = 0

        self.cconfig()
        self.newwopt()
        self.newdel()

    def on_closing_options(self):
        self.ui = 0
        self.options.destroy()

    def optionswind(self, event):
        if self.ui == 0:
            self.ui += 1
            # создание окна
            self.options = tk.Toplevel()
            self.options.config(bg="white")
            self.options.title("Настройки")
            self.options.geometry("400x400")
            self.options.resizable(False, False)

            # вкладки
            tabControl = ttk.Notebook(self.options)

            tab1 = ttk.Frame(tabControl)
            tab2 = ttk.Frame(tabControl)

            tabControl.add(tab1, text='Tab 1')
            tabControl.add(tab2, text='Tab 2')
            tabControl.pack(expand=1, fill="both")

            # Вкладка 1"форматирование окна"

            # Фон

            bg_color = Combobox(tab1, textvariable=self.bg_color)
            bg_color['values'] = ("bisque", "black", "white", "dark green")
            bg_color.current(0)
            bg_color.grid(column=0, row=0)
            bg_color.place(relx=0.5, y=10, anchor=tk.NW)

            # Цвет текста

            font_color = Combobox(tab1, textvariable=self.font_color)
            font_color['values'] = ("black", "white", "dark green")
            font_color.current(0)
            font_color.grid(column=0, row=0)
            font_color.place(relx=0.5, y=40, anchor=tk.NW)

            # Цвет текста на кнопках

            btn_text_color = Combobox(tab1, textvariable=self.btn_text_color)
            btn_text_color['values'] = ("white", "black", "dark green")
            btn_text_color.current(0)
            btn_text_color.grid(column=0, row=0)
            btn_text_color.place(relx=0.5, y=70, anchor=tk.NW)

            # Цвет кнопок

            btn_color = Combobox(tab1, textvariable=self.btn_color)
            btn_color['values'] = ("green", "black", "white", "blue")
            btn_color.current(0)
            btn_color.grid(column=0, row=0)
            btn_color.place(relx=0.5, y=100, anchor=tk.NW)

            lbl_color_btn = tk.Label(tab1, text="Цвет кнопок", fg=self.font_color.get())
            lbl_color_btn.place(relx=0.05, y=100, anchor=tk.NW)

            lbl_color_font_btn = tk.Label(tab1, text="Цвет текста на кнопках", fg=self.font_color.get())
            lbl_color_font_btn.place(relx=0.05, y=70, anchor=tk.NW)

            lbl_color_font = tk.Label(tab1, text="Цвет текста", fg=self.font_color.get())
            lbl_color_font.place(relx=0.05, y=40, anchor=tk.NW)

            lbl_bg = tk.Label(tab1, text="Фон", fg=self.font_color.get())
            lbl_bg.place(relx=0.05, y=10, anchor=tk.NW)

            # Цвет текста в поле ввода

            ent_text_color = Combobox(tab1, textvariable=self.ent_text_color)
            ent_text_color['values'] = ("dark green", "bisque", "black", "white")
            ent_text_color.current(0)
            ent_text_color.grid(column=0, row=0)
            ent_text_color.place(relx=0.5, y=130, anchor=tk.NW)

            # Цвет поля ввода

            ent_color = Combobox(tab1, textvariable=self.ent_color)
            ent_color['values'] = ("white", "bisque", "black",)
            ent_color.current(0)
            ent_color.grid(column=0, row=0)
            ent_color.place(relx=0.5, y=160, anchor=tk.NW)

            lbl_color_ent = tk.Label(tab1, text="输入字段中的文本颜色", fg=self.font_color.get())
            lbl_color_ent.place(relx=0.05, y=130, anchor=tk.NW)

            lbl_color_enter = tk.Label(tab1, text="输入字段颜色", fg=self.font_color.get())
            lbl_color_enter.place(relx=0.05, y=160, anchor=tk.NW)

            btn_prim = tk.Button(tab1, text="申请", width=10, height=1, bg="grey", fg="black")
            btn_prim.bind("<Button-1>", self.cconfig)
            btn_prim.place(relx=0.75, y=370, anchor=tk.SW)

            btn_cansel = tk.Button(tab1, text="消除", width=10, height=1, bg="grey", fg="black")
            btn_cansel.bind("<Button-1>", self.cansel)
            btn_cansel.place(relx=0.5, y=370, anchor=tk.SW)

            btn_ok = tk.Button(tab1, text="好的", width=10, height=1, bg="grey", fg="black")
            btn_ok.bind("<Button-1>", self.ok)
            btn_ok.place(relx=0.25, y=370, anchor=tk.SW)

            # Вкладка 2

            btn_prim = tk.Button(tab2, text="применить", width=10, height=1, bg="grey", fg="black")
            btn_prim.bind("<Button-1>", self.primme)
            btn_prim.place(relx=0.75, y=370, anchor=tk.SW)

            btn_cansel = tk.Button(tab2, text="отмена", width=10, height=1, bg="grey", fg="black")
            btn_cansel.bind("<Button-1>", self.cansel)
            btn_cansel.place(relx=0.5, y=370, anchor=tk.SW)

            btn_ok = tk.Button(tab2, text="ок", width=10, height=1, bg="grey", fg="black")
            btn_ok.bind("<Button-1>", self.ok)
            btn_ok.place(relx=0.25, y=370, anchor=tk.SW)

            text_res2 = tk.Text(tab2, width=55, height=8000, bd=5, )
            text_res2.place(relx=0, y=0, anchor=tk.NW)
            text_res2.pack(pady=(0, 30), side=tk.LEFT)

            self.options.protocol("WM_DELETE_WINDOW", self.on_closing_options)


if __name__ == "__main__":
    phones = PhoneBook()
