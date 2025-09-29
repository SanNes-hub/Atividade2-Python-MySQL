from models import Base, Pedido, ItemPedido
from database import engine
from control import PedidoControl

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

def imprimir_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido encontrado.")
        return
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Categoria: {i.categoria}, Qtd: {i.quantidade}, Preço: {i.preco}")
    print("-" * 30)

if __name__ == "__main__":
    control = PedidoControl()

# 1. INSERÇÃO
    print("### 1. Inserindo novo pedido... ###")
    novo_pedido = Pedido(cliente='Ana Paula')
    novo_pedido.itens = [
        ItemPedido(produto='Smartphone', categoria='Eletrônicos', quantidade=1, preco=1500.00),
        ItemPedido(produto='Capinha', categoria='Acessórios', quantidade=1, preco=50.00)
    ]
    
    pedido_inserido = control.salvar_pedido(novo_pedido)
    print(f"Pedido {pedido_inserido.id} para o cliente '{pedido_inserido.cliente}' inserido com sucesso!\n")

    # 2. LISTAGEM
    print("### 2. Listando todos os pedidos... ###")
    pedidos = control.listar_pedidos_com_itens()
    imprimir_pedidos(pedidos)

    # 3. ATUALIZAÇÃO
    print(f"### 3. Atualizando o pedido {pedido_inserido.id}... ###")
    control.atualizar_pedido(pedido_id=pedido_inserido.id, novo_cliente="Ana Paula Oliveira")
    print(f"Cliente do pedido {pedido_inserido.id} atualizado com sucesso!\n")

    print("### Listando novamente para ver a atualização... ###")
    pedidos = control.listar_pedidos_com_itens()
    imprimir_pedidos(pedidos)

    # 4. DELEÇÃO
    print(f"### 4. Deletando o pedido {pedido_inserido.id}... ###")
    control.deletar_pedido(pedido_inserido.id)
    print(f"Pedido {pedido_inserido.id} deletado com sucesso!\n")

    # Listagem final para confirmar a deleção
    print("### Listagem final... ###")
    pedidos = control.listar_pedidos_com_itens()
    imprimir_pedidos(pedidos)
    
    control.fechar()
