package com.example.redes;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.Socket;

public class ClientThread extends Thread{
    private Socket socket;

    public ClientThread(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try {
            InputStreamReader inputReader = new InputStreamReader(socket.getInputStream());
            BufferedReader in = new BufferedReader(inputReader);
            String x;

            while ((x = in.readLine()) != null) {
                System.out.println("Cliente: " + x);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
