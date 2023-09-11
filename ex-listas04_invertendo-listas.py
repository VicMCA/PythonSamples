def main():
    '''    
    Escrever um programa em Python que leia um vetor V1 de n posições e gere:
    a) Um vetor V2 de tamanho n que é o vetor V1 invertido.
    b) Um vetor V3 cujo tamanho seja o número correspondente aos dígitos invertidos
    do tamanho do vetor V1. (ex: V1 com 12 elementos, V3 com 21 elementos)
    '''
    quant_itens = int(input('Quantos itens a lista V1 deve ter? '))

    V1 = list(range(0, quant_itens))
    print(f'Primeiro vetor "V1": {V1}')
    V2 = V1[:]
    V2.reverse()
    print(f'Segundo vetor "V2": {V2}')

    tamV1 = len(V1)
    tamV1 = str(tamV1)
    tamV1 = tamV1[::-1]
    tamV1 = int(tamV1)

    V3 = list(range(0, tamV1))
    print(f'Terceiro vetor "V3": {V3}')


if __name__ == '__main__':
    main()