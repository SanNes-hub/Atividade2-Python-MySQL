from models import Pedido
from database import SessionLocal

class PedidoControl:
    def __init__(self):
        self.db = SessionLocal()

    def salvar_pedido(self, pedido):
        self.db.add(pedido)
        self.db.commit()
        self.db.refresh(pedido)
        return pedido
    
    def atualizar_pedido(self, pedido_id, novo_cliente):
        pedido = self.db.get(Pedido, pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        
        pedido.cliente = novo_cliente
        self.db.commit()
        return pedido
    

    def deletar_pedido(self, pedido_id):
        pedido = self.db.get(Pedido, pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        self.db.delete(pedido)
        self.db.commit()
    
          
    def listar_pedidos_com_itens(self):
        return self.db.query(Pedido).all()

    def fechar(self):
        self.db.close()
