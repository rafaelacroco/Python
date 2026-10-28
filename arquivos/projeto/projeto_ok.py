contatos = []

def carregarContatos():
    return
def salvarContatos():
    return

def novoContato():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite e-mail: ")

    novo = {"nome":nome, "sobrenome":sobrenome,
            "telefone":telefone, "email":email}

    print("Contato criado com sucesso!")
    contatos.append(novo)

def exibeContato(contato):
    print(f"Nome: {contato["nome"]}\nSobrenome: {contato["sobrenome"]}")
    print(f"Telefone: {contato["telefone"]}\nEmail: {contato["email"]}")

def buscarContato():
    nome = input("Digite o nome a ser buscado: ")
    for i in range(len(contatos)):
        if contatos[i].get("nome") == nome:
            exibeContato(contatos[i])

def exibeMenu():
    print("1 - Novo contato")
    print("2 - Buscar contato (nome)")
    print("3 - Atualizar contato")
    print("4 - Apagar contato")
    print("0 - Sair")

def processaMenu(menu):
    if menu == 1:
        novoContato()
        print(contatos)
        return True
    elif menu == 2:
        buscarContato()
        return True
    elif menu == 3:
        atualizarContato()
        return True
    elif menu == 4:
        apagarContato()
        return True
    elif menu == 0:
        return False
    return False

while True:
    carregarContatos()
    exibeMenu()
    menu = int(input())
    if(not processaMenu(menu)):
       break
    salvarContatos()