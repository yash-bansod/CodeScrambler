'''
Created By: yash-bansod
v1.0
'''
##Imported Modules
import sys
import re
import random

## Pass legit arguments. Usage: python3
file = ''
if(len(sys.argv) != 2 or sys.argv[1][-4:] != '.cpp'):
    sys.exit("Usage: python3 parser.py [<filename>.cpp]")
else:
    file = sys.argv[1][0:-4]


##List of keywords which will be replaced.
##Be sure to not use them inside print statements.
##Feel free to add more keywords:) Supports 128 keywords.
##Increase the size of listGenWords to increase capacity.
keywords = ['else','new','this','auto','enum','operator','throw','bool','explicit','private','true','break','export','protected','try','case','extern','public','typedef','catch','false','register','typeid','char','float','reinterpret_cast','typename','class','for','return','union','const','friend','short','unsigned','const_cast','goto','signed','using','continue','if','sizeof','virtual','default','inline','static','void','delete','int','static_cast','volatile','do','long','struct','wchar_t','double','mutable','switch','while','dynamic_cast','namespace','template', 'cin', 'cout','string', 'endl', 'ceil']

keywords.sort(reverse=True)  ##prevents confusion of keywords which are substrings of other keywords

lines = []

with open(file+'.cpp','r') as f:
    lines = f.readlines()

##used yeeeeet cuz why not!
listGenWords = ['YEEEEET', 'YEEEEEt', 'YEEEEeT', 'YEEEEet', 'YEEEeET', 'YEEEeEt', 'YEEEeeT', 'YEEEeet', 'YEEeEET', 'YEEeEEt', 'YEEeEeT', 'YEEeEet', 'YEEeeET', 'YEEeeEt', 'YEEeeeT', 'YEEeeet', 'YEeEEET', 'YEeEEEt', 'YEeEEeT', 'YEeEEet', 'YEeEeET', 'YEeEeEt', 'YEeEeeT', 'YEeEeet', 'YEeeEET', 'YEeeEEt', 'YEeeEeT', 'YEeeEet', 'YEeeeET', 'YEeeeEt', 'YEeeeeT', 'YEeeeet', 'YeEEEET', 'YeEEEEt', 'YeEEEeT', 'YeEEEet', 'YeEEeET', 'YeEEeEt', 'YeEEeeT', 'YeEEeet', 'YeEeEET', 'YeEeEEt', 'YeEeEeT', 'YeEeEet', 'YeEeeET', 'YeEeeEt', 'YeEeeeT', 'YeEeeet', 'YeeEEET', 'YeeEEEt', 'YeeEEeT', 'YeeEEet', 'YeeEeET', 'YeeEeEt', 'YeeEeeT', 'YeeEeet', 'YeeeEET', 'YeeeEEt', 'YeeeEeT', 'YeeeEet', 'YeeeeET', 'YeeeeEt', 'YeeeeeT', 'Yeeeeet', 'yEEEEET', 'yEEEEEt', 'yEEEEeT', 'yEEEEet', 'yEEEeET', 'yEEEeEt', 'yEEEeeT', 'yEEEeet', 'yEEeEET', 'yEEeEEt', 'yEEeEeT', 'yEEeEet', 'yEEeeET', 'yEEeeEt', 'yEEeeeT', 'yEEeeet', 'yEeEEET', 'yEeEEEt', 'yEeEEeT', 'yEeEEet', 'yEeEeET', 'yEeEeEt', 'yEeEeeT', 'yEeEeet', 'yEeeEET', 'yEeeEEt', 'yEeeEeT', 'yEeeEet', 'yEeeeET', 'yEeeeEt', 'yEeeeeT', 'yEeeeet', 'yeEEEET', 'yeEEEEt', 'yeEEEeT', 'yeEEEet', 'yeEEeET', 'yeEEeEt', 'yeEEeeT', 'yeEEeet', 'yeEeEET', 'yeEeEEt', 'yeEeEeT', 'yeEeEet', 'yeEeeET', 'yeEeeEt', 'yeEeeeT', 'yeEeeet', 'yeeEEET', 'yeeEEEt', 'yeeEEeT', 'yeeEEet', 'yeeEeET', 'yeeEeEt', 'yeeEeeT', 'yeeEeet', 'yeeeEET', 'yeeeEEt', 'yeeeEeT', 'yeeeEet', 'yeeeeET', 'yeeeeEt', 'yeeeeeT', 'yeeeeet']
random.shuffle(listGenWords)

newLines = []
fileHead = []  ##A list of all YOUR macros
startFlag=0

for line in lines:
    ##Remember //start indicates the start of your actual program (after all of YOUR macros)
    if(line != "//start\n" and startFlag==0):
        fileHead.append(line)
        continue
    else:
        startFlag=1
    if startFlag==1:
        for i,keyword in enumerate(keywords):
            line = re.sub(keyword,listGenWords[i],line)  ##This version only substitutes the required keyword

    newLines.append(line)

defLines = []  ##This is the list of all new macros
for i,keyword in enumerate(keywords):
    defLines.append("#define " + listGenWords[i] + " " + keyword + "\n")

with open(file+'Yeet.cpp','w') as f:   ##A new file will be created with suffix 'Yeet'
    for i in fileHead:
        f.write(i)
    for i in defLines:
        f.write(i)
    for i in newLines:
        f.write(i)

##Feel free to optimize
