#Generate Document
#Time Complexity: O(m * (n + m)) || Space Complexity: O(1) where m represents the length of the document
def generateDocument(characters, document):
    for character in document:
        charactersFrequency = countCharacterFrequency(character, characters)
        documentFrequency = countCharacterFrequency(character, document)
        if documentFrequency > charactersFrequency:
            return False
    return True

def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency +=1
    return frequency 
