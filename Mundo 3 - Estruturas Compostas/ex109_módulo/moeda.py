def moeda(valor):
    '''
    -> Realiza formatação do valor passado para dinheiro
    :parâmetro valor: Valor do dinheiro
    :return: Retorna o parâmetro passado em formato de reais (R$)
    '''
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, bonus, view=False):
    '''
    -> Realiza o calculo de aumento sálarial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro bonus: Porcentagem do bônus
    :parâmetro view: Verifica se formata ou não o valor
    :return: Retorna valor com aumento sálarial
    '''
    return moeda(valor + (valor * bonus / 100)) if view else valor + (valor * bonus / 100)


def diminuir(valor, onus, view=False):
    '''
    -> Realiza o calculo de redução salárial e retorna seu valor
    :parâmetro valor: Valor do dinheiro
    :parâmetro onus: Porcentagem do ônus
    :parâmetro view: Verifica se formata ou não o valor
    :return: Retorna o valor da redução salárial
    '''
    return moeda(valor - (valor * onus / 100)) if view else valor - (valor * onus / 100)


def dobro(valor, view=False):
    '''
    -> Realiza o calculo de dobro salárial
    :parâmetro valor: Valor do dinheiro
    :parâmetro view: Verifica se formata ou não o valor
    :return: Retorna o valor dobrado
    '''
    return moeda(valor * 2) if view else valor * 2


def metade(valor, view=False):
    '''
    -> Realiza o calculo de metade salárial
    :parâmetro valor: Valor do dinheiro
    :parâmetro view: Verifica se formata ou não o valor
    :return: Retorna a metade do valor
    '''
    return moeda(valor / 2) if view else valor / 2