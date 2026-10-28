# Crie uma agenda de telefones que salva os dados de maneira
# permanente.
# A agenda deve funcionar em loop infinito, até que o usuário
# decida sair. Os dados armazenados são: nome, sobrenome,
# telefone e e-mail.
# A agenda deve apresentar o seguinte menu para o usuário:
# ▶ 1- Novo contato (create)
# ▶ 2- Procura (pelo nome) (read)
# ▶ 3- Atualiza contato (update)
# ▶ 4- Apaga contato (delete)
# ▶ 0- Sair
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

    novo = {"nome":nome, "sobrenome":sobrenome, "telefone":telefone, "email":email}

    print("Contato criado com sucesso")
    contatos.append(novo)

def exibeContato(contato):
    print(f"Nome: {contato["nome"]}\nsobrenome: {contato["sobrenome"]}")
    print(f"telefone: {contato["telefone"]}, e-mail: {contato["email"]}")

def buscarContato():
        nome = input("Digite o nome a ser buscado: ")
        for i in range(len(contatos)):
            if contatos[i].get("nome") == nome:
                exibeContato(contatos[i])


def exibeMenu():
    print("1- Novo contato")
    print("2- Procura (pelo nome)")
    print("3- Atualiza contato")
    print("4- Apaga contato")
    print("0- Sair")

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
    if (not processaMenu(menu)):
        break
    salvarContatos()
