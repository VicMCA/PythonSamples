def main():
    '''
    Crie um programa que tenha uma função que receba uma lista de 
    números inteiros e exiba todos os valores multiplicados por 
    um valor inserido pelo usuário.
    '''
    lista_num =  [4, 2, 12, 98, 8096, 2, 124, -123, -481, 23]

    def mult_lista(lista, mult):
        lista_res = []
        for x in lista:
            lista_res.append(x * mult)
        return lista_res


    mult = int(input('Informe um valor: '))

    print(mult_lista(lista_num, mult))


if __name__ == '__main__':
    main()