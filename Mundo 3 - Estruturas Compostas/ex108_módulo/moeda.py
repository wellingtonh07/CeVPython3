def moeda(valor=0, moeda='R$'):
    '''
    -> Realiza formatação do valor passado para dinheiro
    :parâmetro moeda: Simbolo da moeda utilizada
    :parâmetro valor: Valor do dinheiro
    :return: Retorna o parâmetro passado em formato de reais (R$)
    '''
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, bonus=0):
    '''
    -> Realiza o calculo de aumento sálarial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro bonus: Porcentagem do bônus
    :return: Retorna valor com aumento sálarial
    '''
    return moeda(valor + (valor * bonus / 100))


def diminuir(valor=0, onus=0):
    '''
    -> Realiza o calculo de redução salárial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro onus: Porcentagem do ônus
    :return: Retorna o valor da redução salárial
    '''
    return moeda(valor - (valor * onus / 100))


def dobro(valor=0):
    '''
    -> Realiza o calculo de dobro salárial
    :parâmetro valor: Valor do dinheiro
    :return: Retorna o valor dobrado
    '''
    return moeda(valor * 2)


def metade(valor=0):
    '''
    -> Realiza o calculo de metade salárial
    :parâmetro valor: Valor do dinheiro
    :return: Retorna a metade do valor
    '''
    return moeda(valor / 2)