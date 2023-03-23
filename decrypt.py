import time
ciphertext = input("Enter a message to decrypt >")
key = int(input("Input a key as a number between 1 and 10 >"))


def decrypt(ciphertext, key):
    
    plaintext = ciphertext[:len(ciphertext):key+1]
    
    return plaintext


while (key < 1 or key > 10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10 >"))


print("...")
time.sleep(1)
print("Decrypting ciphertext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = decrypt(ciphertext, key)
#Output...
print("Plaintext:")
print(ciphertext)