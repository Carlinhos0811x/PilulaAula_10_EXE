def acao_semafaro(cor : str):
    cor = cor.lower()
    if cor == 'vermelho':
        return 'Pare'
    elif cor == 'amarelo':
        return 'Atenção'
    elif cor =='verde':
        return 'Siga'
    return 'Cor invalida'