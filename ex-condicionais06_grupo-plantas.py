def main():
    '''
    Construa uma pequena chave dicotômica para identificar uma determinada
    planta como membro de um dos principais grupos: Bryophyta, Pteridophyta,
    Gymnospermae ou Angiospermae. A identificação se dá com base na presença
    (1) ou ausência (0) de três caracteres: vascularização, sementes e flores.
    Utilize a tabela abaixo como referência.

    Grupo 	    Vascularização 	Sementes 	Flores
    Bryophyta       	0        	0       	0
    Pteridophyta 	    1        	0       	0
    Gymnospermae 	    1        	1       	0
    Angiospermae 	    1        	1       	1
    '''
    # Estas variáveis armazenam a presença (1) ou ausência (0) de cada caractere
    vasc = 0
    sem = 0
    flor = 0
    
    # Seu código aqui
    print('Para identificarmos o grupo ao qual a planta pertence, precisarei que informe 3 características.')
    resp = str(input('Ela possui vascularização? s/n > '))
    resp = resp.lower()
    if resp == 's':
        vasc = 1
    
    resp == ''
    resp = str(input('Ela gera sementes? s/n > '))
    resp = resp.lower()
    if resp == 's':
        sem = 1
    
    resp == ''
    resp = str(input('Ela gera flores? s/n > '))
    resp = resp.lower()
    if resp == 's':
        flor = 1
    
    if vasc == sem == flor == 0:
        print('A planta pertence ao grupo Bryophyta.')
    elif vasc == 1 and sem == flor == 0:
        print('A planta pertence ao grupo Pteridophyta.')
    elif vasc == sem == 1 and flor == 0:
        print('A planta pertence ao grupo Gymnospermae.')
    else:
        print('A planta pertence ao grupo Angiospermae.')
    

if __name__ == '__main__':
    main()