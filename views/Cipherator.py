login = {'User1': 'one', 'User2': 'two', 'User3': 'three'}
print('Wprowadź login:')
while True:
    x = input()
    if x in login.keys():
        print('Login prawidłowy, wprowadź hasło:')
        y = input()
        if y == login[x]:
            print('Hasło prawidłowe.')
            break
        else:
            print('Hasło nieprawidłowe. Wprowadź ponownie login:')
    else:
        print('Login nie znajduje siê w bazie. Wprowadź ponownie login:')

while True:

    print("Szyfrator/deszyfrator\n Co chcesz zrobić?\n 1-zaszyfrować tekst, 2-odszyfrować tekst")

    x = int(input())

    if x != 1 and x != 2:
        print("wybierz poprawnie: 1 lub 2\n")

    if x == 1:
        print("wybrano zaszyfrowanie tekstu, wybierz szyfr:")

        szyfry = ["GADERYPOLUKI", "POLITYKARENU", "KONIECMATURY", "KACEMINUTOWY"]
        for n, s in enumerate(szyfry):
            print(n + 1, s)
        print("0 wróć do poprzedniego menu")

        y = int(input())

        if y == 1:
            print("wybrano 1=GADERYPOLUKI\n wpisz tekst do zaszyfrowania")

            a = input()
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

            print("zaszyfrowany tekst brzmi:{}\n".format(t))

        if y == 2:
            print("wybrano 2=POLITYKARENU\n wpisz tekst do zaszyfrowania")

            a = input()
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

            print("zaszyfrowany tekst brzmi:{}\n".format(t))

        if y == 3:
            print("wybrano 3=KONIECMATURY\n wpisz tekst do zaszyfrowania")

            a = input()
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

            print("zaszyfrowany tekst brzmi:{}\n".format(t))

        if y == 4:
            print("wybrano 4=KACEMINUTOWY\n wpisz tekst do zaszyfrowania")

            a = input()
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

            print("zaszyfrowany tekst brzmi:{}\n".format(t))

        if y == 0:
            print("powrót\n") # do wło¿enia funkcja cofania

        if y != 1 and y != 2 and y != 3 and y != 4 and y != 0:
            print("działanie nieprawidłowe, wybierz 1 lub 2 lub 3 lub 4 lub 0 \n")


    if x == 2:

        szyfry = ["GADERYPOLUKI", "POLITYKARENU", "KONIECMATURY", "KACEMINUTOWY"]
        for n, s in enumerate(szyfry):
            print(n + 1, s)
        print("0 wróć do poprzedniego menu")

        y = int(input())

        if y == 1:
            print("wybrano 1=GADERYPOLUKI\n wpisz tekst do odszyfrowania")

            a = input()
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

            print("odszyfrowany tekst brzmi:{}\n".format(t))

        if y == 2:
            print("wybrano 2=POLITYKARENU\n wpisz tekst do odszyfrowania")

            a = input()
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

            print("odszyfrowany tekst brzmi:{}\n".format(t))

        if y == 3:
            print("wybrano 3=KONIECMATURY\n wpisz tekst do odszyfrowania")

            a = input()
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

            print("odszyfrowany tekst brzmi:{}\n".format(t))

        if y == 4:
            print("wybrano 4=KACEMINUTOWY\n wpisz tekst do odszyfrowania")

            a = input()
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

            print("odszyfrowany tekst brzmi:{}\n".format(t))

        if y == 0:
            print("powrót\n") # do wło¿enia funkcja cofania

        if y != 1 and y != 2 and y != 3 and y != 4 and y != 0:
            print("działanie nieprawidłowe, wybierz 1 lub 2 lub 3 lub 4 lub 0\n")