# Comunicação Segura com Criptografia RSA em Python

Este projeto implementa uma comunicação segura entre cliente e servidor utilizando criptografia RSA. O cliente (Alice) envia uma mensagem criptografada ao servidor (Bob), que a descriptografa, converte para maiúsculas e retorna a mensagem criptografada de volta ao cliente.

## Tecnologias Utilizadas

- Python 3.x
- Criptografia RSA
- Sockets TCP

## Funcionamento

### Cliente

1. O cliente gera um par de chaves (pública e privada) utilizando o algoritmo RSA.
2. O cliente se conecta ao servidor e envia sua chave pública.
3. O cliente recebe a chave pública do servidor.
4. O cliente envia uma mensagem criptografada com a chave pública do servidor.
5. O cliente recebe a resposta do servidor (mensagem em maiúsculas criptografada) e a descriptografa utilizando sua chave privada.

### Servidor

1. O servidor gera um par de chaves (pública e privada) utilizando o algoritmo RSA.
2. O servidor aguarda a conexão do cliente.
3. O servidor recebe a chave pública do cliente e envia sua própria chave pública de volta.
4. O servidor recebe a mensagem criptografada do cliente, a descriptografa utilizando sua chave privada e converte a mensagem para maiúsculas.
5. O servidor criptografa a resposta com a chave pública do cliente e envia de volta.

## Descrição do Algoritmo RSA

Este projeto baseia-se no **algoritmo RSA** de criptografia assimétrica, que foi desenvolvido por Ronald Rivest, Adi Shamir e Leonard Adleman no MIT. O RSA é um dos sistemas de criptografia mais seguros, baseado em teorias matemáticas dos números. Ele permite tanto criptografia quanto assinatura digital.

A criptografia RSA funciona com duas chaves: uma **chave pública** para criptografar dados e uma **chave privada** para descriptografar. A segurança do RSA depende da dificuldade de fatorar grandes números primos.

O algoritmo segue os seguintes passos para gerar as chaves:

### Etapas para Geração de Chaves

1. **Escolher dois números primos p e q** e calcular \( N = p \times q \).
2. Calcular a função totiente \( \phi(N) = (p - 1) \times (q - 1) \).
3. Escolher um número \( e \) tal que \( 1 < e < \phi(N) \) e que \( e \) seja coprimo de \( \phi(N) \).
4. Calcular \( d \) tal que \( e \times d \mod \phi(N) = 1 \).

As chaves geradas são:

- **Chave pública**: \( (e, N) \)
- **Chave privada**: \( (d, N) \)

A **criptografia** de uma mensagem \( P \) é feita com a chave pública:  
\( C = P^e \mod N \)

A **descriptografia** é feita com a chave privada:  
\( P = C^d \mod N \)

### Exemplo de Geração das Chaves

Para os números primos \( p = 3 \) e \( q = 5 \):

1. \( N = p \times q = 3 \times 5 = 15 \)
2. \( \phi(N) = (p - 1) \times (q - 1) = 2 \times 4 = 8 \)
3. Escolher \( e = 7 \) (pois \( \text{GCD}(7, 8) = 1 \))
4. Calcular \( d = 7^{-1} \mod 8 = 7 \)

Portanto, a chave pública é \( (7, 15) \) e a chave privada é \( (7, 15) \).

### Exemplo de Criptografia e Descriptografia

Mensagem: "C" (equivalente ao número 3 no alfabeto)

- **Criptografia** com chave pública \( (7, 15) \):  
  \( C = 3^7 \mod 15 = 12 \) (correspondendo à letra "L")

- **Descriptografia** com chave privada \( (7, 15) \):  
  \( P = 12^7 \mod 15 = 3 \) (correspondendo à letra "C")

## Atividade Realizada

A atividade proposta consistiu em implementar o algoritmo RSA para a geração de chaves pública e privada, bem como para criptografar e descriptografar uma mensagem. O sistema foi configurado para gerar números primos aleatórios \( p \) e \( q \), calcular o módulo \( N \), a função totiente \( \phi(N) \), e as chaves \( e \) e \( d \), garantindo a segurança das informações trocadas entre cliente e servidor.

A frase criptografada e decriptografada durante os testes foi:  
**"The information security is of significant importance to ensure the privacy of communications."**

Essa atividade foi crucial para entender o funcionamento do RSA e sua implementação prática, além de demonstrar como a criptografia de chave pública pode ser utilizada para garantir a segurança de mensagens em uma comunicação entre sistemas distribuídos.

## Requisitos

- Python 3.x instalado.
- Biblioteca `socket` (já inclusa no Python padrão).
- Biblioteca `random` (já inclusa no Python padrão).

# Como Rodar

1. Clone este repositório.
   
   ```
   git clone https://github.com/usuario/arquivo.git
   cd arquivo
## Execute o servidor:


python servidor.py
## Execute o cliente:


python cliente.py
O cliente enviará uma mensagem para o servidor, que retornará a mensagem criptografada com a versão em maiúsculas.

## Funcionalidades
Geração de Chaves: Utiliza o algoritmo RSA para gerar um par de chaves pública e privada.
Criptografia e Descriptografia: Mensagens são criptografadas utilizando a chave pública do destinatário e descriptografadas com a chave privada correspondente.
Comunicação Cliente-Servidor: O cliente se conecta ao servidor via sockets TCP para enviar e receber mensagens criptografadas.
## Contribuição
Se você deseja contribuir para este projeto, siga estas etapas:

Faça um fork deste repositório.

Crie uma branch para sua feature:

git checkout -b minha-feature
Faça commit das suas alterações:


git commit -am 'Adicionando minha feature'
Faça push para a branch:


git push origin minha-feature
Crie um novo Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
