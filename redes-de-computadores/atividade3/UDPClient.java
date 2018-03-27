
// created on 29/09/2010 at 22:30import java.io.*;
import java.io.*;
import java.net.*;

class UDPClient {
  public static void main(String args[]) throws Exception {
    BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
    DatagramSocket clientSocket = new DatagramSocket();
    InetAddress IPAddress = InetAddress.getByName("127.0.0.1");
    byte[] sendData = new byte[1024];
    byte[] receiveData = new byte[1024];
    String sentence = null;
    do {
      sentence = inFromUser.readLine();
      sendData = sentence.getBytes();
      DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);
      clientSocket.send(sendPacket);
      DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
      clientSocket.receive(receivePacket);
      int port = receivePacket.getPort();
      String modifiedSentence = new String(receivePacket.getData());
      System.out.println("Do servidor:" + modifiedSentence + " Porta: " + port );
    } while(!sentence.equals("sair"));
    clientSocket.close();
  }
}
