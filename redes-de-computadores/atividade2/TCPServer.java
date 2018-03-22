import java.io.*;
import java.net.*;

public class TCPServer {
  public static void main(String args[]) throws Exception {
    TCPServer server = new TCPServer();
    server.start_server();
  }

  public int conexoes = 0;

  public void start_server() throws Exception {
    ServerSocket servidor = new ServerSocket(9000);

    System.out.println("Esperando conexões na porta 9000");
    System.out.println("InetAddress:" + servidor.getInetAddress());

    do {
      Socket cliente = servidor.accept();
      Thread comunication = new ThreadSocket(cliente, this);
      comunication.start();
      conexoes += 1;
    } while (conexoes > 0);
  }

  class ThreadSocket extends Thread {
    Socket client;
    TCPServer server;

    ThreadSocket(Socket cliente, TCPServer server) {
      this.client = cliente;
      this.server = server;
    }

    public void run() {
      try{
        System.out.println("Conexão estabelecida de " + client.getInetAddress());
        String user_input = "";
        do {
          BufferedReader br = new BufferedReader(new InputStreamReader(client.getInputStream()));
          user_input = br.readLine();

          DataOutputStream output = new DataOutputStream(client.getOutputStream());
          String dataOutput = user_input.toUpperCase();

          output.writeBytes( dataOutput + "\n");
          System.out.println("Comunicando " + dataOutput + " pela porta: " + client.getPort());
        } while(!user_input.equals("tchau"));
        client.close();
        this.server.conexoes -= 1;
      } catch(Exception e){
        System.out.println(e);
      }
    }
  }
}
