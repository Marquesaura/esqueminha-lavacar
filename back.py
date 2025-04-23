def calcular_desconto(preco_original,percentual_deconto):
    valor_desconto = preco_original * (percentual_deconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final, valor_desconto

preco = float(input("Digite o preço original R$....:"))
desconto = float(input("Percentual de desconto (%)")) 
preco_final, valor_desconto = calcular_desconto(preco, desconto)

print(f"Desconto aplicado...R${valor_desconto:2f}")
print(f"Preço final com desconto...R${preco_final:.2f}")

