#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Utils/translate.py
# Not Delete, Copyright and MIT License, BY Thomas R. © 2025.

""" Sub script-modulo que irá carregar/selecionar/usar
   os arquivos de traduções dependendo da escolha """

import os
import json
from .decoration import color

LANG_DIR_NAME = "LANGUAGE_IPTV_CHK"

def _get_lang_dir_path():
    """
    Tenta encontrar o caminho para a pasta de idiomas de duas maneiras:
    1. Na raiz do projeto (ideal para execução a partir do script principal).
    2. Ao lado deste módulo (dentro de Utils).
    Retorna o caminho correto ou None se não encontrar em nenhum dos locais.
    """
    # Tentativa 1: Procurar na Raiz do Projeto (subindo 2 níveis)
    # Ideal para a estrutura: DS_ULTRA V6/LANGUAGE_IPTV_CHK/
    try:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_attempt1 = os.path.join(project_root, LANG_DIR_NAME)
        if os.path.exists(path_attempt1):
            return path_attempt1
    except Exception:
        pass # Ignora erros se a estrutura de caminho falhar

    # Tentativa 2: Procurar ao Lado deste Módulo (subindo 1 nível)
    # Ideal para a estrutura: DS_ULTRA V6/Utils/LANGUAGE_IPTV_CHK/
    try:
        module_dir = os.path.dirname(os.path.abspath(__file__))
        path_attempt2 = os.path.join(module_dir, LANG_DIR_NAME)
        if os.path.exists(path_attempt2):
            return path_attempt2
    except Exception:
        pass

    # Se nenhuma tentativa funcionou, retorna None
    return None

# Constante Global que armazena o caminho encontrado
LANG_DIR_PATH = _get_lang_dir_path()


def carregar_idioma(idioma):
    """Carrega as traduções de um arquivo de idioma JSON."""
    if not LANG_DIR_PATH: # Se a pasta não foi encontrada
        return {"translations": {}}

    lang_file = f"lang-{idioma}.json"
    lang_path = os.path.join(LANG_DIR_PATH, lang_file)

    if not os.path.exists(lang_path):
        lang_path = os.path.join(LANG_DIR_PATH, "lang-en.json")
        if not os.path.exists(lang_path):
            return {"translations": {}}
    
    try:
        with open(lang_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"translations": {}}


def listar_idiomas_disponiveis():
    """Lista os idiomas disponíveis no diretório 'Language'."""
    if not LANG_DIR_PATH: # Se a pasta não foi encontrada
        return []
    
    idiomas = []
    for arquivo in os.listdir(LANG_DIR_PATH):
        if arquivo.startswith("lang-") and arquivo.endswith(".json"):
            idiomas.append(arquivo[5:-5])
    return idiomas


def selecionar_idioma():
    """Permite ao usuário escolher um idioma"""
    idiomas = listar_idiomas_disponiveis()
    
    if not idiomas:
        print("{}Nenhum arquivo de idioma encontrado na pasta '{}/'!{}".format(color.vermelho, LANG_DIR, color.reset))
        return "pt"
    
    print("\n{}Idiomas disponíveis:{}".format(color.ciano, color.reset))
    for idx, idioma in enumerate(idiomas, 1):
        print("{}{}. {}{}".format(color.azul, idx, idioma, color.reset))
    
    while True:
        try:
            escolha = int(input("{}  Selecione >>> {}".format(color.verde, color.reset))) - 1
            if 0 <= escolha < len(idiomas):
                return idiomas[escolha]
        except:
            pass
        print("{}Seleção inválida!{}".format(color.vermelho, color.reset))


def criar_t(config):
    """Cria e retorna uma função de tradução baseada no idioma configurado."""
    def t(key, default=None):
        keys = key.split('.')
        current = carregar_idioma(config["idioma"]).get("translations", {})
        
        try:
            for k in keys:
                current = current[k]
            return current
        except (KeyError, TypeError):
            return default if default is not None else key
    return t