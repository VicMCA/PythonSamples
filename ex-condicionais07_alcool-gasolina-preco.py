def main():
    '''
    Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    
    a. Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    
    b. Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de
    combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule
    e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
    da gasolina é 2.50 o preço do litro do álcool é 1,90.
    '''
    combustivel = str(input('Bom dia! Qual o tipo de combustível? Digite "a" para álcool, "g" para gasolina: '))
    combustivel = combustivel.lower()
    
    while combustivel != 'a' and combustivel != 'g':
        combustivel = str(input('Opa, não reconheço esse tipo. Informe novamente por favor: '))
        combustivel = combustivel.lower()
    
    litros = float(input('Quantos litros vai querer? '))
    
    while litros < 1:
        litros = float(input('Desculpe, mas essa quantidade não vale. Diz de novo quantos litros deseja: '))
    
    if combustivel == 'g' and litros < 21:
        preco = (litros * 2.5) * 0.96
    elif combustivel == 'g' and litros > 20:
        preco = (litros * 2.5) * 0.94
    elif combustivel == 'a' and litros < 21:
        preco = (litros * 1.9) * 0.97
    elif combustivel == 'a' and litros > 21:
        preco = (litros * 1.9) * 0.95
    
    print(f'O total deu R$ {round(preco, 2)}. Vou pedir para trazerem a maquineta!')


if __name__ == '__main__':
    main()