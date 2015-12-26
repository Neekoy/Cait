import re
import random
import wikipedia
from brain import important
from brain import knowledge

def answers(inputWords, outputAnswer):
    inputWords = ' '.join(inputWords)
    addonStart = ""
    if 'you know' in inputWords:
        addonStart = "Sure I do." 
    elif 'don\'t know' in inputWords:
        addonStart = "Or do I?" 
    elif 'tell me' in inputWords:
        addonStart = "Sure."
    else:
        pass
    if addonStart != "":
        print addonStart, outputAnswer
    else:
        print outputAnswer

def iterating(inputWords):

    hits = {}

    if "error" in inputWords:
        inputWords = ' '.join(inputWords)
        for entry in important:
            for error, answer in entry.iteritems():
                totalMatches = 0
                for searchWord in inputWords:
                    matches = len(re.findall(" {0} ".format(searchWord), error))
                    totalMatches += matches
                hits.update({totalMatches:answer})

        highest = max(hits.keys(), key=int)            

        answers(inputWords, hits[highest])
        return

    for key, value in knowledge.iteritems():
        totalMatches = 0
        for searchWord in inputWords:
            matches = len(re.findall(" {0} ".format(searchWord), key))
            totalMatches += matches
        hits.update({totalMatches:value}) 
    highest = max(hits.keys(), key=int)

    if highest == 0:
        inputWords = ' '.join(inputWords)
        if " who " and " is " in inputWords:
            inputWords = re.sub("who", "", inputWords)
            inputWords = inputWords.replace(" is ", "")
            print inputWords
            try:
                answer = wikipedia.summary(inputWords, sentences=1)
            except:
                print "I know things about stuff. People.. not that much." 
            else:
                print answer.rstrip() 
        else:
            unknown = []
            unknown.append("I'm not really sure what you're talking about. *Walks away slowly*")
            unknown.append("Hm, I don't really think I know that.")
            unknown.append("I wish I knew that.")
            print unknown[random.randint(0,len(unknown)-1)]
    else:
        answers(inputWords, hits[highest])

while True:
    userInput = raw_input('>>> ').translate(None,"?").split()
    iterating(userInput)
