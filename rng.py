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
# Files should be in the same directory folder as rng.py

import random
import os
import time
import sys

print("Welcome to the random number generator!")
filename = input("Type the filename of the class roster you would like to use: $ ")
cmd = ''

if os.path.exists(filename): # checks if file exists in the given path
    print("Reading from %s...\n " % filename)

    #--mainloop--#
    while True:
        cmd = input("Press enter, or type 'quit' to exit the program: $ ")
        if cmd.lower() == 'quit':
            print("--Closing program--")
            sys.exit(0)
        print("The random number generator calls on...")
        time.sleep(3)

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
