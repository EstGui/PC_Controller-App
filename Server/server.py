import ctypes, subprocess, socket

sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sSocket.bind(('IPV4 PC ADDRESS', 'PORT'))

sSocket.listen(1)

print("Server is listening for connections...")

while True:
    cSocket, cAddress = sSocket.accept()

    if cAddress[0] == "PHONE ADDRESS":
        print(f"Accepted connection from {cAddress}")

        data = cSocket.recv(256)
        print(f"Received from client: {data.decode()}")

        if data.decode() == "Bloquear":
            ctypes.windll.user32.LockWorkStation()  

        elif data.decode() == "Desligar":
            EWX_SHUTDOWN = 0x00000001
            EWX_FORCE = 0x00000004
            ctypes.windll.user32.ExitWindowsEx(EWX_SHUTDOWN | EWX_FORCE, 0)

        elif data.decode() == "Spotify":
            subprocess.run('spotify.exe', shell=True)

        elif data.decode() == "Play/Pause":
            ctypes.windll.user32.keybd_event(0xB3, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0xB3, 0, 2, 0)

        elif data.decode() == "Anterior":
            ctypes.windll.user32.keybd_event(0xB1, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0xB1, 0, 2, 0)

        elif data.decode() == "Próximo":
            ctypes.windll.user32.keybd_event(0xB0, 0, 0, 0)
            ctypes.windll.user32.keybd_event(0xB0, 0, 2, 0)

        cSocket.close()
