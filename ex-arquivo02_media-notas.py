def main():
    '''
    Crie um programa que registra as notas de uma pessoa na escola 
    (como o boletim) em um arquivo. Em seguida, leia todos os 
    valores para imprimir o menor valor, o maior e a média.
    Dica: Se você usar listas, pode usar as funções min() e max().
    '''
    lista_notas = []

    quant_notas = int(input('Quantas notas deseja informar para a média? '))

    for x in range(0, quant_notas):
        nota = float(input(f'Informe a {x+1}ª nota: '))
        lista_notas.append(nota)

    with open('notas.txt', 'w') as notas:
      for nota in lista_notas:
        notas.write(str(nota)+'\n')

    with open('notas.txt') as notas:
        lista_notas2 = []
        for x in notas:
            lista_notas2.append(float(x))

        print(lista_notas2)
        print(min(lista_notas2))
        print(max(lista_notas2))
        print(round(sum(lista_notas2)/len(lista_notas2), 2)) # Dessa forma não precisa criar a variável "total"


if __name__ == '__main__':
    main()