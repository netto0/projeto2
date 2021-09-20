from itertools import zip_longest
"""Fórmula: 11 - (x % 11) = y
0  4  2  5  2  0  1  1  0  0  0  1  -  1  0
x
5  4  3  2  9  8  7  6  5  4  3  2
0+16+6+10+18+0+7+6+0+0+0+2= 65
11 - (65 % 11) = 1
0  4  2  5  2  0  1  1  0  0  0  1  1
x
6  5  4  3  2  9  8  7  6  5  4  3  2
0+20+8+15+4+0+8+7+0+0+0+3+2=67
11 - (67 % 11) = 10
se for maior que 9 o digito é 0
04252011000110
04.252.011/0001-10
"""
primeira_sequencia = [5,4,3,2,9,8,7,6,5,4,3,2]
segunda_sequencia = [6,5,4,3,2,9,8,7,6,5,4,3,2]
while True:
    try:
        cnpj = input('Insira o CNPJ: ')
        # cnpj = "04252011000110"
    except:
        if ValueError:
            print('Insira somente números!')
        continue
    if len(str(cnpj)) != 14:
        print('Valor incorreto')
        print(len(str(cnpj)))
    else:
        salvoCnpj = cnpj
        cnpj = cnpj[0:12]
        break

n = 0
soma1 = 0
soma2 = 0
primeira_mult = zip_longest(primeira_sequencia,str(cnpj))
mult_list = list(primeira_mult)
for n in range(0,len(primeira_sequencia)):
    primeiroTermo = int(mult_list[n][0])
    segundoTermo = int(mult_list[n][1])
    resultado = primeiroTermo*segundoTermo
    soma1 += resultado
formula1 = 11 - (soma1 % 11)
if formula1 <= 9:
    cnpj1 = cnpj+str(formula1)
else:
    formula1 = 0
    cnpj1 = cnpj + str(formula1)



segunda_mult = zip_longest(segunda_sequencia,str(cnpj1))
mult_list1 = list(segunda_mult)

for m in range(0,len(segunda_sequencia)):
    primeiroTermo1 = int(mult_list1[m][0])
    segundoTermo1 = int(mult_list1[m][1])
    resultado = primeiroTermo1 * segundoTermo1
    soma2 += resultado
formula2 = 11 - (soma2 % 11)
if formula2 <= 9:
    cnpj2 = cnpj1+str(formula2)
else:
    formula2 = 0
    cnpj2 = cnpj1 + str(formula2)

if salvoCnpj == cnpj2:
    print('CNPJ Válido')
else:
    print('CNPJ Inválido')