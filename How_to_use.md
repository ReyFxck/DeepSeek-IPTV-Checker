## Instalação Pydroid (Android)

Para utilizar o script via Pydroid siga os passos abaixo:

1. Baixe a versão da script você pode clicar aqui para [BAIXAR](https://github.com/ReyFxck/DeepSeek-IPTV-Checker/releases/), ou conferir manualmente nos Releases.

2. Baixe a versão mais recente do Pydroid clicando [AQUI](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)

3. Extrai-a o Zip para obter a pasta "DS ULTRA" você também pode opcionalmente mover essa pasta para onde quiser.

4. Abra o pydroid e Clique em "🗂️" Selecione "OPEN" e no método para abrir arquivos use "Internal Storage" jamais use "~Storage Access Framework~" pois nessa opção irá ocorrer o erro da Script não reconhecer varios sub arquivos ja que esse método é para arquivo aberto temporariamente, depois disso selecione o arquivo py dentro da pasta "DS ULTRA" e execute-a.

5. Caso for a primeira vez aberta a script pedirá que você instale as bibliotecas necessarias, volte a tela de início do Pydroid clique nos três riscos e podera instalar de duas maneiras:

• Método botão "Pip" - escreva o nome da biblioteca qie ele esta pedindo, ex: requests[socks]**

• Método botão "Terminal" - clique no terminal e faça o que o script pediu anteriormente coloque o comando para instalar a biblioteca, Ex: pip install requests[socks]

** Obs esse método não necessita instalar outro apk para plugin, basta desmarcar a opção "use prebuilt libaries repository"

## Instalação Termux (Android)

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
