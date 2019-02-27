def editDistance(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return n
    
    if (str1[m-1] == str2[n-1]):
        return editDistance(str1, str2, m-1, n-1)

    return 1 + min(editDistance(str1, str2, m, n-1),    #insertion
                   editDistance(str1, str2, m-1, n),    #remove
                   editDistance(str1, str2, m-1, n-1))  #substitution

print(str(editDistance("sunday", "saturday", len("sunday"), len("saturday"))))
#output 3
