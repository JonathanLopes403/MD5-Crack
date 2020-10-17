#!/usr/bin/python3
# Created By: Jonathan Lopes 

from sys import argv
from hashlib import md5

hash_alvo = argv[1]
wordlist = argv[2]

with open(wordlist, 'r') as arquivo:
    for senhas in arquivo.readlines():
        senha = senhas.strip()
        result = md5(senha.encode())
        if result.hexdigest() == hash_alvo:
            print (hash_alvo + ': ' + senha)
            break
