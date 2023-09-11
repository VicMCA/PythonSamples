def main():
    '''
    Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
    '''
    l = float(input('Informe por gentileza a lateral de um quadrado, que lhe informarei o dobro de sua área: '))
    print(f'O dobro da área do quadrado informado é de {2 * (l ** 2)} cm²')


if __name__ == '__main__':
    main()