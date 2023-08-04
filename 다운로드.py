#          https://www.python.org/


import webbrowser
webbrowser.open('https://www.sublimetext.com/')
webbrowser.open('https://desktop.github.com/')
webbrowser.open('https://github.com/naver/d2codingfont/releases/tag/VER1.3.2')
webbrowser.open('https://www.pygame.org/docs/')
webbrowser.open('https://www.msys2.org/')
webbrowser.open('https://github.com/Zzajang-bro/msys-mingw64-init-20230725/blob/main/msys-mingw64-init-20230725.sh')
webbrowser.open('https://gist.github.com/thales17/fb2e4cff60890a51d9dddd4c6e832ad2')
# https://github.com/AutoDarkMode/Windows-Auto-Night-Mode/releases/tag/10.3.0.90

import subprocess
subprocess.run(['pip','install','pygame'], capture_output=True)

#         { "ignored_packages":[], "save_on_focus_lost": true, "font_face": "D2Coding", "font_size": 9, }

'''
import os
os.mkdir('tmp')

from urllib import request
giturl = 'https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.3/Git-2.41.0.3-64-bit.exe'
savenm= './tmp/git.exe'
request.urlretrieve(giturl, savenm)

import subprocess
subprocess.call(['./tmp/git.exe', '/VERVSILENT', '/NORESTART'])

os.environ['PATH'] += r'C:\Program Files\Git\bin;'
import os
os.environ['PATH'] += r'C:\Program Files\Git\bin;'

import subprocess
import sys

def sPr( com ):
    subprocess.Popen( com.split() , stdout=sys.stdout, stderr=sys.stdout)

#subprocess.Popen(['git','clone','https://github.com/Zzajang-bro/python-codebucket'], stdout=sys.stdout, stderr=sys.stdout)
#input()
os.chdir('python-codebucket')
#sPr('git config --global user.name Zzajang-bro.Bot')
#sPr('git config --global user.email Zzajang-bro+github@gmail.com')
#input()

sPr('git add .')
sPr('

#subprocess.run(['git','remote','add','origin','https://github.com/Zzajang-bro/python-codebucket'], capture_output=True)

#subprocess.run(['git','push','-u','origin','main'], capture_output=True)
#subprocess.run(['git','add','.'], capture_output=True)
#subprocess.run(['git','commit','-m','update'], capture_output=True)
#subprocess.run(['git','push'], capture_output=True)

'''
