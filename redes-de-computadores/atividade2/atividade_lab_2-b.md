1. Compile e execute os arquivos TCPClient.java e TCPServer.java.

2. Modifique o programa cliente para enviar diversas mensagens digitadas pelo usuário.
  - O programa cliente deve ser interrompido se o usuário digitar a mensagem "tchau" (sem aspas).

3. Execute quatro clientes (a partir de máquinas diferentes). A seguir, envie uma mensagem do primeiro cliente, logo em seguida do segundo, etc.
  - O servidor recebe todas as mensagens?
    Sim. O Server recebe todas as mensagens.
  - O servidor atende todos os usuários simultaneamente?
    Não. O Server response a primeira conexão e, após encerrada a conexão, ele responde a próxima em um esquema FIFO.

4. Modifique o programa servidor para que possa atender a vários clientes simultaneamente.

5. Modifique os programas para que o servidor forneça o serviço de cálculo de IMC (Índice de Massa Corporal). O cliente deve enviar seu peso (em kg) e altura (em cm) e o servidor retorna o resultado. Obs: IMC = peso / (altura)^2

Submeta os códigos gerados (apenas os arquivos .java) nesta atividade.