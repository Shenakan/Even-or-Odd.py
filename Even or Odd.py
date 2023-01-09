import tkinter as tk

class app:

    def __init__(self):
        self.windows = tk.Tk()
        self.windows.geometry("500x250")
        self.windows.configure(bg="black")

        self.frame = tk.Frame(self.windows)
        self.frame.configure(bg="black")

        self.title = tk.Label(self.frame, text="¿Even or Odd?", bg="black", fg="white")
        self.title.configure(font=("Mukta", 24, "bold"))
        self.title.grid(column=1, row=0, sticky=tk.W, padx='150')

        self.label_num = tk.Label(self.frame, text="Write the number here: ", bg="black", fg="white")
        self.label_num.configure(font=("Mukta", 14, "bold"))
        self.label_num.grid(column=1, row=1, sticky=tk.W, pady="28")

        self.label_2 = tk.Label(self.frame,text="respuesta", bg="black", fg="white")
        self.label_2.grid(column=1,row=2,pady=30,padx=270)

        self.dato = tk.StringVar()
        self.input_num = tk.Entry(self.frame, textvariable=self.dato)
        self.input_num.grid(column=1, row=1, sticky=tk.W, padx="200")

        self.warning = tk.Label(self.windows, text="Only Integers!!", bg="black", fg="red")
        self.warning.configure(font=("ubuntu", 10, "bold"))
        self.warning.place(x=220, y=125)

        self.button1 = tk.Button(self.windows, text="Answer:", command= self.even_or_odd)
        self.button1.place(x=220, y=180)

        self.frame.grid(column=0, row=0, sticky=tk.W)
        self.windows.mainloop()

    def even_or_odd(self):
        valor=int(self.dato.get())

        if valor % 2 == 0:
            self.label_2.configure(text=f"The number {valor} is even!")
        elif valor % 2 == 1:
            self.label_2.configure(text=f"The number {valor} is odd!")
        else:
            self.label_2.configure(text=f"The number is zero!")

aplication1 = app()