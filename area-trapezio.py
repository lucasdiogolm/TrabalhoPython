nome = input('Informe seu nome: ')
print(f'Olá {nome} tudo bem? Vamos ao programa! \n')

def trapezio():
    base_maior = int(input('Entre com a BASE MAIOR do trapézio: '))
    base_menor = int(input('Entre com a BASE MENOR do trapézio: '))
    altura = int(input('Entre com a ALTURA do trapézio: '))

    area = ((base_maior + base_menor) * altura) / 2
    print(f'A área do trapézio informado é: {area}')
    
trapezio()

print('Fim do programa, obrigado por utilizar nosso serviço!')