#542_Q1_6511171_Wai_Yan
def AlternateLetters(word1,word2):
    if not (word1 and word2):
        return word1 + word2
    return word1[0] + word2[0]+ '_' + AlternateLetters(word1[1:], word2[1:len(word1)])
word_1 = str(input("Enter word1 = "))
word_2= str(input("Enter word2 = "))
if len(word_2)>= len(word_1):
    word1 = word_1
    word2 = word_2
elif len(word_2) < len(word_1):
    word1 = word_2[::-1]
    word2 = word_1[::-1]
print(f'The output is {AlternateLetters(word1,word2)}.')