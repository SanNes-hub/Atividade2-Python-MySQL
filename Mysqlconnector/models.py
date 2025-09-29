from datetime import date

class Pedido:
    def __init__(self, cliente,):
        self.id = None
        self.cliente = cliente
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

class ItemPedido:
    def __init__(self, produto, categoria, quantidade, preco):
        self.id = None
        self.produto = produto
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
