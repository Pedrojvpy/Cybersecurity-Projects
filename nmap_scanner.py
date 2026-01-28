import os

# Script de Reconhecimento Automatizado - Pedro Mantovani
print("-" * 40)
print("   AUTOMATED RECON TOOL - v1.0")
print("-" * 40)

target = input("Digite o alvo (IP ou Dominio): ")

print(f"\n[+] Iniciando Scan de Versões em {target}...")
# O comando abaixo roda o nmap e salva a saida num arquivo
os.system(f"nmap -sV -Pn {target} > scan_report.txt")

print("\n[!] Scan finalizado. Resultado salvo em: scan_report.txt")
print("-" * 40)
