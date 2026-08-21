# Função simples com retorno
# Os tipos vêm depois de ":" e o tipo de retorno depois de "->".
# JS puro não tem essa anotação de tipos (só existe com TypeScript,
# uma linguagem separada por cima do JS).
def somar(a: int, b: int) -> int:
    return a + b


print(somar(4, 6))  # 10


# Função com parâmetro obrigatório
def saudacao(nome: str):
    print(f"Olá, {nome}! Bem-vindo ao Python.")


saudacao("Júlia")
saudacao("Maria")


# Função com valor padrão — em JS seria: function saudacaoComPadrao(nome = "visitante")
def saudacao_com_padrao(nome: str = "visitante"):
    print(f"Olá, {nome}!")


saudacao_com_padrao()          # usa o padrão: "Olá, visitante!"
saudacao_com_padrao("Pedro")   # usa o valor passado: "Olá, Pedro!"


# Procedimento (função sem retorno, só executa uma ação)
# Em Python, uma função sem "return" devolve None automaticamente
# (em JS, o equivalente seria undefined)
def mostrar_linha():
    print("------------------")


mostrar_linha()

# Python não tem uma sintaxe curta equivalente à arrow function do JS
# ((a, b) => a + b) para funções com várias linhas — mas para expressões
# de uma linha só, existe o lambda, mais limitado:
somar_lambda = lambda a, b: a + b
print(somar_lambda(4, 6))  # 10
