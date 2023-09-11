def main():
    '''
    Complete o código na célula abaixo para imprimir uma mensagem informando
    se um aluno foi aprovado ou reprovado em uma disciplina com base em sua
    nota final. A nota mínima necessária para aprovação é 5 .
    '''
    nota_aluno = float(input('Por favor, insira sua nota: ')) # insira aqui a nota do aluno
    
    # Complete o código abaixo
    if nota_aluno < 5:
        print("Infelizmente você não foi aprovado(a) nesta disciplina.")
    else:
        print("Parabéns! Você está aprovado(a)!")


if __name__ == '__main__':
    main()