# Lê dois números e mostra a soma
# Em Python não é preciso declarar a variável com let/const/var como em JS
# — basta atribuir (a = 5) que ela já existe.

a = 5
b = 3
soma = a + b

# f-string: forma moderna de inserir variáveis dentro de um texto
# equivalente à template string do JS: `A soma de ${a} e ${b} é: ${soma}`
print(f"A soma de {a} e {b} é: {soma}")

# Bônus: em Python, uma variável pode trocar de tipo livremente
# (isso é chamado de tipagem dinâmica — igual ao "let" do JS, sem
# equivalente ao "const", já que Python não trava reatribuição de variável)
a = "agora sou um texto"
print(a)
