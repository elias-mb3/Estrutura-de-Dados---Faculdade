def ordenar_pontuacoes(lista):
    for i in range(len(lista)):
        indice_max = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[indice_max]:
                indice_max = j
        lista[i], lista[indice_max] = lista[indice_max], lista[i]

pontuacoes = [350, 120, 550, 280, 420]
ordenar_pontuacoes(pontuacoes)

print("Ranking de Pontuações: ")
for i, pontuacao in enumerate(pontuacoes, start=1):
    print(f"{i}. Pontuação: {pontuacao}")
