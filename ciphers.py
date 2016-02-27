#!/usr/bin/python3
import array
import string
#Constants available in strings package
#ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#digits = '0123456789'
#hexdigits = '0123456789abcdefABCDEF'
#octdigits = '01234567'
#printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#whitespace = ' \t\n\r\x0b\x0c'

def shift(cipherText="crackme",key=26,alphabet=list(string.ascii_lowercase)):
    key = key%len(alphabet)
    print("Shifting {} by {}".format(cipherText, key))
    result = ""
    for character in cipherText:
        #print(alphabet[alphabet.index(character)+key])
        result=result+(alphabet[alphabet.index(character)+key])
    print("Result: {}".format(result))

#Testing area
shift()