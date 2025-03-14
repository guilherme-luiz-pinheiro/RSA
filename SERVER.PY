import random
from socket import *
 
def miller_rabin(n, k=20):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gerar_primo():
    while True:
        num = random.getrandbits(2048) | (1 << 2047) | 1
        if miller_rabin(num):
            return num

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def inverso_modular(a, m):
    g, x, _ = extended_gcd(a, m)
    return x % m if g == 1 else None

def gerar_chaves():
    p = gerar_primo()
    print(f"P: {p} \n")
    q = gerar_primo()
    print(f"Q: {q} \n")
    while p == q:
        q = gerar_primo()
    
    n = p * q
    totiente = (p - 1) * (q - 1)
    
    e = 65537
    if mdc(e, totiente) != 1:
        e = 3
    
    d = inverso_modular(e, totiente)
    return (e, n), (d, n)

def decriptografar(mensagem_criptografada, chave_privada):
   d, n = chave_privada
   return ''.join([chr(pow(char, d, n)) for char in mensagem_criptografada])
 
def criptografar(mensagem, chave_publica):
   e, n = chave_publica
   return [pow(ord(char), e, n) for char in mensagem]
 
def servidor():
   chave_publica, chave_privada = gerar_chaves()
 
   serverPort = 1300
   serverSocket = socket(AF_INET, SOCK_STREAM)
   serverSocket.bind(("", serverPort))
   serverSocket.listen(5)
   print("Servidor ON\n")
 
   connectionSocket, addr = serverSocket.accept()
   print(f"Conexão recebida de {addr}")
 
   chave_publica_cliente = eval(str(connectionSocket.recv(65000), 'utf-8'))
   print(f"Chave pública recebida do cliente: {chave_publica_cliente}")
 
   connectionSocket.send(str(chave_publica).encode())
   print(f"Chave pública do servidor enviada para o cliente: {chave_publica}")
 
   sentence = connectionSocket.recv(65000)
 
   mensagem_criptografada = eval(str(sentence, 'utf-8'))
   print(f"Mensagem Criptografada recebida do cliente: {mensagem_criptografada}")
 
   mensagem_decriptografada = decriptografar(mensagem_criptografada, chave_privada)
   print(f"Mensagem decriptografada do cliente: {mensagem_decriptografada}")
 
   mensagem_maiuscula = mensagem_decriptografada.upper()
   print(f"Mensagem em maiúsculas: {mensagem_maiuscula}")
 
   mensagem_criptografada_resposta = criptografar(mensagem_maiuscula, chave_publica_cliente)
 
   connectionSocket.send(str(mensagem_criptografada_resposta).encode())
   print(f"Mensagem criptografada (maiúsculas) enviada ao cliente: {mensagem_criptografada_resposta}")
 
   connectionSocket.close()
 
servidor()

