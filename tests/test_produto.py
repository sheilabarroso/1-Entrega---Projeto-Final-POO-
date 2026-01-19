import sys
import os
sys.path.append(os.path.abspath("src"))

from produto import Produto
import pytest

def test_criar_produto_valido():
    p = Produto("SKU1", "Mouse", "Periférico", 100.0, 10)
    assert p.preco_unitario == 100.0
    assert p.estoque == 10

def test_preco_invalido():
    with pytest.raises(ValueError):
        Produto("SKU2", "Teclado", "Periférico", -10, 5)
