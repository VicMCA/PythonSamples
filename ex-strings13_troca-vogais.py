def main():
    '''
    Faça um programa que receba uma palavra e calcule quantas vogais
    (a, e, i, o, u) possui essa palavra. Entre com um caractere (vogal
    ou consoante) e substitua todas as vogais da palavra dada por
    esse caractere.
    '''
    vogais = ['a', 'à', 'á', 'ã', 'â', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú']

    palavra = input('Olá, me informe uma palavra qualquer por favor: ')
    palavra = palavra.lower()
    letra = input('Agora me informe uma letra qualquer: ')
    letra = letra.lower()
    print('Você caiu no meu truque nefasto! Trocarei todas as vogais da palavra pela letra informada!')
    print('hahaHAhaHAHAHAHAHAHAHAHAHAhaHAhaha*cof*ha*cof-cof*')

    for x in palavra:
        for y in vogais:
            palavra = palavra.replace(y, letra)
    print(palavra)


if __name__ == '__main__':
    main()