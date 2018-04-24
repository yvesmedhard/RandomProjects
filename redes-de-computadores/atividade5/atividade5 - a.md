# Utilize o Wireshark para capturar os pacotes.

- Acesse a página http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html

- Observe os pacotes capturados e identifique:
  1. Qual é o endereço IP e número da porta TCP usados pelo computador do cliente?
     - 172.17.14.161:39874
  2. Qual é o endereço IP e o número da porta de envio e de recebimento de segmentos TCP para esta conexão?
     - 128.119.245.12:80
  3. Qual é o número de sequência do segmento TCP SYN que é usado para iniciar a conexão TCP entre o computador do cliente e o servidor da página?
     - sequence number: 0
  4. O que identifica o segmento como um segmento SYN?
     - Existe uma entrada dentro das flags da conexão chamada SYN, essa flag caracteriza o segmento.
    TCP Flags: ··········S·
  5. Qual é o número de sequência do segmento SYNACK enviado pelo servidor para o computador cliente em resposta ao SYN?
     - sequence number: 0
  6. Qual é o valor do campo ACK no segmento SYNACK?
     - ackenowledgment number: 1
  7. O que identifica o segmento como um segmento SYNACK?
     - As flags de identificação possuem os dois indicadores, caracterizando essa composição: TCP Flags: ·······A··S·
  8. Dada a diferença entre quando cada segmento TCP foi enviado, e quando sua confirmação foi recebida, qual é o valor RTT para cada um dos primeiros três segmentos?
     - The RTT to ACK the segment was: 0.150149126 seconds
     - The RTT to ACK the segment was: 0.000051119 seconds
     - The RTT to ACK the segment was: 0.149582190 seconds

- Repita os procedimentos para outra página web escolhida por você.

- Acesse a página http://ufabc.edu.br

- Observe os pacotes capturados e identifique:
  1. Qual é o endereço IP e número da porta TCP usados pelo computador do cliente?
     - 172.17.14.161:39880
  2. Qual é o endereço IP e o número da porta de envio e de recebimento de segmentos TCP para esta conexão?
     - 200.133.215.120:80
  3. Qual é o número de sequência do segmento TCP SYN que é usado para iniciar a conexão TCP entre o computador do cliente e o servidor da página?
     - sequence number: 0
  4. O que identifica o segmento como um segmento SYN?
     - Existe uma entrada dentro das flags da conexão chamada SYN, essa flag caracteriza o segmento.
    TCP Flags: ··········S·
  5. Qual é o número de sequência do segmento SYNACK enviado pelo servidor para o computador cliente em resposta ao SYN?
     - sequence number: 0
  6. Qual é o valor do campo ACK no segmento SYNACK?
     - ackenowledgment number: 1
  7. O que identifica o segmento como um segmento SYNACK?
     - As flags de identificação possuem os dois indicadores, caracterizando essa composição:
    TCP Flags: ·······A··S·
  8. Dada a diferença entre quando cada segmento TCP foi enviado, e quando sua confirmação foi recebida, qual é o valor RTT para cada um dos primeiros três segmentos?
     - The RTT to ACK the segment was: 0.000514504 seconds
     - The RTT to ACK the segment was: 0.000015617 seconds
     - The RTT to ACK the segment was: 0.001449890 seconds

- Apresente as respostas para o Professor.
