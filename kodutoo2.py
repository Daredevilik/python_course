cnt = 0
for char in isikukood:
    if not (char.isdigit() or char == '/'):
        print("Isikukoodis ei saa kasutada tähed. Ainult numbrid!")
        break
    for i,s in enumerate(isikukood):
        if s.isdigit():
            cnt += len(s)
    if cnt > 11 or cnt < 11:
        print("Vale isikukood! Isikukoodis peab olema 11 numbrid.")
    else:
        isikukood = s
        sugu = int(s[0])
        aasta = int(s[1:3])
        kuu = int(s[3:5])
        paev = int(s[5:7])
        region = int(s[7:10])
        bday = str(paev) + "." + str(kuu)+ ".19" + str(aasta)
        try:
            bday_formated = datetime.datetime.strptime(bday, '%d.%m.%Y')
            today = date.today()
            age = today.year - bday_formated.year - ((today.month, today.day) < (bday_formated.month, bday_formated.day))
            if sugu > 6 or aasta > 99 or kuu > 12 or paev > 31:
                print("Vale isikukood!")
            elif sugu == 1 or sugu == 3 or sugu == 5:
                print("Aitah! Te olete mees ja teie sünnipäev:", bday_formated.date().strftime('%d.%m.%Y'))
            elif sugu == 2 or sugu == 4 or sugu == 6:
                print("Aitah! Te olete näine ja teie sünnipäev:", bday_formated.date().strftime('%d.%m.%Y'))
            print("Teile on praegu", age, "aastat")
            if 0 <= region <= 10:
                print("Te olite sündinud Kuressaare Haiglas")
            elif 11 <= region <= 19:
                print("Te olite sündinud Kuressaare Tartu Ülikooli Naistekliinikus, Tartumaa, Tartu")
            elif 21 <= region <= 220:
                print("Te olite sündinud Kuressaare  Ida-Tallinna Keskhaiglas või Pelgulinna sünnitusmajas või Hiiumaal või Keilas või Rapla haiglas või Loksa haiglas")
            elif 221 <= region <= 270:
                print("Te olite sündinud Ida-Viru Keskhaiglas (Kohtla-Järve, endine Jõhvi)")
            elif 271 <= region <= 370:
                print("Te olite sündinud Maarjamõisa Kliinikumis (Tartu) või Jõgeva Haiglas")
            elif 371 <= region <= 420:
                print("Te olite sündinud Narva Haiglas")
            elif 421 <= region <= 470:
                print("Te olite sündinud Pärnu Haiglas")
            elif 471 <= region <= 490:
                print("Te olite sündinud Pelgulinna Sünnitusmajas (Tallinn) või Haapsalu haiglas")
            elif 491 <= region <= 520:
                print("Te olite sündinud Järvamaa Haiglas (Paide)")
            elif 521 <= region <= 570:
                print("Te olite sündinud Rakveres või Tapa haiglas")
            elif 571 <= region <= 600:
                print("Te olite sündinud Valga Haiglas")
            elif 601 <= region <= 650:
                print("Te olite sündinud Viljandi Haiglas")
            elif 651 <= region <= 700:
                print("Te olite sündinud Lõuna-Eesti Haiglas (Võru) või Põlva Haiglas")
        except ValueError:
            print("Vale isikukood!")
