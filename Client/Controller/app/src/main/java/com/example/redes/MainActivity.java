package com.example.redes;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.os.Vibrator;
import android.view.View;
import android.widget.Button;

import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    private Vibrator vibrator;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ArrayList<Button> buttons = new ArrayList<>();

        for (int i = 1; i <= 6; i++) {
            @SuppressLint("DiscouragedApi") int buttonId = getResources().getIdentifier("button" + i, "id", getPackageName());
            Button botao = findViewById(buttonId);
            buttons.add(botao);
        }

        vibrator = (Vibrator) getSystemService(VIBRATOR_SERVICE);

        View.OnLongClickListener LongClick = new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View v) {
                Button bt = (Button) v;

                vibrator.vibrate(1);

                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            Socket socket = new Socket("IPV4 PC ADDRESS", "PORT");

                            ClientThread clientThread = new ClientThread(socket);
                            clientThread.start();
                            PrintStream out = new PrintStream(socket.getOutputStream());
                            out.println(bt.getText().toString());

                            socket.close();
                            out.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                }).start();

                return true;
            }
        };

        for (Button btn : buttons) {
            btn.setOnLongClickListener(LongClick);
        }
    }
}