import string
import base64
s = '123'
data = base64.b64encode(s)
print(data)
my_base64chars  = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

s = s.translate(string.maketrans(my_base64chars, std_base64chars))
data = base64.b64encode(s)
print(data)
