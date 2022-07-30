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
        qtd = input('Quantidade em estoque: ')
        qtdMinima = input('Quantidade mínima de estoque: ')
        preco = input('Valor unitário: ')
        novoProduto = [nome, tipo, qtd, qtdMinima, preco]
        produtos += [novoProduto]

    elif op == 2:
        nomeProduto = input('Digite o nome do produto: ')
        qtdItems = input('Digite a quantidade a ser adicionada ao estoque: ')
        for codigo, produtos in enumerate():
            

    elif op == 3:
        nomeProduto = input('Digite o nome do produto: ')

    elif op == 4:
        for item in enumerate(produtos):
            print(f'{produtos}')

