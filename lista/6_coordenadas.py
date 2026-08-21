# Pratica tuplas — em JS os pontos seriam arrays comuns ([0, 0], [3, 4]),
# sem garantia de imutabilidade real (Object.freeze() não impede erro,
# só ignora silenciosamente a tentativa de alteração).
#
# Calcula a distância entre dois pontos num plano cartesiano.
# Cada ponto é uma tupla (x, y) — os dois valores sempre andam juntos
# e não faz sentido alterar só um deles depois de criado.

import math

ponto_a = (0, 0)
ponto_b = (3, 4)


def calcular_distancia(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1  # desempacotamento de tupla — equivalente ao destructuring do JS
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


distancia = calcular_distancia(ponto_a, ponto_b)

print(f"Ponto A: {ponto_a}")
print(f"Ponto B: {ponto_b}")
print(f"Distância entre os pontos: {distancia}")
