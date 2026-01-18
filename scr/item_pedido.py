class ItemPedido:
  def __init__(self, produto, quantidade: int):
    self.produto = produto
    self.quantidade = quantidade
    self.preco_unitario = produto.preco_unitario
  def subtotal(self):
    return self.preco_unitario * self.quantidade
    

