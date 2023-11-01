import ctypes, subprocess, socket, webbrowser, qrcode
from testes import *

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = socket.gethostbyname(socket.gethostname())

# qr_code = qrcode.QRCode(
#     version=2,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=2,
# )
# qr_code.add_data(ip_address)

# img = qr_code.make_image(fill_color="black", back_color="white")
# img.save("ipv4_qr.png")
# img.show()

server_socket.bind((ip_address, 4000))
server_socket.listen(5)

print(f"{socket.gethostname()} is listening for connections...")

while True:
    client_socket, client_address = server_socket.accept()

    if client_address[0] == "xxx.xxx.xxx.x":
        print(f"Accepted connection from {client_address[0]}")

        data = client_socket.recv(1024)
        print(f"Received from client: {data.decode()}")
        command = str(data.decode()).strip()

        if command == "Bloquear":
            ctypes.windll.user32.LockWorkStation()

        elif command == "Desligar":
            subprocess.call(["shutdown", "/s", "/t", "0"])
            
        elif command == "Spotify":
            subprocess.run('spotify', shell=True)

        elif command == "VS Code":
            subprocess.run('code', shell=True)

        elif command == "YouTube":
            webbrowser.open("https://www.youtube.com")

        elif command == "Próximo" or command == "Anterior" or command == "Enter" or command == "Play/Pause":
            atalho(command)

        elif "+" in command:
            keys = command.split(' + ')
            print(keys)
            atalho(keys[0], keys[1])

    # message = f"{data.decode()}: {'Concluido' if stts else 'Erro'}"
    # client_socket.close()
    
