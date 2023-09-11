def main():
    '''
    Faça um programa para a leitura de duas notas parciais de um aluno. 
    O programa deve calcular a média alcançada por aluno e apresentar:
    1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    2. A mensagem "Reprovado", se a média for menor do que sete;
    3. A mensagem "Aprovado com Distinção", se a média for igual a dez
    '''
    nota1 = float(input('Informe a primeira nota do aluno: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Nota inválida. Informe a primeira nota do aluno: '))
    nota2 = float(input('Informe a segunda nota do aluno: '))
    while nota2 < 0 or nota1 > 10:
        nota2 = float(input('Nota inválida. Informe a primeira nota do aluno: '))

    media = (nota1 + nota2) /2
    
    if 10 > media >= 7:
        print("Aprovado.")
    elif media == 10:
        print('Aprovado com Distinção.')
    else:
        print('Reprovado.')


if __name__ == '__main__':
    main()