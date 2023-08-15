def getTitleCase(aString):
    newStr = aString.split()
    result = []
    for word in newStr:
        newWord = ''
        for letter in word:
            if letter == word[0] and ord('a') <= ord(letter) <= ord('z'):
                newWord += chr(ord(letter) - 32)
            elif letter != word[0] and ord('A') <= ord(letter) <= ord('Z'):
                newWord += chr(ord(letter) + 32)
            else:
                newWord += letter
        result.append(newWord)
    return " ".join(result)

print(getTitleCase('helLO, world!'))