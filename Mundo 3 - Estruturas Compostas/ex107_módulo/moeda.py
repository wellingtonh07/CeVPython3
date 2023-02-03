def aumentar(valor, bonus):
    '''
    -> Realiza o calculo de aumento sálarial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro bonus: Porcentagem do bônus
    :return: Retorna valor com aumento sálarial
    '''
    return valor + (valor * bonus / 100)


def diminuir(valor, onus):
    '''
    -> Realiza o calculo de redução salárial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro onus: Porcentagem do ônus
    :return: Retorna o valor da redução salárial
    '''
    return valor - (valor * onus / 100)


def dobro(valor):
    '''
    -> Realiza o calculo de dobro salárial
    :parâmetro valor: Valor do dinheiro
    :return: Retorna o valor dobrado
    '''
    return valor * 2


def metade(valor):
    '''
    -> Realiza o calculo de metade salárial
    :parâmetro valor: Valor do dinheiro
    :return: Retorna a metade do valor
    '''
    return valor / 2