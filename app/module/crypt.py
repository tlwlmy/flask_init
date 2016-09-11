#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.05.07 tlwlmy
#
from AESCipher import AESCipher
import urllib, base64
from time import time

class Crypt(AESCipher):
    def wx_encrypt(self, appid, uid, feedback=''):
        # 加密微信串
        decrypted = str(uid) + '&' + base64.b64encode(feedback) + '&' + str(int(time()))
        return urllib.quote_plus(appid + base64.b64encode(self.encrypt(decrypted)))

    def wx_decrypt(self, encrypted):
        # 解密微信串
        decrypted = self.decrypt(base64.b64decode(encrypted))
        data = decrypted.split('&')
        final = {
            'uid': int(data[0]),
            'feedback': base64.b64decode(data[1]),
            'jumpt': int(data[2]),
        }
        return final

    def user_encrypt(self, appid, user_name, feedback=''):
        # 加密用户串
        decrypted = user_name + '&' + base64.b64encode(feedback) + '&' + str(int(time()))
        return urllib.quote_plus(appid + base64.b64encode(self.encrypt(decrypted)))

    def user_decrypt(self, encrypted):
        # 解密用户串
        decrypted = self.decrypt(base64.b64decode(encrypted))
        data = decrypted.split('&')
        final = {
            'user_name': data[0],
            'feedback': base64.b64decode(data[1]),
            'jumpt': int(data[2]),
        }
        return final

    def encrypt_str(self, s):
        # 加密一串字符
        return urllib.quote_plus(base64.b64encode(self.encrypt(s)))

    def decrypt_str(self, encrypted):
        # 解密一串字符
        decrypted = self.decrypt(base64.b64decode(encrypted))
        return decrypted

if __name__ == '__main__':
    crypt = Crypt('d4624c36b6795d1d99dcf0547af5443d')
    s = crypt.wx_encrypt('wx347c052a4e58f9ce', 51, 'tlwlmy')
    print s
    decrypted = s[18:]
    decrypted = urllib.unquote(decrypted)
    print crypt.wx_decrypt(decrypted)

    crypt = Crypt('a8562b193263c6946ef21cd793a46768')
    s = crypt.wx_encrypt('wxacf7d47458577b75', 2, 'tlwlmy')
    print s
    decrypted = s[18:]
    decrypted = urllib.unquote(decrypted)
    print crypt.wx_decrypt(decrypted)
