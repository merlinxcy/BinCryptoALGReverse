from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES


# Padding for the input string --not
# related to encryption itself.
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    """
    Usage:
        c = AESCipher('password').encrypt('message')
        m = AESCipher('password').decrypt(c)
    Tested under Python 3 and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()


    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf8')


##
# MAIN
# Just a test.

msg = '{"count":"3"}'
pwd = b"m@t1OSXOqIGrb4H!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
# pwd = b"#kSdmGKNq8BMlZ@zEAVyvv$#JJgIJZ3l"
# pwd = b"m@t1OSXOqIGrb4H!EAVyvv$#JJgIJZ3l"
# pwd = b"m@t1OSXOqIGrb4H!m@t1OSXOqIGrb4H!"
print(len(pwd))
# print('Ciphertext:', AESCipher(pwd).encrypt(msg))
cipher = AES.new(pwd, AES.MODE_ECB)
# print(bytes(pad(msg),'utf-8'))
a = cipher.encrypt(bytes(pad(msg),'utf-8'))
# # a = cipher.encrypt(a)
print(b64encode(a))
a=cipher.decrypt(b64decode("4d6JpSRedv157JfuanpeOrOt49oplds0ddfLVl62tMlJ4KcevbiEWKtu49QRtJRnLR7dsEMmgOoEwRqWdr72a0RykIcQ9G93htARRQ0MkvsLc+bT2pJr2CuYE+tcru+bePzc+mqVxZnMjqA0Joj+9iZZ2mFlnb4VF4EaTQuGi/jgd1R2BSbi3CxeWv0Mukb0xMnbsaus7j/tPbwxf6Ji1RhNVmkMXsI3zttp4MpIjlz/ppMQHRpnsc5kdSGCIKU78wCA4xKiN8cMchqC52sSeLYW4pcLQ0CvCq5Aogwhku2kgZvTZOvV2tys4DHb+Yay5lfpxzODKrJnVgeMO1ui6feNv+NnFSuz171dV1Y//bsYVaI1C73EXRqmJeN1SO93piYwX908Shj9MeJY11WlPZRkBF4wfSySy63U8tSIl6Qte7+KfCGO+uHQA/5wb4eESnjfcR1qYBjEd8uMP8Vk2NsF2nMhzCiVqdrTLto3xevD5PwI/8bmhTrdiINGMsLLW50Ft9pTiFsepBe1Wm6nzzv7UoFt0XAXweQlY8kXBud565/5zwTkPQ6fUCulReM92TO0xLhIZYduvFU6GggGOSxGZfh4vsQwVL964heyG7IuevEf/wRy4SLvsfOwD9dflCWwB7mxxWFNz8StcOtCAAqsOGKiIvQw8vEXQQwGA6W83VqaB2fJxOYm25jG/GQvrHs19eJEtIHYjKuA+mTyGhlCOugZ1cvFXJkaHzKRicgPvIs7iDQmXoFF5736qJUhe/GWybDYHBgyphaYXnoAb9kztMS4SGWHbrxVOhoIBjksRmX4eL7EMFS/euIXshuyCu7M3Dr8dby74KGQyr7vT5QlsAe5scVhTc/ErXDrQgAKrDhioiL0MPLxF0EMBgOlvN1amgdnycTmJtuYxvxkL6x7NfXiRLSB2IyrgPpk8hooTVMlRPz5Gpvw4zzFvYL0tBygNjgaNIKjUWV/Dcmy1El5eaOEW48Bd/PRLmr9l1DYFjjEPDmH0uMlbLpI1uNRQQjrG6LFvLjuGIVyOn7yJYJWB6O/tYuMdOQGKOj1trlFaAnlLPmL7icnXT/B7/9xTLMGE6gXBWhKv0pfg0d8MdoMBADooeFedylDR2V9nmEwawRwJErvsYS18+OcRFHeZ9bFVGcuW8rVxUJ8TbMS3UB4TGLetw+58FdfHAkE27U0nBbOCFQpwZKIAQ4U4cRPm5+4HjyXDaYM97XLJsFvr7ifXlzhhYgZ/jt1lrrso9/KvQQ5dgKH6Opezvhy0Hgma9NkJC8L+uzy6hu2uUSz2jgGPhev117/3frLB+Vs9e1Xy2hY9UK/PU+qetrzEtXdc7CNYtG7epqpKcZA+o0mvorPrDvOwfWwFNnQhm+r75Sj/LTqPauQd21/O2Nqb6J+FfLBw8ZFTFZhVKKsza3MLbLBSg6CkjQZUiXA4+2eeN56fX5ttbtXAN79uGjoHfBc4d8XrnExzYSiH+znaTrc7Ti5/MQEvmCMNAIh0owgDEUd/vnnMOhKCYhPIoKHDvliAfAIXSZnnTj2aKgFV7dOBZ+9i7n26thKDnwdCm3cb/ZHbTqYmBQPjUNXKkn/5pOybDDEtMascKz2kef9jU6qseVgsLDRYQyCW6I+wNoQi4XJDhKtoH0aUtnphT99muRbZXN83LAubSllfyAVO8qlGXmJJVV1vT9iv+/8xIkIFe5OMAnLirsD1Zbo5moK9SyfBPFaMxljG3SSlVW/jn6thA=="))
# print(unpad(a))
a=cipher.decrypt(b64decode("iI5qKHBSjB4iM5KYIKzHyg=="))
print(a)