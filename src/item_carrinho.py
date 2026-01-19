from produto import Produto

class ItemCarrinho:
    def __init__(self, produto: Produto, quantidade: int):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return self.produto.preco_unitario * self.quantidade
