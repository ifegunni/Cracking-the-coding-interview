#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #7 77, #732



#My O(n^2) solution

def uniqueChar(string):
    for i in range(0, len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                break
    print("%s is not unique because of multiple %s", string, string[i])

uniqueChar("jonathan")



#My O(n) solution

def uniqueChar(string):

    if len(string) > 128:   #check if the lenght of the string is more 128 or 256 ASCII character
        return False # return false

    charSet = [False] * 128  #Create a boollean array that to record occurrence of unique character

    for i in range(0, len(string)): #for each element in the string
        val = ord(string[i]) #convert to its equivalent ASCII code using the ord method
        if charSet[val]:  # check if this method has been seen before if so return false,
            return False

        charSet[val] = True #if not assign true to the index val representing the element
    return True #finally return true if string is traversed and all values were unique
print(uniqueChar("abcdefgh"))




#My n(nlogn) solution

def uniqueChar3(string):
    elem = []
    for i in string:
        elem.append(i)

    sortedElem = sorted(elem)

    for i in range(len(sortedElem)):
        if sortedElem[i] == len(sortedElem)-1:
            if sortedElem[i] == sortedElem[i+1]:
                return False
    return True

print(uniqueChar3("abcdefgh"))







