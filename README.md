# Classical cryptographic ciphers
## Functions
All functions will print their results and return them.
### Ceaser/Shift ciphers
```python
shift(cipherText="mbkmuwo",key=16,alphabet=list(string.ascii_lowercase))
```
### Affine Cipher
```python
affineEncipher(plainText="affinecipher",key=(5,8),alphabet=list(string.ascii_lowercase))  
affineDecipher(cipherText="ihhwvcswfrcp",key=(5,8),alphabet=list(string.ascii_lowercase))
```
### Vigenere Cipher
```python
vigenereEncipher(plainText="vigenerecipher", key=list(string.ascii_lowercase), alphabet=list(string.ascii_lowercase))  
vigenereDecipher(cipherText="vigenerecipher", key=list(string.ascii_lowercase), alphabet=list(string.ascii_lowercase))
```
## Notes
Single file for simple integration  
F.L. Bauer's Decrypted Secrets used as a primary source
