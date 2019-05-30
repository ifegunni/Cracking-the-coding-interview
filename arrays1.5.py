# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false

def oneEditaway(str1, str2):   #create a function that checks if length condition is met before calling other functions to do the work.
    if len(str1) == len(str2):   # check if len of both strings are the same which mean edit was a replace
        return(replace(str1, str2))

    elif len(str1) + 1 == len(str2):    # check if len of the first string is lower by 1, which mean edit was an insert
        return(insert(str1, str2))

    elif len(str1) - 1 == len(str2):    # check if len of the first string is greater by 1, which mean edit was a removal

        return(remove(str1, str2))

    else:                     #else there was more that one edit
        return False


def replace(str1, str2):
    check = False      # create a flag
    for i in range(len(str1)):
        if str1[i] != str2[i]:   #check if the elemenets in string are the same
            check = True
        else:
            check = False
    return check


def insert(str1, str2):

    for i in range(len(str1)):
        if str1[i] != str2[i]:   #check if element are the same if not
            if str1[i] == str2[i+1]:  #check if the element in string one is the same as the next element
                return True
            else:
                return False


def remove(str1, str2):
    for i in range(len(str2)):
        if str1[i] != str2[i]:   #check if element are the same if not
            if str1[i+1] == str2[i]: #check if the next element in string one is the same as the  element in the second string
                return True
            else:
                return False
        else:
            return True



if __name__ == '__main__':
    str1 = "pales"
    str2 = "bales"
    print(oneEditaway(str1, str2))
