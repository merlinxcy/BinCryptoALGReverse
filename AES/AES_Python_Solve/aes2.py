from Crypto.Cipher import AES

key = b'abcdefghijklmnop'

cipher = AES.new(key, AES.MODE_ECB)
msg =cipher.encrypt(b'TechTutorialsX!!TechTutorialsX!!')
print (type(msg))

print()

decipher = AES.new(key, AES.MODE_ECB)
print(decipher.decrypt(msg))