def main():
    '''
    Faça um programa que leia dez conjuntos de dois valores, o primeiro representando 
    o número do aluno e o segundo representando a sua altura em centímetros. Encontre 
    o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número 
    do aluno mais baixo, junto com suas alturas.
    '''
    alunos = []
    alturas = []

    for x in range(10):
        alunos.append(input('Diga o nome do(a) aluno(a): '))
        alturas.append(float(input('Digite a altura do(a) aluno(a) em cm:')))

    index = alturas.index(max(alturas))
    print(f'A pessoa mais alta da sala é {alunos[index]} com {alturas[index]}')
    index = alturas.index(min(alturas))
    print(f'A pessoa mais alta da sala é {alunos[index]} com {alturas[index]}')


if __name__ == '__main__':
    main()