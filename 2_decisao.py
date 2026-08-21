# Classifica uma nota
# Repare: Python não usa parênteses na condição nem chaves {} no bloco,
# como o JS faz (if (nota >= 7) { ... }) — usa só ":" e indentação.
# O "else if" (duas palavras) do JS vira "elif" (uma palavra) em Python.

nota = 7.5

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
