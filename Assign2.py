
# Rubaisha Aslam
# Assignment: 2
# To program this Soundex Algorithm, I have used user input, while loop, for loops, lists, conditionals and functions.
# With this program we will be able to find soundex, compare them and see Soundex algorithm for simplicity.

# first we will create a function which will prompt us to ask for the names
def add_name():
    print('Enter names, one on each line. Type DONE to quit entering names.')
    user_name = ""
    name_inputs = []
    while user_name != "DONE":
        user_name = input()
        if user_name == "DONE":
            break
        else:
            name_inputs.append(user_name)
    return name_inputs


# A function to complete step 3- compare the letters and numbers and start a new string
def replacement_digit(name):
    # list of letters to compare in function
    letters0 = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
    letters1 = ['b', 'f', 'p', 'v']
    letters2 = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']
    letters3 = ['d', 't']
    letters4 = ['l']
    letters5 = ['m', 'n']
    letters6 = ['r']
    D = ''
    space = ''
    # for loop that checks the character and changes it with the digit desired for the replacement
    for char in range(len(name)):
        if name[char] in letters0:
            D = D + "0"
        if name[char] in letters1:
            D = D + "1"
        if name[char] in letters2:
            D = D + "2"
        if name[char] in letters3:
            D = D + "3"
        if name[char] in letters4:
            D = D + "4"
        if name[char] in letters5:
            D = D + "5"
        if name[char] in letters6:
            D = D + "6"
    return D


# the function removes digits that are stated more than once in the string
def remove_repeats(user_rep):
    position = 1
    while position in range(len(user_rep)):
        if user_rep[position] == user_rep[position - 1]:
            repeats = user_rep[:position] + user_rep[position + 1:]
            user_rep = repeats
        elif user_rep[position] != user_rep[position - 1]:
            position = position + 1
    return user_rep


# function to make the combination of numbers equal to 4
# if it already has 4 digits leave it, if it has less than 4 add 0 and if it has more remove
def len_equal_four(user_len):
    user_len2 = len(user_len)
    if user_len2 == 4:
        user_len = user_len
    elif user_len2 < 4:
        user_len3 = 4 - user_len2
        user_len = user_len + ("0" * user_len3)
    elif user_len2 > 4:
        user_len = user_len[:4]

    return user_len


# function bring everything together and create the soundex
def overall(user_name):
    user_lower = user_name.lower()
    F1 = user_lower[0]  # First letter save for later
    D = remove_repeats(replacement_digit(user_lower))  # the functions remove_repeats and replacement_digit applied
    D = D.replace("0", "")  # if there are 0s they are removed
    F = replacement_digit(F1)  # first letter replaced with digit
    # check if the length of the digits are more than 0 if yes, letter added to the last 3 digits depending on their condition
    if len(D) > 0:
        if F == D[0]:
            D = F1 + D[1:]
        elif len(D) == 0:
            D = F1
        else:
            D = F1 + D
    len_D = len_equal_four(D)
    return len_D


# main function to compare soundex and print which ones are the same
def main():
    # create list and and sorts them alphabetically than makes a list of all the soundex
    listOfNames = add_name()
    listOfNames.sort()
    soundexList = []
    for i in range(len(listOfNames)):
        soundexList.append(overall(listOfNames[i]))
    # compare soundex by doing a nested loop and printing which names have the same soundex
    listOfOutput = []
    lenSoundexList = len(soundexList)
    y = 0
    while lenSoundexList > y:
        z = y + 1
        while z in range(lenSoundexList):
            if soundexList[y] == soundexList[z]:
                listOfOutput.append(listOfNames[y] + " and " + listOfNames[z] + ' have the same Soundex encoding.')
            z = z + 1

        y = y + 1
    # print statement
    for a in range(len(listOfOutput)):
        print(listOfOutput[a])


# recall function
main()
