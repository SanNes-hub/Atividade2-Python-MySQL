from livro import Livro
from eletronico import Eletronico
from carrinho_compras import CarrinhoCompras

catalogo = [
Livro(nome="Coraline", preco=59.90, estoque=15, autor="Neil Gaiman"),
Livro(nome="O Guia do Mochileiro das Galáxias", preco=39.99, estoque=10, autor="Douglas Adams"),
Eletronico(nome="Fone de Ouvido Bluetooth", preco=199.00, estoque=20, garantia_meses=12),
Eletronico(nome="Teclado", preco=350.50, estoque=8, garantia_meses=24),
Eletronico(nome="Monitor 32 polegadas", preco=1800.00, estoque=5, garantia_meses=36)]

# (continuação do arquivo main.py)

def exibir_menu():
    """Mostra as opções para o usuário."""
    print("\n--- Loja Virtual ---")
    print("1. Ver produtos disponíveis")
    print("2. Adicionar item ao carrinho")
    print("3. Remover item do carrinho")
    print("4. Ver meu carrinho")
    print("5. Finalizar compra (ver total)")
    print("0. Sair da loja")
    print("--------------------")

def main():
    """Função principal que executa o loop da loja."""
    carrinho = CarrinhoCompras()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\n--- Produtos Disponíveis ---")
            for i, produto in enumerate(catalogo):
                print(f"[{i+1}] ", end="") # Mostra o índice para seleção
                produto.exibir_info()
        
        elif escolha == '2':
            # Adicionar item
            try:
                num_produto = int(input("Digite o número do produto que deseja adicionar: "))
                if not 1 <= num_produto <= len(catalogo):
                    print("Erro: Número de produto inválido.")
                    continue
                
                produto_escolhido = catalogo[num_produto - 1]

                qtd = int(input(f"Qual a quantidade de '{produto_escolhido.nome}' deseja? "))
                carrinho.adicionar_item(produto_escolhido, qtd)

            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite um número.")

        elif escolha == '3':
            # Remover item
            if not carrinho._itens:
                print("Seu carrinho está vazio.")
                continue
            
            print("\n--- Itens no seu Carrinho ---")
            for i, (produto, qtd) in enumerate(carrinho._itens):
                 print(f"[{i+1}] {produto.nome} (Quantidade: {qtd})")
            
            try:
                num_remover = int(input("Digite o número do item que deseja remover: "))
                if not 1 <= num_remover <= len(carrinho._itens):
                    print("Erro: Número de item inválido.")
                    continue
                
                # Pega o objeto produto de dentro da tupla no carrinho
                produto_para_remover = carrinho._itens[num_remover - 1][0]
                carrinho.remover_item(produto_para_remover)

            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite um número.")

        elif escolha == '4':
            carrinho.listar_itens()

        elif escolha == '5':
            if not carrinho._itens:
                print("Seu carrinho está vazio.")
                continue
            total = carrinho.calcular_total()
            print(f"\n>>> Total da sua compra com descontos: R$ {total:.2f}")
            print("Obrigado por comprar conosco!")
            break # Finaliza a compra e o programa

        elif escolha == '0':
            print("Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
        
        input("\nPressione Enter para continuar...")


# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    main()

