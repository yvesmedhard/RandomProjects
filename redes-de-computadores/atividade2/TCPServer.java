// package tcpsocket;
import java.io.*;
import java.net.*;

class TCPServer {

  public Server(Socket cliente){
    this.cliente = cliente;
  }

  public Thread(Server tratamento){
    
  }

  public static void main (String args[]) throws Exception {
    ServerSocket serverSocket = new ServerSocket(9000);
    while (true) {
      Socket cliente = servidor.accept();
      Thread t = new Thread(cliente){
        public void run() {
        
        }
      }
      


      t.start();
    }

    // waits for a new connection. Accepts connetion from multiple clients
    while (close_conection) {
      System.out.println("Esperando conexões na porta 9000");
      
      
          Socket s = serverSocket.accept();
          System.out.println("Conexão estabelecida de " + s.getInetAddress());
          
          String user_input = "";
          do {
            // create a BufferedReader object to read strings from
            // the socket. (read strings FROM CLIENT)
            BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
            user_input = br.readLine();
            
            //create output stream to write to/send TO CLINET
            DataOutputStream output = new DataOutputStream(s.getOutputStream());
            String dataOutput = user_input.toUpperCase();
            output.writeBytes( dataOutput + "\n");
            System.out.println("Comunicando " + dataOutput + " pela porta: " + s.getPort());
          } while(!user_input.equals("tchau"));
          // close current connection
          s.close();
        }
      }.start())
    if(threads.count == 0)  {
      close_conection = false;
    }
  }
}


public Socket cliente;
    

    public static void main(String[] args)  throws IOException{     
        //Cria um socket na porta 12345
        System.out.println("Porta 12345 aberta!");
        // Aguarda alguém se conectar. A execução do servidor
        // fica bloqueada na chamada do método accept da classe
        // ServerSocket. Quando alguém se conectar ao servidor, o
        // método desbloqueia e retorna com um objeto da classe
        // Socket, que é uma porta da comunicação.
        System.out.println("Aguardando conexão do cliente...");   

        
    }