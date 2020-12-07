def choose1():
    try:
        fname = input("Enter the name of the file:")
        infile = open(fname, 'r')
        uniques = set()
        words = 0
        for line in infile:
            wordslist = line.split()
            uniques |= set(line.split())
            words = words + len(wordslist)
            outfile = open(fname + "_copy.txt", 'w', encoding='UTF8')
            outfile.write("In this text: " + str(words) + " words.\n" + "Unique words: " + str(uniques) + " ( " + str(len(uniques)) + " pcs )")
            print('Great! Please check file with name _copy.txt !')
        infile.close()

    except FileNotFoundError:
        print("Wrong filename!")
        choose1()



def choose2():
    print('Option2')

def check():
    print('Please choose option:\n 1) Calculate words and unique words \n 2) Calculate words and unique words in directory \n 3) Close program\n')
    choose = int(input('Type here:'))

    if choose == 1:
        choose1()
    elif choose == 2:
        choose2()
    elif choose == 3:
        print('\nThank you!')
        exit()
    else:
        print('\nChoose from 1 to 3')
        check()
try:
    check()
except ValueError:
    print('\nOnly numbers!')
    check()
