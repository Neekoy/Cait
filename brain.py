import re

important = {}
knowledge = {}

with open("knowledge.txt") as f:
    content = f.readlines();

for i in range (0, len(content)):
    addon = re.split(' : ', content[i].rstrip())
    if '!!!' in addon[0]:
       important[addon[0]] = addon[1]
    else:
       knowledge.update({" {0} ".format(addon[0]):" {0} ".format(addon[1])})

print knowledge
print important
