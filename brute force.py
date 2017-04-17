import string
from itertools import product, combinations, permutations


def dictHack(dictonary):
    print("Trying dictonary hack...")
    with open(dictonary) as fileObj:
        for line in fileObj:
            line = line.strip()
            if line == password:
                print("Dictionary hack successfully cracked password: It is",line)
                print("Dictionary hack ended...")
                return ""
    print("Dictonary hack failed to crack the password...")


def numHack(maxLength):
    print("Trying number hack...")
    number = 0
    numberstring = str(number)
    while number <= maxLength:
        if numberstring == password:
            print("Number hack successfully cracked password: It is",numberstring)
            print("Number hack ended...")
            return ""
            break
        number += 1
        numberstring = str(number)
    print("Number hack failed to crack the password...")


def lowercaseHack(maxLength,doubledChars):
    print("Trying lowercase hack...")  
    n = 1
    while n < maxLength: 
        for guess_chars in combinations(alphabet, n):
                i = 0
                while i <= doubledChars: 
                    for doubled_chars in combinations(guess_chars, i):
                        for guess in permutations(guess_chars + doubled_chars):
                            bruteforce = ''.join(guess)
                            if bruteforce == password:
                                print("Lowercase hack successfully cracked password: It is",bruteforce)
                                return True
                    i += 1
        n += 1
        print("Nothing found yet. Trying with",n,"letters and max",doubledChars,"doubled chars...")
    print("Lowercase hack failed to crack the password...")


password = "99999999"
#dictonary = "dict.txt"
alphabet = set('abcdefghijklmnopqrstuvwxyz')

def bruteforce():
    dictHack("dict.txt")
    numHack(99999999)
    lowercaseHack(9,1)

bruteforce()
