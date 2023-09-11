def main():
    '''
    Faça um programa para o cálculo de uma folha de pagamento, sabendo que os 
    descontos são do Imposto de Renda, que depende do salário bruto (conforme
    tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
    Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário
    Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá
    pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
        1. Salário Bruto até 900 (inclusive) - isento
        2. Salário Bruto até 1500 (inclusive) - desconto de 5%
        3. Salário Bruto até 2500 (inclusive) - desconto de 10%
        4. Salário Bruto acima de 2500 - desconto de 20%
    
    Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        A. Salário Bruto: (5 * 220)        : R$ 1100,00
        B. (-) IR (5%)                     : R$   55,00  
        C. (-) INSS ( 10%)                 : R$  110,00
        D. FGTS (11%)                      : R$  121,00
        E. Total de descontos              : R$  165,00
        F. Salário Liquido                 : R$  935,00

    '''
    print('Bem vindo(a).  Para o cálculo de sua folha de pagamento para este mês, por favor informe:')
    trab_horas = int(input('Quantidade de horas trabalhadas >> '))
    trab_custo = int(input('Valor da sua hora de trabalho >> R$ '))

    sal_bruto = trab_horas * trab_custo
    desc_INSS = sal_bruto * 0.10
    desc_sind = sal_bruto * 0.03
    bonus_FGTS = sal_bruto * 0.11
    
    if sal_bruto <= 900: desc_IR = 0
    if sal_bruto <= 900: perc_IR = 'ISENTO'
    if 900 < sal_bruto <= 1500: desc_IR = sal_bruto * 0.05
    if 900 < sal_bruto <= 1500: perc_IR = ' 5% = '
    if 1500 < sal_bruto <= 2500: desc_IR = sal_bruto * 0.1
    if 1500 < sal_bruto <= 2500: perc_IR = '10% = '
    if 2500 < sal_bruto: desc_IR = sal_bruto * 0.2
    if 2500 < sal_bruto: perc_IR = '20% = '
    
    total_desc = desc_INSS + desc_IR
    sal_liqui = sal_bruto - total_desc

    resultado = (f'''Salário Bruto = R$ {sal_bruto}
    Desconto do IR: {perc_IR}{desc_IR}
    Desconto do INSS: 10% = {desc_INSS}
    Taxa do Sindicato: 3% = {desc_sind}
    Bônus do FGTS: 11% = {bonus_FGTS}
    Total de descontos = R$ {total_desc}
    Salário Líquido = R$ {sal_liqui}''')

    print(resultado.replace('    ', ''))


if __name__ == '__main__':
    main()