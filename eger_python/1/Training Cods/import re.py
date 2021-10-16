string = str("""hi my name is ALI RAhMANI. Ali Rahmani want be a python programmer.
             his mail is alirahmani@yahoo.com and another mail is ali93rahmani @gmail.com.
             his 23 years old""") 

import re

result = re.search(r'[aALlIi]',string)
result1 = re.findall(r'[aALlIi]',string)
result2 = re.search(r'[aA][Ll][Ii]',string)
result3 = re.findall(r'[aA][Ll][Ii]',string)
result4 = re.findall(r'\@(.*).',string)
#result5 = re.sub(r'\(.*).com','hotmailcom',string)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
#print(result4.group)
