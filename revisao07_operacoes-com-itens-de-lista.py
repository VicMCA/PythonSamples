def main():
    '''
    Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
    '''
    nums = []
    x = 0

    while x < 5:
        nums.append(int(input('Informe um número inteiro: ')))
        x += 1

    mult = 1
    soma = 0

    for n in nums:
        mult *= n
        soma += n

    print(f'Soma = {soma}')
    print(f'Multiplicação = {mult}')
    print(f'Lista de números usados = {nums}')


if __name__ == '__main__':
    main()