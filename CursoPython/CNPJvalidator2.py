from functions import *

while True:
    entrada = input('CNPJ: ')
    if validaEntrada(entrada) != False:
        verificado = validaEntrada(entrada)
        validaCNPJ(verificado)
        break
    else:
        continue