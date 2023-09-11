def main():
    '''    
    Faça um Programa que leia 2 números e em seguida pergunte ao usuário
    qual operação ele deseja realizar. O resultado da operação deve ser
    acompanhado de uma frase que diga se o número é:

    a. par ou ímpar;    
    b. positivo ou negativo;
    c. inteiro ou decimal.
    '''
    a, b = [float(x) for x in input('Por favor, informe dois números quaisquer separados por espaço: ').split()]
    print('''Confira a lista de possíveis operações aritméticas abaixo:
    [1] Adição
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Módulo
    [6] Exponenciação
    [7] Radiciação
    [0] Sair do programa''')
    operacao = int(input('''Considerando os números na ordem que foram informados, digite 
    o número correspondente à operação que deseja realizar >> '''))
    
    if 0 < operacao < 8:
        if operacao == 1: resultado = (a + b)
        if operacao == 2: resultado = (a - b)
        if operacao == 3: resultado = (a * b)
        if operacao == 4: resultado = (a / b)
        if operacao == 5: resultado = (a % b)
        if operacao == 6: resultado = (a ** b)
        if operacao == 7: resultado = (a ** 1/b)
    else:
        print('Muito bem. Até a próxima')
    
    pos = 'negativo' if 0 > resultado else 'positivo'
    par = 'par' if (resultado % 2 == 0) else 'ímpar'
    dec = 'inteiro' if (resultado % 1 == 0) else 'decimal'
    
    print(f'O resultado da operação escolhida com os números informados é {pos}, {par} e {dec}')


if __name__ == '__main__':
    main()