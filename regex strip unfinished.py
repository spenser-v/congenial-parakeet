#find space, tab, and newline before and after a string and remove it
#OR remove specific character from the beginning and end of a string
#examples
#
#spam = '     Hello, World    '
#spam.strip()
#'Hello, World'
#
#spam = 'SpamSpamBaconSpamEggsSpamSpam'
#spam.strip('ampS')
#'BaconSpamEggs'

#COME BACK TO THIS
import re
print('Enter message to strip.')
message = input()
print('Define class of characters to strip.')
characters_to_remove = input()

def strip(string, custom_class):
    string = input()
    strip_regex_beginning = re.compile(
    strip_regex_end = re.compile(
print(message, characters_to_remove)