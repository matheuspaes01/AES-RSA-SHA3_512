"""Função Hash (SHA3_512 - hashlib)"""


import hashlib

mensagem = "Matheus Paes"

# Gera o hash SHA3_512
hash_obj = hashlib.sha3_512(mensagem.encode())
hash_hex = hash_obj.hexdigest()

print("Hash SHA3_512:", hash_hex)