# TODO
# variapls
text = input("Text: ")
char = 0
word = 0
sent = 0
indx = 0
skip = False
# count words, sentences and chars
for i in text:
    if (skip):
        skip = False
        continue
    if (i.isalpha()):
        char += 1
    if (i == ' '):
        word += 1
    if i in ['?', '!', '.']:
        sent += 1
        if (indx + 1) in range(len(text)):
            if text[indx + 1] == ' ':
                skip = True
                indx += 1
        word += 1
    indx += 1
# how to get L and S per 100 word
L = (float(char) / word) * 100
S = (float(sent) / word) * 100
print("Letters " + str(char))
print("Words " + str(word))
print("Sentence " + str(sent))
# the formela
index = (0.0588 * L) - (0.296 * S) - 15.8
Idx = int(index)
if ((index - Idx) > 0.5):
    Idx += 1
if (Idx >= 2 and Idx < 16):
    print("Grade " + str(Idx))
elif (Idx > 16):
    print("Grade 16+\n")
else:
    print("Before Grade 1")
