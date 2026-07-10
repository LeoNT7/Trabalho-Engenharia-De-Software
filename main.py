# SISTEMA SIMPLES DE CONTROLE DE ESTOQUE
# Atividade Prática - Engenharia de Software

# Dicionário de produtos já cadastrados no sistema
produtos = {
    1: {"nome": "Martelo de borracha", "quantidade": 10},
    2: {"nome": "Luvas de proteção", "quantidade": 5},
    3: {"nome": "Chave de fenda", "quantidade": 8},
    4: {"nome": "Cabo elétrico 2,5 mm", "quantidade": 12}
}

# Lista para armazenar o histórico de entradas e saídas
movimentacoes = []

# Função para exibir uma linha de separação
def linha():
    print("-" * 60)

# Função para ler números inteiros sem quebrar o programa
def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Digite apenas números inteiros!")

# Função para listar os produtos cadastrados
def listar_produtos():
    linha()
    print("PRODUTOS DISPONÍVEIS")
    linha()
    print(f"{'CÓDIGO':<10}{'PRODUTO':<30}{'QUANTIDADE':<10}")
    
    for codigo, dados in produtos.items():
        print(f"{codigo:<10}{dados['nome']:<30}{dados['quantidade']:<10}")
    
    print("0 - Voltar")
    linha()

# Função para voltar ao menu principal
def voltar():
    linha()
    print("Voltando ao menu principal...")
    linha()

# Função para registrar a entrada de produtos no estoque
def registrar_entrada():
    while True:
        print("\nREGISTRAR ENTRADA DE PRODUTO")
        listar_produtos()

        codigo = ler_inteiro("Digite o código do produto a ser adicionado: ")

        if codigo == 0:
            voltar()
            break

        if codigo not in produtos:
            print("Código inválido! Escolha um produto cadastrado.")
            continue

        produto = produtos[codigo]
        print(f"Produto selecionado: {produto['nome']}")

        quantidade = ler_inteiro("Digite a quantidade recebida: ")

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        data = input("Digite a data da entrada (XX/XX/XXXX) : ")
        responsavel = input("Digite o nome do responsável: ")

        if data == "" or responsavel == "":
            print("A data e o responsável devem ser informados.")
            continue

        # Atualiza automaticamente o estoque
        produto["quantidade"] += quantidade

        # Registra a movimentação no histórico
        movimentacoes.append({
            "tipo": "Entrada",
            "produto": produto["nome"],
            "quantidade": quantidade,
            "data": data,
            "responsavel": responsavel,
            "estoque_atual": produto["quantidade"]
        })

        print("Entrada registrada com sucesso!")
        print(f"Quantidade atualizada de {produto['nome']}: {produto['quantidade']}")
        break


# Função para registrar a saída de produtos do estoque
def registrar_saida():
    while True:
        print("\nREGISTRAR SAÍDA DE PRODUTO")
        listar_produtos()

        codigo = ler_inteiro("Digite o código do produto a ser retirado: ")

        if codigo == 0:
            voltar()
            break

        if codigo not in produtos:
            print("Código inválido! Escolha um produto cadastrado.")
            continue

        produto = produtos[codigo]
        print(f"Produto selecionado: {produto['nome']}")

        quantidade = ler_inteiro("Digite a quantidade a retirar: ")

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        # Validação para não permitir saída maior que o estoque disponível
        if quantidade > produto["quantidade"]:
            print("Quantidade insuficiente em estoque!")
            print(f"Estoque disponível do produto {produto['nome']}: {produto['quantidade']}")
            continue

        data = input("Digite a data da saída (XX/XX/XXXX): ")
        responsavel = input("Digite o nome do responsável: ")

        if data == "" or responsavel == "":
            print("A data e o responsável devem ser informados.")
            continue

        # Atualiza automaticamente o estoque
        produto["quantidade"] -= quantidade

        # Registra a movimentação no histórico
        movimentacoes.append({
            "tipo": "Saída",
            "produto": produto["nome"],
            "quantidade": quantidade,
            "data": data,
            "responsavel": responsavel,
            "estoque_atual": produto["quantidade"]
        })

        print("Saída registrada com sucesso!")
        print(f"Quantidade atualizada de {produto['nome']}: {produto['quantidade']}")
        break


# Função para listar o histórico de movimentações
def listar_movimentacoes():
    print("\nHISTÓRICO DE MOVIMENTAÇÕES")
    linha()

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")
    else:
        for indice, mov in enumerate(movimentacoes, start=1):
            print(f"Movimentação {indice}")
            print(f"Tipo: {mov['tipo']}")
            print(f"Produto: {mov['produto']}")
            print(f"Quantidade: {mov['quantidade']}")
            print(f"Data: {mov['data']}")
            print(f"Responsável: {mov['responsavel']}")
            print(f"Estoque atual: {mov['estoque_atual']}")
            linha()

# Programa principal
while True:
    linha()
    print("SISTEMA DE CONTROLE DE ESTOQUE")
    linha()
    print("1 - Registrar entrada de produto")
    print("2 - Registrar saída de produto")
    print("3 - Listar registros de movimentações")
    print("4 - Sair")
    linha()

    menu_opcao = ler_inteiro("Digite a opção desejada: ")

    if menu_opcao == 1:
        registrar_entrada()

    elif menu_opcao == 2:
        registrar_saida()

    elif menu_opcao == 3:
        listar_movimentacoes()

    elif menu_opcao == 4:
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida! Digite uma opção do menu.")