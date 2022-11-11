taxa_imposto = float(input('Entre com a porcentagem da taxa de imposto: '))
print(f'Taxa informada: {taxa_imposto} % \n')

custo = float(input('Entre com o custo inicial do produto: '))
print(f'Custo informado: R${custo:.2f} \n')

def soma_imposto(taxa_imposto, custo):
    novo_custo = custo + (taxa_imposto / 100)
    print(f'O valor com imposto é: {novo_custo:.2f} \n')
    return novo_custo

soma_imposto(taxa_imposto, custo)

print('Fim da operação! Espero ter ajudado :)')


