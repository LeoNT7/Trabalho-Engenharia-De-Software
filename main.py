produtos = {
    1: {"cod": "Arroz", "quantidade": 10},
    2: {"cod": "Feijão", "quantidade": 5},
    3: {"cod": "Macarrão", "quantidade": 8},
    4: {"cod": "Açúcar", "quantidade": 12}
}

def listarProdutos ():
        print("Produtos disponíveis:")      
        for codigo, nome in produtos.items():
            print(f"Cod {codigo}: {nome['cod']} (Qtd: {nome['quantidade']})")
        print ()
        print("Quantidade de produtos na lista", len(produtos))

def voltar():
    print("-----------------------------------------------")
    print()
    print()
    print("Voltando...")
    print()
    print()
    print("-----------------------------------------------")

while True:
    print("-----------------------------------------------")
    print("------- SISTEMA DE PRODUTOS NO ESTOQUE --------")
    print("-----------------------------------------------")
    print(" 1 - Registrar entrada de produto")
    print(" 2 - Retirar produto")
    print(" 3 - Sair")
    print("-----------------------------------------------")
    menuOp = int(input("Digite a opção >> "))

    if menuOp == 1:
        while True:
            print("------------ REGISTRAR ENTRADA DE PRODUTO --------------")
            print("--------------------------------------------------------")

            ##Implementar aqui

            print("0 - Voltar")
            op = int(input("Digite a opção >>"))
            if op == 0:
                voltar()
                break
            
    elif menuOp == 2:
        while True:
            print("------- REGISTRAR RETIRADA DE PRODUTOS --------")
            print("-----------------------------------------------")

            listarProdutos()
            ##Implementar aqui


            print("0 - Voltar")
            op = int(input("Digite o código do produto a ser retirado >> "))

            if op in produtos:

                while True:
                    print(f"Produto selecionado: {produtos[op]}")
                    teste = input("teste") #criar validação pra retirar produto do estoque

            elif op == 0:
                voltar()
                break
            else:
                print("Código inválido!")

    elif menuOp == 3:
        print("SAINDO..")
        break
    


       
                

    



    
