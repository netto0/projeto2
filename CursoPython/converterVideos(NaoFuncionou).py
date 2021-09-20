import os
import fnmatch
import sys
if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = ''
input_legenda = ''
map_legenda = ''

caminho_origem = r'C:\Users\Netto\Documents\videoteste'
caminho_destino = r'C:\Users\Netto\Documents\novo'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
        print(f'Nome arquivo: {nome_arquivo}')
        arquivo_saida = fr'{caminho_destino}\{nome_arquivo}_copia{ext_arquivo}'
        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} {map_legenda} "{arquivo_saida}"'

        print(comando)
        os.system(comando)