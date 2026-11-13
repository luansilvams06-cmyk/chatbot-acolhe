# DOCUMENTAÇÃO TÉCNICA
## Projeto Acolhe – Chatbot de Apoio Emocional

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Linguagem:** Python  
**Plataforma:** Telegram  
**Inteligência Artificial:** Google Gemini

---

## 1. Introdução

O Acolhe é um chatbot de apoio emocional desenvolvido como projeto acadêmico. O sistema permite que usuários conversem por meio do Telegram, recebendo respostas geradas por inteligência artificial.

O projeto foi desenvolvido em Python e utiliza a API do Telegram para receber e enviar mensagens, além da API do Google Gemini para gerar respostas em linguagem natural.

## 2. Objetivo do sistema

O objetivo é desenvolver um assistente virtual capaz de oferecer acolhimento inicial a pessoas que desejam conversar sobre sentimentos, preocupações e dificuldades cotidianas.

O sistema também possui mecanismos básicos para identificar mensagens que podem indicar sofrimento emocional ou situações de risco.

## 3. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Telegram Bot API | Comunicação com os usuários |
| python-telegram-bot | Gerenciamento de mensagens e comandos |
| Google Gemini API | Geração de respostas por inteligência artificial |
| google-genai | Integração com o Gemini |
| python-dotenv | Carregamento de variáveis de ambiente |
| Git | Controle de versão |
| GitHub | Hospedagem do código-fonte |

## 4. Arquitetura do sistema

O funcionamento do Acolhe envolve os seguintes componentes:

1. Usuário: envia uma mensagem pelo Telegram.
2. Telegram: encaminha a mensagem para a aplicação.
3. Python: recebe e processa a mensagem.
4. Mecanismo local de identificação: verifica expressões relacionadas a possíveis situações de risco.
5. Google Gemini: gera respostas acolhedoras quando o fluxo local não determina uma resposta específica.
6. Telegram: entrega a resposta ao usuário.

## 5. Estrutura do código

O arquivo principal do sistema é `bot.py`.

### 5.1 Importação de bibliotecas

O código importa as bibliotecas necessárias para comunicação com o Telegram, integração com o Gemini e gerenciamento de variáveis de ambiente.

### 5.2 Configuração das credenciais

As credenciais são carregadas por meio do arquivo `.env`, utilizando a biblioteca python-dotenv.

São utilizadas duas variáveis principais:

- `BOT_TOKEN`: token de acesso ao bot do Telegram.
- `GEMINI_API_KEY`: chave de acesso à API do Google Gemini.

### 5.3 Identificação de expressões de risco

O sistema possui duas listas:

- `TERMOS_RISCO_EXPLICITO`: contém expressões associadas a possíveis intenções ou ações de risco explícitas.
- `TERMOS_POSSIVEL_RISCO`: contém expressões relacionadas a sofrimento intenso ou possível risco.

A verificação é realizada por meio de comparação textual.

### 5.4 Função iniciar()

A função `iniciar()` é responsável por apresentar o chatbot ao usuário quando o comando `/start` é enviado.

Ela informa a finalidade do sistema, suas limitações e orienta o usuário a evitar o compartilhamento de dados pessoais.

### 5.5 Função conversar()

A função `conversar()` recebe e processa as mensagens enviadas pelo usuário.

Primeiramente, o texto é normalizado e comparado com as listas de expressões de risco.

Quando uma expressão de risco explícito é identificada, o sistema apresenta uma resposta específica com orientações de segurança.

Nos demais casos, o sistema utiliza o Google Gemini para gerar uma resposta, incluindo instruções adicionais quando são identificados sinais de possível sofrimento intenso.

Caso ocorra uma falha na comunicação com a API, o sistema apresenta uma mensagem informando que não conseguiu responder naquele momento.

### 5.6 Função main()

A função `main()` verifica