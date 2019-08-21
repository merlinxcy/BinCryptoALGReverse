from base64 import *
import base64
import string
import binascii
class RC4:
    """
    This class implements the RC4 streaming cipher.

    Derived from http://cypherpunks.venona.com/archive/1994/09/msg00304.html
    """

    def __init__(self, key, streaming=True):
        assert (isinstance(key, (bytes, bytearray)))

        # key scheduling
        S = list(range(0x100))
        j = 0
        for i in range(0x100):
            j = (S[i] + key[i % len(key)] + j) & 0xff
            S[i], S[j] = S[j], S[i]
        self.S = S

        # in streaming mode, we retain the keystream state between crypt()
        # invocations
        if streaming:
            self.keystream = self._keystream_generator()
        else:
            self.keystream = None

    def crypt(self, data):
        """
        Encrypts/decrypts data (It's the same thing!)
        """
        assert (isinstance(data, (bytes, bytearray)))
        keystream = self.keystream or self._keystream_generator()
        return bytes([a ^ b for a, b in zip(data, keystream)])

    def _keystream_generator(self):
        """
        Generator that returns the bytes of keystream
        """
        S = self.S.copy()
        x = y = 0
        while True:
            x = (x + 1) & 0xff
            y = (S[x] + y) & 0xff
            S[x], S[y] = S[y], S[x]
            i = (S[x] + S[y]) & 0xff
            yield S[i]
a=[32, 195, 26, 174, 151, 60, 122, 65, 222, 246, 120, 21, 203, 75, 76, 220, 38, 85, 139, 85, 229, 233, 85, 117, 64, 61, 130, 19, 165, 96, 19, 59, 245, 216, 25, 14, 71, 207, 95, 94, 222, 157, 20, 189]
b=['0x20', '0xc3', '0x1a', '0xae', '0x97', '0x3c', '0x7a', '0x41', '0xde', '0xf6', '0x78', '0x15', '0xcb', '0x4b', '0x4c', '0xdc', '0x26', '0x55', '0x8b', '0x55', '0xe5', '0xe9', '0x55', '0x75', '0x40', '0x3d', '0x82', '0x13', '0xa5', '0x60', '0x13', '0x3b', '0xf5', '0xd8', '0x19', '0xe', '0x47', '0xcf', '0x5f', '0x5e', '0xde', '0x9d', '0x14', '0xbd']

strrr = b""
# for i in b:
#     print(i[2:])
#     strrr = strrr + binascii.a2b_hex(i[2:])

print(strrr)

print(b64encode(strrr))

strrr = bytes(a)


flagdd  = b64decode('IMODGsKuwpc8ekHDnsO2eBXDi0tMw5wmVcKLVcOlw6lVdUA9woITwqVgEzvDtcOYGQ5Hw49fXsOewp0Uwr0=')
tt = RC4(b"flag{this_is_not_the_flag_hahaha}").crypt(strrr)
print(tt)
# print(mybase_d(tt))

import base64
import string

# base 字符集

# base64_charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
base64_charset = 'ABCDEFGHIJSTUVWKLMNOPQRXYZabcdqrstuvwxefghijklmnopyz0123456789+/'


def encode(origin_bytes):
    """
    将bytes类型编码为base64
    :param origin_bytes:需要编码的bytes
    :return:base64字符串
    """

    # 将每一位bytes转换为二进制字符串
    base64_bytes = ['{:0>8}'.format(str(bin(b)).replace('0b', '')) for b in origin_bytes]

    resp = ''
    nums = len(base64_bytes) // 3
    remain = len(base64_bytes) % 3

    integral_part = base64_bytes[0:3 * nums]
    while integral_part:
        # 取三个字节，以每6比特，转换为4个整数
        tmp_unit = ''.join(integral_part[0:3])
        tmp_unit = [int(tmp_unit[x: x + 6], 2) for x in [0, 6, 12, 18]]
        # 取对应base64字符
        resp += ''.join([base64_charset[i] for i in tmp_unit])
        integral_part = integral_part[3:]

    if remain:
        # 补齐三个字节，每个字节补充 0000 0000
        remain_part = ''.join(base64_bytes[3 * nums:]) + (3 - remain) * '0' * 8
        # 取三个字节，以每6比特，转换为4个整数
        # 剩余1字节可构造2个base64字符，补充==；剩余2字节可构造3个base64字符，补充=
        tmp_unit = [int(remain_part[x: x + 6], 2) for x in [0, 6, 12, 18]][:remain + 1]
        resp += ''.join([base64_charset[i] for i in tmp_unit]) + (3 - remain) * '='

    return resp


def decode(base64_str):
    """
    解码base64字符串
    :param base64_str:base64字符串
    :return:解码后的bytearray；若入参不是合法base64字符串，返回空bytearray
    """
    if not valid_base64_str(base64_str):
        return bytearray()

    # 对每一个base64字符取下标索引，并转换为6为二进制字符串
    base64_bytes = ['{:0>6}'.format(str(bin(base64_charset.index(s))).replace('0b', '')) for s in base64_str if
                    s != '=']
    resp = bytearray()
    nums = len(base64_bytes) // 4
    remain = len(base64_bytes) % 4
    integral_part = base64_bytes[0:4 * nums]

    while integral_part:
        # 取4个6位base64字符，作为3个字节
        tmp_unit = ''.join(integral_part[0:4])
        tmp_unit = [int(tmp_unit[x: x + 8], 2) for x in [0, 8, 16]]
        for i in tmp_unit:
            resp.append(i)
        integral_part = integral_part[4:]

    if remain:
        remain_part = ''.join(base64_bytes[nums * 4:])
        tmp_unit = [int(remain_part[i * 8:(i + 1) * 8], 2) for i in range(remain - 1)]
        for i in tmp_unit:
            resp.append(i)

    return resp


def valid_base64_str(b_str):
    """
    验证是否为合法base64字符串
    :param b_str: 待验证的base64字符串
    :return:是否合法
    """
    if len(b_str) % 4:
        return False

    for m in b_str:
        if m not in base64_charset:
            return False
    return True


print('使用本地base64解密：', decode('ZeptZ3l5UHQra25nd19yYzMrYR5wX2Jtc2P2VF9gYNM9'))