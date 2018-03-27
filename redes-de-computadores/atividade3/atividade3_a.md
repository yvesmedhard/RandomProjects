## Instruções
1. Compile os arquivos UDPClient.java e UDPServer.java.

2. Execute o servidor e o cliente na mesma máquina.
  - Explique o que acontece ao executar o servidor e depois o cliente.
  Ao digitar uma mensagem no cliente o servidor responde. O cliente exibe a mensagem e termina a execução.
  - O que acontece se você executar o cliente antes do servidor?
  O client não envia propriamente as mensagens para o servidor e fica travado recebendo entradas sem terminar a execução. O servidor permanece aguardando conexão.
  - Altere as portas do servidor e cliente. O que acontece se as portas forem diferentes?
  Semelhantemente ao caso anterior o Client permanesce enviando mensagens mas não tem resposta do servidor. O servidor permanece aguardando conexão.

3. Envie várias mensagens ao servidor a partir de várias máquinas virtuais diferentes (tente enviá-las ao mesmo tempo).
  - O servidor recebe todas as mensagens?
  Sim, o servidor recebeu e devolveu todas as mensagens corretamente.
  - Modifique os programas para que o cliente e o servidor mostrem as portas que estão sendo utilizadas na comunicação e imprima na tela essas portas.

4. Modifique o programa cliente para enviar diversas mensagens digitadas pelo usuário. O programa só deve ser interrompido se o usuário digitar a mensagem “sair” (sem aspas). É necessário alterar também o código do servidor? Faça as modificações necessárias.
  Não é necessário modificar o servidor pois ele já fica aguardando uma nova conexão.

5. Mostre os resultados acima para o Professor.
