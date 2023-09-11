def main():
    '''
    Faça um programa que calcule as raízes de uma equação do segundo grau, na
    forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
    as consistências, informando ao usuário nas seguintes situações:
      a- Se o usuário informar o valor de A igual a zero, a equação não é do segundo
      grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
      b- Se o delta calculado for negativo, a equação não possui raizes reais.
      Informeao usuário e encerre o programa;
        c- Se o delta calculado for igual a zero a equação possui apenas uma
        raiz real; informe-a ao usuário;
        d- Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
    '''
    a, b, c = [float(x) for x in input('Informe 3 números para realizarmos uma equação do segundo grau: ').split()]

    delta = b**2 - (4*a*c)
    
    x_pos = (-b + (delta ** 1/2)) / (2 * a)
    x_neg = (-b - (delta ** 1/2)) / (2 * a)
    
    if a == 0:
        print('Esta equação é do primeiro grau e não será computada.')
    else: 
        if delta < 0:
            print('O valor do delta é negativo, portanto o resultado não possui raízes reais.')
        elif delta == 0:
            print('O delta resulta em zero, e há apenas uma raíz real.')
            print(f'A raíz é de {-b / (2 * a)}')
        else:
            print(f'As duas raízes são {round(x_pos, 2)} e {round(x_neg, 2)}')


if __name__ == '__main__':
    main()