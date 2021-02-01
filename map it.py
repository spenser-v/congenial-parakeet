#! python3
#map_it.py - launches a map in the browser using an address
#from either the command line or the clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #get address from command line.
    address = ''.join(sys.argv[1:])
else:
    #get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

