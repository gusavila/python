from traceback import print_tb
from wsgiref.validate import validator


produtos = [] # declaraçao da lista
opcao = 1 # variavel que recebera a resposta do usuario
while opcao != 0: # O menu será repetido enquanto a resposta do usuário for diferente de 0

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

    opcao = int(input('Digite o número da opção escolhida: ')) # a variavel opcao receberá a resposta do usuário

    if opcao == 1: #  sera feito o cadastro de novos produtos
        nome = input('Nome do produto: ')
        tipo = input('Tipo (M) para matéria-prima ou (P) para produto fabricado: ')
        qtd = int(input('Quantidade em estoque: '))
        qtdMinima = int(input('Quantidade mínima de estoque: '))
        preco = float(input('Valor unitário: '))
        novoProduto = [nome, tipo, qtd, qtdMinima, preco] # nome, tipo, quantidade, quantidade minima e preço foram adicionados a lista novoProduto
        produtos.append(novoProduto) # A lista novoProduto foi adicionada a lista produtos

    elif opcao == 2: # sera realizada a entrada de items no estoque
        for endereco, produto in enumerate(produtos):
            print(f'\nEndereço do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

        enderecoProduto = int(input('\nDigite o endereço do produto: ')) #o usuaria devera digitar o número do enredeço do produto e não o nome
        qtdItems = int(input('Digite a quantidade de items que entrara no estoque: ')) # o usuário digitara a quantidade de items para entrar no estoque

        produtos[enderecoProduto][2] += qtdItems # o produto escolhido receberá  a quantidade digitada no estoque 

    elif opcao == 3: # sera realizada a saida de items do estoque
        for endereco, produto in enumerate(produtos):
            print(f'\nCodigo do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

        enderecoProduto = int(input('\nDigite o endereço do produto: ')) #o usuaria devera digitar o número do enredeço do produto e não o nome
        qtdItems = int(input('Digite a quantidade de items que será removida do estoque: '))  # o usuário digitara a quantidade de items a ser retirada do estoque

        if qtdItems <= produtos[endereco][2]: # Faz uma verificação se a quantidade desejada a ser retirada está disponível em estoque
            produtos[enderecoProduto][2] -= qtdItems 
        else: #se não tiver disponivel em estoque
            print('Quantidade de item está indisponível para retirada!')

    elif opcao == 4: #sera mostrado todos o produtos cadastrados
        for endereco, produto in enumerate(produtos):
            print(f'\nCodigo do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

    elif opcao == 5:
        pegar = [] # lista de produtos que serão encontrados
        nome = str(input('Nome do produto: '))

        for n in produtos:
            if nome in n[0] or nome == n:  # testa se existe a resposta do cliente no nome do produto
                pegar.append(n)
        
        for endereco, produto in enumerate(pegar):  # lista de produtos encontrados
            print(f'\nCodigo do produto({endereco})')
            print(f'Nome(descrição)  - {produto[0]}')
            print(f'Tipo de produto  - {produto[1]}')
            print(f'Quantidade atual - {produto[2]}')
            print(f'Valor unitario   - {produto[4]}')
            print(f'Valor Total      - {produto[2] * produto[4]}')

    elif opcao == 6: # Produtos Fabricados que estão abaixo do estoque mínimo
        qtdProdutosAbaixoEstoque = 0 # variavel para contar os items abaixo do estoque
        for endereco, produto in enumerate(produtos):
            if produto[1] == 'P' and produto[2] < produto[3]: #Se tipo do produto for igual(==) a 'P' e(and) Quantidade atual for menor(<) que a quantidade mínima então será exibida a mensagem do código do produto, nome e a quantidade que falta para atingir o estoque
                print(f'\nCodigo do produto({endereco})')
                print(f'Nome(descrição)  - {produto[0]}')
                print(f'Faltam {produto[3] - produto[2]} para atingir o estoque')
                qtdProdutosAbaixoEstoque += 1 # aqui será feita a contagem de items abaixo do estoque e que será utilizada para mostrar a mensagem a seguir caso não houver items abaixo do estoque
        if qtdProdutosAbaixoEstoque == 0: # verifica se tem não tem items abaixo do estoque
            print('Não há quantidade de Produtos Fabricados abaixo do estoque!') # mensagem exibida se não tiver items abaixo do estoque
        else:
            print(f'Quantidade de Produtos Fabricados abaixo do estoque: {qtdProdutosAbaixoEstoque}')
    
    elif opcao == 7: # Matéria-prima abaixo do estoque. Será realizada a mesma operação como a de cima, mudando apenas o tipo do produto que será agora matéria-prima
        qtdMateriaAbaixoEstoque = 0
        for endereco, produto in enumerate(produtos):
            if produto[1] == 'M' and produto[2] < produto[3]:
                print(f'\nCodigo do produto({endereco})')
                print(f'Nome(descrição)  - {produto[0]}')
                print(f'Faltam {produto[3] - produto[2]} para atingir o estoque')
                qtdMateriaAbaixoEstoque += 1
        if qtdMateriaAbaixoEstoque == 0:
            print('Não há quantidade de matéria-prima abaixo do estoque!')
        else:
            print(f'Quantidade de Matéria-prima abaixo do estoque: {qtdMateriaAbaixoEstoque}')
    
    elif opcao == 8: #Aqui será exibido o valor total gasto com o estoque atual de matéria-prima, o valor total de produtos fabricados que estão em estoque e a diferença entra o valor total de produtos fabricados que estão em estoque com o valor total das matérias-primas armazenadas em estoque
        valorTotalMateria = 0
        valorTotalProduto = 0
        for endereco, produto in enumerate(produtos): #será percorrida a lista de produtos
            if produto[1] == 'M': # se tipo for igual a 'M' então será executada a seguinte operação:
                valorTotalMateria += (produto[2] * produto[4]) #valorTotalMeteria receberá ele mesmo mais a quantidade total referente a cada produto cadastrado como 'M'(Materia-prima)
            elif produto[1] == 'P':# se tipo for igual a 'P' então será executada a seguinte operação:
                valorTotalProduto += (produto[2] * produto[4])#valorTotalProduto receberá ele mesmo mais a quantidade total referente a cada produto cadastrado como 'P'(Produto-fabricado)

        print(f'Total gasto com matéria-prima: {valorTotalMateria}')
        print(f'Total gasto com produtos: {valorTotalProduto}')
        print(f'Diferença  entre o valor total de produtos com o valor total das matérias-primas: {valorTotalProduto - valorTotalMateria}')
        if valorTotalMateria > valorTotalProduto: #se o valor total de matéria-prima for maior que o de produto fabricados então o comando será executado
            print('O estoque da matéria-prima está mais caro')
        elif valorTotalMateria < valorTotalProduto: #se o valor total de matéria-prima for menor que o de produto fabricados então o comando será executado
            print('O estoque de produtos está mais caro')
        elif valorTotalMateria == valorTotalProduto: #se o valor total de matéria-prima for igual ao de produto fabricados então o comando será executado
            print('O valor do estoque de produtos está igual ao valor do estoque de matéria-prima')
