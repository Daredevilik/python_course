def choose1():
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

    infile.close()



def choose2():
    print('Option2')

def check():
    print('Please choose option:\n 1) Calculate words and unique words \n 2) ......... \n 3) Close program\n')
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
