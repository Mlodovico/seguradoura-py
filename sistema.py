"""
Sistema de seguro de carros básico desenvolvido

@author Murilo Lodovico
@version 0.1

"""


print('----------Seguro Veicular Muroguro----------')

print('Digite 1 (um) caso já é cliente,'
      'Digite 2 (doís) caso queira ser cliente,'
      'Digite 3 (três) caso queira fazer uso do serviço teste.')

Digito = int(input('Digíte qual valor será utilizado? '))

if Digito == 1:
    print('------------------------------------Login--------------------------------------')
    nome = input("Digite seu nome: ")
    senha = input("Digíte sua senha")
    print(f'Bem-vindo nomavente {nome}')
    print('---------------Obrigado por utilizar os serviços da Muroguro-------------------')


elif Digito == 2:
    print('---------------------------------Novo Cadastro---------------------------------')
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite sua idade? "))
    end = input("Endereço de onde mora: ")
    senha = input("Digite sua nova senha: ")
    print('-------------------------------------------------------------------------------')
    print(f'Parabéns {nome}, você está cadastrado na nossa seguradoura')
    print('---------------Obrigado por utilizar os serviços da Muroguro-------------------')


elif Digito == 3:
    print('--------------------------Serviço de seguro------------------------------------')
    nome = input("Digite seu nome? ")
    idade = int(input("Digite sua idade? "))
    end = input("Endereço de onde mora: ")
    marca = input("Digite a marca do carro ")
    modelo = input("Digite o modelo do carro: ")
    valorCarro = int(input("Digite o valor do carro: "))
    anoAtual = int(input("Digite o ano atual: "))

    if 18 <= idade < 24:
        valorSeguro = (valorCarro * 0.10)
        print(f'O seguro do carro {modelo}, marca {marca}, saira no valor de {valorSeguro}, '
              f'para a idade entre 18 - 24 anos do cliente, no ano de {anoAtual}')


    elif 24 <= idade < 32:
        valorSeguro = (valorCarro * 0.08)
        print(f'O seguro do carro {modelo}, marca {marca}, saira no valor de {valorSeguro},'
              f' para a idade entre 24 - 32 anos do cliente, no ano de {anoAtual}')


    elif 32 <= idade < 65:
        valorSeguro = (valorCarro * 0.05)
        print(f'O seguro do carro {modelo}, marca {marca}, saira no valor de {valorSeguro}, '
              f'para a idade entre 32 - 65 anos do cliente, no ano de {anoAtual}')


    elif idade > 65:
        print(f'O senhor(a) {nome}, não pode mais fazer um seguro veicular pelo risco, segundo a lei N°: 3532456-43, '
              f'no ano de {anoAtual}')


    else:
        print('Você não pode fazer seguro veicular')

    print('---------------Obrigado por utilizar os serviços da Muroguro-------------------')

else:
    print('Não foi selecionado nenhum serviço')
