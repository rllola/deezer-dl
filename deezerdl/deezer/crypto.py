from Crypto.Hash import MD5
from Crypto.Cipher import AES, Blowfish
import struct
import urllib.parse
import html.parser
import requests
from binascii import a2b_hex, b2a_hex

def md5hex(data):
    """ return hex string of md5 of the given string """
    # type(data): bytes
    # returns: bytes
    h = MD5.new()
    h.update(data)
    return b2a_hex(h.digest())

def hexaescrypt(data, key):
    """ returns hex string of aes encrypted data """
    c = AES.new(key.encode(), AES.MODE_ECB)
    return b2a_hex(c.encrypt(data))

def calcbfkey(songid):
    """ Calculate the Blowfish decrypt key for a given songid """
    key = b"g4el58wc0zvf9na1"
    songid_md5 = md5hex(songid.encode())

    xor_op = lambda i: chr(songid_md5[i] ^ songid_md5[i + 16] ^ key[i])
    decrypt_key = "".join([xor_op(i) for i in range(16)])
    return decrypt_key


def blowfishDecrypt(data, key):
    iv = a2b_hex("0001020304050607")
    c = Blowfish.new(key.encode(), Blowfish.MODE_CBC, iv)
    return c.decrypt(data)

def decryptfile(fh, key, fo):
    """
    Decrypt data from file <fh>, and write to file <fo>.
    decrypt using blowfish with <key>.
    Only every third 2048 byte block is encrypted.
    """
    blockSize = 2048
    i = 0

    for data in fh.iter_content(blockSize):
        if not data:
            break

        isEncrypted = ((i % 3) == 0)
        isWholeBlock = len(data) == blockSize

        if isEncrypted and isWholeBlock:
            data = blowfishDecrypt(data, key)

        fo.write(data)
        i += 1