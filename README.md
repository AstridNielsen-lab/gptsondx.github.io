# GPTsondx

Bem-vindo ao projeto GPTsondx! Este é um projeto emocionante de rastreamento de frequências usando Python, Flask e Scapy.

## Descrição

O GPTsondx é um projeto de código aberto que visa detectar e rastrear frequências usando tecnologias de comunicação sem fio. Ele utiliza Python para a lógica do servidor, Flask para a criação da API web, e Scapy para a análise de pacotes de rede.

## Estrutura do Projeto

- `backend/`: Contém o código do servidor Flask e a lógica de rastreamento de frequências.
- `frontend/`: (se aplicável) Poderia conter o código da interface do usuário.
- `venv/`: Ambiente virtual Python para gerenciar dependências.

## Configuração

1. Certifique-se de ter o Python instalado.
2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - No Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute o aplicativo:

    ```bash
    python app.py
    ```

Acesse o aplicativo em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Contribuindo

Se você quiser contribuir para o projeto, siga estas etapas:

1. Fork o repositório.
2. Crie uma nova branch:

    ```bash
    git checkout -b feature/sua-feature
    ```

3. Faça suas alterações e faça commit:

    ```bash
    git add .
    git commit -m "Adiciona sua incrível feature"
    ```

4. Empurre a branch:

    ```bash
    git push origin feature/sua-feature
    ```

5. Abra uma solicitação pull.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

