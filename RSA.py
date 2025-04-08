"""Criptografia com Chave Assimétrica (RSA - cryptography)"""


from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# Gera par de chaves RSA
chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
chave_publica = chave_privada.public_key()

# Mensagem
mensagem = "Matheus Paes"

# Criptografa com chave pública
# The message needs to be encoded to bytes before encryption.
mensagem_criptografada = chave_publica.encrypt(
    mensagem.encode('utf-8'),  # Encode the message to bytes using UTF-8
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Criptografado:", mensagem_criptografada)

# Descriptografa com chave privada
mensagem_original = chave_privada.decrypt(
    mensagem_criptografada,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Original:", mensagem_original.decode())
