def exibir_menu():
    """Exibe o menu de opções."""
    print("\nMenu de Opções:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar inventário")
    print("4. Sair")
    
def adicionar_item(inventario):
    """Adiciona um novo item ao inventário."""
    nome = input("Nome do item: ")
    quantidade = int(input("Quantidade: "))
    inventario.append({"nome": nome, "quantidade": quantidade})
    print(f"Item '{nome}' adicionado ao inventário.")
    
def remover_item(inventario):
    """Remove um item do inventário pelo nome."""
    nome = input("Nome do item a remover: ")
    for item in inventario:
        if item["nome"] == nome:
            inventario.remove(item)
            print(f"Item '{nome}' removido do inventário.")
            return
    print(f"Item '{nome}' não encontrado. Digite o item corretamente.")    

def listar_inventario(inventario):
    """Exibe o inventário."""
    if not inventario:
        print("Inventário vazio.")
    else:
        print("\n* Inventário *")
        for item in inventario:
            print(f"- {item['nome']}: {item['quantidade']}")
        print("_________________")

def main():
    """Função principal que gerencia o menu e o inventário."""
    inventario = []

    while True:
        exibir_menu()
        escolha = input("Escolha a opção desejada (1-4): ")

        if escolha == '1':
            adicionar_item(inventario)
        elif escolha == '2':
            remover_item(inventario)
        elif escolha == '3':
            listar_inventario(inventario)
        elif escolha == '4':
            print("Inventário encerrado.")
            break
        else:
            print("Opção inválida. Digite outra opção.")

if __name__ == "__main__":
    main()