def main():
    '''    
    A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em 
    disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador 
    de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários 
    com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu 
    gerar o seguinte arquivo, chamado "usuarios.txt":

      alexandre       456123789
      anderson        1245698456
      antonio         123456456
      carlos          91257581
      cesar           987458
      rosemary        789456125

    Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você 
    deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

    ACME Inc.       Uso do espaço em disco pelos usuários
     
    Nr.  Usuário        Espaço utilizado     % do uso
     
    1    alexandre       434,99 MB             16,85%
    2    anderson       1187,99 MB             46,02%
    3    antonio         117,73 MB              4,56%
    4    carlos           87,03 MB              3,37%
    5    cesar             0,94 MB              0,04%w
    6    rosemary        752,88 MB             29,16%
     
    Espaço total ocupado: 2581,57 MB
    Espaço médio ocupado: 430,26 MB

    O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso 
    sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado 
    em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será 
    chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito 
    através de uma função, que será chamada pelo programa principal.
    '''
    with open('usuarios.txt', 'w') as usuarios:
        usuarios.write('alexandre       456123789\n')
        usuarios.write('anderson        1245698456\n')
        usuarios.write('antonio         123456456\n')
        usuarios.write('carlos          91257581\n')
        usuarios.write('cesar           987458\n')
        usuarios.write('rosemary        789456125')
    
    usuarios_nome = []
    usuarios_quota_bytes = []
    usuarios_quota_mb = []
    usuarios_quota_percentual = []

    with open('usuarios.txt', 'r') as usuarios:
        users = usuarios.readlines()
        split_list(users)
        usuarios_nome, usuarios_quota_bytes = split_list(users)
        usuarios_quota_mb = byte_conversion(usuarios_quota_bytes)
        usuarios_quota_percentual = percentual_quota(usuarios_quota_mb)

    texto_relatorio = ('ACME Inc.       Uso do espaço em disco pelos usuários\n\n'
    + 'Nr.\tUsuário\t\tEspaço utilizado\t'+'%'+' do uso\n\n'
    + f'1\t{usuarios_nome[0]}\t{usuarios_quota_mb[0]}MB\t\t{usuarios_quota_percentual[0]}%\n'
    + f'2\t{usuarios_nome[1]}\t{usuarios_quota_mb[1]}MB\t\t{usuarios_quota_percentual[1]}%\n'
    + f'3\t{usuarios_nome[2]}\t\t{usuarios_quota_mb[2]}MB\t\t{usuarios_quota_percentual[2]}%\n'
    + f'4\t{usuarios_nome[3]}\t\t{usuarios_quota_mb[3]}MB\t\t\t{usuarios_quota_percentual[3]}%\n'
    + f'5\t{usuarios_nome[4]}\t\t{usuarios_quota_mb[4]}MB\t\t\t{usuarios_quota_percentual[4]}%\n'
    + f'6\t{usuarios_nome[5]}\t{usuarios_quota_mb[5]}MB\t\t{usuarios_quota_percentual[5]}%\n')

    with open('relatorio.txt', 'w') as relatorio:
            relatorio.write(texto_relatorio)
            
            
def split_list(lista):
    
    names = []
    disk_quota = []
    
    for x in lista:
        name, quota = x.split()
        names.append(name)
        disk_quota.append(quota)
    
    return names, disk_quota


def byte_conversion(lista):
    
    lista = [round(int(x) / (1024 ** 2), 2) for x in lista]

    return lista


def percentual_quota(lista_quotas):
    lista_quotas = [round(((x * 100) / sum(lista_quotas)), 2) for x in lista_quotas]
    return lista_quotas


if __name__ == '__main__':
    main()