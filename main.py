produtos = {'item1': 2, 'item2': 0, 'item3': 5}

while True:
    print("-----------------------------------------------")
    print("------- SISTEMA DE PRODUTOS NO ESTOQUE --------")
    print("-----------------------------------------------")
    print(" 1 - Registrar entrada de produto")
    print(" 2 - Retirar produto")
    print(" 3 - Sair")
    print("-----------------------------------------------")
    menuOp = int(input("Digite a opção >>"))

    if menuOp == 1:
        while True:
            print("------------ REGISTRAR ENTRADA DE PRODUTO --------------")
            print("--------------------------------------------------------")
            print("0 - Voltar")
            op = int(input("Digite a opção >>"))
            if op == 0:
                print("-----------------------------------------------")
                print()
                print()
                print("Voltando...")
                print()
                print()
                print("-----------------------------------------------")
                break
            
    elif menuOp == 2:
        while True:
            print("------- REGISTRAR RETIRADA DE PRODUTOS --------")
            print("-----------------------------------------------")
            print("CODIGO | PRODUTO  | QUANTIDADE                 ")
                   
            i = 0
            for produto, quantidade in produtos.items():
                print(f"  {i}       {produto}         {quantidade}     ")
                i += 1
            print("Lista contém", i, "itens")

            print("0 - Voltar")
            op = int(input("Digite o produto a ser retirado >>"))
            if op == 0:
                print("-----------------------------------------------")
                print()
                print()
                print("Voltando...")
                print()
                print()
                print("-----------------------------------------------")
                break

    elif menuOp == 3:
        print("SAINDO..")
        break
    


       
                

    



    
