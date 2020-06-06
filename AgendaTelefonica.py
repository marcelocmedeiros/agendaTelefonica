# criou a lista p receber agenda
agenda = []


def pede_nome():
    return (input("Nome: "))


def pede_telefone():
    return (input("Telefone: "))


def mostra_dados(nome, telefone):
    print("Nome: %s Telefone: %s" % (nome, telefone))


def pede_nome_arquivo():
    return (input("Nome do arquivo: "))


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def cadastrar():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])


def Remover():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        del agenda[p]
    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pede_nome())
    if p != None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("------\n")

def buscar():
    print("\nPesquisar\n------")
    if len(agenda) > 0:
        p = pesquisa(pede_nome())
        if p != None:
            nome = agenda[p][0]
            telefone = agenda[p][1]
            print("Encontrado:")
            mostra_dados(nome, telefone)
        else:
            print('Não existe este contato cadastrado!')
        print("------\n")
    else:
        print('Não existe nenhum contato na agenda!')


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return (valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))


def menu():
    print("""
   1 - Cadastrar
   2 - Editar
   3 - Remover
   4 - Lista
   5 - Pesquisa

   0 - Sai
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        cadastrar()
    elif opção == 2:
        altera()
    elif opção == 3:
        Remover()
    elif opção == 4:
        lista()
    elif opção == 5:
        buscar()