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

#Taken from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

#E(x) = (x+a)%m
def shift(cipherText="mbkmuwo",key=16,alphabet=list(string.ascii_lowercase)):
    key = key%len(alphabet)
    print("Shifting {} by {}".format(cipherText, key))
    result = ""
    for character in cipherText:
        #print(alphabet[((alphabet.index(character)+key)%len(alphabet))])
        result=result+(alphabet[((alphabet.index(character)+key)%len(alphabet))])
    print("Result: {}".format(result))

#E(x) = (ax+b)%m
def affineEncipher(plainText="affinecipher",key=(5,8),alphabet=list(string.ascii_lowercase)):
    print("Affine Enciphering {} with a={} b={}".format(plainText, key[0], key[1]))
    result = ""
    for character in plainText:
        result = result+(alphabet[((key[0]*alphabet.index(character)+key[1])%len(alphabet))])
    print("Result: {}".format(result))

def affineDecipher(cipherText="ihhwvcswfrcp",key=(5,8),alphabet=list(string.ascii_lowercase)):
    print("Affine Deciphering {} with a={} b={}".format(cipherText, key[0], key[1]))
    inverseKey = modinv(key[0], len(alphabet))
    if inverseKey == None:
        print("No inverse key. Exiting.")
        return
    result = ""
    for character in cipherText:
        result = result+(alphabet[((inverseKey*(alphabet.index(character)-key[1]))%len(alphabet))])
    print("Result: {}".format(result))

#Testing area
#shift()
affineEncipher()
affineDecipher()
