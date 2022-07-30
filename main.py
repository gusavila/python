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
        for codigo, produto in enumerate(produtos):
            print(f'\nCodigo do produto({codigo})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

        codigoProduto = int(input('\nDigite o codigo do produto: '))
        qtdItems = int(input('Digite a quantidade de items que entrara no estoque: '))  

        produtos[codigo][2] += qtdItems 

    elif op == 3:
        nomeProduto = input('Digite o nome do produto: ')

    elif op == 4:
        for item in enumerate(produtos):
            print(f'{produtos}')

