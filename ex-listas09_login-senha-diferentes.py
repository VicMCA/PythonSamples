def main():
    '''    
    Faça um programa que leia um nome de usuário e a sua senha e não
    aceite a senha igual ao nome do usuário, mostrando uma mensagem
    de erro e voltando a pedir as informações.
    '''
    nome = input('Informe seu nome de usuário: ')
    senha = input('Informe sua senha: ')
    while senha == nome:
        senha = input('Senha inválida, não pode ser igual ao nome. Informe novamente: ')
    else:
        print(f'Seu nome de usuário é {nome}. Sua senha é {senha}')


if __name__ == '__main__':
    main()