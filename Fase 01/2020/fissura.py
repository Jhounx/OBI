# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/fissura/

# acima, abaixou, esquerda ou direita tem que ter sido ocupado para que haja a possibilidade daquele lugar ser invadido
matriz = []


def main():
    global matriz
    tamanho, forca = [int(x) for x in input().split(" ")]
    matriz = []
    bomb_positions = []
    for _ in range(tamanho):
        matriz.append(list(input()))

    if (int(matriz[0][0]) < forca):
        matriz[0][0] = '*'
        bomb_positions.append([0, 0])
    else:
        return

    for indexLinha, indexCaractere in bomb_positions:
        if (indexLinha != 0 and
            matriz[indexLinha-1][indexCaractere] != "*" and
                int(matriz[indexLinha-1][indexCaractere]) <= forca):
            matriz[indexLinha-1][indexCaractere] = "*"
            bomb_positions.append([indexLinha-1, indexCaractere])

        if (indexLinha != (tamanho-1) and
            matriz[indexLinha+1][indexCaractere] != "*" and
                int(matriz[indexLinha+1][indexCaractere]) <= forca):
            matriz[indexLinha+1][indexCaractere] = "*"
            bomb_positions.append([indexLinha+1, indexCaractere])

        if (indexCaractere != 0 and
            matriz[indexLinha][indexCaractere - 1] != "*" and
                int(matriz[indexLinha][indexCaractere - 1]) <= forca):
            matriz[indexLinha][indexCaractere - 1] = "*"
            bomb_positions.append([indexLinha, indexCaractere - 1])

        if (indexCaractere != (tamanho - 1) and
            matriz[indexLinha][indexCaractere + 1] != "*" and
                int(matriz[indexLinha][indexCaractere + 1]) <= forca):
            matriz[indexLinha][indexCaractere + 1] = "*"
            bomb_positions.append([indexLinha, indexCaractere + 1])


if __name__ == "__main__":
    main()
    for linha in matriz:
        print(''.join(linha))
