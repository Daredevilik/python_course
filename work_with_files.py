def user_input():
    user_choise = input("1. Parse one file, 2: Parse directory, 3: Exit \n --->")
    if user_choise == "1":
        filename = input("Please enter filename: \n --->")
        check_file_exist(filename)
        user_input()
    elif user_choise == "2":
        user_input()
    elif user_choise == "3":
        print("Have a nice day!")
        exit()
    else:
        print("Entered wrong number, please choose 1 or 2 or 3")
        user_input()

def check_file_exist(file_name):
    try:
        with open(file_name + '.txt', 'r', encoding='UTF8') as file:
            data = file.read()
        parse_one_file(data)
    except FileNotFoundError:
        print('File ' + file_name + '.txt doesn\'t exist!')
        user_input()
    return data

def parse_one_file(data):
    data = data.lower().replace('\n', '')
    symbols_list = ['.', ',', '!', '?']
    for sym in symbols_list:
        data = data.replace(sym, '')
    word_list = data.split(' ')
    word_count = len(word_list)
    word_set = set(word_list)
    unique_count = len(word_set)
    save_file(filename, word_set, word_count, unique_count)

def save_file(filename, word_set, word_count, unique_count):
    with open(filename + '_copy.txt', 'w', encoding='UTF8') as result:
        result.write("Word counter: " + str(word_count) + "\n")
        result.write("Unique counter: " + str(unique_count) + "\n")
        for word in word_set:
            result.write(word + '\n')

user_input()
