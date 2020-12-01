def ID():
    try:
        identity_code = input("Please insert personal identity code: ")
        array_identity_code = list(identity_code)
        controll_symbol = list("0123456789ABCDEFHJKLMNPRSTUVWXY")
        controll_number = int((((int("".join(array_identity_code[0:6]+array_identity_code[7:10])))/31) - ((int("".join(array_identity_code[0:6]+array_identity_code[7:10])))//31))*31) #Считает позицию управляющего символа

        if array_identity_code[10] == controll_symbol[controll_number]: #Сравнивает позицию управляющего символа с позицией в листе
            if array_identity_code[6] == str("+"):
                year = str('18')
            elif array_identity_code[6] == str("-"):
                year = str('19')
            elif array_identity_code[6] == str("A"):
                year = str('20')

            perem = year + str("".join(array_identity_code[4:6]))
            print("Your birhtday date: " + str("".join(array_identity_code[0:2])) + "." + str("".join(array_identity_code[2:4])) + "." +
                    perem)

            check_status = int("".join(array_identity_code[7:10]))
            if check_status >= 2 and check_status <= 899:
                print("You are true Finland person!")
            elif check_status >= 900 and check_status <= 999:
                print("Your status: Dzamsut")
            else:
                print("Wrong identity code!")
                ID()
            if check_status % 2 == 0:
                print("You are famale.")
            else:
                print("You are male.")
        else:
            print("False personal identity code")
            ID()

    except IndexError:
        print("Wrong identity code !")
        ID()
    except ValueError:
        print("Wrong identity code !")
        ID()

ID()

ID()
