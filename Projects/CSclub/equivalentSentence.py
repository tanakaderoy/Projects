def buildDictionary(fileName):
    file = open(fileName,"r")
    synonymDict = {}
    for line in file:
        words = line.split()
        if words[0] not in synonymDict:
            synonymDict[words[0]] = {words[1]}
        else:
            synonymDict[words[0]].add(words[1])
        if words[1] not in synonymDict:
            synonymDict[words[1]] = {words[0]}
        else:
            synonymDict[words[1]].add(words[0])
    file.close()
    return(synonymDict)



def equivalentSentence():
    synonyms =  buildDictionary("synonyms.dat")
    sentence1 = input("Please enter sentence 1: ").lower().split()
    sentence2 = input("Please enter sentence 2: ").lower().split()
    print(sentence1,sentence2)
    if len(sentence1) != len(sentence2):
        print("Sentences are not equal")
    else:
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 != word2:
                if word1 in synonyms:
                    words = synonyms[word1]
                    if word2 not in words:
                        print("Sentences not equal")
                        return

                else:
                    print("Sentences not equal")
                    return
        print("Yes the Sentences are equivalent")
    
               




equivalentSentence()


    