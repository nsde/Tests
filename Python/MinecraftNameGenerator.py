# code by styx: github.com/nsde/mcnames
# feel free to use, but we appreciate credit.

# The code generates 100 unused minecraft names (used minecraft api)

from random import randint as rdi
import random
import requests

random.seed()

# preprefixes
ppx = ['','','','','','','','','','','','','','','','TTV_','Twitch_','YouTube_','YT_','callMe','iAm','just','not','FaZe_','real']

# prefixes
px = ['Killer','Pro','Dead','Extreme','Fire','Ice','Xtreme','Crazy','Ultra','Toxic','Fearless','Elite']

# suffixes
sx = ['Dragon','Lion','Ninja','Tiger','Spider','Wolf','Python','Gorilla','Samurai','King','Ghost']

names = 0
while names != 100:
    # choose randoms
    myppx = ppx[rdi(0,len(ppx)-1)]
    mypx = px[rdi(0,len(px)-1)]
    mysx = sx[rdi(0,len(sx)-1)]

    r = rdi(0,30)

    if r<10:
        num = str(rdi(0,100))

    elif r==30:
        num = '1337'

    elif r== 29:
        num = '69'

    else:
        num = ''

    # generate and print
    name = myppx+mypx+mysx+num
    nameurl = 'https://api.mojang.com/users/profiles/minecraft/'+name

    rq = requests.get(nameurl)
    output = rq.text

    if output == '':
        exists = False
    else:
        exists = True

    if exists:
        continue

    else:
        print(name)
        names+=1
