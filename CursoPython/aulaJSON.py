import json

clientes_dict = {'maria': 27, 'Pedro': 22, 'João': 14, 'Ana': 17}


# Criando e Salvando Arquivo Json convertendo dicionário
with open('clientes.json', 'a+') as arquivo:
    json.dump(clientes_dict, arquivo)

# # Abrindo arquivo Json e convertendo o objeto em dicionario python
# with open('clientes.json', 'r') as arquivo:
#     dados = json.load(arquivo)
# print(dados)