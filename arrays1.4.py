#  Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat'; "atco eta·; etc.)

#my solution O(n)
def palindromePermutation(phrase):
    value = 0
    phrase = phrase.lower()   #convert all element of the string to lower case
    dic = {}                 #intial a dictionary to count the number of occurence of each element in the string
    for key in phrase:       #traverse through each element in the string and count it's occurence
        if key != " " and key in dic:
            dic[key] += 1
        elif key != " ":
            dic[key] = 1
        elif key == " ":  #also take note of the number of spaces in the string and so we can know the actual lenght of the string
            value += 1
    lenght = len(phrase) - value # calculating the actual lenght of the string

    if lenght % 2 == 0:  #if this lenght is even then we need to ensure that the every character in the string has an even occurence
        for key in dic:
            if dic[key] % 2 != 0:
                return False

    if lenght % 2 != 0: #if this lenght is odd  then we need to ensure that atmost one character has an old occurence
        count = 0
        for key in dic:     #checking the number of keys with odd occurence
            if dic[key] % 2 != 0:
                count += 1
        if count > 1:
            return False
        else:
            return True


if __name__ == '__main__':
    j = "atco cta"
    print(palindromePermutation(j))
