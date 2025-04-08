"""Criptografia com Chave Simétrica (AES - cryptography)"""

from cryptography.fernet import Fernet

# Gera uma chave simétrica
chave = Fernet.generate_key()
fernet = Fernet(chave)

# Texto original
mensagem = "Matheus Paes"

# Criptografa
mensagem_criptografada = fernet.encrypt(mensagem.encode())
print("Criptografado:", mensagem_criptografada)

# Descriptografa
mensagem_original = fernet.decrypt(mensagem_criptografada).decode()
print("Original:", mensagem_original)
