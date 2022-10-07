import os

os.system("pip install selenium==3.141.0")
from webbot import Browser

web = Browser()
web.go_to('https://3kh0.github.io')
website = input('Service has audio')
