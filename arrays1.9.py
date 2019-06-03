# String Rotation: Assumeyou have a method i5Sub 5tring which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to i5Sub5tring (e.g.,"waterbottle" is a rotation of"erbottlewat").

def isSubstring(s1,s2):

    if s2 in s1:
        return True

    else:
        return False

def isolate(s1, s2):

    string1 = s1 + s1

    return isSubstring(string1, s2)


if __name__ == '__main__':

    s1 = "waterbottle"
    s2 = "erbottlewat"

    print(isolate(s1,s2))
