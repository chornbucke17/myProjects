#!/usr/bin/python3
# Author: Christopher Hornbuckle
# Date: Oct 13th, 2020
#
# A simple pseudo-random name generator. Run it like this:
#   ./rng.py
# or
#   python3 ./rng.py
#
# Program will ask the user to provide the name of a txt file to read from. Press
# enter to select a new name from the list, or can type 'quit' to exit the program.
#
# Files should be in the same directory folder as rng.py and have each name listed
# on a separate line from one another. Make sure files end in '.txt'.

import random
import os
import time
import sys

# handles obtaining the list of classes from current working directory
def getClassList():
    classes = []
    dir = os.getcwd()
    for item in os.listdir(dir):
        if not item.startswith(".") and item.endswith(".txt"):
            name = item.split(".", 1) # at most [1] split is done
            classes.append(name[0])
    return classes

# initial print statement
print("    \nrandom name generator, by C. Hornbuckle [Oct.2020]")
print("\nList of courses found:")
print(getClassList())

filename = input("Which class roster you would like to use?: $ ")
filename += ".txt"
cmd = ''

if os.path.exists(filename): # checks if file exists in the given path
    print("Reading from (%s)...\n " % filename)

    #--mainloop--#
    while True:
        cmd = input("Press enter, or type 'quit' to exit the program: $ ")
        if cmd.lower() == 'quit':
            print("--Closing program--")
            sys.exit(0)
        print("The random name generator calls on...")
        time.sleep(0.5)

        with open(filename) as f:
            try:
                lines = f.readlines()
                print(random.choice(lines))
            except:
                print("Error reading file.")
                sys.exit(0)

else:
    print("--File does not exist in this directory--")
    print("--Closing program--")
