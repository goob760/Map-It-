import webbrowser
import pyperclip
import sys

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)