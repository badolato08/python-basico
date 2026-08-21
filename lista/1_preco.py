#preço do produto
preco = 50.00 

quantidade = 7

valor_total = preco * quantidade

print(f"Valor total sem desconto: R${valor_total:.2f}")


if valor_total >= 200:
    desconto = valor_total * 0.10
    valor_total -= desconto

   
print(f"desconto aplicado: R${desconto:.2F}")
print(f"valor final: R${valor_total:.2F}")



