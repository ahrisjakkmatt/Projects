# Created by:           Ahriel Godoy
# Student ID:           871928876
# Program Description:  this script counts the frequencies of characters in a text file, or multiple files
#                       from flags

import sys
import csv
import os

# Create alphabet list of lowercase letters
alphabetLower = []
for letter in range(97, 123):
    alphabetLower.append(chr(letter))

# Create alphabet list of uppercase letters
alphabetUpper = []
for letter in range(65, 91):
    alphabetUpper.append(chr(letter))

# All possible letters
alphabetCombined = alphabetUpper
for letter in alphabetLower:
    alphabetCombined.append(letter)


# Flag Options:

# -l option:        restrict what characters are printed.
# -c option:        make the counting case-sensitive. When omitted, defaults to being case-insensitive.
# -z option:        print out chars that occurred with a frequency of zero. If omitted, chars with a frequency of zero are not printed.

# Ignore Case
# Count multiple files
# Print out frequency of zero
# CSV format
# Help

# Example command prompt:
#   python count.py [-c] [-l letters] [-z] file_1 file_2 ... file_n
#   python count.py file_1.txt file_2.txt

def help():
    print("# Created by:           Ahriel Godoy")
    print("# Student ID:           871928876")
    print("# Program Description:  This script counts the frequencies of characters in a text file, or multiple files from flags")
    print('---------------------------------------------------------------------------------------------------------------------')
    print("-c :: an optional flag that distinguishes between upper and lower case.")
    print("      For example, the file 'aA' would count one 'a' and one 'A'.")
    print("-l :: an optional flag with an argument, that only prints out the frequencies of the characters in the argument letters.")
    print("      For example, '-l aeiou' counts only vowels.")
    print("-z :: an optional flag that prints a row for every character, even when it occurs zero times")


def flags():
    """"This function parses flags from the command line arguments"""
    possibleFlags = ['-c', '-l', '-z', '-help']
    queryLetters = ""
    flags = set()

    for i in range(1, len(sys.argv)):
        if '-' in sys.argv[i]:
            flags.add(sys.argv[i][1:])
            if '-l' in sys.argv[i]:
                queryLetters = sys.argv[i+1]
    flagsLetters = [flags, queryLetters]
    return(flagsLetters)

def add_frequencies(d, file, remove_case):
    """a dictionary d, a file object file, and a boolean remove_case (from -c)"""
    file = open(file, mode='r', encoding='ASCII')
    fullText = file.read()
    """flags has to be called from within this function because the function parameters as per rubrik do no allow for the cases of -z and -l"""
    flagsLetters = flags()
    flagSet = flagsLetters[0]
    """the following line takes care of -c"""
    if remove_case == True:
        fullText = fullText.lower()
    if "z" in flagSet:
        """create a dictionary with values of 0 prior to counting"""
        if remove_case == True:
            for letter in alphabetLower:
                d[letter] = 0
        else:
            for letter in alphabetCombined:
                d[letter] = 0

    for letter in fullText:
        if "l" in flagSet:
            if letter in flagsLetters[1]:
                """flagsLetters[1] is the set of letters from which to limit when -l is called"""
                if letter in d:
                    d[letter] = d[letter] + 1
                else:
                    d[letter] = 1
        else:
            if letter in alphabetCombined:
                if letter in d:
                    d[letter] = d[letter] + 1
                else:
                    d[letter] = 1
    return(d)

def main():

    if '-help' in sys.argv: #-help flag explains script functionality
        help()
        return

    flagsLetters = flags()
    flagSet = flagsLetters[0]
    """Parse the command line arguments -c, -l, -z by calling function flags()"""

    totalletterFrequencies = {}
    """"Create an empty dictionary"""

    fileList = []
    """parse the file names"""
    for i in range(1,len(sys.argv)):
        if '.txt' in sys.argv[i]:
            fileList.append(sys.argv[i])

    for i in range(len(fileList)):
            letterFrequencies = {}
            file = fileList[i]
            print(f'File name: {file}')
            if "c" in flagSet:
                """provide count of letters within the file"""
                letterFrequencies = add_frequencies(letterFrequencies, file, False)
                """provide count of letters as a running total"""
                totalletterFrequencies = add_frequencies(totalletterFrequencies, file, False)
            else:
                letterFrequencies = add_frequencies(letterFrequencies, file, True)
                totalletterFrequencies = add_frequencies(totalletterFrequencies, file, True)
            for key, value in letterFrequencies.items():
                print(f'"{key}",{value}')
            print()
    print("Total letters in all files:")
    for key, value in totalletterFrequencies.items():
        print(f'"{key}",{value}')

    """Add the frequencies for each file in the argument list to the dictionary"""

# ---------------------------------------

main()