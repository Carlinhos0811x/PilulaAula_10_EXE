from nota import calcular_nota
def test_nota_a():
    assert calcular_nota(9.0) == "A"   

def test_nota_b():
    assert calcular_nota(7.5) == "B"

def test_nota_c():
    assert calcular_nota(6.0) == "C"

def test_nota_d():
    assert calcular_nota(4.0) == "D"

def test_nota_f():
    assert calcular_nota(2.0) == "F"
    