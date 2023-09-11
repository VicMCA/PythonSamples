def main():
    '''
    Faça um programa que lê as duas notas parciais obtidas por um aluno
    numa disciplina ao longo de um semestre, e calcule a sua média.
    A atribuição de conceitos obedece à tabela abaixo:
        1. Média de Aproveitamento  Conceito
        2. Entre 9.0 e 10.0        A
        3. Entre 7.5 e 9.0         B
        4. Entre 6.0 e 7.5         C
        5. Entre 4.0 e 6.0         D
        6. Entre 4.0 e zero        E
    O algoritmo deve mostrar na tela as notas, a média, o conceito 
    correspondentee a mensagem “APROVADO” se o conceito for 
    A, B ou C ou “REPROVADO” se o conceito for D ou E.
    '''
    print('Olá, vamos calcular as notas parciais do aluno e seu conceito.')
    nota1 = float(input('Informe a primeira nota parcial >> '))
    while nota1 < 0 and nota1 > 10:
        nota1 = float(input('Valor inválido. Informe a primeira nota parcial >> '))
    nota2 = float(input('Informe a segunda nota parcial >> '))
    while nota2 < 0 and nota2 > 10:
        nota2 = float(input('Valor inválido. Informe a segunda nota parcial >> '))

    media = (nota1 + nota2) / 2

    if 10 >= media >= 9: conceito = 'A'
    if 9 > media >= 7.5: conceito = 'B'
    if 7.5 > media >= 6: conceito = 'C'
    if 6 > media >= 4.0: conceito = 'D'
    if 4.0 > media >= 0: conceito = 'E'
    if (conceito == 'A') or (conceito == 'B') or (conceito == 'C'): prefixo = 'A'
    if (conceito == 'D') or (conceito == 'E'): prefixo = 'RE'

    resultado = (f'''As notas parciais do aluno foram: {nota1} e {nota2}
    Sua média foi de: {media}
    O conceito deste aluno foi: {conceito}
    O referido aluno está {prefixo}PROVADO.''')

    print(resultado.replace('    ', ''))
    

if __name__ == '__main__':
    main()