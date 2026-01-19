import sys
import os
sys.path.append(os.path.abspath("src"))

from carrinho import Carrinho
from produto import Produto
from cliente import Cliente

def test_adicionar_item_carrinho():
    cliente = Cliente(1, "João", "joao@email.com", "12345678900", [])
    carrinho = Carrinho(cliente)
    produto = Produto("SKU1", "Mouse", "Periférico", 100.0, 10)

    carrinho.adicionar(produto, 2)
    assert len(carrinho) == 2
