import hashlib

senha = input("Digite sua senha: ")
hash = hashlib.sha256(senha.encode()).hexdigest()

print("Hash da senha:", hash)
