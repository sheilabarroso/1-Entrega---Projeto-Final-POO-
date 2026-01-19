from item_carrinho import ItemCarrinho
from produto import Produto
from cliente import Cliente


class Carrinho:
    def __init__(self, cliente: Cliente, id_carrinho: int | None = None):
        self.id = id_carrinho
        self.cliente = cliente
        self.itens = {}
    
    def adicionar(self, produto: Produto, quantidade: int = 1):
        self.adicionar_produto(produto, quantidade)

    def adicionar_produto(self, produto: Produto, quantidade: int = 1):
        if not produto.ativo:
            raise ValueError("Produto inativo")

        if quantidade > produto.estoque:
           raise ValueError("Estoque insuficiente")

        if produto.sku in self.itens:
            self.itens[produto.sku].quantidade += quantidade
        else:
            self.itens[produto.sku] = ItemCarrinho(produto, quantidade)

    def remover_produto(self, sku: str):
        if sku not in self.itens:
            raise ValueError("Produto não está no carrinho")
        del self.itens[sku]

    def total(self):
        return sum(item.subtotal() for item in self.itens.values())

    def __len__(self):
        return sum(item.quantidade for item in self.itens.values())

    def exibir(self):
        print(f"\n--- Carrinho #{self.id} | Cliente: {self.cliente.nome} ---")

        if not self.itens:
            print("Carrinho vazio.")
            return

        for item in self.itens.values():
            print(
                f"{item.produto.nome} ({item.quantidade}x) "
                f"R$ {item.produto.preco_unitario:.2f} = R$ {item.subtotal():.2f}"
            )

        print(f"TOTAL: R$ {self.total():.2f}\n")
    
