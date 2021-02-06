# Created by:           Ahriel Godoy
# Student ID:           871928876
# Program Description:  this script counts the frequencies of characters in a text file, or multiple files
#                       from flags

import sys
# import csv
# import os
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
# -z option:        print out chars that occurred with a frequency of zero. If omitted,
# chars with a frequency of zero are not printed.

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
    return dict_3


def flags():
    """"This function parses flags from the command line arguments"""
    query_letters = ""
    flag_set = set()
    all_flags = []
    file_list = []
    """parse the file names"""
    for i in range(1, len(sys.argv)):
        if '.txt' in sys.argv[i]:
            file_list.append(sys.argv[i])

    for i in range(1, len(sys.argv)):
        if '-' in sys.argv[i]:
            flag_set.add(sys.argv[i][1:])
            if '-l' in sys.argv[i]:
                query_letters = sys.argv[i + 1]
    all_flags.append([flag_set, query_letters, file_list])
    print(all_flags)
    return all_flags

def w_to_csv(filename, dictionary):
    """function takes a filename, and a dictionaryionary and prints to the file the dictionary in csv format"""
    csv_file = filename
    with open(csv_file, 'w') as f:
        for key in dictionary.keys():
            f.write("%s,%s\n" % (key, dictionary[key]))

def add_freq(d, file, remove_case, flag_set, query_letters):
    """a dictionary d, a file object file, and a boolean remove_case (from -c)"""
    file = open(file, mode='r', encoding='ASCII')
    fullText = file.read()
    """the following line takes care of -c"""
    if remove_case is True:
        fullText = fullText.lower()
    if "z" in flag_set:
        """create a dictionary with values of 0 prior to counting"""
        if remove_case is True:
            for letter in alphabetLower:
                d[letter] = 0
        else:
            for letter in alphabetCombined:
                d[letter] = 0

    if "l" in flag_set:
        for letter in fullText:
            if letter in query_letters:
                if letter in d:
                    """flagsLetters[1] is the set of letters from which to limit when -l is called"""
                    d[letter] = d[letter] + 1
                else:
                    d[letter] = 1
    else:
        for letter in fullText:
            if letter in alphabetCombined:
                """only select the char within the alphabet, excluding punctuations"""
                if letter in d:
                    d[letter] = d[letter] + 1
                else:
                    d[letter] = 1
    return d


def returnDict(totalFlags):
    totl_letter_frenquencies = {}
    """"Create an empty dictionary"""
    file_list = totalFlags[2]
    dictionary_list = []
    for i in range(len(file_list)):
        letterFrequencies = {}
        file = file_list[i]
        print(f'File name: {file}')
        if "c" in totalFlags[0]:
            """provide count of letters within the file"""
            letterFrequencies = add_freq(letterFrequencies, file, False, totalFlags[0], totalFlags[1])
            dictionary_list.append(letterFrequencies)
            """provide count of letters as a running total"""
            totl_letter_frenquencies = add_freq(totl_letter_frenquencies, file, False, totalFlags[0], totalFlags[1])
        else:
            letterFrequencies = add_freq(letterFrequencies, file, True, totalFlags[0], totalFlags[1])
            dictionary_list.append(letterFrequencies)
            totl_letter_frenquencies = add_freq(totl_letter_frenquencies, file, True, totalFlags[0], totalFlags[1])
        print(dictionary_list[i])

    if len(dictionary_list) == 1:
        totl_letter_frenquencies = dictionary_list[0]
    elif len(dictionary_list) == 2:
        totl_letter_frenquencies = merge(dictionary_list[0], dictionary_list[1])
    elif len(dictionary_list) == 3:
        temp = merge(dictionary_list[0], dictionary_list[1])
        totl_letter_frenquencies = merge(temp, dictionary_list[2])
    else:
        print("ERROR: There is more than 3 .txt files.")
    emptyDict = {}
    if ('z' in totalFlags[0]) and ('c' in totalFlags[0]):
        for letter in alphabetCombined:
            emptyDict[letter] = 0
        totl_letter_frenquencies = emptyDict | totl_letter_frenquencies
    elif ('z' in totalFlags[0]) and ('c' not in totalFlags[0]):
        for letter in alphabetLower:
            emptyDict[letter] = 0
        totl_letter_frenquencies = emptyDict | totl_letter_frenquencies

    print()
    print(f'Total Frequencies:')
    print(totl_letter_frenquencies)
    w_to_csv("out.csv", totl_letter_frenquencies)
    """Add the frequencies for each file in the argument list to the dictionary"""
    return totl_letter_frenquencies


# ---------------------------------------
all_flags = flags()

#
if __name__ == "__main__":
    returnDict(all_flags)
