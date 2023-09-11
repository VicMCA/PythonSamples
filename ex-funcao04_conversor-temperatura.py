def main():
    '''
    Implemente um programa que possa receber do usuário a temperatura em 
    graus Celsius ou Fahrenheit. Antes de receber a temperatura, pergunte 
    ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. Se a 
    entrada for em graus Celsius, o programa deverá retornar a temperatura 
    em Fahrenheit. Se a entrada for em Fahrenheit, o programa deverá 
    retornar a temperatura em Celsius.
    F = C x 1,8 + 32
    '''
    print('Olá, este é um conversor de temperatura, entre Celsius e Fahrenheit.')
    escolha = int(input('Digite "1" para entrar uma temperatura em Celsius, "2" para Fahrenheit, "0" para sair: '))

    while escolha != 1 and escolha != 2 and escolha != 0:
        escolha = int(input('Opção inválida. Digite novamente, entre "1", "2" ou "0": '))
    
    if escolha == 0:
        print('Programa encerrado.')
    elif escolha == 1:
        temperatura = float(input('Informe a temperatura em Celsius: '))
        print(f'A temperatura em Fahrenheit é de {celsius_to_fahr(temperatura)}\nPrograma encerrado.')
    elif escolha == 2:
        temperatura = float(input('Informe a temperatura em Fahrenheit: '))
        print(f'A temperatura em Fahrenheit é de {fahr_to_cel(temperatura)}\nPrograma encerrado.')


def celsius_to_fahr(temp):
    ctf = round(((temp * 1.8) + 32), 2)
    return ctf


def fahr_to_cel(temp):
    ftc = round((5 * ((temp - 32)) / 9), 2)
    return ftc


if __name__ == '__main__':
    main()