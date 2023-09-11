def main():
    '''    
    Faça um programa que recebe um número inteiro de 1 a 10 do usuário
    e imprime a tabuada de multiplicação desse número.
    '''
    num = int(input('Digite o número para o qual deseja ver a tabuada: '))
    for x in range(1, 11):
        print(f'{num} * {x} = {num * x}')


if __name__ == '__main__':
    main()