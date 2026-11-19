
# Apresenta o GScan ao usuário
print("Bem Vindo ao GScan")


# Importa as bibliotecas necessárias para acessar a API do GitHub e interpretar os dados recebidos
import urllib.request
import json


# Solicita o endereço do repositório que será analisado
repositorio = input("Digite o endereço do seu Repositório: ")


# Verifica se o endereço informado está vazio
if repositorio == "":
    print("Nenhum repositório foi informado")


# Valida se o endereço informado pertence ao GitHub
else:
    if repositorio.startswith("https://github.com/"):

        print("Repositório válido")

        # Separa o endereço para identificar o usuário e o nome do repositório
        partes = repositorio.rstrip("/").split("/")

        # Verifica se o endereço possui as informações necessárias
        if len(partes) >= 5:

            usuario = partes[3]
            repositorio_nome = partes[4].replace(".git", "")

            # Exibe os dados identificados do repositório
            print(f"Usuario: {usuario}")
            print(f"Repositório: {repositorio_nome}")

            # Monta o endereço da API do GitHub para consultar os arquivos do repositório
            url_api = f"https://api.github.com/repos/{usuario}/{repositorio_nome}/contents/"

            # Prepara a requisição para acessar a API do GitHub
            requisicao = urllib.request.Request(
                url_api,
                headers={"User-Agent": "GScan"}
            )

            # Tenta acessar o repositório e receber a lista de arquivos
            try:
                resposta = urllib.request.urlopen(requisicao)

                dados = json.loads(resposta.read())

                print("\nArquivos encontrados no repositório:")

                # Exibe a quantidade de itens encontrados na raiz do repositório
                print(f"\nQuantidade de itens encontrados: {len(dados)}")

                # Exibe os nomes e tipos dos itens retornados pela API
                for item in dados:
                    print(f"Nome: {item['name']} | Tipo: {item['type']}")

                # Define as extensões de arquivos que o GScan está preparado para analisar
                extensoes = (
                    ".py", ".js", ".jsx",
                    ".java", ".php", ".c", ".html",
                    ".css", ".json", ".env",
                )

                # Percorre os arquivos encontrados e verifica quais possuem extensões suportadas
                for arquivo in dados:

                    nome_arquivo = arquivo["name"]

                    if arquivo["type"] == "file" and nome_arquivo.lower().endswith(extensoes):

                        print(f"\nAnalisando: {nome_arquivo}")

                        # Obtém o endereço para baixar o conteúdo do arquivo
                        url_arquivo = arquivo["download_url"]

                        # Prepara a requisição para acessar o conteúdo do arquivo
                        requisicao_arquivo = urllib.request.Request(
                            url_arquivo,
                            headers={"User-Agent": "GScan"}
                        )

                        # Acessa o arquivo e realiza a leitura do seu conteúdo
                        resposta_arquivo = urllib.request.urlopen(requisicao_arquivo)

                        conteudo = resposta_arquivo.read().decode("utf-8")

                        # Exibe o conteúdo encontrado no arquivo
                        print(conteudo)

            # Trata erros relacionados à resposta da API do GitHub
            except urllib.error.HTTPError as erro:
                print(f"Erro HTTP ao acessar o GitHub: {erro.code}")

            # Trata erros de conexão com o GitHub
            except urllib.error.URLError:
                print("Não foi possível conectar ao GitHub.")

        else:
            print("Endereço de repositório incompleto.")

    else:
        print("Endereço inválido. Informe um link do GitHub.")
