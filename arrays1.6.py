# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string.You can assume the string has only uppercase and lowercase letters (a - z).

# this solution is O(n2) because we are concatinating a new string and that result to an O(n2)
def stringCompression(string):

    res = ""   # create an empty string
    count = 0       # initialize count for each element in the string to 0
    prev = string[0]   # to keep record of previous character in the string

    for char in string:
        if char == prev:  #if the current element in a string equal to the previous element
            count+=1   # count the occurrence
        else:
            res += prev + str(count)  #if not equal start adding the string to the new string and
            prev = char    #set previous to current character and take not of occurence
            count = 1  #by initializing count to 1

    if len(res) < len(string):
        return(res)
    else:
        return(string)

if __name__ == '__main__':
    x = "aabcccccaaa"
    print(stringCompression(x))
    
    
    
    
#A better solution is to use a list rather that creating a new list  Making the new solution O(n)

def stringCompression(string):

    res = []  #using list in place of creating a new string is the only difference and changes time complexity to O(n)

    countConsecutive = 0
    prev = string[0]

    for char in string:
        if char == prev:
            countConsecutive += 1
        else:
            res += prev + str(countConsecutive)
            prev = char
            countConsecutive = 1

    res = ''.join(res)

    if len(res) < len(string):
        return res
    else:
        return string



if __name__ == '__main__':
    x = "aabcccccaaa"
    print(stringCompression(x))
