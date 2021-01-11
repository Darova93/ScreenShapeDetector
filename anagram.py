word = "darova"
combinations = []

def getDifferentElements(elements):
    uniqueElements = {}

    for element in elements:
        found = False
        for uniqueElement in uniqueElements:
            if uniqueElement == element:
                uniqueElements[uniqueElement] += 1
                found = True
                break
        if not found:
            uniqueElements[element] = 1

    return uniqueElements
            

def getVariation(word):
    elements = getDifferentElements(word)
    for letter in word:
        combinations.append(letter + word[1:])
    # for index in range(0,len(word)):
    #     getVariation(word[index+1:])

print(getDifferentElements("a"))