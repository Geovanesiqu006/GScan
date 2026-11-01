print("Bem Vindo ao GScan")

repositorio = input("Digite o endereço do seu Repositório: ")

print(repositorio)
print(repositorio.startswith("https://github.com/"))

if repositorio == "":
    print("Nenhum repositório foi informado")
else:
# Verifica se o endereço informado começa com o GitHub
    if repositorio.startswith("https://github.com/"):
        print("Repositório válido")

# Divide o endereço do repositório em partes
        partes = repositorio.split("/")

        usuario = partes [3]
        repositorio_nome = partes[4]

        print(f"Usuario: {usuario}")
        print(f"Repositório: {repositorio_nome}")

         # Abre o arquivo para leitura
        arquivo = open ("teste1.py", "r" )

        # Lê o conteúdo do arquivo
        codigo = arquivo.read()

        # Fecha comando         
        arquivo.close()

        print(codigo)
        print("Iniciando análise...")

        if "senha" in codigo or "password" in codigo or "api_key" in codigo or "token" in codigo or "secret" in codigo:
            print("Risco encontrado!")
            print("Risco: Alto")
            print("Descrição: Possível informação sensível encontrada no código.")
            print("Recomendação: Evite armazenar senhas e tokens diretamente nos arquivos.")

        else:
            print("Nenhum risco encontrado!")
        
        

        