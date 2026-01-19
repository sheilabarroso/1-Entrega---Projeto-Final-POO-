from item_pedido import ItemPedido
from status_pedido import StatusPedido
from cupom import Cupom
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
        self.status = StatusPedido.CRIADO
        self.frete = 0.0
        self.cupom = None

        for item in carrinho.itens.values():
            self.itens.append(ItemPedido(item.produto, item.quantidade))

    def subtotal(self):
        return sum(item.subtotal() for item in self.itens)

    def total(self):
        desconto = 0
        if hasattr(self, "cupom") and self.cupom:
            desconto = self.cupom.calcular_desconto(self.subtotal())

        total = self.subtotal() + self.frete - desconto
        return max(total, 0)

    def __str__(self):
        return (
            f"Pedido #{self.id} | "
            f"Status: {self.status.value if hasattr(self.status, 'value') else self.status} | "
            f"Total: R$ {self.total():.2f}"
    )
    def aplicar_cupom(self, cupom: Cupom):
        self.cupom = cupom

    def pagar(self):
        self.status = StatusPedido.PAGO

    def cancelar(self):
        if self.status in (StatusPedido.CRIADO, StatusPedido.PAGO):
            self.status = StatusPedido.CANCELADO
