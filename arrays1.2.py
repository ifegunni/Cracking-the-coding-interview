# Check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.
# Hints: #7, #84, #722, #737

#My solution with ?? time complexity

def permutation(str1, str2):

    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return False

    else:

        a =  " ".join(sorted(str1))
        b =  " ".join(sorted(str2))

        for i in range(n1):
            if a[i] != b[i]:
                return False
        return True

if __name__ == '__main__':
    str1 = "test"
    str2 = "tset"
    if (permutation(str1, str2)):
        print("Yes")
    else:
        print("No")



#my O(n) solution

def permutation2(string1, string2):

    if len(string1) != len(string2):
        return False

    countArray1 = [0] * 128
    countArray2 = [0] * 128

    for i in string1:
        countArray1[ord(i)] += 1

    for i in string2:
        countArray2[ord(i)] += 1

    for i in range(128):
        if countArray1[i] != countArray2[i]:
            return False
    return True


if __name__ == '__main__':
    str1 = "test1"
    str2 = "tsat1"
    if permutation2(str1, str2):
        print("yes")
    else:
        print("No")

