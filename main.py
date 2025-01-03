import re
string = 'search this'

pattern = re.compile('this')
a = pattern.search(string)
print(a)