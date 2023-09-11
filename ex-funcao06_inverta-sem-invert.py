def main():
    '''
    Crie um programa que tenha uma função que receba uma lista de
    números inteiros e exiba todos os seus valores em ordem invertida.
    Obs.: Sem usar invert ou o fatiador com passo -1.
    '''
    l = [1, 2, 3]

    def reverse(lista):
        lista_aux = []
        for x in lista:
            lista_aux.insert(0, x)
        return lista_aux
    
    print(reverse(l))
    
    lista = [1,2,3,4,5]
    v = list(range(-len(lista),0))
    for x in v:
        print(lista[(x*-1)-1])


if __name__ == '__main__':
    main()