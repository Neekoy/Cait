import re

def webhosting(check):
    containsDomain = re.search(r'(([\w]{3,63})(\.[\w]{1,5}))', check)
    if containsDomain != None:
        domainName = containsDomain.group()
        return domainName
