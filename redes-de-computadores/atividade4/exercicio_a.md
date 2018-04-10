# Atividade 4 - A

O Wireshark é um analisador de protocolos (sniffer) distribuído gratuitamente a partir do endereço http://www.wireshark.com. Ele pode ser executado em diversas plataformas, incluindo sistemas Unix e Windows.

## Capturando pacotes

  - Abra o Wireshark e ative a captura de pacotes (Menu Capture->Interfaces).
  - Na opção "interface", escolha a interface Ethernet.
  - Identifique a interface Ethernet; em opções (Options) seleciona a opção "enable network name resolution".
  - Inicie a captura (pressionando em Start).
  - Acesse a rede por alguns segundos (exemplo: acesse o site www.uol.com.br). Não é necessário muito tempo (basta acessar uma única página).
  - Pare a captura de pacotes pressionando no botão Stop da janela de captura.
  - A interface do Wireshark é dividida em três partes:
    1) A primeira contém uma relação dos pacotes capturados, um por linha. Selecione um dos pacotes.
    2) A segunda contém informações sobre o pacote que está selecionado, onde cada linha contém um protocolo, na ordem em que eles são empilhados. Dentro de cada protocolo, são mostrados os campos do seu cabeçalho.
    3) A terceira parte contém os dados, ou seja, a carga útil (payload) do pacote, que será utilizada pela aplicação. A carga útil é apresentada no formato hexadecimal e o seu correspondente para ASCII.
  - Selecione os vários pacotes e observe os seus campos e valores.

## HTTP

Para os exercícios abaixo, utilize o Wireshark para capturar os pacotes.

### Interação básica HTTP

  - Acesse a página http://news.mit.edu/2017/tim-berners-lee-wins-turing-award-0404
  - Aplique o filtro HTTP para ver apenas os pacotes do protocolo HTTP.
  - Observe os pacotes capturados e identifique:
    1) Versão do HTTP do navegador e do servidor web acessado;
        - V1.1 - Navegador
        - V1.1 - Servidor
    2) Línguas que o navegador aceita;
        - Accept-Language: en-US,en;q=0.5
    3) IP do seu computador e do servidor;
        - Src: 172.17.14.161
        - Dst: 23.38.154.77
    4) Código de status retornado do servidor para o navegador;
      Status 200 - OK
    5) HTTP persistente ou não persistente;
        - Connection: keep-alive - Persistente
    6) Última modificação do arquivo HTML do servidor;
        - Last-Modified: Wed, 28 Mar 2018 19:36:06 GMT
    7) Número de bytes de conteúdo retornado ao navegador;
        - File Data: 109434 bytes

  - Repita os procedimentos para outra página web escolhida por você.

  - Acesse a página http://ufabc.edu.br
  - Aplique o filtro HTTP para ver apenas os pacotes do protocolo HTTP.
  - Observe os pacotes capturados e identifique:
    1) Versão do HTTP do navegador e do servidor web acessado;
        - V1.1 - Navegador
        - V1.1 - Servidor
    2) Línguas que o navegador aceita;
        - Accept-Language: en-US,en;q=0.5
    3) IP do seu computador e do servidor;
        - Src: 172.17.14.161
        - Dst: 200.133.215.120
    4) Código de status retornado do servidor para o navegador;
        - Status 200 - OK
    5) HTTP persistente ou não persistente;
        - Keep-Alive: timeout=5, max=91 - Persistente
    6) Última modificação do arquivo HTML do servidor;
        - Last-Modified: Mon, 15 Jan 2018 20:34:26
    7) Número de bytes de conteúdo retornado ao navegador;
       - File Data: 92091 bytes


### GET Condicional

  - Limpe o cache do seu navegador.
  - Acesse o site: http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
  - Observe os pacotes capturados e identifique:
    1) Na primeira requisição GET. É possível ver “IF-MODIFIEDSINCE” no HTTP GET?
        - Não
    2) Verifique a resposta do servidor. O servidor retorna o conteúdo do arquivo?
        - Sim o servidor retorna a página HTML requisitada.
    3) Na segunda requisição GET. É possível ver “IF-MODIFIED-SINCE” no HTTP GET? Explique;
       - Sim If-Modified-Since: Mon, 09 Apr 2018 05:59:01 GMT
    4) Verifique a resposta do servidor ao segundo GET. O servidor retorna o conteúdo do arquivo? Explique.
       - Não retorna. Para economizar processamento e transporte (banda), caso o arquivo salvo em uma requisição anterior não tenha sido alterado desde sua requisição, o cliente não precisa receber todo o mesmo arquivo novamente. Caso seja este o caso o servidor retorna um STATUS 304 - Not Modified e o navegador exibe a página salva. Caso contrário o servidor retorna STATUS 200 - OK e a página normalmente.
