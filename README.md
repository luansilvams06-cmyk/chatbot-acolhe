# Acolhe – Chatbot de Apoio Emocional

## 1. Apresentação

O Acolhe é um chatbot desenvolvido como projeto acadêmico do curso de Análise e Desenvolvimento de Sistemas (ADS). Seu objetivo é oferecer um espaço de conversa acolhedor, permitindo que usuários expressem sentimentos, preocupações e dificuldades emocionais por meio do Telegram.

O sistema utiliza inteligência artificial para gerar respostas empáticas e possui mecanismos básicos de identificação de mensagens que podem indicar sofrimento emocional ou risco.

## 2. Objetivo

Desenvolver um assistente virtual capaz de oferecer apoio emocional inicial, utilizando linguagem natural e orientações adequadas para situações de sofrimento.

## 3. Tecnologias utilizadas

- Python
- Telegram Bot API
- Biblioteca python-telegram-bot
- Google Gemini API
- Biblioteca google-genai
- Biblioteca python-dotenv

## 4. Funcionalidades

- Inicialização da conversa pelo comando `/start`.
- Recebimento e processamento de mensagens de texto.
- Geração de respostas com inteligência artificial.
- Identificação básica de expressões associadas a sofrimento emocional.
- Resposta específica para mensagens com expressões explícitas de risco.
- Orientações para buscar apoio de pessoas de confiança e serviços de atendimento.

## 5. Estrutura do projeto

```text
chatbot_saude_mental/
├── .venv/
├── .env
├── .gitignore
├── bot.py
├── bot_backup.py
├── bot_backup_2.py
└── README.md
```

## 6. Instalação e configuração

É necessário ter Python instalado, uma conta no Telegram, um token de bot e uma chave de API do Google Gemini.

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install python-telegram-bot python-dotenv google-genai
```

Crie um arquivo `.env` na pasta principal do projeto:

```env
BOT_TOKEN=SEU_TOKEN_DO_TELEGRAM
GEMINI_API_KEY=SUA_CHAVE_DO_GEMINI
```

Substitua os valores de exemplo pelas respectivas credenciais. Não compartilhe esse arquivo.

## 7. Execução

Com o ambiente virtual ativado, execute:

```powershell
python bot.py
```

O bot poderá ser acessado pelo Telegram após sua inicialização.

Para encerrar a execução, pressione `Ctrl + C` no terminal.

## 8. Testes realizados

Foram realizados testes manuais com diferentes tipos de mensagens:

| Cenário | Resultado observado |
|---|---|
| Dificuldade cotidiana | Resposta acolhedora |
| Sofrimento emocional indireto | Identificação de possível risco e pergunta de acompanhamento |
| Mensagem com negação e sinais preocupantes | Resposta considerando o contexto |
| Expressão explícita de risco | Orientações específicas de segurança |

Os resultados são preliminares e não representam uma validação clínica do sistema.

## 9. Limitações e cuidados

O Acolhe é um protótipo acadêmico e não substitui acompanhamento psicológico, atendimento médico ou serviços de emergência.

A identificação de risco utiliza expressões previamente definidas e inteligência artificial. Portanto, pode apresentar falsos positivos ou deixar de identificar determinadas situações.

Mensagens enviadas para geração de respostas são processadas pela API do Google Gemini. O projeto deve considerar aspectos de privacidade e proteção de dados.

Em situações de perigo imediato, a orientação é procurar um pronto-socorro ou ligar para o SAMU (192). O CVV oferece

## 🎥 Vídeo de demonstração

Confira o funcionamento do Projeto Acolhe no Telegram:

[▶️ Assistir à demonstração do Acolhe](https://youtu.be/ZttQ8EaNDrE)