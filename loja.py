from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base
        
    @abstractmethod
    def calcular_preco_final(self):
        pass
    
class ProdutoFisico(Produto):
    def __init__(self, nome, preco_base, custo_frete):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete
        
    def calcular_preco_final(self):
        return self.preco_base + self.custo_frete
        
class ProdutoDigital(Produto):
    def __init__(self, nome, preco_base, taxa_servico):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico
        
    def calcular_preco_final(self):
        return self.preco_base + self.taxa_servico
    
carrinho = [
    ProdutoFisico("Teclado", 300.00, 55.00),
    ProdutoDigital("Ingresso Festival", 250.00, 15.00),
]

print("Carrinho de Compras:")
total = 0.

for produto in carrinho:
    preco_final = produto.calcular_preco_final()
    print(f"{produto.nome}: R$ {preco_final:.2f}")
    total += preco_final
    
print(f"\nTotal da compra: R$ {total:.2f}")