import sys

# Create alphabet list of lowercase letters
alphabetLower = []
for letter in range(97, 123):
    alphabetLower.append(chr(letter))

# Create alphabet list of uppercase letters
alphabetUpper = []
for letter in range(65, 91):
    alphabetUpper.append(chr(letter))

# Vowels
# Ignore Case
# Count multiple files
# Print out frequency of zero
# CSV format
# Help

# Example command prompt:
#   python count.py [-c] [-l letters] [-z] file_1 file_2 ... file_n
#   python count.py file_1.txt file_2.txt

def help():
    print()
    print("-c :: an optional flag that distinguishes between upper and lower case.")
    print("      For example, the file 'aA' would count one 'a' and one 'A'.")
    print("-l :: an optional flag with an argument, that only prints out the frequencies of the characters in the argument letters.")
    print("      For example, '-l aeiou' counts only vowels.")
    print("-z :: an optional flag that prints a row for every character, even when it occurs zero times")

def flags():
    flags = ''
    for i in range(1, len(sys.argv)):
        if 'help' in sys.argv[i]:
            help()
            break
        elif '-' in sys.argv[i]:
            flags += str(sys.argv[i])
    return(flags)

def readFile(flag):
    fileList = {}
    for i in range(1,len(sys.argv)):
        if '.txt' in sys.argv[i]:
            file = open(sys.argv[i], mode='r', encoding='ASCII')
            temp = frequency(file.read(), flag)
            fileList[i] = temp
            print(fileList)



def frequency(text, flag):
    #userinput = input('What is your name?')
    #print(f'Hello {userinput}!')
    if flag == 'n':
        text = text.lower()
        frequency = {}
        for letter in text:
            if letter in alphabetLower:
                if letter in frequency:
                    frequency[letter] = frequency[letter] + 1
                else:
                    frequency[letter] = 1
    elif flag == 'c':
        frequency = {}
        for letter in text:
            if letter in alphabetLower or letter in alphabetUpper:
                if letter in frequency:
                    frequency[letter] = frequency[letter] + 1
                else:
                    frequency[letter] = 1
    return(frequency)



    # vals = []
    # for val in sys.argv:
    #     vals.append(val)
    # #print(vals)
    # punctuation = ''
    # if '-q' in vals:
    #     punctuation = '?'
    # elif '-Q' in vals:
    #     punctuation = '?!'
    # else:
    #     punctuation = '!'
    # if '-n' in val:
    #     flagIndex = vals.index('-n')
    #     num = vals[flagIndex+1]
    #     print(f'Hello, {vals[-1]}{punctuation*int(num)}')
    # else:
    #     print(f'Hello, {vals[-1]}{punctuation}')

# def frequency(text):
#
#
def main():
    flagList = ''
    flagList = flags()
    # print(flagList)
    # print(sys.argv)
    if "help" in flagList:
        help()
    elif "-c" in sys.argv:
        readFile('c')
    elif "-" != sys.argv:
        readFile('n')

    # word = 'Abracadabra!'
    # print(f'Frequency of letters is {frequency(word)}')

# ---------------------------------------

main()

