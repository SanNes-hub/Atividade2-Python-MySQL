from produto import Produto

class Livro(Produto):
    def __init__(self, nome, preco, estoque, autor):
        super().__init__(nome, preco, estoque)
        self.autor = autor
    
    def aplicar_desconto(self, percentual):
        return self.get_preco() *0.90 
    
    def resumo(self):
        print(f"Resumo de {self.nome} por {self.autor}.")
               

                    
