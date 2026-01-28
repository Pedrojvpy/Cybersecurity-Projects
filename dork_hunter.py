# Google Dork Generator - Pedro Mantovani
# Ferramenta para gerar buscas de arquivos sensíveis

alvo = input("Digite o domínio alvo (ex: alvo.com.br): ")

dorks = [
    f"site:{alvo} filetype:sql",
    f"site:{alvo} filetype:pdf 'confidencial'",
    f"site:{alvo} intitle:'index of' 'parent directory'",
    f"site:{alvo} filetype:env",
    f"site:{alvo} inurl:phpinfo.php"
]

print(f"\n[!] Gerando Dorks para: {alvo}\n")
for dork in dorks:
    query = dork.replace(" ", "+")
    print(f"Pesquisar: https://www.google.com/search?q={query}")
