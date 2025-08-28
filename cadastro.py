usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o e-mail: ")
    usuarios.append({"nome": nome, "idade": idade, "email": email})
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, u in enumerate(usuarios, 1):
            print(f"{i}. {u['nome']} - {u['idade']} anos - {u['email']}")

while True:
    print("\n1. Cadastrar usuário\n2. Listar usuários\n3. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        cadastrar_usuario()
    elif escolha == "2":
        listar_usuarios()
    elif escolha == "3":
        break
    else:
        print("Opção inválida!")
