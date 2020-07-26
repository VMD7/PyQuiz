#pyquiz

import random
#create a function to get difinition and pop
def get_definition_and_pop(wd_list,wd_dct):
    random_index = random.randrange(len(wd_list))
    word = wd_list.pop(random_index)
    definition = wd_dct.get(word)
    return word, definition

#creat a function for split word and definition
def word_and_definition(rawstring):
    word, definition = rawstring.split(',',1)
    return word, definition

def main():
    # Read the file
    fh = open("Vocabulary_list.csv", "r")
    wd_list = fh.readlines()

    # Remove the first line from the file
    wd_list.pop(0)

    # Remove duplicates and store it in another file
    # For remove duplicate we can use set data structure
    wd_set = set(wd_list)
    fh = open("Vocabulary_set.csv", "w")
    fh.writelines(wd_set)

    # create dictionary to store the word with definition
    wd_dct = {}
    for rawstring in wd_set:
        word, definition = word_and_definition(rawstring)
        wd_dct[word] = definition

    # creating user interface for choice
    while True:
        wd_list = list(wd_dct)
        choice_list = []
        for x in range(4):
            word, definition = get_definition_and_pop(wd_list, wd_dct)
            choice_list.append(definition)
        random.shuffle(choice_list)
        print(word)
        print("________")
        for idx, choice in enumerate(choice_list):
            print(idx + 1, choice)
        choice = int(input('Enter 1,2,3 or 4: o to exit\n'))
        if choice_list[choice - 1] == definition:
            print('Correct!!\n\n')
        elif choice == 0:
            exit()
        else:
            print('Incorrect\n\n')
if __name__ =='__main__':
    main()



