#Hello and wecome to My Licence Genorator, copy/paste the code #below to http://pythontutor.com/visualize.html#mode=edit to #execute. Thank you and have a great day!

import random

rnd = random.randint(0, 25)
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(letterList[rnd] + letterList[random.randint(0, 25)] + \
      letterList[random.randint(0, 25)] + '-' + str(random.randint(0, 999)))
