"""
Projeto1-organizador
Descrição: programa que cria diretórios com nome 'documentos' e 'planilhas'
e move arquivos existentes paras os diretórios criados, conforme seu tipo/extensão,
utilizando a função OS e Shutil
Autor: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.1
"""

import utilitarios
import os
import shutil


def main():
    arquivos = os.listdir()
    for diretorio in ['documentos', 'planilhas']:
        utilitarios.cria_dir(diretorio)
        utilitarios.mov_arquivo(arquivos)
    
if __name__=="__main__":
    main()
