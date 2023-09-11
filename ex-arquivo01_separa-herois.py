import os

def main():
    '''
    Aumente a lista de heróis no arquivo herois.txt. Feito isso, crie 
    um programa que leia esse arquivo e crie dois novos arquivos:
    1. Um arquivo apenas com heróis da Marvel;
    2. Outro apenas com heróis da DC.
    '''
    with open('heroisDC.txt', 'w') as dc:
        with open('heroisMarvel.txt', 'w') as marvel:
            with open('CesarSchool/auxFiles/herois.txt', 'r') as arquivo:
                for linha in arquivo:
                    if 'DC' in linha:
                        dc.write(linha)
                    else:
                        marvel.write(linha)

    with open('heroisDC.txt', 'r') as dc:
        print(dc.read())
    with open('heroisMarvel.txt', 'r') as marvel:
        print(marvel.read())


if __name__ == '__main__':
    main()