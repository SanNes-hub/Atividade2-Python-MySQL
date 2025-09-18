class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def set_preco(self, novo_preco):
        if novo_preco <0:
            raise ValueError("O preço não pode ser negativo")
        else:
            self.__preco = float(novo_preco)

    def get_preco(self):
        return self.__preco

    def set_estoque(self, novo_estoque):
        if novo_estoque <0:
            raise ValueError("O estoque não pode ser negativo")
        else:
            self.__estoque = int(novo_estoque)
            
    def get_estoque(self):
        return self.__estoque
    
    def exibir_info(self):
        print(f"produto: {self.nome}, preço: R${self.get_preco()}, estoque: {self.get_estoque()} ")

    def aplicar_desconto(self, percentual):
        if not 0 <= percentual <=100:
            raise ValueError("O percentual de desconto deve estar entre 0 e 100")
        desconto = self.get_preco() * (percentual/100)
        return self.get_preco() - desconto
        