'''
> 1: Item:
        Receber Item(nome, código, qtd, preço e validade)
        Salvar em arquivo separado
        Função Ler Lista de Arquivos
        Extrair Preços de Planilha
> 2: Interface Gráfica:
'''

import csv
from unidecode import unidecode
import re

def salvarItem(temp):
    with open('itens.csv', 'a', newline='') as arquivo:
        escreve = csv.writer(
            arquivo,
            delimiter=',',  # Delimitador (Vírgula no caso)
            quotechar='"',  # Caractere de citação (No caso deixa os valores entre aspas)
            quoting=csv.QUOTE_ALL
        )
        escreve.writerow([temp[0], temp[1], temp[2], temp[3], temp[4]])


def addItem(cod,nome,preco,qtd,validade):
    temp = []
    temp.append(cod)
    temp.append(nome)
    temp.append(preco)
    temp.append(qtd)
    temp.append(validade)
    salvarItem(temp)
    temp.clear()


def verLista():
    with open('itens.csv', 'r', newline='') as arquivo:
        # Necessário a indentação por ser um gerador
        # csv.reader = lê como listas
        # csv.DictReader = lê como dicionários
        #dados = csv.reader(arquivo) #Modo mais comum
        dados = [x for x in csv.DictReader(arquivo)]  # Método para não esgotar o uso dos dados
        for dado in dados:
            print(dado)


def to_ascii(ls):
    for i in range(len(ls)):
        ls[i] = unidecode(ls[i])


def buscaItem(key):
    #key = unidecode(key)

    with open('itens.csv', 'r', newline='') as arquivo:
        # Necessário a indentação por ser um gerador
        # csv.reader = lê como listas
        # csv.DictReader = lê como dicionários
        #dados = csv.reader(arquivo) #Modo mais comum
        dados = [x for x in csv.reader(arquivo)]  # Método para não esgotar o uso dos dados
        cont = 0
        results = []
        for dado in dados:
            #to_ascii(dado)
            if re.findall(f'{key}',str(dado), flags=re.I) != []:
                results.append(dados[cont])
            cont += 1
        return results

print(buscaItem('arroz'))

def vender(cod,qtd,prc,val):
    pass

def getPreco():
    pass




# addItem(1212,'arroz','14,25',32,'24/12/21')
# verLista()






