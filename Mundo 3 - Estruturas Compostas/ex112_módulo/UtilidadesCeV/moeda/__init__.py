def resumo(valor, bonus, onus):
    '''
    -> Print na tela uma tabela formatada com todos os valores e operações realizadas
    :parâmetro valor: Valor do dinheiro
    :parâmetro bonus: Porcentagem do bônus
    :parâmetro onus: Porcentagem do ônus
    :return: Não possui retorno
    '''
    print('-' * 35 + f'\n{" RESUMO DO VALOR ":^35}\n' + '-' * 35)

    print(f'Preço analisado:   {moeda(valor)}')
    print(f'Dobro do preço:    {dobro(valor)}')
    print(f'Metade do preço:   {metade(valor)}')
    print(f'{bonus}% de aumento:    {aumentar(valor, bonus)}')
    print(f'{onus}% de redução:    {diminuir(valor, onus)}')

    print('-' * 35)


def moeda(valor):
    '''
    -> Realiza formatação do valor passado para dinheiro
    :parâmetro valor: Valor do dinheiro
    :return: Retorna o parâmetro passado em formato de reais (R$)
    '''
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, bonus):
    '''
    -> Realiza o calculo de aumento sálarial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro bonus: Porcentagem do bônus
    :return: Retorna valor com aumento sálarial
    '''
    return moeda(valor + (valor * bonus / 100))


def diminuir(valor, onus):
    '''
    -> Realiza o calculo de redução salárial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro onus: Porcentagem do ônus
    :return: Retorna o valor da redução salárial
    '''
    return moeda(valor - (valor * onus / 100))


def dobro(valor):
    '''
    -> Realiza o calculo de dobro salárial
    :parâmetro valor: Valor do dinheiro
    :return: Retorna o valor dobrado
    '''
    return moeda(valor * 2)


def metade(valor):
    '''
    -> Realiza o calculo de metade salárial
    :parâmetro valor: Valor do dinheiro
    :return: Retorna a metade do valor
    '''
    return moeda(valor / 2)