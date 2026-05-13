from bonus import test_bonus    

def test_bonus_bom():
    assert test_bonus(1000.0, "Bom") == 100.0

def test_bonus_excelente():
    assert test_bonus(1000.0, "Excelente") == 200.0

def test_bonus_regular():
    assert test_bonus(1000.0, "Regular") == 20.0

def test_bonus_ruim():
    assert test_bonus(1000.0, "Ruim") == 0.0

def test_bonus_avaliacao_invalida():
    assert test_bonus(1000.0, "Mais ou Menos") == 0.0

def test_salario_negativo():
    assert test_bonus(-1000.0, "Excelente") == 0.0