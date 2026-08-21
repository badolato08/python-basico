notas = [
    [9.5, 5.8, 8.6],  #aluno 1
    [5.0, 9.0, 3.0],  #aluno 2
    [8.0, 9.0, 10.0], #aluno 3
    [2.0, 6.0, 9.0],  #aluno 4
    [7.0, 7.0, 7,0]   #aluno 5
]

maior_media = 0
for i, aluno in enumerate(notas):
    media = sum(aluno) / len(aluno)
    print(f"Aluno {i + 1}: Média = {media:.2f}")
    if media > maior_media:
        maior_media = media

print(f"A maior média da sala é: {maior_media:.2f} do aluno {notas.index(max(notas, key=lambda x: sum(x)/len(x))) + 1}")

media_sala = sum(sum(aluno) for aluno in notas) / (len(notas) * len(notas[0]))
print(f"A média da sala é: {media_sala:.2f}")