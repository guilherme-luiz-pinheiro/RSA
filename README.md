# 🔒 Comunicação Segura com Criptografia RSA em Python

Este projeto implementa uma comunicação segura entre cliente e servidor utilizando criptografia RSA. O cliente (Alice) envia uma mensagem criptografada ao servidor (Bob), que a descriptografa, converte para maiúsculas e retorna a mensagem criptografada de volta ao cliente.

## ⚙️ Tecnologias Utilizadas
- Python 3.x
- Criptografia RSA
- Sockets TCP

## 🔄 Funcionamento
### ⭐ Cliente
1. Gera um par de chaves (pública e privada) utilizando o algoritmo RSA.
2. Conecta-se ao servidor e envia sua chave pública.
3. Recebe a chave pública do servidor.
4. Envia uma mensagem criptografada com a chave pública do servidor.
5. Recebe a resposta do servidor (mensagem em maiúsculas criptografada) e a descriptografa utilizando sua chave privada.

### 💻 Servidor
1. Gera um par de chaves (pública e privada) utilizando o algoritmo RSA.
2. Aguarda a conexão do cliente.
3. Recebe a chave pública do cliente e envia sua própria chave pública de volta.
4. Recebe a mensagem criptografada do cliente, a descriptografa utilizando sua chave privada e converte a mensagem para maiúsculas.
5. Criptografa a resposta com a chave pública do cliente e envia de volta.

## 🤖 Descrição do Algoritmo RSA
O **RSA** é um sistema de criptografia assimétrica desenvolvido por Ronald Rivest, Adi Shamir e Leonard Adleman no MIT. Ele utiliza um par de chaves: uma **chave pública** para criptografar e uma **chave privada** para descriptografar. Sua segurança baseia-se na dificuldade de fatorar grandes números primos.

### Etapas para Geração de Chaves
1. **Escolha de dois números primos p e q** e cálculo de \( N = p \times q \).
2. Cálculo da função totiente \( \phi(N) = (p - 1) \times (q - 1) \).
3. Escolha de um número \( e \) tal que \( 1 < e < \phi(N) \) e que seja coprimo de \( \phi(N) \).
4. Cálculo de \( d \) tal que \( e \times d \mod \phi(N) = 1 \).

As chaves são:
- **Chave pública**: \( (e, N) \)
- **Chave privada**: \( (d, N) \)

**Criptografia:**  \( C = P^e \mod N \)  
**Descriptografia:**  \( P = C^d \mod N \)

## 🔧 Como Rodar
1. Clone este repositório:
   ```bash
   git clone https://github.com/usuario/arquivo.git
   cd arquivo
   ```
2. Execute o servidor:
   ```bash
   python servidor.py
   ```
3. Execute o cliente:
   ```bash
   python cliente.py
   ```
O cliente enviará uma mensagem para o servidor, que retornará a mensagem criptografada com a versão em maiúsculas.

## 📄 Funcionalidades
- **Geração de Chaves:** Utiliza o algoritmo RSA para criar um par de chaves pública e privada.
- **Criptografia e Descriptografia:** Mensagens criptografadas com a chave pública do destinatário e descriptografadas com a chave privada correspondente.
- **Comunicação Cliente-Servidor:** Conexão via sockets TCP para troca de mensagens seguras.

## 📚 Contribuição
1. Faça um fork do repositório.
2. Crie uma nova branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m 'Adicionando minha feature'
   ```
4. Faça push para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Crie um novo Pull Request.

## 👥 Autores
- DUARTE BARBOSA PIRES
- DAYANE ALMEIDA DAMACENO
- WESLEY OLIVEIRA DA SILVA
- GUILHERME LUIZ PINHEIRO COSTA

## ⚖️ Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

