from produto import Produto

class CarrinhoCompras:

    def __init__(self):
        self._itens = []

    def adicionar_item(self, produto, qtd):
        if qtd <=0:
            print(f"Erro. A quantidade deve ser positiva.")
            return
        if produto.get_estoque() >= qtd:
            novo_estoque = produto.get_estoque() - qtd
            produto.set_estoque(novo_estoque)
            self._itens.append((produto, qtd))
            print(f"{qtd} unidade(s) de {produto.nome} adicionada(s) ao carrinho")
    
        else:
            print(f"Estoque insuficiente para {produto.nome}. Disponível: {produto.get_estoque()}.")
    
    def remover_item(self, produto_para_remover):
        item_encontrado = None
        for item_tuple in self._itens:
            if item_tuple[0] == produto_para_remover:
                item_encontrado = item_tuple
                break
    
        if item_encontrado:
            produto, qtd = item_encontrado
            produto.set_estoque(produto.get_estoque() + qtd)
            self._itens.remove(item_encontrado)
            
            print(f"{produto.nome} foi removido do carrinho")

        else:
            print(f"{produto_para_remover.nome} não encontrado no carrinho.")

    def calcular_total(self):
        total = 0
        for p, q in self._itens:
            subtotal = p.aplicar_desconto(0) *q
            total += subtotal
        return total 

    def listar_itens(self):
        print("\n---Itens no carrinho---")
        if not self._itens: 
            print("\nO carrinho de compras está vazio.")
            return
            
        for p, q in self._itens:
            p.exibir_info()
            print(f"Quantidade no carrinho: {q}")
        print("-------------------------------")
