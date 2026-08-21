# DICIONÁRIOS — equivalente ao objeto do JS ({ chave: valor })
#
# A sintaxe até parece: {chave: valor} nos dois. A diferença é que em
# Python o acesso é sempre com colchetes e a chave entre aspas
# (dicionario["chave"]), enquanto em JS o mais comum é o ponto
# (objeto.chave), embora colchetes também funcionem lá.
#
# É a estrutura usada mais pra frente no projeto Sabor Express para
# representar cada restaurante antes de virar classe.

restaurante = {
    "nome": "Praça",
    "categoria": "Japonesa",
    "ativo": False,
}

# Acessando um valor pela chave (não pelo índice numérico como na lista)
print(restaurante["nome"])
print(restaurante["categoria"])

# Alterando um valor existente
restaurante["ativo"] = True
print(restaurante)

# Lista de dicionários — vários restaurantes, cada um com seus próprios dados.
# Em JS seria um array de objetos: mesma estrutura, chaves sem aspas.
restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
    {"nome": "Pizza Suprema", "categoria": "Pizza", "ativo": True},
    {"nome": "Cantina", "categoria": "Italiano", "ativo": False},
]

for r in restaurantes:
    status = "ativado" if r["ativo"] else "desativado"
    print(f"{r['nome']} ({r['categoria']}) — {status}")

# .get() é uma forma segura de acessar uma chave que pode não existir —
# em vez de dar erro, retorna um valor padrão.
# Diferença importante: em Python, acessar uma chave inexistente com []
# (ex: restaurante["telefone"]) gera KeyError. Em JS o mesmo acesso
# (objeto.telefone) simplesmente retorna undefined, sem erro.
# O ?? do JS (objeto.telefone ?? "não cadastrado") é o equivalente do .get() daqui.
telefone = restaurante.get("telefone", "não cadastrado")
print(f"Telefone: {telefone}")
