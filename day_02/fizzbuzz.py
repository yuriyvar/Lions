#!/usr/bin/env python
#fizzbuzz.py

def fizz_buzz(innumber):
    outstring=""
    if (innumber % 3 ==0):
        outstring="Fizz"
    if (innumber % 5 ==0):
        outstring=outstring+"Buzz"
    if (outstring==""):
        outstring=innumber

    return outstring


for anumber in range(100):
    print fizz_buzz(anumber+1)
