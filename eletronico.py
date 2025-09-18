from produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, estoque, garantia_meses):
        super().__init__(nome, preco, estoque)
        self.garantia_meses = garantia_meses

    def aplicar_desconto(self, percentual):
        if self.garantia_meses >12:
            return self.get_preco() *0.95
        else:
            return self.get_preco() *0.98
    
    def estender_garantia(self, meses):
        if meses >0:
            self.garantia_meses += meses
            print(f"Garantia de {self.nome} estendida. Nova garantia {self.garantia_meses} meses.")
        else:
            print("O número de meses para estender a garantia deve ser positivo.")
