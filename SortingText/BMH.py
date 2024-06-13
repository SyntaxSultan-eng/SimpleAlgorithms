pattern = "abra"
text = "abracabra"

counter = 0
n = set()
lenght = len(pattern)
dict = {}
for i in range(lenght-2, -1, -1):
    if pattern[i] not in n:
        dict[pattern[i]] = lenght-i-1
        n.add(pattern[i])
if pattern[lenght-1] not in n:
    dict[pattern[lenght-1]] = lenght
dict["*"] = lenght

Pattlenght = len(pattern)

textlen = len(text)
textmove = lenght
pattmove = lenght
i = lenght


while i <= textlen:
    if text[textmove-1] == pattern[pattmove-1]:
        textmove -= 1
        pattmove -= 1
        if pattmove == 0 :
            counter += 1
            pattmove = lenght
            i += 1
            textmove = i
    elif pattmove == lenght:
        if text[textmove-1] in n:
            i += dict[text[textmove-1]]
        else:
            i += dict["*"]
        textmove = i
        pattmove = Pattlenght
    elif pattmove != lenght:
        i += dict[pattern[pattmove-1]]
        textmove = i
        pattmove = Pattlenght

print(counter)


        
