#Jonah Blaydes-Greenberg Crypto Project
#Mr. Redmond C Block
#9/29/20

import math
import random

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypt_dummy = []
    #runs through the list and checks for between the accepted values
    for i in plaintext:
        print("input charcter : " + i)
        if i.isupper():
            character_dummy = chr(ord('A') + ((ord(i) - ord('A') + offset) % 26))
            print("Changed character : " + character_dummy)
            encrypt_dummy.append(character_dummy)
            #makes adjustments using the offset
        else:
            encrypt_dummy.append(i)
        
    return ''.join(encrypt_dummy)

# Arguments: string, integer
# Returns: string
#runs through the list and checks for between the accepted values
def decrypt_caesar(ciphertext, offset):
    encrypt_dummy = []
    for i in ciphertext:
        if i.isupper():
            character_dummy = chr(ord('A') + ((ord(i) - ord('A') - offset) % 26))
            print("Changed character : " + character_dummy)
            encrypt_dummy.append(character_dummy)
            #makes adjustments using the offset
        else:
            encrypt_dummy.append(i)
        
    return ''.join(encrypt_dummy)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypt_dummy = []
    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            offset = ord(keyword[i % len(keyword)]) - ord('A')
            character_dummy = chr(ord('A') + ((ord(plaintext[i]) - ord('A') + offset) % 26))
            encrypt_dummy.append(character_dummy)
        else:
            encrypt_dummy.append(plaintext[i])
    return ''.join(encrypt_dummy)

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    encrypt_dummy = []
    for i in range(len(ciphertext)):
        if ciphertext[i].isupper():
            offset = ord(keyword[i % len(keyword)]) - ord('A')
            character_dummy = chr(ord('A') + ((ord(ciphertext[i]) - ord('A') - offset) % 26))
            encrypt_dummy.append(character_dummy)
        else:
            encrypt_dummy.append(ciphertext[i])
    return ''.join(encrypt_dummy)
    

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    W = []
    W.append(random.randint(1,10))
    #creates the key using a random integer, superincreases
    for i in range (0,n -1):
        W.append(random.randint(sum(W) + 1, 2 * sum(W)))
    Q = random.randint(sum(W) + 1, 2 * sum(W))
    R = 0
    for r in range(2,Q):
        if math.gcd(r, Q) == 1:
            R = r
            break
    return (tuple(W),Q,R)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    W,Q,R = private_key
    B = []
    #Uses the private key to go back
    for element in W:
        B.append(R * element % Q)
    return tuple(B)

#Arguments: bits : a list of 0 and 1
# Returns: an integer in between 0 and 255, the byte that is associated with the bits
def bits_to_byte(bits):
    returnByte = 0
    #runs through the positions
    for i in range(0,8):
        if bits[i] > 0:
            returnByte = returnByte + 2 ** (7-i)
    return returnByte

#Argument byte: a number between 0 and 255
#Returns: a list of 0 and 1 of length 8
def byte_to_bits(byte):
    returnList = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if 2 ** (7 -i) <= byte:
            returnList[i] = 1
            byte = byte - 2 ** (7-i)
    return returnList

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):  
    encryptedList = []
    #running through the letters
    for letter in plaintext:
        M = byte_to_bits(ord(letter))
        C = 0
        #going through each bit
        for i in range(0,8):
            MPosition = M[i]
            keyPosition = public_key[i]
            #makes adjustments to C
            C = C + (keyPosition * MPosition)
        encryptedList.append(C)
    return encryptedList
    

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    returnList = []
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    #calls the calculate S method that finds the modulo inverse
    S = calculateS(R,Q)
    #moves through the ciphertext
    for i in range(len(ciphertext)):
        C = ciphertext[i] * S % Q
        bitDummy = []
        #moves from back to front
        for w in reversed(W):
            #if it is present
            if w <= C:
                #adds a 1 in the byte to show true
                bitDummy.append(1)
                C = C - w
            else:
                #adds a 0 to the byte to show false
                bitDummy.append(0)
        #Formats everything correctly
        byteDummy = bits_to_byte(list(reversed(bitDummy)))
        returnList.append(chr(byteDummy))
    return ''.join(returnList)

def calculateS(R,Q):
    for S in range (2,Q):
        if (R * S % Q == 1):
            return S

def main():

     print(decrypt_vigenere("TAE ST!", "B"))
    
if __name__ == "__main__":
    main()
