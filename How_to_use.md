## Instalação

Para utilizar o script via termux/linux, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/ReyFxck/DeepSeek-IPTV-Checker.git
    cd DeepSeek-IPTV-Checker
    ```

2.  **Instale as dependências:**
    Certifique-se de ter o Python 3 instalado. Em seguida, instale as bibliotecas necessárias:
    ```bash
    pip install requests requests[socks] tabulate
    ```

## Como Usar

1.  **Execute o script:**
    ```bash
    python IPTV-CHK-DS-ULTRA_BY_ReyFxck.py
    ```

2.  **Configuração Inicial:**
    Na primeira execução, o script solicitará que você escolha o seu sistema operacional e o idioma de preferência. Essas configurações serão salvas em `config.json`.

3.  **Forneça o Host do Servidor:**
    O script pedirá o host do servidor IPTV que você deseja verificar (ex: `seuservidor.com:port`).

4.  **Carregue seus Combos:**
    Coloque seus arquivos de combo (`user:pass` por linha) na pasta `Combo/` (ou na pasta configurada para o seu SO).
    O script listará os arquivos disponíveis para você selecionar.

5.  **Use Proxies (Opcional):**
    Se desejar usar proxies, coloque seus arquivos de proxy (um por linha) na pasta `Proxy/` (ou na pasta configurada para o seu SO).
    O script perguntará se você quer usar proxies e qual tipo (HTTP/HTTPS, SOCKS4, SOCKS5).

6.  **Defina o Número de Bots (Threads):**
    Escolha quantos bots (threads) o script deve usar para a verificação simultânea. Um número maior pode acelerar o processo, mas também pode consumir mais recursos do sistema.

7.  **Acompanhe os Resultados:**
    O script exibirá o progresso em tempo real, mostrando o número de Hits, Bads e Bans. Os Hits serão salvos em um arquivo `.txt` na pasta `Hits/` (ou na pasta configurada para o seu SO).

## Estrutura de Pastas

O script criará as seguintes pastas (ou as utilizará, se já existirem) com base no sistema operacional configurado:

-   `Combo/`: Para armazenar os arquivos de combo (`user:pass`).
-   `Proxy/`: Para armazenar os arquivos de proxy.
-   `Hits/`: Para salvar as contas IPTV válidas.
-   `Language/`: Contém os arquivos de tradução (`lang-en.json`, `lang-pt.json`, etc.).
