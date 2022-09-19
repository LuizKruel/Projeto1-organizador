"""
Projeto1-organizador
Descrição: programa que cria diretórios com nome 'documentos' e 'planilhas'
e move arquivos existentes paras os diretórios criados, conforme seu tipo/extensão,
utilizando a função OS e Shutil
Autor: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.1
"""

import os
import shutil


# Criando diretórios

import os
import shutil

def cria_dir(nome: str):
    if os.path.exists(nome) == False:
        os.mkdir(nome)
    


# Movendo arquivos


def mov_arquivo(arquivos: list):
    for arquivo in arquivos:
        if '.xlsx' in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".docx" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
        elif '.xls' in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")   
