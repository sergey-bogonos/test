import time
print()
print("Добро пожаловать в кафе - Сладкоежка!!!")
print()
print("В нашем кафе вы можете приобрести: Кофе, Коктейль, Чай, Десерт, Фрукты!")
print()
name = input("Как вас зовут: ")
print("Добро пожаловать в наше кафе -", name)
print()
while True:
    try:
        time.sleep(2)
        kofe = input(str("Вы будете кофе (да или нет): ")) .lower()
        print()
        if kofe == "да":
            time.sleep(0.8)
            print("Вот что мы можем предложить: ")
            print()
            from sklad_kofe import dictkofe

            if dict in dictkofe:
                print(dictkofe.values())
            print()
            time.sleep(1.5)
            kofe = int(input("Выберите кофе под номером: "))
            print()
            if kofe == 1:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 1:
                    cenakofe = 12
                print()
                from sklad_kofe import dictkofe

                kofe = "Эспрессо (30мл)"
                print(dictkofe["1"])
                break
            if kofe == 2:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 2:
                    cenakofe = 12
                print()
                from sklad_kofe import dictkofe

                kofe = "Американо (150мл)"
                print(dictkofe["2"])
                break
            if kofe == 3:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 3:
                    cenakofe = 16
                print()
                from sklad_kofe import dictkofe

                kofe = "Кофе со сливками (120мл)"
                print(dictkofe["3"])
                break
            if kofe == 4:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 4:
                    cenakofe = 14
                print()
                from sklad_kofe import dictkofe

                kofe = "Капучино (170мл)"
                print(dictkofe["4"])
                break
            if kofe == 5:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 5:
                    cenakofe = 19
                print()
                from sklad_kofe import dictkofe

                kofe = "Латте (200мл)"
                print(dictkofe["5"])
                break
            if kofe == 6:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 6:
                    cenakofe = 16
                print()
                from sklad_kofe import dictkofe

                kofe = "Гляссе (170мл)(кофе мороженое)"
                print(dictkofe["6"])
                break
            if kofe == 7:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 7:
                    cenakofe = 17
                print()
                from sklad_kofe import dictkofe

                kofe = "Цветок Миндаля (150мл)"
                print(dictkofe["7"])
                break
            if kofe == 8:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 8:
                    cenakofe = 12
                print()
                from sklad_kofe import dictkofe

                kofe = "Детский капучино (150мл) (какао, молоко, шоколад)"
                print(dictkofe["8"])
                break
            if kofe == 9:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 9:
                    cenakofe = 10
                print()
                from sklad_kofe import dictkofe

                kofe = "Молоко с медом (150мл)"
                print(dictkofe["9"])
                break
            if kofe == 10:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if kofe == 10:
                    cenakofe = 3
                print()
                from sklad_kofe import dictkofe

                kofe = "Сироп в ассортименте (25мл)"
                print(dictkofe["10"])
                break
        elif kofe == "нет":
            time.sleep(0.5)
            cenakofe = 0
            print("Очень жаль оно у нас самое лучшее, пошли дальше по меню: ")
            print()
            break
        else:
            print("Выберите (да) или (нет)")
            time.sleep(0.5)
    except:
        print("Введите цифру из меню:")
        continue

while True:
    try:
        time.sleep(0.8)
        kokt = input(str("Вы будете коктейл? (да/нет/ничего): ")) .lower()
        if kokt == "да":
            print()
            print("Вот наше меню по коктейлям: ")
            print()
            from sklad_kokteli import dictkokt

            if dict in dictkokt:
                print(dictkokt.values())
                print()
            time.sleep(0.5)
            kokt = int(input("Выберите номер коктейля: "))
            print()
            if kokt == 1:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 1:
                    cenakokt = 12
                print()
                from sklad_kokteli import dictkokt

                kokt = "Коктейль молочный в ассортименте (180мл) (молоко, мороженое, сироп)"
                print(dictkokt['1'])
                break
            elif kokt == 2:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 2:
                    cenakokt = 17
                print()
                from sklad_kokteli import dictkokt

                kokt = "Айсберг (180мл) (молоко, мороженое, лед, сироп Blue Curacao, сливки)"
                print(dictkokt['2'])
                break
            elif kokt == 3:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 3:
                    cenakokt = 14
                print()
                from sklad_kokteli import dictkokt

                kokt = "Милк банан (180мл) (молоко, банан, сироп)"
                print(dictkokt['3'])
                break
            elif kokt == 4:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 4:
                    cenakokt = 18
                print()
                from sklad_kokteli import dictkokt

                kokt = "Пина колада (220мл) (сок, кокосовый сироп, сливки)"
                print(dictkokt['4'])
                break
            elif kokt == 5:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 5:
                    cenakokt = 22
                print()
                from sklad_kokteli import dictkokt

                kokt = "Сахара (220мл) (сок, киви, банан, сироп, лимонный сок, сливки)"
                print(dictkokt['5'])
                break
            elif kokt == 6:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 6:
                    cenakokt = 18
                print()
                from sklad_kokteli import dictkokt

                kokt = "Зелёный попугай (220мл)(сок, киви, лимонный сок, сироп Blue Curacao )"
                print(dictkokt['6'])
                break
            elif kokt == 7:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 7:
                    cenakokt = 15
                print()
                from sklad_kokteli import dictkokt

                kokt = "Молодёжный (180мл) (сок в ассортименте, мороженое)"
                print(dictkokt['7'])
                break
            elif kokt == 8:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 8:
                    cenakokt = 15
                print()
                from sklad_kokteli import dictkokt

                kokt = "Первоклашка (220мл) (сок, молоко, сироп)"
                print(dictkokt['8'])
                break
            elif kokt == 9:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 9:
                    cenakokt = 21
                print()
                from sklad_kokteli import dictkokt

                kokt = "Умница (180мл) (молоко, какао, грецкий орех, сироп)"
                print(dictkokt['9'])
                break
            elif kokt == 10:
                time.sleep(0.5)
                print('Вы выбрали')
                if kokt == 10:
                    cenakokt = 20
                print()
                from sklad_kokteli import dictkokt

                kokt = "Поплавок (180мл) (мороженое, кефир детский, сливки)"
                print(dictkokt['10'])
                break
        elif kokt == "нет":
            cenakokt = 0
            time.sleep(0.5)
            print("Хорошо, может чай?")
            break
        elif kokt == "ничего":
            time.sleep(1)
            print()
            print(name)
            print("Ваш заказ составил: ")
            print()
            print("Меню кофе: ", kofe)
            print("Стоимость заказа: ", cenakofe, "рублей")
            print("Спасибо за визит в наше кафе, приходите еще!!!")
            input('для выхода нажмите enter')
            quit()
            continue
        else:
            print('Извините такого коктейля нет, выберите вариант из меню!')
    except:
        print("Выберите цифру из меню!")
        quit()

while True:
    try:
        time.sleep(0.5)
        chai = input("Будете чай? (да/нет/ничего): ") .lower()
        if chai == "да":
            print()
            time.sleep(0.5)
            print("Вот список нашего чая: ")
            print()
            from sklad_chai import dictchai

            if dict in dictchai:
                print(dictchai.values())
            print()
            time.sleep(0.5)
            chai = int(input("Выберите какой чай вы будете: "))
            if chai == 1:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if chai == 1:
                    cenachai = 16
                print()
                from sklad_chai import dictchai

                chai = "Чай заварной в ассортименте (450мл)"
                print(dictchai["1"])
                break
            elif chai == 2:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if chai == 2:
                    cenachai = 20
                print()
                from sklad_chai import dictchai

                chai = "Чай заварной в ассортименте (600мл)"
                print(dictchai["2"])
                break
            elif chai == 3:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if chai == 3:
                    cenachai = 6
                print()
                from sklad_chai import dictchai

                chai = "Мёд (45гр)"
                print(dictchai["3"])
                break
            elif chai == 4:
                time.sleep(0.5)
                print("Вы выбрали: ")
                if chai == 4:
                    cenachai = 2
                print()
                from sklad_chai import dictchai

                chai = "Лимон (30гр)"
                print(dictchai["4"])
                break
            else:
                time.sleep(0.5)
                print("Такого чая нет, продолжим по меню!")

        elif chai == "нет":
            time.sleep(0.5)
            cenachai = 0
            print("Окей пойдем дальше по меню!")
            break
        elif chai == "ничего":
            time.sleep(0.5)
            print()
            print(name)
            print("Ваш заказ составил: ")
            print()
            print("Меню кофе: ", kofe)
            print("Меню коктейли: ", kokt)
            print("Стоимость заказа: ", cenakofe + cenakokt, "рублей")
            print("Спасибо за визит в наше кафе, приходите еще!")
            input('для выхода нажмите enter')
            quit()
            continue
        else:
            print("Извините вы что то указали не правильно! (да/нет/ничего)")

    except:
        print("Выберите цыфру из меню")
        quit()
    print()
while True:
    try:
        time.sleep(1)
        print()
        des = input("Вы будете десерт? (да/нет/ничего): ") .lower()
        if des == "да":
            time.sleep(0.5)
            print('Вот наши десерты:')
            print()
            from sklad_desert import dictdes

            if dict in dictdes:
                print(dictdes.value())
            print()
            des = int(input("Выберите десерт из меню: "))
            print()
            if des == 1:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 1:
                    cenades = 6
                from sklad_desert import dictdes

                des = "Мороженое (Рожок) (90гр)"
                print()
                print(dictdes["1"])
                break
            if des == 2:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 2:
                    cenades = 19
                from sklad_desert import dictdes

                des = "Мороженое (Наш Малыш) (120/30гр) (мороженое, шоколад, орехи, сироп, сливки)"
                print()
                print(dictdes["2"])
                break
            if des == 3:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 3:
                    cenades = 21
                from sklad_desert import dictdes

                des = "Мороженое (Фруктовое настроение) (90/100гр) (мороженое, фрукты, сироп, сливки)"
                print()
                print(dictdes["3"])
                break
            if des == 4:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 4:
                    cenades = 19
                from sklad_desert import dictdes

                des = "Мороженое (Три Богатыря) (75/150гр) (мороженое, шоколад, орехи, сливки)"
                print()
                print(dictdes["4"])
                break
            if des == 5:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 5:
                    cenades = 15
                from sklad_desert import dictdes

                des = "Мороженое с сиропон (125гр) (мороженое, сироп в ассортименте)"
                print()
                print(dictdes["5"])
                break
            if des == 6:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 6:
                    cenades = 19
                from sklad_desert import dictdes

                des = "Салат (Тутти фрутти) (150гр) (фрукты, сироп, сливки)"
                print()
                print(dictdes["6"])
                break
            if des == 7:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 7:
                    cenades = 21
                from sklad_desert import dictdes

                des = "Десерт (Винни пух)(120гр) (бисквит, сгущенное молоко, фрукты, соус, сливки)"
                print()
                print(dictdes["7"])
                break
            if des == 8:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 8:
                    cenades = 19
                from sklad_desert import dictdes

                des = "Десерт (Солнечный кристал) (120гр) (фрукты, соус, желе)"
                print()
                print(dictdes["8"])
                break
            if des == 9:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 9:
                    cenades = 22
                from sklad_desert import dictdes

                des = "Десерт (Два острова) (150гр) (молочное и шоколадное суфле)"
                print()
                print(dictdes["9"])
                break
            if des == 10:
                time.sleep(0.5)
                print('Вы выбрали:')
                if des == 10:
                    cenades = 19
                from sklad_desert import dictdes

                des = "Десерт - коктейл (Яблочный штрудель) (220мл) (сок, молоко, мёд, грецкие орехи, сироп, корица)"
                print()
                print(dictdes["10"])
                break
        elif des == "нет":
            time.sleep(1)
            cenades = 0
            print("Хорошо тогда может фрукты?")
            break
        elif des == "ничего":
            time.sleep(1)
            print("Очень жаль у нас лучшие десерты в городе и шикарное меню, ждём вас еще!")
            print()
            print(name)
            print("Ваш заказ составил: ")
            print()
            print("Меню кофе: ", kofe)
            print("Меню коктейли: ", kokt)
            print("Меню чай: ", chai)
            print("Стоимость заказа: ", cenakofe + cenakokt + cenachai, "рублей")
            print("Спасибо за визит в наше кафе, приходите еще!")
            input('для выхода нажмите enter')
            quit()
            break

        else:
            print("Извините такого варианта у нас нет!")

    except:
        print()
        quit()
while True:
    try:
        time.sleep(1)
        print()
        fr = input("Фрукты будем? (да/нет/ничего):") .lower()
        if fr == "да":
            time.sleep(0.5)
            print()
            print('Смотрите какие у нас фрукты:')
            print()
            from sklad_frukti import dictfr, dictfr_cena

            if dict in dictfr:
                print(dictdfr.value())
                print()
            time.sleep(0.5)
            fr = int(input("Выберите фрукты из меню: "))
            print()
            if fr == 1:
                time.sleep(0.5)
                print('Вы выбрали:')
                if fr == 1:
                    cenafr = 4
                from sklad_frukti import dictfr, dictfr_cena


                fr = "Банан (1шт)"
                print()
                print(dictfr["1"])
                break
            if fr == 2:
                time.sleep(0.5)
                print('Вы выбрали:')
                from sklad_frukti import dictfr, dictfr_cena

                if fr == 2:
                    cenafr = 4
                fr = "Киви (1шт)"
                print()
                print(dictfr["2"])
                break
            if fr == 3:
                time.sleep(0.5)
                print('Вы выбрали:')
                from sklad_frukti import dictfr

                if fr == 3:
                    cenafr = 3.50
                fr = "Апельсин (100гр)"
                print()
                print(dictfr["3"])
                break
            if fr == 4:
                time.sleep(0.5)
                print('Вы выбрали:')
                from sklad_frukti import dictfr

                if fr == 4:
                    cenafr = 5
                fr = "Мандарин (1шт)"
                print()
                print(dictfr["4"])
                break
            if fr == 5:
                time.sleep(0.5)
                print('Вы выбрали:')
                from sklad_frukti import dictfr

                if fr == 5:
                    cenafr = 3.50
                fr = "Яблоко (100гр)"
                print()
                print(dictfr["5"])
                break
            if fr == 6:
                time.sleep(0.5)
                print('Вы выбрали:')
                from sklad_frukti import dictfr

                if fr == 6:
                    cenafr = 3.50
                fr = "Груша (100гр)"
                print()
                print(dictfr["6"])
                break
            if fr == 7:
                time.sleep(0.5)
                print('Вы выбрали:')
                from sklad_frukti import dictfr

                if fr == 7:
                    cenafr = 3.50
                fr = "Виноград (100гр)"
                print()
                print(dictfr["7"])
                break
            print()
        elif fr == "нет":
            time.sleep(0.5)
            cenafr = 0
            print("Очень жаль, такие фрукты вы не купите нигде!")
            print()
            break
        elif fr == "ничего":
            time.sleep(1)
            print()
            print(name)
            print("Ваш заказ составил: ")
            print()
            print("Меню кофе: ", kofe)
            print("Меню коктейли: ", kokt)
            print("Меню чай: ", chai)
            print("Меню десерты: ", des)
            print("Стоимость заказа: ", cenakofe + cenakokt + cenachai + cenades)
            print("Очень жаль у нас лучшие фрукты на районе и шикарное меню, ждём вас еще!")
            quit()
            continue
        else:
            print("Вы что то нажали не так")

    except:
        print()
        quit()
time.sleep(1)
print()
print(name, "вот ваш чек:")
print("Ваш заказ составил: ")
print()
print("Меню кофе: ", kofe)
print("Меню коктейли: ", kokt)
print("Меню чай: ", chai)
print("Меню десерты: ", des)
print("Меню фрукты: ", fr)
print()
print("Стоимость заказа: ", cenakofe + cenakokt + cenachai + cenades + cenafr, "Рублей")
print("Спасибо за покупку, приходите еще!")
input('для выхода нажмите enter')
