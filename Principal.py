
print("Bem Vindo ao GScan")

import urllib.request
import json

repositorio = input("Digite o endereço do seu Repositório: ")

if repositorio == "":
    print("Nenhum repositório foi informado")

else:
    if repositorio.startswith("https://github.com/"):

        print("Repositório válido")

        partes = repositorio.rstrip("/").split("/")

        if len(partes) >= 5:

            usuario = partes[3]
            repositorio_nome = partes[4].replace(".git", "")

            print(f"Usuario: {usuario}")
            print(f"Repositório: {repositorio_nome}")

            url_api = f"https://api.github.com/repos/{usuario}/{repositorio_nome}/contents/"

            requisicao = urllib.request.Request(
                url_api,
                headers={"User-Agent": "GScan"}
            )

            try:
                resposta = urllib.request.urlopen(requisicao)

                dados = json.loads(resposta.read())

                print("\nArquivos encontrados no repositório:")

                # Extensões de arquivos suportadas
                extensoes = (
                    ".py", ".js", ".jsx",  
                    ".java", ".php", ".c", ".html",
                    ".css", ".json", ".env", 
                )

                # Percorre os arquivos encontrados
                for arquivo in dados:

                    nome_arquivo = arquivo["name"]

                    # Verifica se o arquivo possui extensão suportada
                    if arquivo["type"] == "file" and nome_arquivo.lower().endswith(extensoes):

                        print(f"\nAnalisando: {nome_arquivo}")

            except urllib.error.HTTPError as erro:
                print(f"Erro HTTP ao acessar o GitHub: {erro.code}")

            except urllib.error.URLError:
                print("Não foi possível conectar ao GitHub.")

        else:
            print("Endereço de repositório incompleto.")

    else:
        print("Endereço inválido. Informe um link do GitHub.")
