# Pratica dicionário e lista de dicionários — em JS seria um array de
# objetos, exatamente o formato que uma query MySQL retorna no Node
# antes de virar dado renderizado. Serve como aquecimento direto para
# a lista de restaurantes do projeto Sabor Express.

produtos = [
    {"nome": "Notebook", "preco": 3500.00, "estoque": 5},
    {"nome": "Mouse", "preco": 45.00, "estoque": 20},
    {"nome": "Teclado", "preco": 120.00, "estoque": 0},
]

# .ljust() é o equivalente do .padEnd() do JS
print(f"{'Produto'.ljust(15)} | {'Preço'.ljust(10)} | Situação")

for produto in produtos:
    situacao = "disponível" if produto["estoque"] > 0 else "esgotado"
    preco_formatado = f"R$ {produto['preco']:.2f}"
    print(f"{produto['nome'].ljust(15)} | {preco_formatado.ljust(10)} | {situacao}")

# Soma o valor total em estoque — o generator dentro do sum() é o
# equivalente do produtos.reduce((total, p) => total + p.preco * p.estoque, 0) do JS
valor_total = sum(p["preco"] * p["estoque"] for p in produtos)
print(f"\nValor total em estoque: R$ {valor_total:.2f}")
