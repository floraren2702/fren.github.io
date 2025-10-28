# calculating the minimum number of changes needed to convert string
def hamming_distance(s1, s2):
    count = 0 
    if (len(s1) != len(s2)):
        return "Invalid, the strings should be the same length"
    elif (s1 == s2):
        return count
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count = count + 1
        return count

def is_palindrome(s3):
    if s3 == s3[::-1]:
        return True
    else:
        return False

        

