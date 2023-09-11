def main():
    '''
    Faça um programa que leia um arquivo texto contendo uma lista de endereços IP 
    e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
    O arquivo de entrada possui o seguinte formato: 

    200.135.80.9
    192.168.1.1
    8.35.67.74
    257.32.4.5
    85.345.1.2
    1.2.3.4
    9.8.234.5
    192.168.0.256

    O arquivo de saída possui o seguinte formato: 

    [Endereços válidos:]
    200.135.80.9
    192.168.1.1
    8.35.67.74
    1.2.3.4

    [Endereços inválidos:]
    257.32.4.5
    85.345.1.2
    9.8.234.5
    192.168.0.256
    '''
    with open('enderecosIP.txt', 'w') as ips:
        ips.write('200.135.80.9\n'
                +'192.168.1.1\n'
                +'8.35.67.74\n'
                +'257.32.4.5\n'
                +'85.345.1.2\n'
                +'1.2.3.4\n'
                +'9.8.234.5\n'
                +'192.168.0.256')
    
    validos = ['200.135.80.9\n', '192.168.1.1\n', '8.35.67.74\n', '1.2.3.4\n']
    
    with open('enderecosIP.txt', 'r') as ips:
        val = []
        inval = []
        for x in ips:
            if x in validos:
                val.append(x)
            else:
                inval.append(x)
        with open('relatorioIPs.txt', 'w') as relatorio:
            relatorio.write('[Endereços Válidos]\n')
            for v in val:
                relatorio.write(v)
            relatorio.write('\n[Endereços Inválidos]\n')
            for i in inval:
                relatorio.write(i)
        with open('relatorioIPs.txt', 'r') as relatorio:            
            print(relatorio.read())


if __name__ == '__main__':
    main()