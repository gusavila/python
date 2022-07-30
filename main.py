from wsgiref.validate import validator


produtos = []
op = 1
while op != 0:

    print('---------------------------MENU----------------------------')
    print('1 - Cadastro de novos produtos')
    print('2 - Entrada de itens em estoque')
    print('3 - Saída de itens do estoque')
    print('4 - Exibir todos produtos fabricados')
    print('5 - Consultar pelo nome de um produto fabricado')
    print('6 - Produtos Fabricados que estão abaixo do estoque mínimo')
    print('7 - Matérias-primas que estão abaixo do estoque mínimo')
    print('8 - Situação financeira')
    print('0 - Encerrar o programa')
    print('-----------------------------------------------------------')

    op = int(input('Digite o número da opção escolhida: '))

    if op == 1:
        nome = input('Nome do produto: ')
        tipo = input('Tipo (M) para matéria-prima ou (P) para produto fabricado: ')
        qtd = int(input('Quantidade em estoque: '))
        qtdMinima = int(input('Quantidade mínima de estoque: '))
        preco = float(input('Valor unitário: '))
        novoProduto = [nome, tipo, qtd, qtdMinima, preco]
        produtos.append(novoProduto)

    elif op == 2:
        for endereco, produto in enumerate(produtos):
            print(f'\nEndereço do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

        enderecoProduto = int(input('\nDigite o endereço do produto: '))
        qtdItems = int(input('Digite a quantidade de items que entrara no estoque: '))  

        produtos[enderecoProduto][2] += qtdItems 

    elif op == 3:
        for endereco, produto in enumerate(produtos):
            print(f'\nCodigo do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

        enderecoProduto = int(input('\nDigite o endereço do produto: '))
        qtdItems = int(input('Digite a quantidade de items que será removida do estoque: '))  

        if qtdItems <= produtos[endereco][2]:
            produtos[enderecoProduto][2] -= qtdItems 
        else:
            print('Quantidade de item está indisponível para retirada!')

    elif op == 4:
        for endereco, produto in enumerate(produtos):
            print(f'\nCodigo do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

    elif op == 5:
        achou = []
        nome = str(input('Nome do produto: '))

        for n in produtos:
            if nome in n[0] or nome == n:
                achou.append(n)
        
        for endereco, produto in enumerate(achou):
            print(f'\nCodigo do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

    elif op == 6:
        for endereco, produto in enumerate(produtos):
            if produto[1] == 'P' and produto[2] < produto[3]:
                print(f'\nCodigo do produto({endereco})')
                print(f'Nome(descrição)  - {produto[0]}')
                print(f'Faltam {produto[3] - produto[2]} para atingir o estoque')
            else:
                print('Não há quantidade de produtos abaixo do estoque!')
    
    elif op == 7:
        for endereco, produto in enumerate(produtos):
            if produto[1] == 'M' and produto[2] < produto[3]:
                print(f'\nCodigo do produto({endereco})')
                print(f'Nome(descrição)  - {produto[0]}')
                print(f'Faltam {produto[3] - produto[2]} para atingir o estoque')
            else:
                print('Não há quantidade de matérias-primas abaixo do estoque!')
    
    elif op == 8:
        valorTotalMateria = 0
        valorTotalProduto = 0
        for endereco, produto in enumerate(produtos):
            if produto[1] == 'M':
                valorTotalMateria += [produto[2] * produto[4]]
            elif produto[1] == 'P':
                valorTotalProduto += [produto[2] * produto[4]]

        print(f'Total gasto com matéria-prima: {valorTotalMateria}')
        print(f'Total gasto com produtos: {valorTotalProduto}')
        print(f'Diferença  entre o valor total de produtos com o valor total das matérias-primas: {valorTotalProduto - valorTotalMateria}')
        if valorTotalMateria > valorTotalProduto:
            print('O estoque da matéria-prima está mais caro')
        elif valorTotalMateria < valorTotalProduto:
            print('O estoque de produtos está mais caro')
        elif valorTotalMateria == valorTotalProduto:
            print('O valor do estoque de produtos está igual ao valor do estoque de matéria-prima')
