isikukood = input("Palun sisesta oma isikukood: ").split()
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
        if sugu > 6 or aasta > 99 or kuu > 12 or paev > 31:
            print("Vale isikukood!")
        elif sugu == 1 or sugu == 3 or sugu == 5:
            print("Aitah! Te olete mees ja teie sünnipäev: ", paev, ".", kuu, ".19", aasta, sep="")
        elif sugu == 2 or sugu == 4 or sugu == 6:
            print("Aitah! Te olete näine ja teie sünnipäev: ", paev, ".", kuu, ".19", aasta, sep="")
        else:
            print("Ne znaju zachem ese else nuzen, no pust budet")