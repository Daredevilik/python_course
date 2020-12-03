def choose1():
    print('Option1')

def choose2():
    print('Option2')


print('Please choose option:\n 1) ..... \n 2) ......... \n 3) Close program\n')
choose = int(input('Type here: '))

if choose == 1:
    choose1()
elif choose == 2:
    choose2()
elif choose == 3:
    print('Thank you!')
    exit()