import tkinter, sys

def koniec():
    sys.exit()

def zaloguj():
    slownik = {'klucz1':'haslo1', 'klucz2':'haslo2'}
    mtext = str(e.get())
    mtext2 = str(e2.get())
    licznik = 0
    if mtext in slownik.keys() and mtext2 == slownik[mtext]:
        l1 = tkinter.Label(main, text='login: ' + mtext).grid(row = 6, column = 1)
        l2 = tkinter.Label(main, text = 'has³o: '+ mtext2).grid(row = 7, column = 1)
        l3 = tkinter.Label(main, text = 'Dane prawid³owe. \n Rozpocznij pracê w programie klikaj¹c na przycisk poni¿ej.', fg = 'green').grid(row = 8, column = 1)
        b = tkinter.Button(main, text = 'Rozpocznij',bg = 'green',command = program).grid(row = 9, column = 1)
    else:
        l3 = tkinter.Label(main, text='Dane nieprawid³owe. \n Wprowad ponownie login i has³o.',
                               fg='red').grid(row = 5, column = 1)
        # dodaæ licznik wy³¹czaj¹cy po 3 nieudanych próbach
        licznik += 1
        if licznik > 2:
            sys.exit()
    return

def program():
    l = tkinter.Label(main, text='Witaj w programie szyfrator/deszyfrator. \n Co chcesz zrobiæ?',
                       fg='blue').grid(row = 9, column =1)
    b = tkinter.Button(main, text = 'Szyfruj', command = szyfruj).grid(row = 10, column =1, sticky = tkinter.W)
    b2 = tkinter.Button(main, text = 'Odszyfruj', command = odszyfruj).grid(row = 10, column =1, sticky = tkinter.E)

def szyfruj():
    l = tkinter.Label(main, text='Wybrano zaszyfrowanie tekstu, wybierz szyfr:',
                      fg='blue').grid(row = 11, column =1)
    b = tkinter.Button(main, text='GADERYPOLUKI', command=gaderypoluki).grid(row = 12, column =1, sticky = tkinter.W)
    b2 = tkinter.Button(main, text='KACEMINUTOWY', command=kaceminutowy).grid(row = 12, column =1, sticky = tkinter.E)
    b3 = tkinter.Button(main, text='KONIECMATURY', command=koniecmatury).grid(row = 13, column =1, sticky = tkinter.W)
    b4 = tkinter.Button(main, text='POLITYKARENU', command=politykarenu).grid(row = 13, column =1, sticky = tkinter.E)

def odszyfruj():
    l = tkinter.Label(main, text='Wybrano odszyfrowanie tekstu, wybierz szyfr:',
                      fg='blue').grid(row = 11, column =1)
    b = tkinter.Button(main, text='GADERYPOLUKI', command=gaderypoluki).grid(row = 12, column =1, sticky = tkinter.W)
    b2 = tkinter.Button(main, text='KACEMINUTOWY', command=kaceminutowy).grid(row = 12, column =1, sticky = tkinter.E)
    b3 = tkinter.Button(main, text='KONIECMATURY', command=koniecmatury).grid(row = 13, column =1, sticky = tkinter.W)
    b4 = tkinter.Button(main, text='POLITYKARENU', command=politykarenu).grid(row = 13, column =1, sticky = tkinter.E)

def gaderypoluki():
    l = tkinter.Label(main, text='Wybra³e: gaderypoluki.\n Wpisz wiadomoæ i zatwierd przyciskiem.',
                      fg='blue').grid(row = 14, column =1)
    b = tkinter.Button(main, text='Zatwierd', command=zatwierdzgad).grid(row=16, column=1)

def kaceminutowy():
    l = tkinter.Label(main, text='Wybra³e: kaceminutowy.\n Wpisz wiadomoæ i zatwierd przyciskiem.',
                      fg='blue').grid(row = 14, column =1)
    b = tkinter.Button(main, text='Zatwierd', command=zatwierdzkac).grid(row=16, column=1)

def koniecmatury():
    l = tkinter.Label(main, text='Wybra³e: koniecmatury.\n Wpisz wiadomoæ i zatwierd przyciskiem.',
                      fg='blue').grid(row = 14, column =1)
    b = tkinter.Button(main, text='Zatwierd', command=zatwierdzkon).grid(row=16, column=1)

def politykarenu():
    l = tkinter.Label(main, text='Wybra³e: politykarenu.\n Wpisz wiadomoæ i zatwierd przyciskiem.',
                      fg='blue').grid(row = 14, column =1)
    b = tkinter.Button(main, text='Zatwierd', command=zatwierdzpol).grid(row=16, column=1)

def zatwierdzgad():
    mtext = e3.get()
    l2 = tkinter.Label(main, text=mtext)
    l2.grid(row = 18, column =1)
    a = mtext.lower()
    b = a.replace("g", "1")
    c = b.replace("a", "g")
    d = c.replace("1", "a")
    e = d.replace("d", "1")
    f = e.replace("e", "d")
    g = f.replace("1", "e")
    h = g.replace("r", "1")
    i = h.replace("y", "r")
    j = i.replace("1", "y")
    k = j.replace("p", "1")
    l = k.replace("o", "p")
    m = l.replace("1", "o")
    n = m.replace("l", "1")
    o = n.replace("u", "l")
    p = o.replace("1", "u")
    r = p.replace("k", "1")
    s = r.replace("i", "k")
    t = s.replace("1", "i")

    l3 = tkinter.Label(main, text="Tekst brzmi:", fg = 'blue')
    l3.grid(row = 19, column =1)
    l4 = tkinter.Label(main, text='{}'.format(t), fg = 'yellow', bg = 'green')
    l4.grid(row = 20, column =1)

def zatwierdzkac():
    mtext = e3.get()
    l2 = tkinter.Label(main, text=mtext)
    l2.grid(row = 18, column =1)
    a = mtext.lower()
    b = a.replace("k", "1")
    c = b.replace("a", "k")
    d = c.replace("1", "a")
    e = d.replace("c", "1")
    f = e.replace("e", "c")
    g = f.replace("1", "e")
    h = g.replace("m", "1")
    i = h.replace("i", "m")
    j = i.replace("1", "i")
    k = j.replace("n", "1")
    l = k.replace("u", "n")
    m = l.replace("1", "u")
    n = m.replace("t", "1")
    o = n.replace("o", "t")
    p = o.replace("1", "o")
    r = p.replace("w", "1")
    s = r.replace("y", "w")
    t = s.replace("1", "y")

    l3 = tkinter.Label(main, text="Tekst brzmi:", fg='blue')
    l3.grid(row=19, column=1)
    l4 = tkinter.Label(main, text='{}'.format(t), fg = 'yellow', bg = 'green')
    l4.grid(row=20, column=1)

def zatwierdzkon():
    mtext = e3.get()
    l2 = tkinter.Label(main, text=mtext)
    l2.grid(row = 18, column =1)
    a = mtext.lower()
    b = a.replace("k", "1")
    c = b.replace("o", "k")
    d = c.replace("1", "o")
    e = d.replace("n", "1")
    f = e.replace("i", "n")
    g = f.replace("1", "i")
    h = g.replace("e", "1")
    i = h.replace("c", "e")
    j = i.replace("1", "c")
    k = j.replace("m", "1")
    l = k.replace("a", "m")
    m = l.replace("1", "a")
    n = m.replace("t", "1")
    o = n.replace("u", "t")
    p = o.replace("1", "u")
    r = p.replace("r", "1")
    s = r.replace("y", "r")
    t = s.replace("1", "y")

    l3 = tkinter.Label(main, text="Tekst brzmi:", fg = 'blue')
    l3.grid(row = 19, column =1)
    l4 = tkinter.Label(main, text='{}'.format(t), fg = 'yellow', bg = 'green')
    l4.grid(row = 20, column =1)

def zatwierdzpol():
    mtext = e3.get()
    l2 = tkinter.Label(main, text=mtext)
    l2.grid(row = 18, column =1)
    a = mtext.lower()
    b = a.replace("p", "1")
    c = b.replace("o", "p")
    d = c.replace("1", "o")
    e = d.replace("l", "1")
    f = e.replace("i", "l")
    g = f.replace("1", "i")
    h = g.replace("t", "1")
    i = h.replace("y", "t")
    j = i.replace("1", "y")
    k = j.replace("k", "1")
    l = k.replace("a", "k")
    m = l.replace("1", "a")
    n = m.replace("r", "1")
    o = n.replace("e", "r")
    p = o.replace("1", "e")
    r = p.replace("n", "1")
    s = r.replace("u", "n")
    t = s.replace("1", "u")

    l3 = tkinter.Label(main, text="Tekst brzmi:", fg = 'blue')
    l3.grid(row = 19, column =1)
    l4 = tkinter.Label(main, text='{}'.format(t), fg = 'yellow', bg = 'green')
    l4.grid(row = 20, column =1)

main = tkinter.Tk()
main.title('Szyfrator/deszyfrator')
main.geometry('400x600')
#main.configure(bg = 'black') - zmiana t³a na czarne

photo1 = tkinter.PhotoImage(file = 'sd.png')
l0 = tkinter.Label(main, image = photo1, bg = 'black')
l = tkinter.Label(main, text='Wprowad login:', fg = 'blue', bg = 'black')
l2 = tkinter.Label(main, text='login: ')
l3 = tkinter.Label(main, text = 'has³o: ')
e = tkinter.Entry(main)
e2 = tkinter.Entry(main)
b = tkinter.Button(main, text = 'Zaloguj',bg = 'yellow', command = zaloguj)
b2 = tkinter.Button(main, text = 'Zakoñcz', bg = 'red', command = koniec)
e3 = tkinter.Entry(main)
mtext2 = str()

l0.grid(columnspan = 4)
l.grid(row = 1, column = 1)
l2.grid(row = 2, column = 0)
l3.grid(row = 3, column = 0)
e.grid(row = 2, column = 1)
e2.grid(row = 3, column = 1)
b.grid(row = 4, column = 1)
b2.grid(row = 22, column = 1)
e3.grid(row = 15, column =1)
main.mainloop()