def leiaDinheiro(mensagem):
    '''
    -> Verifica se o preço está no formato de dinheiro
    :parâmetro mensagem: Mensagem a ser exibida ao usuário
    :return: Retorna o preço convertido para float
    '''
    while True:
        preço = input(mensagem).strip()
        analisa_preço = preço

        # Em caso de preço conter vírgula, força substituir por ponto
        if ',' in preço:
            analisa_preço = analisa_preço.replace(',', '.')

        # Dividindo preco onde tem ponto para verificação individual do valor informado
        preço_split = analisa_preço.split('.')

        valido = True

        # Percorrendo a lista gerada ao converter o preco em lista para validação
        for digito in preço_split:
            if not digito.isnumeric():
                valido = False
                break

        # Verificação final
        if not valido or analisa_preço.count('.') > 1:
            print(f'\33[31mERRO: "{preço}" é um preço inválido!\33[m')
            print()
            continue
        else:
            return float(analisa_preço)