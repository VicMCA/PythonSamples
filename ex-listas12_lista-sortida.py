def main():
    '''
    Faça um Programa que leia três números e mostre-os em ordem decrescente.
    '''
    print('Informe três números e os exibirei em ordem decrescente.')
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))
    num3 = float(input('Informe o terceiro número: '))

    sem_ordem = [num1, num2, num3]
    sem_ordem.sort(reverse = True)
    print(sem_ordem)
    

if __name__ == '__main__':
    main()