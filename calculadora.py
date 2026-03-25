termo1 = float(input('\n----------------------------------\n\tDIGITE O 1º TERMO\n----------------------------------\n'))

op = int(input('\n----------------------------------\n[1]Para (+)\n[2]Para (-)\n[3]Para (÷)\n[4]Para (X)\n----------------------------------\n'))

if op == 1:
    print('\nOPERAÇÃO ESCOLHIDA: SOMA')
elif op == 2:
    print('\nOPERAÇÃO ESCOLHIDA: SUBTRAÇÃO')
elif op == 3:
    print('\nOPERAÇÃO ESCOLHIDA: DIVISÃO')
elif op == 4:
    print('\nOPERAÇÃO ESCOLHIDA: MULTIPLICAÇÃO')

while op != 1 and op != 2 and op != 3 and op != 4:
    print('ERRO: NÚMERO INVÁLIDO\n   TENTE NOVAMENTE')
    op = int(input('\n----------------------------------\n[1]Para (+)\n[2]Para (-)\n[3]Para (÷)\n[4]Para (X)\n----------------------------------\n'))

termo2 = float(input('\n----------------------------------\n\tDIGITE O 2º TERMO\n----------------------------------\n'))

if op == 1:
    resultado = termo1 + termo2
elif op == 2:
    resultado = termo1 - termo2
elif op == 3:
    while termo2 == 0:
        print('\nERRO: NÃO É POSSÍVEL DIVIDIR POR 0')
        termo2 = float(input('\n----------------------------------\n\tDIGITE O 2º TERMO\n----------------------------------\n'))
    resultado = termo1 / termo2
elif op == 4:
    resultado = termo1 * termo2


print(f'\n----------------------------------\nO RESULTADO É: {resultado}\n----------------------------------')
