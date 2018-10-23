import pymysql


class DBConnect:
    def __init__(self):
        try:
            self.conn = pymysql.connect("localhost", "root", "123qwerty", "korkomistrz")
            print("Ustanowiono połączenie z bazą danych.")
            self.logowanie()
            self.conn.close()
        except:
            print("Podałeś błędne dane. Program zostanie zamknięty.")

    def logowanie(self):

        login = input("Podaj login: ")
        password = input("Podaj hasło: ")

        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from administratorzy where login=%s and password=%s", (login, password))
        allResults = self.cursor.fetchall()


        if (len(allResults) == 1):
            print("Zalogowano.")
            self.menu()

        else:
            print("Podano niepoprawny login, lub hasło.")
            self.logowanie()

    def menu(self):

        dec = input("MENU: \n p - pokaż, w - wprowadź, u - usuń, q - wyjdź \n")
        while (True):
            if (dec == "p"):
                while (True):
                    dec = input(
                        "\nWybierz tabelę do wyświetlenia:\n  a - administratorzy, k - korepetytorzy, l - lekcje, u - uczniowie, r - rodzice \n  p - przedmioty korepetytorów, d - dyspozycyjność korepetytorów, q - wyjdź \n")
                    if (dec == "a"):
                        self.select_administratorzy()
                    elif (dec == "k"):
                        self.select_korepetytorzy()
                    elif (dec == "l"):
                        self.select_lekcje()
                    elif (dec == "u"):
                        self.select_uczniowie()
                    elif (dec == "r"):
                        self.select_rodzice()
                    elif (dec == "p"):
                        self.select_przedmioty_korepetytorzy()
                    elif (dec == "d"):
                        self.select_dys_kor()
                    elif (dec == "q"):
                        break
                    else:
                        break
            elif (dec == "w"):

                while (True):
                    dec = input(
                        "\nWybierz tabelę do wprowadzenia danych:\n  a - administratorzy, k - korepetytorzy, l - lekcje, u - uczniowie, r - rodzice \n  p - przedmioty korepetytorów, d - dyspozycyjność korepetytorów, q - wyjdź \n")
                    if (dec == "a"):
                        self.insert_administratorzy()
                    elif (dec == "k"):
                        self.insert_korepetytorzy()
                    elif (dec == "l"):
                        self.insert_lekcje()
                    elif (dec == "u"):
                        self.insert_uczniowie()
                    elif (dec == "r"):
                        self.insert_rodzice()
                    elif (dec == "p"):
                        self.insert_przedmioty_korepetytorzy()
                    elif (dec == "d"):
                        self.insert_dys_kor()
                    elif (dec == "q"):
                        break
                    else:
                        break
            elif (dec == "u"):

                while (True):
                    dec = input(
                        "\nWybierz tabelę do usnięcia danych:\n k - korepetytorzy, l - lekcje, u - uczniowie, r - rodzice \n  p - przedmioty korepetytorów, d - dyspozycyjność korepetytorów, q - wyjdź \n")
                    if (dec == "k"):
                        self.delete_korepetytorzy()
                    elif (dec == "l"):
                        self.delete_lekcje()
                    elif (dec == "u"):
                        self.delete_uczniowie()
                    elif (dec == "r"):
                        self.delete_rodzice()
                    elif (dec == "p"):
                        self.delete_przedmioty_korepetytorzy()
                    elif (dec == "d"):
                        self.delete_dys_kor()
                    elif (dec == "q"):
                        break
                    else:
                        break

            elif (dec == "q"):
                print("\nKoniec programu.")
                break
            else:
                print("\nNiepoprawne dane wejściowe.\n")
                break

    def select_administratorzy(self):
        print("\nTabela administratorzy:\n")
        self.cursor.execute("select * from administratorzy")
        for i in self.cursor.fetchall():
            print(i)
    def select_korepetytorzy(self):
        print("\nTabela korepetytorzy:\n")
        self.cursor.execute("select * from korepetytorzy")
        for i in self.cursor.fetchall():
            print(i)


    def select_lekcje(self):
        print("\nTabela lekcje:\n")
        self.cursor = self.conn.cursor()
        self.cursor.execute("select concat('id_lekcje: ', l.id_lekcje), concat('imie i nazwisko ucznia: ', u.imie, ' ', u.nazwisko), concat('przedmiot: ', p.nazwa_przedmiotu), concat('imie i nazwisko kor: ', k.imie, ' ', k.nazwisko), concat('dzień tyg: ', dn.dni_tygodnia), concat('godzina: ', g.godziny), concat('data: ', l.data_lekcji) from lekcje l left join uczniowie u on l.id_uczniowie = u.id_uczniowie left join dys_kor d on l.id_dys_kor = d.id_dys_kor left join godz_dys g on d.id_godz_dys = g.id_godz_dys left join dni_tyg dn on d.id_dni_tyg = dn.id_dni_tyg left join przedmioty_korepetytorzy pk on l.id_przedmioty_korepetytorzy = pk.id_przedmioty_korepetytorzy left join przedmioty p on pk.id_przedmioty = p.id_przedmioty left join korepetytorzy k on pk.id_korepetytorzy = k.id_korepetytorzy")
        for i in self.cursor.fetchall():
            print(i)

    def select_uczniowie(self):
        print("\nTabela uczniowie:\n")
        self.cursor.execute("select * from uczniowie")
        for i in self.cursor.fetchall():
            print(i)

    def select_rodzice(self):
        print("\nTabela rodzice:\n")
        self.cursor.execute("select * from rodzice")
        for i in self.cursor.fetchall():
            print(i)

    def select_przedmioty_korepetytorzy(self):
        print("\nTabela przedmioty_korepetytorzy:\n")
        self.cursor.execute("SELECT concat('id_przedmioty_korepetytorzy: ', pk.id_przedmioty_korepetytorzy), concat('id_przedmioty :', pk.id_przedmioty), concat('nazwa_przedmiotu: ', p.nazwa_przedmiotu), concat('id_korepetytorzy: ', pk.id_korepetytorzy), concat('imie i nazwisko kor: ', k.imie, ' ', k.nazwisko) from przedmioty_korepetytorzy pk left join przedmioty p on pk.id_przedmioty = p.id_przedmioty left join korepetytorzy k on pk.id_korepetytorzy = k.id_korepetytorzy")
        for i in self.cursor.fetchall():
            print(i)

    def select_dys_kor(self):
        print("\nTabela dys_kor:\n")
        self.cursor.execute("select concat('id_dys_kor: ', d.id_dys_kor), concat('id_korepetytora: ', k.id_korepetytorzy), concat('imie i nazwisko kor: ', k.imie, ' ', k.nazwisko), concat('id_godz_dys: ', g.id_godz_dys), concat('godziny: ', g.godziny), concat('id_dni_tyg: ', dn.id_dni_tyg), concat('dzień tygodnia: ', dn.dni_tygodnia) from dys_kor d left join godz_dys g on d.id_godz_dys = g.id_godz_dys left join korepetytorzy k on d.id_korepetytorzy = k.id_korepetytorzy left join dni_tyg dn on d.id_dni_tyg = dn.id_dni_tyg")
        for i in self.cursor.fetchall():
            print(i)

    def select_przedmioty(self):
        print("\nTabela przedmioty:\n")
        self.cursor.execute("select * from przedmioty order by id_przedmioty asc")
        for i in self.cursor.fetchall():
            print(i)

    def select_godz_dys(self):
        print("\nTabela godz_dys:\n")
        self.cursor.execute("select * from godz_dys")
        for i in self.cursor.fetchall():
            print(i)

    def select_dni_tyg(self):
        print("\nTabela dni_tyg:\n")
        self.cursor.execute("select * from dni_tyg")
        for i in self.cursor.fetchall():
            print(i)

    def insert_administratorzy(self):
        self.select_administratorzy()
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")
        self.cursor.execute("insert into administratorzy (login, password) values (%s, %s)", (login, haslo))
        self.conn.commit()
        print("Dodano administratora")

    def insert_korepetytorzy(self):
        self.select_korepetytorzy()
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        nr_tel = input("Podaj numer telefonu: ")
        email = input("Podaj adres email: ")
        self.cursor.execute("insert into korepetytorzy (imie, nazwisko, nr_tel, email) values (%s, %s, %s, %s)",
                            (imie, nazwisko, nr_tel, email))
        self.conn.commit()
        print("\nDodano korepetytora.\n")

    def insert_lekcje(self):
        self.select_lekcje()
        self.select_uczniowie()
        self.select_przedmioty_korepetytorzy()
        self.select_dys_kor()
        id_uczniowie = input("Podaj id_uczniowie: ")
        id_przedmioty_korepetytorzy = input("Podaj id_przedmioty_korepetytorzy: ")
        id_dys_kor = input("Podaj id_dys_kor: ")
        data_lekcji = input("Podaj datę lekcji: ")
        self.cursor.execute(
            "insert into lekcje (id_uczniowie, id_przedmioty_korepetytorzy, id_dys_kor, data_lekcji) values (%s, %s, %s, %s)",
            (id_uczniowie, id_przedmioty_korepetytorzy, id_dys_kor, data_lekcji))
        self.conn.commit()
        print("\nDodano lekcje.\n")

    def insert_uczniowie(self):
        self.select_uczniowie()
        self.select_rodzice()
        id_rodzice = input("Podaj id_rodzice: ")
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        ulica = input("Podaj ulice: ")
        nr_dm = input("Podaj numer domu/mieszkania: ")
        miasto = input("Podaj miasto: ")
        kod_pocztowy = input("Podaj kod pocztowy: ")
        nr_tel = input("Podaj numer telefonu: ")
        email = input("Podaj adres email: ")
        self.cursor.execute(
            "insert into uczniowie (id_rodzice, imie, nazwisko, ulica, nr_dm, miasto, kod_pocztowy, nr_tel, email) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (id_rodzice, imie, nazwisko, ulica, nr_dm, miasto, kod_pocztowy, nr_tel, email))
        self.conn.commit()
        print("\nDodano ucznia.\n")

    def insert_rodzice(self):
        self.select_rodzice()
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        nr_tel = input("Podaj numer telefonu: ")
        email = input("Podaj adres email: ")
        self.cursor.execute("insert into rodzice (imie, nazwisko, nr_tel, email) values (%s, %s, %s, %s)",
                            (imie, nazwisko, nr_tel, email))
        self.conn.commit()
        print("\nDodano rodzica.\n")

    def insert_przedmioty_korepetytorzy(self):
        self.select_przedmioty_korepetytorzy()
        self.select_przedmioty()
        self.select_korepetytorzy()
        id_przedmioty = input("Podaj id_przedmioty: ")
        id_korepetytorzy = input("Podaj id_korepetytorzy: ")
        self.cursor.execute(
            "insert into przedmioty_korepetytorzy (id_przedmioty, id_korepetytorzy) values (%s, %s)",
            (id_przedmioty, id_korepetytorzy))
        self.conn.commit()
        print("\nDodano dane do tabeli.\n")

    def insert_dys_kor(self):
        self.select_dys_kor()
        self.select_godz_dys()
        self.select_korepetytorzy()
        self.select_dni_tyg()
        id_korepetytorzy = input("Podaj id_korepetytorzy: ")
        id_godz_dys = input("Podaj id_godz_dys: ")
        id_dni_tyg = input("Podaj id_dni_tyg: ")
        self.cursor.execute("insert into dys_kor (id_korepetytorzy, id_godz_dys, id_dni_tyg) values (%s, %s, %s)", (id_korepetytorzy, id_godz_dys, id_dni_tyg))
        self.conn.commit()
        print("\nDodano dane do tabeli.\n")

    def delete_korepetytorzy(self):
        self.select_korepetytorzy()
        klucz = input("\nPodaj klucz główny rekordu do usunięcia: \n")
        self.cursor.execute("delete from korepetytorzy where id_korepetytorzy = %s", klucz)
        dec = input("\n Czy na pewno usuwamy? t/n\n")
        if (dec == "t"):
            self.conn.commit()
            print("Usunieto.")
        else:
            self.conn.rollback()



    def delete_lekcje(self):
        self.select_lekcje()
        klucz = input("\nPodaj klucz główny rekordu do usunięcia: \n")
        self.cursor.execute("delete from lekcje where id_lekcje = %s", klucz)
        dec = input("\n Czy na pewno usuwamy? t/n\n")
        if (dec == "t"):
            self.conn.commit()
            print("Usunieto.")
        else:
            self.conn.rollback()

    def delete_uczniowie(self):
        self.select_uczniowie()
        klucz = input("\n Podaj klucz główny rekordu do usunięcia: \n")
        self.cursor.execute("delete from uczniowie where id_uczniowie = %s", klucz)
        dec = input("\n Czy na pewno usuwamy? t/n\n")
        if (dec == "t"):
            self.conn.commit()
            print("Usunieto.")
        else:
            self.conn.rollback()

    def delete_rodzice(self):
        self.select_rodzice()
        klucz = input("\n Podaj klucz główny rekordu do usunięcia: \n")
        self.cursor.execute("delete from rodzice where id_rodzice = %s", klucz)
        dec = input("\n Czy na pewno usuwamy? t/n\n")
        if (dec == "t"):
            self.conn.commit()
            print("Usunieto.")
        else:
            self.conn.rollback()

    def delete_przedmioty_korepetytorzy(self):
        self.select_przedmioty_korepetytorzy()
        klucz = input("\n Podaj klucz główny rekordu do usunięcia: \n")
        self.cursor.execute("delete from przedmioty_korepetytorzy where id_przedmioty_korepetytorzy = %s", klucz)
        dec = input("\n Czy na pewno usuwamy? t/n\n")
        if (dec == "t"):
            self.conn.commit()
            print("Usunieto.")
        else:
            self.conn.rollback()

    def delete_dys_kor(self):
        self.select_dys_kor()
        klucz = input("\n Podaj klucz główny rekordu do usunięcia: \n")
        self.cursor.execute("delete from dys_kor where id_dys_kor = %s", klucz)
        dec = input("\n Czy na pewno usuwamy? t/n\n")
        if (dec == "t"):
            self.conn.commit()
            print("Usunieto.")
        else:
            self.conn.rollback()



korkomistrz = DBConnect()
