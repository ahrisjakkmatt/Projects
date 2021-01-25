import sys

# Vowels
# Ignore Case
# Count multiple files
# Print out frequency of zero
# CSV format
# Help

# Example command prompt:
#   python count.py [-c] [-l letters] [-z] file_1 file_2 ... file_n

def flags():
    flags = ''
    for i in range(1, len(sys.argv)):
        if '-' in sys.argv[i]:
            flags += str(sys.argv[i][1:])
    print(flags)

def frequency(text):
    #userinput = input('What is your name?')
    #print(f'Hello {userinput}!')
    frequency = {}

    for letter in text:
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
    flags()
    word = 'Abracadabra!'
    print(frequency(word))

# ---------------------------------------

main()

