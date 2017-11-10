import random

# str is a string, int is size(integer)
#The function is used to given a str and a size (an int) return a list of length size of single character strs comprised of the characters in the given str.
#For example, given the string 'YGBOPR' and int 4, one possible list is ['G', 'B', 'R', 'B'].
def create_code(str, int):
        length = len(str);
        Codestr = []
        for i in range(int):
            character=random.choice(str)
            Codestr.append(character)
        return Codestr

#list is single character strs, str is a string, int is the size
#The function is used to return True if every character is in the given str and the list of length equal to the given int.
#For example, given the list 'afd', str 'abcdef', int 4, it will return True
def valid(list,str,int):
    j=0
    for i in range(len(list)):
        if list[i] in str and len(list)== int:
            j=j+1
            if j==4:
                return True
        else:
            return False
            break

#list_1 is answer code, list_2 is guess
#The function is used to return a list containing a 'b' for each correctly positioned colour in the guess.
#For example, if the answer code is['P', 'G', 'R', 'O'] and the guess is ['Y', 'G', 'O', 'O']then return ['b', 'b'].
def find_fully_correct(list_1, list_2):
    correct_result=[]
    for i in range(len(list_1)):
        if list_2[i] == list_1[i]:
            correct_result.append('b')
    return correct_result

#list_1 is answer code, list_2 is guess
#The function is used to return a new list that is the result of removing from the first list all chars that are the same and in the same position in the second list.
#For example, if the lists are ['A','B','C','D'] and ['D','B','A','D'] then['A', 'C'] is returned.
def remove_fully_correct(list_1, list_2):
    returned_list=[]
    for i in range(len(list_1)):
        if list_1[i]!=list_2[i]:
            returned_list.append(list_1[i])
    return returned_list

#list_1 is answer code, list_2 is guess
#The function is used to return a list of 'w's where the number of 'w's is equal to the number of str in the second list that have the same value as str in the first list but different position.
#For example if the two lists are['Y','P','G','G'] and ['G','P','O','R'] return ['w'].
def find_colour_correct(list_1, list_2):
    returned_list = []
    list_3 = remove_fully_correct(list_1, list_2)
    list_4 = list(set(list_3))
    list_5 = remove_fully_correct(list_2, list_1)
    list_6 = list(set(list_5))
    for i in range(len(list_4)):
        for j in range(len(list_6)):
           if list_4[i] == list_6[j]:
               returned_list.append('w')
    return returned_list

#list_1 is list of guess and list_2 is list of clues
#The function is used to return a string (that could be printed to the display the current state of the game.
def display_game(list_1,list_2):
    returned_list="Guess\tClues\n****************\n"
    for i in range(len(list_1)):
        line = ' '.join(list_1[i]) + '\t' + ' '.join(list_2[i]) + '\n'
        returned_list = returned_list + line
    return print(returned_list)









