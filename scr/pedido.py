from item_pedido import ItemPedido
from pagamento import Pagamento
from frete import Frete

class Pedido:
    STATUS_CRIADO = "CRIADO"
    STATUS_PAGO = "PAGO"
    STATUS_ENVIADO = "ENVIADO"
    STATUS_ENTREGUE = "ENTREGUE"
    STATUS_CANCELADO = "CANCELADO"

    def __init__(self, id_pedido: int, cliente, carrinho):
        self.id = id_pedido
        self.cliente = cliente
        self.itens = []
        self.status = Pedido.STATUS_CRIADO
        self.frete = 0.0

        for item in carrinho.itens.values():
            self.itens.append(ItemPedido(item.produto, item.quantidade))

    def subtotal(self):
        return sum(item.subtotal() for item in self.itens)

    def total(self):
        return self.subtotal() + self.frete

    def __str__(self):
        return (
            f"Pedido #{self.id} | "
            f"Status: {self.status} | "
            f"Total: R$ {self.total():.2f}"
        )
