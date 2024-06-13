def cache(pattern):
    cache = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            j += 1
            cache.append(i)
        else:
            if i > 0:
                i = 0
                if pattern[i] == pattern[j]:
                    i += 1
                    j += 1
                    cache.append(i)
            else:
                cache.append(i)
                j += 1
    return cache

def KMP(pat, txt):
    n = len(txt)
    i = j = counter = 0
    patterncache = cache(pat)
    while i < n:
        if pat[j] == txt[i]:
            i += 1  
            j += 1
        if j == len(pat):
            counter += 1
            j = patterncache[j-1]
        elif pat[j] != txt[i]:
            if j != 0:
                j = patterncache[j-1]
            else:
                i += 1
    return counter
pattern = "aba"
text = "swqabaaaerwqsssababl"
print(KMP(pattern,text))
print(cache(pattern))
