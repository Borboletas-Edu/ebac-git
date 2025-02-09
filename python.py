def escrita(msg):

    print('=' * 50)
    print(f'{msg:^50}')
    print('=' * 50)

   



escrita('calculadora simples!')

print()
num1 = float(input('Digite um número: '))
print()

print('Escolha sua operação: ')
operações = ("+ adição", "- subtração", "* multiplicação", "/ divisão")
for v, c in enumerate(operações):
    print (f'[{v+1:^3}] {c:<10}' )
print()

num_op = float(input('Número da operação: '))


