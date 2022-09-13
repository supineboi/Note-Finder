#-----------------------------------------------PROJECT-1---------------------------------------------------------

#                                          Word Finder in Surah

#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
### Approach - 1
##
##import os
##
##finding = input("Enter a text : ")
##finding = finding.lower()
##
##surah = ["AL-Fatihah.txt", "Al-Qadr.txt", "Al-Fil.txt"]
##
##flag = True
##
##for surahName in surah:
##    
##   with open(surahName,mode= "r") as myFile:
##       alist = myFile.readlines()
##       for i in alist[0:len(alist):2]:
##            verse = i.lower()
##            if finding in verse:
##                print(surahName,":")
##                print(i)
##                flag = False
##                
##if flag == True:
##   print("The word you enter isn't mention in any Verse of Surah")
   
#-----------------------------------------------------------------------------------------------------------------
# Approach - 2

import os
import re

text = input("Enter a text : ")
text = text.lower()

# surah = ["AL-Fatihah.txt", "Al-Qadr.txt", "Al-Fil.txt"]
surah = ["MyPython\Projects\Al-Fatihah.txt", "MyPython\Projects\Al-Fil.txt", "MyPython\Projects\Al-Fil.txt"]

flag = True

for surahName in surah:
    
   with open(surahName,mode= "r") as myFile:

        file = myFile.read()
        aFile = file.lower()
        ranged = "{1,3}"

        pattern = r"verse \d{} : .*{}.*".format(ranged,text)

        matches = re.findall(pattern,aFile)
        length = len(list(matches))

        if length > 0:
           flag = False
           print(surahName,":")
           for i in matches:
              print(i)
           print("*"*74)
         
if flag == True:
   print("The word you enter isn't mention in any Verse of Surah")

#-----------------------------------------------------------------------------------------------------------------
# Approach - 3 [taking inputs]

##import os
##import re
##
##surah = []
##
##num = int(input("Number of surah : "))
##
##for i in range(num):
##   surah.append(input("Enter file name : "))
##
##flag = True
##
##text = input("Enter a text : ")
##text = text.lower()
##
##for surahName in surah:
##    
##   with open(surahName,mode= "r") as myFile:
##
##        file = myFile.read()
##        aFile = file.lower()
##        ranged = "{1,3}"
##
##        pattern = r"verse \d{} : .*{}.*".format(ranged,text)
##
##        matches = re.findall(pattern,aFile)
##        length = len(list(matches))
##
##        if length > 0:
##           flag = False
##           print(surahName,":")
##           for i in matches:
##              print(i)
##           print("*"*74)
##         
##if flag == True:
##   print("The word you enter isn't mention in any Verse of Surah")

#-----------------------------------------------------------------------------------------------------------------

   
