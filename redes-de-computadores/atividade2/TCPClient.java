// package tcpsocket;

import java.io.*;
import java.net.*;

public class TCPClient {

	public static void main (String args[]) throws Exception {
		
		// Connect to the server process running at host
		Socket s = new Socket("127.0.0.1", 9000);
	
    // The next 2 lines create a output stream we can
		// write to.  (To write TO SERVER)
		OutputStream os= s.getOutputStream();
		DataOutputStream serverWriter = new DataOutputStream(os);
		
		// The next 2 lines create a buffer reader that
		// reads from the standard input. (to read stream FROM SERVER)
		InputStreamReader isrServer = new InputStreamReader(s.getInputStream());
		BufferedReader serverReader = new BufferedReader(isrServer);
             
    String user_input = "";
    do {
      //create buffer reader to read input from user. Read the user input to string 'sentence'
      BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
      user_input = inFromUser.readLine();
              
      // Send a user input to server
      System.out.println("Comunicando " + user_input + " pela porta: " + s.getPort());    
      serverWriter.writeBytes(user_input +"\n");

      // Server should convert to upper case and reply.
      // Read server's reply below and output to screen.
      String response = serverReader.readLine();
      System.out.println(response);
    } while(!user_input.equals("tchau"));
    s.close();
	}
}
