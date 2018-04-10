1. DNS
  Para os exercícios utilize o Wireshark para capturar os pacotes. A resposta deverá conter sua análise e um screenshot do wireshark (que permita observar a resposta).

  Limpe o cache do seu navegador.
  Acesse o site https://www.w3.org/
  Observe os pacotes capturados e identifique:
    1) As mensagens DNS são enviadas sobre TCP ou UDP?
    2) Identifique a porta de destino da mensagem query DNS e a porta de origem da mensagem de resposta do DNS.
    3) Examine a resposta DNS. Quantas “respostas” foram dadas? Qual o conteúdo destas respostas?
    4) Esta página contém imagens. Antes de requisitar cada imagem, seu host faz novas queries DNS?

2. Usando nslookup

  nslookup é uma ferramenta que permite obter informações sobre os registros do DNS. A sintaxe do comando nslookup é:

    nslookup –option1 –option2 host-to-find dns-server

  Em geral, nslookup pode ser executado com zero, uma, duas ou mais opções. O servidor DNS também é opcional; se não for indicado, a query é enviada ao servidor DNS local.

  Execute o comando

    nslookup www.ucla.edu

  Observe os pacotes capturados e identifique:
    1) Qual é a porta de destino da mensagem query DNS e a porta de origem da mensagem de resposta do DNS?
    2) Examine a resposta DNS. Quantas “respostas” foram dadas?
    3) Qual o conteúdo destas respostas?

Repita o procedimento para buscar os registros DNS de outro site da web.