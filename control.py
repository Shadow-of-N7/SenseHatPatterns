#!/usr/bin/env python3

# The main control script. It chooses which pattern gets displayed based on randomness.

import os
import subprocess
import datetime
from time import sleep
from random import randint
from sense_hat import SenseHat

#curr_dir = os.getcwd()
curr_dir = "/home/pi/SenseHatPatterns"
sensehat_scripts = curr_dir + "/sensehat/"

today = datetime.date.today()
if datetime.date(datetime.datetime.now().year, 12, 1) <= today <= datetime.date(datetime.datetime.now().year, 12, 31):
  sensehat_scripts = curr_dir + "/sensehat/christmas/"

sense = SenseHat()

def main():
  sense.clear()
  sense.show_message("Hello, world!")
  sense.clear()
  DIR = sensehat_scripts
  script_count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
  
  while True:
    target = randint(1, script_count) # Start with one, as with one script it would only work half the time
    executeSenseHatScript(target)
    sense.clear()
  
  
def executeSenseHatScript(target):
  print(target)
  opencommand = 'python3 ' + sensehat_scripts + str(target) + '.py'
  process = subprocess.Popen(opencommand, shell=True)
  process.wait()
  
if __name__== "__main__":
  main()
