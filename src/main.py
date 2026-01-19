from data.dados import carregar_dados, salvar_dados
from produto import Produto
from cliente import Cliente
from carrinho import Carrinho
from pedido import Pedido
from cupom import Cupom
from frete import Frete
from status_pedido import StatusPedido


def main():
    print("=== LOJA VIRTUAL ===\n")

    cliente = Cliente(
        1,
        "Vitória Cavalcante",
        "vitoria@email.com",
        "12345678900",
        []
    )

    produto1 = Produto("001", "Mouse Gamer", "Periférico", 120.00, 10)
    produto2 = Produto("002", "Teclado Mecânico", "Periférico", 250.00, 5)

    carrinho = Carrinho(1, cliente)
    carrinho.adicionar(produto1, 2)
    carrinho.adicionar(produto2, 1)

    print(f"Total do carrinho: R$ {carrinho.total():.2f}\n")

    frete = Frete("CE")
    valor_frete, prazo = frete.calcular()
    print(f"Frete: R$ {valor_frete:.2f} | Prazo: {prazo} dias\n")

    pedido = Pedido(1, cliente, carrinho)
    pedido.frete = valor_frete
    pedido.status = StatusPedido.PAGO

    print(pedido)
    print("\n=== COMPRA FINALIZADA COM SUCESSO ===")


if __name__ == "__main__":
    main()
