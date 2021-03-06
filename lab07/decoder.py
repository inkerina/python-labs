# File:    decoder.py
# Started: by Dr. Gibson
# Author:  Ingrid Nkenlifack
# Date:    3/15/18
# Section: 2
# E-mail:  tz57818@umbc.edu
# Description:
#   This file contains python code that uses a function to 
#   pull out the uppercase letters from a list of strings
#   to decode a secret message.


######################################################################
# decode() decodes a message by extracting all of the 
#          lowercase letters to reveal the hidden meaning
# Input:   msgList; a list of strings
# Output:  secret;  a string containing the hidden message
def decode(msgList):
    secret = ""
    
    index = 0

    #check word in each list
    while index < len(msgList):
        #get word in each list
        aString = msgList[index]
        index2 = 0
        #checks if index2 than less of word
        while index2 < len(aString):
            #get letter in each word
            letter = aString[index2]
            #checks if letter is capital in word
            if letter == letter.lower():
                #add upper letter to string secret
                secret += letter
            #goes through letters in list aString
            index2 += 1
        #goes through words in list msgList
        index += 1
        
    return secret

def main():
    # message lists
    msg1 = ["THIs", "LIFe", "cANNOT", "rEALLY", "Be", "tRUE"]
    msg2 = ["WONdERING", "HoW", "gOOD", "SCOREs", "CaN", "REGULArLY", \
                "Be", "MANAgED", "YoU", "SHoULD", "STUdY"]
    msg3 = ["STUDYINg", "oNCE", "THRoUGH", "MIdNIGHT", "WIlL", \
                "CAuSE", "INcOMPLETE", "kNOWLEDGE", "oF", "InFORMATION", \
                "NOt", "hELPING", "THe", "EARNeD", \
                "ExAM", "GRaDE", "ImPROVE"]

    # calling the decode function for each
    ans1 = decode(msg1)
    ans2 = decode(msg2)
    ans3 = decode(msg3)

    # printing out the secret messages
    print("Message 1's secret was:")
    print(ans1)
    print()

    print("Message 2's secret was:")
    print(ans2)
    print()

    print("Message 3's secret was:")
    print(ans3)
    print()



main()

