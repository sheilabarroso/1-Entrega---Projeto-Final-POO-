from typing import List
from pedido import Pedido
from produto import Produto
from status_pedido import StatusPedido


class Relatorios:
    """
    Classe responsável por gerar relatórios do sistema.
    Todos os métodos são estáticos.
    """

    @staticmethod
    def faturamento_total(pedidos: List[Pedido]) -> float:
        """
        Soma o total de todos os pedidos pagos.
        """
        return sum(
            p.total()
            for p in pedidos
            if p.status == StatusPedido.PAGO
        )

    @staticmethod
    def pedidos_por_status(pedidos: List[Pedido]):
        """
        Retorna a quantidade de pedidos por status.
        """
        resultado = {}
        for pedido in pedidos:
            status = pedido.status
            resultado[status] = resultado.get(status, 0) + 1
        return resultado

    @staticmethod
    def produtos_mais_vendidos(pedidos: List[Pedido]):
        """
        Retorna um dicionário com a quantidade vendida por produto.
        """
        vendidos = {}

        for pedido in pedidos:
            if pedido.status != StatusPedido.PAGO:
                continue

            for item in pedido.itens:
                sku = item.produto.sku
                vendidos[sku] = vendidos.get(sku, 0) + item.quantidade

        return vendidos

    @staticmethod
    def ticket_medio(pedidos: List[Pedido]) -> float:
        """
        Calcula o ticket médio dos pedidos pagos.
        """
        pagos = [p for p in pedidos if p.status == StatusPedido.PAGO]

        if not pagos:
            return 0.0

        return sum(p.total() for p in pagos) / len(pagos)

