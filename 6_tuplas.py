# TUPLAS — conceito que não existe nativamente em JS
#
# Uma tupla é parecida com uma lista, mas é IMUTÁVEL: depois de criada,
# não dá para adicionar, remover ou alterar itens. Em JS, o mais próximo
# seria um array com Object.freeze() — mas lá a tentativa de alteração
# é simplesmente ignorada, sem erro. Em Python, ela SEMPRE gera erro.
#
# Use lista quando os dados podem mudar (ex: lista de restaurantes cadastrados).
# Use tupla quando os dados representam algo fixo, tipo um "pacote" de valores
# que sempre andam juntos (ex: uma coordenada, uma cor RGB, um par de notas).

# Criando uma tupla — geralmente com parênteses (mas eles são opcionais)
coordenada = (10, 20)
print(coordenada)
print(f"x = {coordenada[0]}, y = {coordenada[1]}")

# Tentar alterar um item de uma tupla gera erro de verdade — descomente para ver:
# coordenada[0] = 99   # TypeError: 'tuple' object does not support item assignment
# (em JS, o mesmo código com array + Object.freeze() NÃO geraria erro,
# só ignoraria a alteração silenciosamente — diferença importante)

# "Empacotamento e desempacotamento" — um dos usos mais comuns de tupla em Python.
# É bem parecido com o destructuring do JS: const [x, y] = coordenada;
x, y = coordenada
print(f"x separado: {x} | y separado: {y}")

# Uso comum: uma função pode "retornar mais de um valor" empacotando numa tupla.
# Em JS o padrão mais comum pra isso é retornar um objeto { quociente, resto }.
def dividir_com_resto(a, b):
    quociente = a // b   # divisão inteira
    resto = a % b        # resto da divisão
    return quociente, resto   # aqui está criando uma tupla (quociente, resto)


q, r = dividir_com_resto(17, 5)
print(f"17 ÷ 5 = {q} e sobra {r}")

# Lista de tuplas: um padrão muito comum, por exemplo para guardar
# pares de (nome, nota) sem risco de alguém alterar a nota por engano
# — em JS isso seria um array de arrays, sem a garantia de imutabilidade
alunos = [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.2)]

for nome, nota in alunos:
    print(f"{nome}: {nota}")
