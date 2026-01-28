import socket

# Banner Grabbing Tool - Pedro Mantovani
# Identifica a versão de serviços em portas abertas

def get_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return f"Erro: {e}"
    finally:
        s.close()

target_ip = input("Digite o IP do alvo: ")
target_port = int(input("Digite a porta (ex: 21, 22, 3306): "))

print(f"\n[+] Tentando capturar banner em {target_ip}:{target_port}...")
print(f"[Result]: {get_banner(target_ip, target_port)}")
