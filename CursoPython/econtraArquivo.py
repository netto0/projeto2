import os

caminho_procura = r'C:\Users\Netto\Documents\Trabalho'

termo_procura = input('Termo: ').lower()

contador = 0


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = tamanho
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2,)
    return f'{tamanho}{texto}'.replace('.',',')

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo.lower():
            try:
                caminho_completo = os.path.join(raiz,arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print(f'{arquivo:<45} {formata_tamanho(tamanho)}')
                contador += 1
            except PermissionError as e:
                print('Sem Permissões')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except Exception as e:
                print(f'Erro: {e}')

print()
print(f'{contador} arquivo(s) encontrado(s)')