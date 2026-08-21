def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


# Programa principal
peso = 70
altura = 1.75

imc = calcular_imc(peso, altura)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")