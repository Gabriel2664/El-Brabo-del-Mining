def faz_conta():
    return 0

def oi ():
    print('oi')
    print('oi')

def soma_dois_valores (valor1, valor2):
    return valor1 + valor2


oi()
x = soma_dois_valores (3,4)
print (x)
x = soma_dois_valores (2,8)
print (x)
print (faz_conta())

def eleva_dois_valores (valor1, valor2):
    return valor1 ** valor2
x = eleva_dois_valores (9,1/2)
print (x)
def raiz_quadrada (valor, base):
    return valor ** (1/base)
y = raiz_quadrada(9,2)
print (y)
def e_par (valor):
    return (valor % 2) == 0
print (e_par(4))
print (e_par(21))
def div_por_seis (valor):
    return (valor % 2) == 0 and (valor %3) == 0
print (div_por_seis(12))
print (div_por_seis(9))


def teste_par():
    '''Le um valor inserido pelo usuáriuo, verifica se tal valor é par e retorna'''
    parada = False
    while parada == False:
        valor = input ('Insira um valor numérico, ou aperte ENTER para encerrar...\n')
        if valor == '':
            parada = True
        elif e_par (int(valor)) == True:
            print('o valor inserido é par.')
        else:
            print('o valor inserido é ímpar .')

def dez_mult_tres():
    '''Imprime os primeiros 10 números múltiplos de 3.'''
    cont = 0
    numero = 1
    while cont <10:
        if numero % 3 == 0:
            print(numero)
            cont += 1
        numero += 1

dez_mult_tres()



teste_par()
