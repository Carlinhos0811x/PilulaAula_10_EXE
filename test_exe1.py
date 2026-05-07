from exe1 import acao_semafaro

def test_cor_vermelho():
    assert acao_semafaro('vermelho') == 'Pare'
    
def test_cor_vermelho():
    assert acao_semafaro('amarelo') == 'Atenção'
    
def test_cor_vermelho():
    assert acao_semafaro('verde') == 'Siga'
    
def test_cor_vermelho():
    assert acao_semafaro('rosa') == 'Cor invalida'
    