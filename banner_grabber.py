import socket

# Banner Grabbing Tool - Pedro Mantovani
# Identifica a versão de serviços em portas abertas

ip = input("Digite o IP do alvo: ")
porta = int(input("Digite a porta (ex: 21, 22, 80): "))

try:
    s = socket.socket()
    s.settimeout(2)
    s.connect((ip, porta))
    banner = s.recv(1024)
    print(f"\n[+] Resultado da porta {porta}:")
    print(banner.decode().strip())
except Exception as e:
    print(f"\n[-] Erro ao conectar: {e}")
finally:
    s.close()
