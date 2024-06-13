B = 5179
Q = 256
 
 
def get_hash(pattern):
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result
 
 
def rabincarp(text, pattern):
    global B, Q
    patternlen = len(pattern)
    textlen = len(text)
 
    maxB = 1
    for i in range(1,patternlen):
        maxB = (maxB * B) % Q
 
    pattern_hash = get_hash(pattern)
    texthash = get_hash(text[:patternlen])
 
    count = 0
    for elem in range(textlen - patternlen + 1):
        if pattern_hash == texthash:
            count += 1
 
        if elem < textlen - patternlen:
            texthash = ((texthash - ord(text[elem]) * maxB) * B + ord(text[elem + patternlen])) % Q
    return count
p = "ababa"
text = "ababasdfwafafawfafarababaweqesf"
print(rabincarp(text,p))