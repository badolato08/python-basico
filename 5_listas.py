# Lista (equivalente ao array do JS)
frutas = ["Maçã", "Banana", "Uva"]

# enumerate() gera (índice, valor) a cada volta — equivalente ao
# .entries() do JS, usado em "for (const [indice, fruta] of frutas.entries())"
for indice, fruta in enumerate(frutas):
    print(f"Posição {indice}: {fruta}")

print()

# Matriz (lista de listas) com pilotos de F1
matriz = [
    ["Lando Norris", "Oscar Piastri", "Max Verstappen"],
    ["Charles Leclerc", "Lewis Hamilton", "George Russell"],
    ["Fernando Alonso", "Carlos Sainz", "Ayrton Senna"],
]

# 1ª saída: exibindo a matriz normalmente
for linha in matriz:
    for piloto in linha:
        print(piloto, end=" | ")
    print()

print()

# 2ª saída: exibindo a posição de cada linha
# for indice, linha in enumerate(matriz):
#     print(f"Posição {indice}: ", end="")
#     for piloto in linha:
#         print(piloto, end=" | ")
#     print()

# Python resolve com list comprehension o que o JS faz com .map()/.filter()
numeros = [1, 2, 3, 4, 5]

dobrados = [n * 2 for n in numeros]   # equivalente a numeros.map(n => n * 2)
print(dobrados)  # [2, 4, 6, 8, 10]

pares = [n for n in numeros if n % 2 == 0]  # equivalente a numeros.filter(n => n % 2 === 0)
print(pares)  # [2, 4]
