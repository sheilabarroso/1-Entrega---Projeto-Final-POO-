import sys
import os
sys.path.append(os.path.abspath("src"))

from pedido import Pedido
from carrinho import Carrinho
from produto import Produto
from cliente import Cliente

def test_total_pedido():
    cliente = Cliente(1, "Maria", "maria@email.com", "12345678900", [])
    carrinho = Carrinho(cliente)
    produto = Produto("SKU1", "Monitor", "Periférico", 500.0, 5)

    carrinho.adicionar(produto, 1)
    pedido = Pedido(1, cliente, carrinho)
    pedido.frete = 50

    assert pedido.total() == 550
