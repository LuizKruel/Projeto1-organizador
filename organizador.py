"""
Projeto1-organizador
Descrição: programa que cria diretórios com nome 'documentos' e 'planilhas'
e move arquivos existentes paras os diretórios criados, conforme seu tipo/extensão,
utilizando a função OS e Shutil
Data: 19/09/2022
Autor: Luiz Kruel
versão: 0.0.1
"""

import shutil
import os

# cria diretorios 'documentos' e 'planilhas'

def criadiretorio():
    if os.path.exists('documentos')==False:
        os.mkdir('documentos')

    if os.path.exists('planilhas')==False:
        os.mkdir('planilhas')
    
# move arquivo para os diretórios criados

def movearquivo():
    arquivos = os.listdir()
    for arquivo in arquivos:
        if ".xls" in arquivos:
            shutil.move(arquivo,f"./planilhas/{arquivo}")
        elif ".xlsx" in arquivos:
            shutil.move(arquivo,f"./documentos/{arquivo}")
        elif ".doc" in arquivos:
            shutil.move(arquivo,f"./documentos/{arquivo}")
        elif ".docx" in arquivos:
            shutil.move(arquivo,f"./documentos/{arquivo}")
            
# execução do programa

def main():
    criadiretorio()
    movearquivo()

if __name__ == "__main__":
    main()
