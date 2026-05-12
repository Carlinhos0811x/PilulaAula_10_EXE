from frete import calcular_frete

def test_peso_zero():
    assert calcular_frete(0) == 0

def test_peso_negativo():
    assert calcular_frete(-10) == 0

def test_ate_1kg_limite():
    assert calcular_frete(1.0) == 5.0

def test_ate_1kg():
    assert calcular_frete(0.5) == 5.0

def test_acima_1kg():
    assert calcular_frete(1.01) == 10.0

def test_ate_5kg_limite():
    assert calcular_frete(5.0) == 10.0

def test_acima_5kg():
    assert calcular_frete(5.01) == 18.0