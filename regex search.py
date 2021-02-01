### COMMENT CODE
# list of steps:
# 1: open all text files in a folder
#   TODO:
#       -find all text files
#       -create a list from glob
#       -open each file using glob list
#       -when finished, close each file
#
# 2: search for defined regex
#   TODO:
#       -take user input for regex, save to variable
#       -use created regex to search the current text file
#       -append each result to a search results array
#
# 3: print results to screen
#   TODO:
#       -print search results array to screen

from pathlib import Path
import re

p = Path.home()

print('Please enter your regex to use for your search.')
user_regex = re.compile(input())
search_results = []

text_list = list(p.glob('*.txt'))
for i in text_list:
    with open(i) as content:
        #print(len(text_list)) #testing code
        #print(content.read()) #testing code
        for j in user_regex.findall(content.read()):
            print("found match %s" % j)
            search_results.append(j)


print(search_results)





