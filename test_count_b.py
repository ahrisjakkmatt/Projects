# Created by:           Ahriel Godoy
# Student ID:           871928876
# Program Description:  this script tests the function returnDict from count_b in the previous project
#                       given all combinations of flags

import unittest
import count_b

class TestCount(unittest.TestCase):
    def test_returnDict(self):
        noFlags = [set(),'', ['test.txt','file_1.txt','file_2.txt']]
        result_noFlags = count_b.returnDict(noFlags)
        flags_C = [{'c'}, '', ['test.txt', 'file_1.txt','file_2.txt']]
        result_C = count_b.returnDict(flags_C)
        flags_L = [{'l'}, 'ab', ['test.txt', 'file_1.txt', 'file_2.txt']]
        result_L = count_b.returnDict(flags_L)
        flags_Z = [{'z'}, '', ['test.txt','file_1.txt','file_2.txt']]
        result_Z = count_b.returnDict(flags_Z)
        flags_CL = [{'c','l'}, 'Ahriel', ['test.txt', 'file_1.txt', 'file_2.txt']]
        result_CL = count_b.returnDict(flags_CL)
        flags_CZ = [{'c','z'}, '', ['test.txt','file_1.txt', 'file_2.txt']]
        result_CZ = count_b.returnDict(flags_CZ)
        flags_LZ = [{'l', 'z'}, 'Ahriel', ['file_1.txt', 'file_2.txt', 'test.txt']]
        result_LZ = count_b.returnDict(flags_LZ)
        flags_CLZ = [{'c','l','z'}, 'Ahriel', ['file_1.txt', 'file_2.txt', 'test.txt']]
        result_CLZ = count_b.returnDict(flags_CLZ)

        self.assertEqual(result_noFlags,
                         #return all letter counts after converting all letters to lowercase
                         {'a': 3, 'b': 2, 'c': 4, 'd': 4, 'h': 4, 'e': 6, 'l': 6, 'o': 5, 'w': 2, 'r': 1, 't': 5, 'i': 7, 's': 6, 'f': 1, 'n': 5})
        self.assertEqual(result_C,
                         #return all letters without changing capitalization
                         {'A': 2, 'b': 2, 'C': 1, 'c': 3, 'd': 3, 'D': 1, 'H': 1, 'e': 6, 'l': 6, 'o': 5, 'w': 2,
                          'r': 1, 'T': 2, 'h': 3, 'i': 7, 's': 6, 'f': 1, 'n': 5, 't': 3, 'a': 1})
        self.assertEqual(result_L,
                         #only looking for a and b
                         {'a': 3, 'b': 2})
        self.assertEqual(result_Z,
                         #these are all letters in the lower alphabet
                         {'a': 3, 'b': 2, 'c': 4, 'd': 4, 'e': 6, 'f': 1, 'g': 0, 'h': 4, 'i': 7, 'j': 0, 'k': 0,
                          'l': 6, 'm': 0, 'n': 5, 'o': 5, 'p': 0, 'q': 0, 'r': 1, 's': 6, 't': 5, 'u':
                              0, 'v': 0, 'w': 2, 'x': 0, 'y': 0, 'z': 0})
        self.assertEqual(result_CL,
                         #looking for the letters in the string Ahriel without changing capitalization
                         {'A': 2, 'e': 6, 'l': 6, 'r': 1, 'h': 3, 'i': 7})
        self.assertEqual(result_CZ,
                         #these are all letters in the combined upper and lower alphabets
                         {'A': 2, 'B': 0, 'C': 1, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 1, 'I': 0, 'J': 0, 'K': 0,
                          'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 2, 'U':
                              0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 6, 'f': 1,
                          'g': 0, 'h': 3, 'i': 7, 'j': 0, 'k': 0, 'l': 6, 'm': 0, 'n': 5, 'o': 5, 'p'
                          : 0, 'q': 0, 'r': 1, 's': 6, 't': 3, 'u': 0, 'v': 0, 'w': 2, 'x': 0, 'y': 0, 'z': 0})
        self.assertEqual(result_LZ,
                         #within the given string 'Ahriel' what letters matches the lowercase letters ... 'hriel' and give 0 to all others
                         #this is somewhat contradictory, confusing, redundant and not necessarily useful feedback

                         {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 6, 'f': 0, 'g': 0, 'h': 4, 'i': 7, 'j': 0, 'k': 0,
                          'l': 6, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 1, 's': 0, 't': 0, 'u':
                              0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})
        self.assertEqual(result_CLZ,
                         #sampling out of the combined upper and lower alphabets, count the correct case and letter match within the string 'Ahriel'
                         #providing 0 to all other entries

                         {'A': 2, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                          'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U':
                              0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 6, 'f': 0,
                          'g': 0, 'h': 3, 'i': 7, 'j': 0, 'k': 0, 'l': 6, 'm': 0, 'n': 0, 'o': 0, 'p'
                          : 0, 'q': 0, 'r': 1, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})


if __name__ == '__main__':
    unittest.main()