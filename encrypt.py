import base64
from Crypto.Cipher import AES


def AES_encrypt(key, data):
    vi = '0102030405060708'
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    data = pad(data)
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    encodestrs = base64.b64encode(encryptedbytes)
    enctext = encodestrs.decode('utf8')
    return enctext


def AES_decrypt(key, data):
    vi = '0102030405060708'
    data = data.encode('utf8')
    encodebytes = base64.decodebytes(data)
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)

    unpad = lambda s: s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted)
    text_decrypted = text_decrypted.decode('utf8')
    
    return text_decrypted


if __name__ == "__main__":
    with open("data.txt", "r") as f:
      data = f.read()
    with open("key.txt","r") as f:
      key = f.read()
    if len(key) > 32:
        key = key[0:32]
        print("key: ", key)
    elif len(key) < 32:
        raise AssertionError("密钥字符串key.txt内容小于32字符")
    with open("encrypt.txt","w") as f:
        AES_encrypt(key, data)
        enctext = AES_encrypt(key, data)
        f.write(enctext)
        print(enctext)
        print(AES_decrypt(key, enctext))

    print("加密成功")

