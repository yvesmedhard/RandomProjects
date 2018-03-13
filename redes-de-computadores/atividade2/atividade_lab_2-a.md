1. Compile e execute os arquivos `TCPClient.java` e `TCPServer.java`.
  - Use o NetBeans ou linha de comando (Linux):
  - Compile: `javac TCPServer.java`
  - Execute: `java TCPServer`
  - Faça o mesmo para TCPClient.

2. Execute o servidor e o cliente na mesma máquina. 
  - Explique o que acontece no cliente e no servidor ao executá-los.
  - O que acontece se você executar o cliente antes do servidor? 
    - Ao executar o Client sem o servidor estar em execução recebemos uma mensagem de erro indicando que a conexão foi recusada.
    - Ao executar o Server sem recebemos a mensagem indicando que o server espera conexão e a porta que ele está 'escutando'.
    - Ao executar o Client com o Server em execução não recebemos mensagem do Client, mas recebemos uma mensagem dizendo que uma conexão foi estabelecida e o endereço ip da conexão.
    - Ao enviar uma entrada pelo Client, recebemos de volta a mensagem em caixa alta e a conexão é encerrada. O Server exibe uma mensagem indicando que espera conexão e a porta.
    
  - Altere as portas do servidor e cliente. O que acontece se as portas forem diferentes?
    - Ao alterar a porta do Client para a porta 3000 o server continua com o comportamento igual e o Client exibe a mensagem de erro de conexão recusada.

3. Modifique os programas para que o cliente e o servidor mostrem as portas que estão sendo utilizadas na comunicação e imprima na tela essas portas. (ver método getPort() do socket)
  - A porta criada pelo servidor para atender o cliente após a conexão é a mesma porta utilizada na escuta (9000)?
    - Não, o Server comunica ao Client a resposta em uma porta diferente da aberta para a escuta.
  - A porta criada pelo cliente para trocar mensagens com o servidor é a mesma porta utilizada para realizar a conexão (9000)?
    - Sim, o Client envia as mensagens exclusivamente pela porta em que a conexão foi estabelecida.
  - Execute novamente o cliente e o servidor. O número da portas utilizada após estabelecer a conexão entre o cliente e o servidor sempre são as mesmas
    - A porta para escuta do Server e envio do Client é sempre a mesma, porém a porta que o Client recebe a resposta do Server é diferente todas as vezes. 
  - Explique todas as portas (e números) criadas no servidor e no cliente.
    - Pensando na arquitetura de Cliente-Servidor, o Servidor deve sempre ser conhecido e ter disponibilidade para receber conexões, enquanto o Client pode se conectar a qualquer momento e de qualquer endereço disponível. O Sever aguarda conexão em uma porta padrão. O Client por sua vez, cria um socket com o endereço ip e porta da aplicação servidor e nesse processo uma porta 'limpa' é associada como porta de resposta. Com isso feito assim que o Client enviar uma mensagem pela conexão o Server poderá responder para a porta em que o client está esperando a resposta. 

Mostre para o Professor.