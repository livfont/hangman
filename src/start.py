import random

def randomwordgenerator():
    f = open("./src/words.txt")
    listofwords = [] 
    for word in f:
        listofwords.append(word.strip().upper())
    
    randomindex = random.randint(0, 9)
    randomword = listofwords[randomindex]
    return randomword

word = randomwordgenerator()    
print(word)

