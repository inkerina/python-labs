# File: factors.py
# Author: Ingrid Nkenlifack
# Date: 4/9/18
# Section: 2
# E-mail: tz57818@umbc.edu
# Description: YOUR DESCRIPTION GOES HERE AND HERE
# YOUR DESCRIPTION CONTINUED SOME MORE

def factors(number):

    for i in range(1, number+1):
        if number % i == 0:
            print(i," is a factor of ",number)

def main():

    num = int(input("Enter a (positive) number to find the factors of: "))
    while num <=0 :
        num = int(input("Sorry, enter a number greater than zero: "))


    factors(num)
main()
