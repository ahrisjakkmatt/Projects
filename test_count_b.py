import unittest
import count_b
#import count_to_csv
#import csv


'''
from count_b import returnDict
emptyDict = {}
returnDict()

class flags:
    def __init__(self, files=[''], flags={}, queryLetters=''):
        self.files = files
        self.flagSet = flags
        self.queryLetters = queryLetters
'''

class TestCount(unittest.TestCase):
    def test_returnDict(self):
        noFlags = [{},'', 'test.txt']
        result_noFlags = count_b.returnDict(noFlags)
        flags_C = [{'c'}, '', ['test.txt']]
        result_C = count_b.returnDict(flags_C)
        flags_L = [{'l'}, 'ab', ['test.txt']]
        result_L = count_b.returnDict(flags_L)
        flags_Z = [{'z'}, '', ['test.txt']]
        result_Z = count_b.returnDict(flags_Z)
        flags_CL = [{'c','l'}, '', ['file_1.txt', 'file_2.txt']]
        result_CL = count_b.returnDict(flags_CL)
        flags_CZ = [{'c','z'}, '', ['file_1.txt', 'file_2.txt']]
        result_CZ = count_b.returnDict(flags_CZ)
        flags_LZ = [{'l', 'z'}, '', ['file_1.txt', 'file_2.txt']]
        result_LZ = count_b.returnDict(flags_LZ)
        flags_CLZ = [{'c','l','z'}, 'Ahriel', ['file_1.txt', 'file_2.txt', 'test.txt']]
        result_CLZ = count_b.returnDict(flags_CLZ)

        self.assertEqual(result_noFlags,
                         {"a": 2,"b":2,"c":2,"d":2})
        self.assertEqual(result_C,
                         {"b":2,"c":1,"d":1,"A":2,"C":1,"D":1})
        self.assertEqual(result_L,
                         {"a":2,"b":2})
        self.assertEqual(result_Z,
                         {"a":2, "b":2,"c":2,"d":2,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,
                          "o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0})
        self.assertEqual(result_CL,
                         {'H': 1, 'e': 6, 'l': 6, 'o': 5, 'w': 2, 'r': 1, 'd': 2, 'T': 2, 'h': 3, 'i': 7, 's': 6,
                          'f': 1, 'c': 2, 'n': 5, 't': 3, 'a': 1})
        self.assertEqual(result_CZ,
                         {'H': 1, 'e': 6, 'l': 6, 'o': 5, 'w': 2, 'r': 1, 'd': 2, 'T': 2, 'h': 3, 'i': 7, 's': 6,
                          'f': 1, 'c': 2, 'n': 5, 't': 3, 'a': 1})
        self.assertEqual(result_LZ,
                         {'H': 1, 'e': 6, 'l': 6, 'o': 5, 'w': 2, 'r': 1, 'd': 2, 'T': 2, 'h': 3, 'i': 7, 's': 6,
                          'f': 1, 'c': 2, 'n': 5, 't': 3, 'a': 1})
        self.assertEqual(result_CLZ,
                         {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                          'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U':
                              0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
                          'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p'
                          : 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
                         )


if __name__ == '__main__':
    unittest.main()