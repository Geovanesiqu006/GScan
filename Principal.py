
print("Bem Vindo ao GScan")

repositorio = input("Digite o endereço do seu Repositório: ")

if repositorio == "":
    print("Nenhum repositório foi informado")

else:
    # Verifica se o endereço informado começa com o GitHub
    if repositorio.startswith("https://github.com/"):
        print("Repositório válido")

        # Divide o endereço do repositório em partes
        partes = repositorio.rstrip("/").split("/")

        if len(partes) >= 5:
            usuario = partes[3]
            repositorio_nome = partes[4]

            print(f"Usuario: {usuario}")
            print(f"Repositório: {repositorio_nome}")

            # Abre o arquivo para leitura
            try:
                with open("teste1.py", "r", encoding="utf-8") as arquivo:

                    # Lê o conteúdo do arquivo
                    codigo = arquivo.read()

                print("Iniciando análise...")

                # Divide o código em linhas
                linhas = codigo.splitlines()

                risco_encontrado = False

                # Busca por possíveis informações sensíveis
                for numero, linha in enumerate(linhas, start=1):

                    if ("senha" in linha.lower() or
                        "password" in linha.lower() or
                        "api_key" in linha.lower() or
                        "token" in linha.lower() or
                        "secret" in linha.lower()):

                        risco_encontrado = True

                        print("\nRisco encontrado!")
                        print(f"Linha: {numero}")
                        print(f"Detecção: {linha}")

                        print("Descrição: Possível informação sensível encontrada no código.")
                       
                if risco_encontrado == False:
                    print("Nenhum risco encontrado!")

                print("\nAnálise finalizada!")
            # tratamento de erro, caso não aquivo não for encontrado.
            except FileNotFoundError:
                print("Arquivo teste1.py não encontrado.")

        else:
            print("Endereço de repositório incompleto.")

    else:
        print("Endereço inválido. Informe um link do GitHub.")


        