# ChatBot - Um Chatbot de Conversação com Modelos de Transformadores

Este é um projeto que utiliza modelos de **Transformers**, como o **BlenderBot** da Hugging Face, para criar um chatbot inteligente capaz de responder a perguntas e manter uma conversa fluida. O projeto está estruturado em Python utilizando a biblioteca **transformers** da Hugging Face e **Flask** para a API do chatbot.

## Índice

1. [Descrição](#descrição)
2. [Instalação](#instalação)
3. [Como Usar](#como-usar)
4. [Arquitetura do Projeto](#arquitetura-do-projeto)
5. [Dependências](#dependências)
6. [Exemplos de Uso](#exemplos-de-uso)
7. [Desenvolvimento Futuro](#desenvolvimento-futuro)
8. [Licença](#licença)

## Descrição

Este chatbot é baseado em um modelo de transformador (transformer model) treinado para interação em inglês. O objetivo principal deste projeto é criar um assistente virtual que seja capaz de compreender e gerar respostas com base em entradas de texto. Ele é adequado para integrar com outras plataformas de serviços de chatbot ou aplicativos de mensagens.

### Funcionalidades principais:

- **Resposta a perguntas**: O modelo gera respostas para perguntas feitas pelo usuário.
- **Manutenção de conversa**: O modelo mantém o contexto da conversa, respondendo com base no histórico da interação.
- **API Flask**: O chatbot é exposto por meio de uma API Flask, permitindo fácil integração em aplicações web.

## Instalação

1. **Clonar o repositório**:

```bash
git clone https://github.com/Ibsen-Gomes/ChatBot.git
cd ChatBot
Criar e ativar um ambiente virtual:
bash
Copiar
Editar
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
Instalar dependências:
bash
Copiar
Editar
pip install -r requirements.txt
Baixar o modelo: O modelo do Hugging Face será baixado automaticamente quando o código for executado pela primeira vez.
Como Usar
Rodar o servidor Flask:
bash
Copiar
Editar
python app.py
Isso iniciará o servidor localmente e o chatbot estará disponível em http://localhost:5000.

Interagir com o ChatBot via API:
Envie uma requisição POST para a API com curl ou Postman:

bash
Copiar
Editar
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello, chatbot!"}' http://localhost:5000/chat
Integração com outras plataformas: A API pode ser facilmente integrada a sistemas como Slack, Telegram, ou outros chatbots.
Arquitetura do Projeto
app.py: Configuração e execução da API Flask.
bot.py: Lógica do chatbot (carregamento do modelo e geração de respostas).
requirements.txt: Dependências do projeto.
Dependências
Flask: Framework web para Python.
transformers: Biblioteca da Hugging Face para modelos de linguagem.
torch: Framework de deep learning.
requests: Para fazer requisições HTTP.
gunicorn (opcional): Para rodar o Flask em produção.
Instale as dependências com:

bash
Copiar
Editar
pip install -r requirements.txt
Exemplos de Uso
Enviando Mensagens: Envie um JSON com a chave "message".
json
Copiar
Editar
{
  "message": "Qual é o seu nome?"
}
Resposta:

json
Copiar
Editar
{
  "response": "Olá, sou o BlenderBot, e estou aqui para conversar com você!"
}
Desenvolvimento Futuro
Suporte a múltiplos idiomas.
Melhorias no contexto de conversação.
Otimizações de desempenho e escalabilidade.
Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

Copiar
Editar
