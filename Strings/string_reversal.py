"""
Input : "I am the   best"
output: "best   the am I"

Time Complexity : O(n)
Space COmplexity: O(n)

n : Length of string
"""

def revWordsInSentence(string):

    tempStr = ""
    revStr = ""
    wordsList = []
    ind = 0

    while ind < len(string):
        tempStr += string[ind]

        if tempStr[-1] == " ":
            word = tempStr[:-1] if len(tempStr) > 1 else " "
            wordsList.append(word)
            tempStr = ""

        ind += 1

    wordsList.append(tempStr)

    for i in reversed(range(len(wordsList))):
        revStr += wordsList[i] if wordsList[i] == " " else wordsList[i] + " "

    return revStr[:-1]


# print(revWordsInSentence("I am the   best") == "best   the am I")