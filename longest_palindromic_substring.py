def longest_palindrome(s):
    opt = [[False for i in range(len(s))] for j in range(len(s))]

    # opt[i][j] denotes if s[i:j] is palindrome or not

    max_length = 1

    for i in range(len(s)):
        opt[i][i] = True # Single characters are always palindromic

    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            opt[i][i+1] = True
            start = i
            max_length = 2
        else:
            opt[i][i+1] = False

    for k in range(3,len(s)+1): # Current length of candidate substrings
        for i in range(len(s)-k+1):
            if opt[i+1][i+k-2] == True and s[i] == s[i+k-1]:
                opt[i][i+k-1] = True
                if k>max_length:
                    max_length = k
            else:
                opt[i][i+k-1] = False

    for i in range(len(s)-max_length+1):
        if opt[i][i+max_length-1]==True:
            return s[i:i+max_length]
        
    return ""

print(longest_palindrome('aabcdcb'))