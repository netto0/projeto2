import csv

# Abrindo arquivo csv         #newline='' serve para nao pular linha sim linha não
with open('clientes.csv', 'r',newline='') as arquivo:
    # Necessário a indentação por ser um gerador
    # csv.reader = lê como listas
    # csv.DictReader = lê como dicionários
    # dados = csv.DictReader(arquivo) #Modo mais comum
    dados = [x for x in csv.DictReader(arquivo)] #Método para não esgotar o uso dos dados
    # for dado in dados:
    #     print(dado['Nome'],dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

with open('clientes2.csv', 'w',newline='') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',', #Delimitador (Vírgula no caso)
        quotechar='"', # Caractere de citação (No caso deixa os valores entre aspas)
        quoting=csv.QUOTE_ALL
    )
    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow([chaves[0],chaves[1],chaves[2],chaves[3]])

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )