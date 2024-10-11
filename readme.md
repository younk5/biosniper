# Twitter Bio Checker (DESATUALIZADA)

## Descrição

Este projeto é uma aplicação de desktop construída com **Tkinter** que permite ao usuário verificar e monitorar a bio (descrição) de um usuário no **Twitter**. A aplicação utiliza a API interna do Twitter para buscar as informações da bio e exibi-las em tempo real. O projeto foi desenvolvido em **Python** e oferece uma interface gráfica simples e intuitiva.

### Funcionalidades

- **Buscar a Bio de um Usuário**: O usuário pode inserir o nome de usuário do Twitter (sem o "@" na frente) e a aplicação exibirá a bio atual do usuário.
- **Monitorar Mudanças na Bio**: A aplicação verifica automaticamente se a bio do usuário foi alterada a cada 10 segundos e atualiza a interface se houver alterações.
- **Interface Gráfica**: A aplicação tem uma interface gráfica amigável construída com Tkinter, com campos para inserir o nome de usuário e exibir a bio atual.
  
### Dependências

- **requests**: Para fazer requisições HTTP para a API do Twitter.
- **Pillow (PIL)**: Para manipulação de imagens (para exibir uma imagem de fundo).
- **dotenv**: Para carregar variáveis de ambiente de um arquivo `.env`.
- **tkinter**: Para construir a interface gráfica.
- **json**: Para manipulação de dados JSON.
- **threading**: Para realizar a verificação da bio em segundo plano.

### Requisitos

- Python 3.x
- As bibliotecas listadas em `requirements.txt`

### Como Rodar o Projeto

1. **Instale as dependências**:
    ```bash
    pip install requests pillow python-dotenv
    ```

2. **Configure o arquivo `.env`**:
    Crie um arquivo `.env` na raiz do projeto com os seguintes dados:

    ```
    BEARER=seu_bearer_token
    CSRF=seu_token_csrf
    COOKIE=seu_cookie
    ```

3. **Execute o script**:
    ```bash
    python twitter_bio_checker.py
    ```

4. **Interface**:
    - Insira o nome de usuário do Twitter (sem o `@`) na entrada de texto.
    - Clique em "Verificar Bio" para ver a bio atual.
    - A bio será monitorada a cada 10 segundos e exibida automaticamente quando houver alterações.

### Estrutura do Código

- **Twitter Class**: Classe principal que gerencia a interface gráfica e a lógica para buscar e monitorar a bio de usuários.
- **TwitterJson Function**: Função que carrega as configurações necessárias para realizar a requisição à API do Twitter a partir de um arquivo JSON (`default.json`).
- **poll_bio_changes Method**: Método que roda em uma thread separada e verifica periodicamente se a bio do usuário foi alterada.
- **check_bio Method**: Método que busca e exibe a bio atual do usuário quando solicitado.

### Exemplo de Uso

1. Ao rodar o script, a interface gráfica será aberta.
2. Insira o nome de usuário do Twitter na caixa de texto (sem o `@`).
3. Clique em "Verificar Bio" e a bio do usuário será exibida na tela.
4. A aplicação continuará verificando automaticamente se a bio muda a cada 10 segundos.


