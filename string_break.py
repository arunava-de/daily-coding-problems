def break_string(s, k):
    lines = []
    if len(s)<k: #Base case, where length of string is less than k
        return [s]
    
    curr_len = 0
    words = s.split()
    curr_line = ""

    for i in range(len(words)):
        if curr_len + len(words[i])> k: #If we've exhausted the current line
            lines.append(curr_line.strip())
            curr_line = words[i] + " "
            curr_len = len(words[i]) + 1
        else:
            curr_len += len(words[i]) + 1
            curr_line += words[i] + " "

        if i==len(words)-1:
            lines.append(curr_line.strip())
            break
        
    return lines

s = "the quick brown fox jumps over the lazy dog"
k = 10

print(break_string(s,k))

s = "aaa bb cc ddddd"
k = 6

print(break_string(s,k))