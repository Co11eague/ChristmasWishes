from tkinter import *
from tkinter import messagebox

# __________________________________________________________________
# Šriftai, kuriuos naudoju.
f = ("Times", "17", "bold italic")
f1 = ("Times", "20", "bold italic underline")


# __________________________________________________________________
def isejimas():
    ats = messagebox.askyesno("Išėjimas", "Ar norite išeiti iš šios programos")
    if ats:
        pg.destroy()


# Mamos sveikinimas (Pakeičiamas paveiksliukas, mygtukų spalvos, sveikinimo tekstas)
def mama():
    global photo
    a.config(bg="palegreen")
    b.config(bg="salmon")
    c.config(bg="turquoise")
    photo = PhotoImage(file="kaledos.gif")
    photo = photo.zoom(x)
    photo = photo.subsample(y)
    nuotrauka.config(image=photo)
    remasreme.config(text="Mama, aš Tave labai myliu...")
    tekstas1.config(
        text="Baltieji bokštai siekia dangų -\n Kalėdų rytas šerkšnuose,\n  Apgaubk mane Tu meilės rankom,"
             "\n  O aš bučiuosiu vien Tave,\n\n  Su Šv. Kalėdom ir Najaisiais metais!")


# Tėvo sveikinimas (Pakeičiamas paveiksliukas, mygtukų spalvos, sveikinimo tekstas)
def tetis():
    global photo
    photo = PhotoImage(file="Kaledos-1.gif")
    photo = photo.zoom(x)
    photo = photo.subsample(y)
    nuotrauka.config(image=photo)
    a.config(bg="lightgreen")
    b.config(bg="lightsalmon")
    c.config(bg="turquoise")
    remasreme.config(text="Tėti, aš Tave labai myliu...")
    tekstas1.config(
        text="Tegul Kalėdų žvakių šiesoje sudega\nvisi rūpesčiai ir liūdesys\no suspindi laimė, džiugesys ir "
             "meilė\n\n  Su Šv. Kalėdom ir Najaisiais metais!")


# Sesės sveikinimas (Pakeičiamas paveiksliukas, mygtukų spalvos, sveikinimo tekstas)
def sese():
    global photo
    a.config(bg="lightgreen")
    b.config(bg="salmon")
    c.config(bg="paleturquoise")
    photo = PhotoImage(file="kaledeles.gif")
    photo = photo.zoom(x)
    photo = photo.subsample(y)
    nuotrauka.config(image=photo)
    remasreme.config(text="Sese, aš Tave labai myliu...")
    tekstas1.config(
        text="Sušildysiu. Priglausiu Tave,\nPasveikinsiu su Viešpaties diena.\nŠventų Kalėdų meilės Angelai\nGlobos "
             "ir saugos mudu amžinai\n\n  Su Šv. Kalėdom ir Najaisiais metais!")


# __________________________________________________________________
# Nustatomi lango parametrai
pg = Tk()
pg.config(background='white')
pg.resizable(False, False)
ilgis = pg.winfo_screenwidth()
plotis = pg.winfo_screenheight()
pg.attributes("-fullscreen", True)
# Tikrinamas lango dydis ir pagal tai nustatomas paveiksliuko dydis.
if ilgis < 1200 or plotis < 700:
    x, y = 1, 2
elif 1200 < ilgis < 1600 or 700 < plotis <= 900:
    x, y = 1, 1
else:  # Panašiai su šia rezoliucija buvo daryta programa
    x, y = 3, 2
pg.geometry("%dx%d" % (ilgis, plotis))
# __________________________________________________________________
# Sukūriamas rėmas.
remasreme = LabelFrame(pg, text="Mama, aš Tave labai myliu...", font=f1, bd=5, bg="white")
remasreme.place(x=ilgis / 12, y=plotis * 0.20)
# __________________________________________________________________
# Patalpinama nuotrauka
photo = PhotoImage(file="kaledos.gif")
photo = photo.zoom(x)
photo = photo.subsample(y)
nuotrauka = Label(remasreme, image=photo)
nuotrauka.grid(row=0, column=0, padx=15, pady=15)
# __________________________________________________________________
# Patalpinamas eiliuotas sveikinimas
tekstas1 = Label(remasreme, justify=RIGHT, bg="white",
                 text="Baltieji bokštai siekia dangų -\n Kalėdų rytas šerkšnuose,\n  Apgaubk mane Tu meilės rankom,"
                      "\n  O aš bučiuosiu vien Tave,\n\n  Su Šv. Kalėdom ir Najaisiais metais!",
                 font=f)
tekstas1.grid(row=0, column=1, padx=10)
# __________________________________________________________________
# Sukūriami mygtukai
a = Button(pg, bg="palegreen", text="Sveikinimas Mamai", font=f, relief=RAISED, borderwidth=5, command=mama,
           cursor="heart")
a.grid(column=0, row=0)
b = Button(pg, text="Sveikinimas Tėčiui", font=f, relief=RAISED, borderwidth=5, command=tetis, bg="salmon",
           cursor="heart")
b.grid(column=1, row=0)
c = Button(pg, text="Sveikinimas Sesei", font=f, relief=RAISED, borderwidth=5, command=sese, bg="turquoise",
           cursor="heart")
c.grid(column=2, row=0)
d = Button(pg, text="X", font=("Arial", "17", "bold"), bg="red", command=isejimas)
d.place(x=ilgis - 36, y=0)
# __________________________________________________________________
# Nustatomi tarpai tarp mygtukų
pg.grid_columnconfigure(0, minsize=ilgis / 3, weight=1)
pg.grid_columnconfigure(1, minsize=ilgis / 3, weight=1)
pg.grid_columnconfigure(2, minsize=ilgis / 3, weight=1)
pg.grid_rowconfigure(0, minsize=plotis / 3.5)
mainloop()
