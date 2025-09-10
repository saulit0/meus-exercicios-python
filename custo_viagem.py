def calcular_custo_viagem(distancia, consumo, preco):
  """calcula o custo de viagem baseado na distancia (KM), consumo (KM/L) e preco do combustivel (R$)"""
  
distancia = float(input("Informe a distância da viagem em KM: "))
consumo = float(input("Informe o consumo do carro em KM/L: "))
preco_combustivel = float(input("Informe o preço do combustível por litro em R$: "))

litros_necessarios = distancia / consumo
custo_total = litros_necessarios * preco_combustivel

print(f"O custo total da viagem será de: R$ {custo_total:.2f}")