import random
import math
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

# Gerar número primo de 2048 bits
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

# Função de criptografia RSA
def criptografar(mensagem, chave_publica):
   e, n = chave_publica
   return [pow(ord(char), e, n) for char in mensagem]
 
# Função de decriptação RSA
def decriptografar(mensagem_criptografada, chave_privada):
   d, n = chave_privada
   return ''.join([chr(pow(char, d, n)) for char in mensagem_criptografada])
 
 
# Código do Cliente (Alice) com Criptografia RSA
def cliente():
   # Gerando chaves pública e privada
   chave_publica, chave_privada = gerar_chaves()
 
   # Conectando ao servidor
   serverName = '10.1.70.17'
   serverPort = 1300
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((serverName, serverPort))
 
   # Enviando a chave pública para o servidor
   clientSocket.send(str(chave_publica).encode())
   print(f"Chave pública do cliente enviada para o servidor: {chave_publica}")
 
   # Recebendo a chave pública do servidor
   chave_publica_servidor = eval(str(clientSocket.recv(65000), 'utf-8'))
   print(f"Chave pública do servidor recebida: {chave_publica_servidor}")
 
   # O cliente digita a mensagem
   mensagem = input("Digite a mensagem para enviar ao servidor: ")
 
   # Criptografando a mensagem com a chave pública do servidor
   mensagem_criptografada = criptografar(mensagem, chave_publica_servidor)
 
   # Enviando a mensagem criptografada para o servidor
   clientSocket.send(str(mensagem_criptografada).encode())
 
   # Recebendo a mensagem criptografada do servidor
   mensagem_criptografada_do_servidor = eval(str(clientSocket.recv(65000), 'utf-8'))
   print(f"Mensagem criptografada recebida do servidor: {mensagem_criptografada_do_servidor}")
 
   # Descriptografando a mensagem recebida usando a chave privada do cliente
   mensagem_decriptografada = decriptografar(mensagem_criptografada_do_servidor, chave_privada)
   print(f"Mensagem decriptografada recebida do servidor: {mensagem_decriptografada}")
 
   # Fechando a conexão
   clientSocket.close()
 
# Executando o cliente
cliente()
 