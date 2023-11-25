def idade(nascimento, nome):
    idade = 2022 - nascimento
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    
invalid = True
while invalid:
    try:
        nome = input('Digite seu nome: ')
        nascimento = int(input('Digite ano de nascimento entre 1921 a 2021: '))
        if (nascimento>1921 and nascimento<2021):
            idade(nascimento, nome)
            invalid = False
        else:
            invalid = True
            print('Digite um ano entre 1921 a 2021\n')
    except ValueError:
        print('Ano inválido')
    