def main():
    '''
    As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento 
    ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver 
    a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
    Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes 
    do sindicato laboral, chegou-se a seguinte forma de cálculo: 
    
    a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
        a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito 
        baixo, recebem este valor mínimo; 
        
    Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, 
    descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do 
    salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 
    (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular 
    o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, 
    o programa deverá apresentar:
        1. O salário de cada funcionário, juntamente com o valor do abono;
        2. O número total de funcionário processados;
        3. O valor total a ser gasto com o pagamento do abono;
        4. O número de funcionário que receberá o valor mínimo de 100 reais;
        5. O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, 
           apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa. 

    Projeção de Gastos com Abono
    ============================ 
    
    Salário: 1000
    Salário: 300
    Salário: 500
    Salário: 100
    Salário: 4500
    Salário: 0
    
    Salário    - Abono     
    R$ 1000.00 - R$  200.00
    R$  300.00 - R$  100.00
    R$  500.00 - R$  100.00
    R$  100.00 - R$  100.00
    R$ 4500.00 - R$  900.00
    
    Foram processados 5 colaboradores
    Total gasto com abonos: R$ 1400.00
    Valor mínimo pago a 3 colaboradores
    Maior valor de abono pago: R$ 900.00
    '''
    valor = 1
    salariosBase = []
    salariosAbono = []

    while valor != 0:
        valor = float(input('Informe o salário do colaborador: R$ '))
        salariosBase.append(valor)
        salariosAbono.append(valor * 0.2 if (valor * 0.2) > 100 else 100.0)
        # salariosAbono.append(max([valor * 0.2, 100,0]))
    
    salariosBase.pop()
    salariosAbono.pop()
    print('\nProjeção de Gastos com Abono\n')

    for x in salariosBase:
        print(f'Salario: R$ {x}')
    
    print('\nSalários \t - \t Abono\n----------------------------------')

    for x in range(len(salariosBase)):
        print(f'R$ {salariosBase[x]} \t - \t R$ {salariosAbono[x]}')

    print(f'Foram processados {len(salariosBase)} colaboradores\n'
    +f'Total de gastos com abonos: R$ {sum(salariosAbono)}\n'
    +f'Valor mínimo pago a {calculaMinimo(salariosBase)} colaboradores\n'
    +f'Maior valor de abono pago: R$ {max(salariosAbono)}\n')


def calculaMinimo(lista):
    count = 0
    for x in lista:
        if x == 100:
            count += 1
    return count


if __name__ == '__main__':
    main()