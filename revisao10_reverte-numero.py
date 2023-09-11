def main():
    '''
    Reverso do número. Faça uma função que retorne o reverso de 
    um número inteiro informado. Por exemplo: 127 -> 721.
    '''
    x = (int(input('Informe um número inteiro: ')))

    print(f'Invertido fica: {reverte(x)}')


def reverte(a):
    z = str(a)
    return int(z[::-1])


if __name__ == '__main__':
    main()