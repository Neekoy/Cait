import re

important = []
knowledge = {}

with open("knowledge.txt") as f:
    content = f.readlines();

for i in range (0, len(content)):
    addon = re.split(' : ', content[i].rstrip())
    if '!!!' in addon[0]:
       listing = addon[0].split()
       for each in listing:
           if "!!!" in each:
               importantKey = re.sub("!!!", '', each)
               important.append(importantKey)
           else:
               knowledge.update({" {0} ".format(addon[0]):" {0} ".format(addon[1])})
    else:
       knowledge.update({" {0} ".format(addon[0]):" {0} ".format(addon[1])})

#print knowledge
#print important
