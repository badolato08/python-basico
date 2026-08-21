# FOR — tabuada do 5
# Python não usa o for de 3 blocos do JS (for (let i = 1; i <= 10; i++)).
# range(1, 11) gera os números de 1 até 10 (o último número nunca é incluído)
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

print()

# WHILE — contagem regressiva
n = 5
while n > 0:
    print(n)
    n -= 1  # Python não tem n-- como o JS, o jeito certo é n -= 1

print()

# DO WHILE — diferença real entre as linguagens: JS tem essa estrutura pronta
# (do { ... } while (condição)), Python não tem.
# O jeito de simular "executa pelo menos uma vez, depois checa a condição"
# é com while True + um if...break no final do bloco.
x = 0
while True:
    print(f"x vale {x}")
    x += 1
    if x > 10:
        break
