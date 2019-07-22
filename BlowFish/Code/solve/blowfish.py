from Crypto.Cipher import Blowfish
import base64
'''
cipher = Blowfish.new("TESTKEY")
encrypted_data = cipher.encrypt(b'\x00\x00\x00\x00\x00\x00\x00\x01')
print(encrypted_data)

print()
decryped_data = cipher.decrypt(b'\xDF\x33\x3F\xD2\x30\xa7\x1b\xb4')
print(decryped_data)
'''
cipher = Blowfish.new("TESTKEY")
encrypted_data = cipher.encrypt(b"aaaaaaaabbbbbbbb")
print(encrypted_data)
