# URLif: Write a method to replace all spaces in a string with '%20' You may assume that the string
# has suffcient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"


#My first soltion with Output: "Mr%20John%20Smith%20" It failed to indentify the end of the string and added an extra %20
# Time complexity is O(n)

def URLify(string):
    str = ''
    for i in string:
        if i == " ":
            str = str + "%20"
        else:
            str = str + i

    return str

if __name__ == '__main__':
    j = "Mr John Smith "
    print(URLify(j))
    
 
 
 
 #My second soltion with Output: "Mr%20John%20Smith"
 #time complexity O(n)
 
 def URLify2(string):
    str = ''   #create an empty string since string can't be easily manipulated

    filled = False #create a flag for indicating whitespaces

    for i in reversed(string):  #traverse through the each element in the list reversed for find the actual
        if i != " ":     #end of the string. if character set flag to True
            filled = True # this means that we are the actual end of the string
        if i == " " and filled == True: #From here on, every whitespaces would be replaced with a "%20" and vice versa
            str = "%20" + str
        else:
            str =  i + str
    return(str)
    
    
    
    
#Cracking the coding solution, implemented in python by me
#time complexity O(n)
    
def URLify2(string, lenght):   #This algorithm is broken in different phase
    spaceCount = 0  #first phase involves counting the number of spaces in the string
    for i in range(lenght-1, -1, -1): #traversing backwards through the string to Implement space count
        if string[i] == " ":
            spaceCount += 1
    index = spaceCount * 2 + (lenght) #calculate the amount of slots need for the new string
    charArray = [None] * index   #initialing a new array and setting it size
    for i in range(lenght-1,-1, -1):
        if string[i] != " ":   #checking to for spaces
            charArray[index-1] = string[i]
            index-=1
        else:   #replacing the each whitespace with "%20"
            charArray[index-1] = '0'
            charArray[index-2] = '2'
            charArray[index-3] = '%'
            index-=3
    return " ".join(charArray) #joining every element in the array charArray into a sentence
