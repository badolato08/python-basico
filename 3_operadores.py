# Verifica se pode tirar carteira de motorista
# Operadores lógicos em Python são escritos por extenso: and, or, not
# (em JS são &&, ||, !)

# 🐍 Snake Case (tem_documento)Como funciona: Todas as letras ficam em minúsculo e as palavras são separadas por um sublinhado (_).Uso no Python: É o padrão oficial do Python (definido na PEP 8) para nomear variáveis, funções, métodos e atributos. Em JS é usado 🐫 CamelCase (temDocumento).
idade = 19
tem_documento = True  # Booleanos em Python começam com maiúscula: True / False
# (em JS são minúsculos: true / false)

if idade >= 18 and tem_documento:
    print("Pode tirar a carteira")
else:
    print("Não pode tirar a carteira")

# Exemplo com OU (or) e negação (not)
feriado = False
fim_de_semana = True

if feriado or fim_de_semana:
    print("\nHoje não tem aula")

if not feriado:
    print("Não é feriado")

# Verifica se o aluno está presente
presente = False

if not presente:
    print("O aluno está ausente.")
else:
    print("O aluno está presente.")

# Ponto sem equivalente em Python: JS tem == (comparação "frouxa", convertendo
# tipos) e === (comparação "estrita", sem converter). Python só tem um jeito
# de comparar, ==, e ele já se comporta como o === do JS — não converte tipos.
print(0 == "0")  # False em Python (em JS, 0 == "0" seria True — cuidado lá)
