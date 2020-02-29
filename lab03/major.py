# File: major.py
# Author: Ingrid Nkenlifack
# Date: 2/12/2018
# Section: 02
# E-mail: tz57818@umbc.edu
# Description: Use decision structures to determine the grade a user needs depending on his or her major to pass CMSC 201 
# 


def main():

    major = input("What is your major?")
    #decide grade user needs to pass class
    if major == "CMSC" or major == "CMPE":
        print("You need to earn at least a B for CMSC 201 to count.")
    #if user does not belong to either major
    else:
        print("You need to earn at least a C for CMSC 201 to count.")

main()
