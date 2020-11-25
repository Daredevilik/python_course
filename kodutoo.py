print("This program calculate taxes which you pay from gross salary")
sal = float(input("Please insert your gross salary: "))
while sal <= 0:
    sal = float(input("WRONG! Please insert your gross salary: "))


def maksavaba():
    if sal <= 500:
        maks = 0
    elif sal <= 600:
        maks = 20
    elif sal <= 800:
        maks = 40
    elif sal <= 1000:
        maks = 60
    else:
        maks = 100

    return maks


kogumispension = sal * 0.0149
tootuskindlustusmakse = sal * 0.012
tulumaks = sal * 0.14
netsal = sal - kogumispension - tootuskindlustusmakse - tulumaks - maksavaba()

print("Kogumispension (1.49%): ", kogumispension, "\nTootuskindlustusmakse (1.2%): ", tootuskindlustusmakse,
      "\nTulumaks (14%): ", tulumaks, "\nMaksavaba tulu: ", maksavaba(), "\nNetsalary: ", netsal)