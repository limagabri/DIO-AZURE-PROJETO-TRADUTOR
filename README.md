# DIO-AZURE-PROJETO-TRADUTOR

> **Nota:** Este projeto utiliza uma conta de estudante no Azure, com limite de apenas 1000 tokens para os modelos que tenho acesso. Por esse motivo, o artigo completo não pôde ser traduzido em uma única execução.

## Sumário

1. [Introdução](#introdução)
2. [Pré-requisitos](#pré-requisitos)
3. [Configurando o Azure](#configurando-o-azure)
   - [1. Criando uma Conta no Azure](#1-criando-uma-conta-no-azure)
   - [2. Criando um Grupo de Recursos](#2-criando-um-grupo-de-recursos)
   - [3. Configurando o Serviço de Linguagem no Azure](#3-configurando-o-serviço-de-linguagem-no-azure)
   - [4. Configurando o Visual Studio Code para o Azure](#4-configurando-o-visual-studio-code-para-o-azure)
4. [Configurando o Projeto](#configurando-o-projeto)
5. [Uso do Tradutor](#uso-do-tradutor)
6. [Ferramentas e Tecnologias Utilizadas](#ferramentas-e-tecnologias-utilizadas)
7. [Conclusão](#conclusão)

---

## Introdução

Este projeto é um tradutor de artigos que utiliza a API do Azure Cognitive Services para traduzir textos de forma automática. A tradução é feita por meio de um modelo GPT-3.5 Turbo implantado no Azure OpenAI, e o projeto foi desenvolvido em Python utilizando a biblioteca LangChain.

## Pré-requisitos

- Conta no [Microsoft Azure](https://azure.microsoft.com/).
- Acesso ao Azure para Estudantes, com crédito de estudante ou uma conta com os serviços do Azure Cognitive habilitados.
- Visual Studio Code (VS Code) com a extensão do Azure instalada (opcional, mas recomendado).
- Conhecimentos básicos em Python.

## Configurando o Azure

### 1. Criando uma Conta no Azure

Se você ainda não possui uma conta no Azure, siga estes passos:

1. Acesse [azure.microsoft.com](https://azure.microsoft.com/) e clique em **Iniciar gratuitamente**.
2. Escolha a opção **Azure para Estudantes** se for estudante e tiver um e-mail acadêmico. Esta opção oferece um crédito inicial e acesso a alguns serviços gratuitos.
3. Complete o cadastro e verifique sua conta de estudante para receber o crédito.

### 2. Criando um Grupo de Recursos

Após configurar sua conta, crie um grupo de recursos:

1. No painel do Azure, navegue até **Grupos de recursos** no menu à esquerda.
2. Clique em **Criar grupo de recursos**.
3. Dê um nome ao grupo, escolha uma região próxima e clique em **Revisar + Criar** e, em seguida, em **Criar**.

### 3. Configurando o Serviço de Linguagem no Azure

Para utilizar a API de tradução com o modelo GPT-3.5 Turbo:

1. No portal do Azure, vá para **Criar um recurso** e procure por **Azure OpenAI**.
2. Escolha **Criar** e vincule-o ao grupo de recursos que você criou.
3. Configure o serviço escolhendo a região e os detalhes do modelo:
   - **API**: GPT-3.5 Turbo
   - **Versão da API**: A versão mais recente que você possui acesso. No exemplo, estamos usando `"2023-05-15"`.
4. Complete a configuração e aguarde até que o serviço esteja pronto.

### 4. Configurando o Visual Studio Code para o Azure

Você pode utilizar o VS Code para gerenciar seus recursos no Azure:

1. Instale o [Visual Studio Code](https://code.visualstudio.com/) se ainda não o tiver.
2. Adicione a extensão do **Azure** no marketplace de extensões do VS Code.
3. Conecte sua conta do Azure na extensão para acessar seus grupos de recursos e serviços diretamente do editor.

## Configurando o Projeto

Clone este repositório em seu ambiente local ou abra o Colab, e siga os passos:

1. Instale as dependências necessárias:
   ```bash
   !pip install openai requests beautifulsoup4 langchain

2. No código, configure a API do Azure OpenAI com suas informações:

  ```bash 
   cliente = AzureOpenAI(
    azure_endpoint="https://<SEU_ENDPOINT>.openai.azure.com/",
    api_key="<SUA_API_KEY>",
    api_version="2023-05-15",  # Use a versão da API correta para o Azure OpenAI
    deployment_name="gpt-35-turbo",
    temperature=1  
)
  ```

3. Substitua <SEU_ENDPOINT> e <SUA_API_KEY> com os valores específicos da sua conta Azure.

Uso do Tradutor
1. Extraindo o Texto do Artigo
Utilize a função extract_text_from_url(url) para buscar o conteúdo de um artigo da web. Esta função remove elementos de estilo e script para limpar o texto extraído:

url = 'https://dev.to/mrcaption49/collection-and-record-context-of-oracle-sql-50l0'
text = extract_text_from_url(url)

Nota: Como a conta de estudante tem um limite de tokens, traduções muito longas podem não ser concluídas. Recomendamos dividir o texto em partes menores se necessário.

Ferramentas e Tecnologias Utilizadas:</br>

Azure OpenAI: API para acessar os modelos GPT do Azure.</br>

Python: Linguagem de programação principal.</br>

LangChain: Biblioteca para integração com o modelo GPT e gerenciamento das mensagens.</br>

BeautifulSoup: Biblioteca para extração de texto de páginas HTML.</br>

Visual Studio Code: Editor recomendado para gerenciamento de recursos do Azure.</br>

### Conclusão

Este projeto demonstra como configurar e utilizar o Azure OpenAI para tradução de textos de maneira prática e eficiente. Embora o limite de tokens da conta de estudante possa restringir traduções muito extensas, esta é uma ótima oportunidade para explorar a integração com APIs de IA e desenvolver soluções de tradução personalizadas.

Explore e adapte este projeto para outras necessidades, e sinta-se à vontade para contribuir com melhorias!




