# Created by:           Ahriel Godoy
# Student ID:           871928876
# Program Description:  this script counts the frequencies of characters in a text file, or multiple files
#                       from flags

import sys
import csv
import os
import collections

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

def merge(dict_1, dict_2):
    a_counter = collections.Counter(dict_1)
    b_counter = collections.Counter(dict_2)
    add_dict = a_counter + b_counter
    dict_3 = dict(add_dict)
    return(dict_3)
'''
def recursiveAdd(list):
    rates = {}
    for d, value in list:
        merge(rates, list[d])
        if value == list[-1]:
            print(rates)
            return rates
        print(rates)
        return rates + recursiveAdd(rates,list[i:])'''

def flags():
    """"This function parses flags from the command line arguments"""
    queryLetters = ""
    flags = set()

    fileList = []
    """parse the file names"""
    for i in range(1, len(sys.argv)):
        if '.txt' in sys.argv[i]:
            fileList.append(sys.argv[i])

    for i in range(1, len(sys.argv)):
        if '-' in sys.argv[i]:
            flags.add(sys.argv[i][1:])
            if '-l' in sys.argv[i]:
                queryLetters = sys.argv[i + 1]
    total_flags = [flags, queryLetters, fileList]
    print(total_flags)
    return (total_flags)

def w_to_csv(filename, dict):
    csv_file = filename
    with open(csv_file, 'w') as f:
        for key in dict.keys():
            f.write("%s,%s\n" % (key, dict[key]))

def add_frequencies(d, file, remove_case, flagSet, queryLetters):
    """a dictionary d, a file object file, and a boolean remove_case (from -c)"""
    file = open(file, mode='r', encoding='ASCII')
    fullText = file.read()
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
            if letter in queryLetters:
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

def returnDict(totalFlags):
    totalletterFrequencies = {}
    """"Create an empty dictionary"""
    fileList = totalFlags[2]
    dictionaryList = []
    for i in range(len(fileList)):
            letterFrequencies = {}
            file = fileList[i]
            print()
            print(f'File name: {file}')
            if "c" in totalFlags[0]:
                """provide count of letters within the file"""
                letterFrequencies = add_frequencies(letterFrequencies, file, False, totalFlags[0], fileList)
                dictionaryList.append(letterFrequencies)
                """provide count of letters as a running total"""
                totalletterFrequencies = add_frequencies(letterFrequencies, file, False, totalFlags[0], fileList)
            else:
                letterFrequencies = add_frequencies(letterFrequencies, file, True, totalFlags[0], fileList)
                dictionaryList.append(letterFrequencies)
                totalletterFrequencies = add_frequencies(letterFrequencies, file, True, totalFlags[0], fileList)
            print(dictionaryList[i])
    frenquencyList = []
    if len(dictionaryList) == 1:
        totalletterFrequencies = dictionaryList[0]
    elif len(dictionaryList) == 2:
        totalletterFrequencies = merge(dictionaryList[0],dictionaryList[1])
    elif len(dictionaryList) == 3:
        temp = merge(dictionaryList[0],dictionaryList[1])
        totalletterFrequencies = merge(temp, dictionaryList[2])
    else:
        print("ERROR: There is more than 3 .txt files.")
    print()
    print(f'Total Frequencies:')
    print(totalletterFrequencies)
    w_to_csv("out.csv",totalletterFrequencies)
    """Add the frequencies for each file in the argument list to the dictionary"""

# ---------------------------------------
total_flags = flags()

#
if __name__ == "__main__":
    returnDict(total_flags)