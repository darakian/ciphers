#!/usr/bin/python3
import array
import string

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
#End wikibooks code

#E(x) = (x+a)%m
def shift(cipherText="mbkmuwo",key=16,alphabet=list(string.ascii_lowercase)):
    cipherText = cipherText.lower()
    key = key%len(alphabet)
    print("Shifting {} by {}".format(cipherText, key))
    result = ""
    for character in cipherText:
        #print(alphabet[((alphabet.index(character)+key)%len(alphabet))])
        result=result+(alphabet[((alphabet.index(character)+key)%len(alphabet))])
    print("Result: {}".format(result))
    return result

#E(x) = (ax+b)%m
def affineEncipher(plainText="affinecipher",key=(5,8),alphabet=list(string.ascii_lowercase)):
    plainText = plainText.lower()
    print("Affine Enciphering {} with a={} b={}".format(plainText, key[0], key[1]))
    result = ""
    for character in plainText:
        result = result+(alphabet[((key[0]*alphabet.index(character)+key[1])%len(alphabet))])
    print("Result: {}".format(result))
    return result

def affineDecipher(cipherText="ihhwvcswfrcp",key=(5,8),alphabet=list(string.ascii_lowercase)):
    cipherText = cipherText.lower()
    print("Affine Deciphering {} with a={} b={}".format(cipherText, key[0], key[1]))
    inverseKey = modinv(key[0], len(alphabet))
    if inverseKey == None:
        print("No inverse key. Exiting.")
        return
    result = ""
    for character in cipherText:
        result = result+(alphabet[((inverseKey*(alphabet.index(character)-key[1]))%len(alphabet))])
    print("Result: {}".format(result))
    return result

def vigenereEncipher(plainText="vigenerecipher", key=list(string.ascii_lowercase), alphabet=list(string.ascii_lowercase)):
    plainText = plainText.lower()
    print("Vigenere Enciphering {} with key = {}".format(plainText, key))
    result = ""
    i=0
    for character in plainText:
        result = result+alphabet[(alphabet.index(character)+alphabet.index(key[i%len(key)]))%len(alphabet)]
        i=i+1
    print("Result: {}".format(result))
    return result

def vigenereDecipher(cipherText="vigenerecipher", key=list(string.ascii_lowercase), alphabet=list(string.ascii_lowercase)):
    cipherText = cipherText.lower()
    print("Vigenere Enciphering {} with key = {}".format(cipherText, key))
    result = ""
    i=0
    for character in cipherText:
        result = result+alphabet[(alphabet.index(character)-alphabet.index(key[i%len(key)]))%len(alphabet)]
        i=i+1
    print("Result: {}".format(result))
    return result

#Testing area
#shift()
#affineEncipher()
#affineDecipher()
#vigenereEncipher(plainText="attackatdawn",key="lemon")
#vigenereDecipher(cipherText="lxfopvefrnhr",key="lemon")
