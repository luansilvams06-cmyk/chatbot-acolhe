# DOCUMENTAÇÃO TÉCNICA
## Projeto Acolhe – Chatbot de Apoio Emocional

**Instituição:** FMU – Centro Universitário  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Aluno:** Luan Silva Miranda dos Santos  
**Professor:** Rafael Bonangelo  
**Cidade:** São Paulo – SP  
**Linguagem:** Python  
**Plataforma:** Telegram  
**Inteligência Artificial:** Google Gemini  

---

## 1. INTRODUÇÃO

O Acolhe é um chatbot de apoio emocional desenvolvido como projeto acadêmico do curso de Análise e Desenvolvimento de Sistemas.

O sistema permite que usuários conversem por meio da plataforma Telegram, recebendo respostas geradas por inteligência artificial.

O projeto foi desenvolvido utilizando Python e integra a API do Telegram com a API do Google Gemini, possibilitando interações em linguagem natural.

A proposta é oferecer um ambiente digital de acolhimento, no qual as pessoas possam expressar sentimentos, compartilhar preocupações e conversar sem julgamentos.

## 2. OBJETIVO DO SISTEMA

O objetivo principal do Acolhe é desenvolver um assistente virtual capaz de oferecer acolhimento inicial a pessoas que desejam conversar sobre sentimentos, preocupações e dificuldades cotidianas.

Entre os objetivos específicos estão:

- Facilitar o acesso a um ambiente de conversa e acolhimento.
- Utilizar inteligência artificial para gerar respostas contextualizadas.
- Identificar expressões relacionadas a possíveis situações de risco.
- Apresentar orientações de segurança em situações que exigem atenção.
- Incentivar a busca por ajuda profissional quando necessário.

## 3. TECNOLOGIAS UTILIZADAS

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Telegram Bot API | Comunicação com os usuários |
| python-telegram-bot | Gerenciamento de mensagens e comandos |
| Google Gemini API | Geração de respostas por inteligência artificial |
| google-genai | Integração com o Gemini |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| Git | Controle de versão |
| GitHub | Hospedagem do código-fonte |

## 4. ARQUITETURA DO SISTEMA

O funcionamento do Acolhe envolve diferentes componentes integrados.

O fluxo de funcionamento ocorre da seguinte maneira:

1. O usuário envia uma mensagem pelo Telegram.
2. A plataforma encaminha a mensagem para o chatbot.
3. A aplicação Python recebe e processa o conteúdo.
4. Um mecanismo local verifica expressões relacionadas a possíveis situações de risco.
5. Quando necessário, o sistema apresenta uma resposta específica de segurança.
6. Nos demais casos, a mensagem é encaminhada ao Google Gemini para geração de uma resposta.
7. A resposta é enviada novamente ao usuário pelo Telegram.

Essa arquitetura permite combinar processamento local de mensagens com inteligência artificial generativa.

## 5. ESTRUTURA DO CÓDIGO

O arquivo principal do projeto é `bot.py`, responsável pela execução e pelo gerenciamento das funcionalidades do chatbot.

### 5.1 Importação de bibliotecas

O código utiliza bibliotecas responsáveis pela comunicação com o Telegram, integração com o Google Gemini e gerenciamento das variáveis de ambiente.

### 5.2 Configuração das credenciais

As credenciais são carregadas por meio do arquivo `.env`, utilizando a biblioteca python-dotenv.

São utilizadas duas variáveis principais:

- `BOT_TOKEN`: token de acesso ao bot do Telegram.
- `GEMINI_API_KEY`: chave de acesso à API do Google Gemini.

Essa abordagem evita inserir diretamente as credenciais no código-fonte.

### 5.3 Identificação de expressões de risco

O sistema possui duas listas de identificação:

- `TERMOS_RISCO_EXPLICITO`: contém expressões associadas a possíveis situações de risco explícito.
- `TERMOS_POSSIVEL_RISCO`: contém expressões relacionadas a sofrimento emocional ou possíveis situações de vulnerabilidade.

A verificação é realizada por comparação textual.

O objetivo desse mecanismo é identificar mensagens que merecem atenção especial e direcionar o fluxo de resposta.

Esse recurso é básico e não substitui uma avaliação profissional ou um sistema clínico de identificação de risco.

### 5.4 Função iniciar()

A função `iniciar()` é responsável por apresentar o chatbot ao usuário quando o comando `/start` é enviado.

Ela apresenta o objetivo do projeto, explica suas limitações e orienta o usuário a evitar o compartilhamento de informações pessoais e sensíveis.

### 5.5 Função conversar()

A função `conversar()` recebe e processa as mensagens enviadas pelo usuário.

Inicialmente, o texto é analisado para verificar a presença de expressões relacionadas a possíveis situações de risco.

Quando uma expressão de risco explícito é identificada, o sistema apresenta uma resposta específica com orientações de segurança, incluindo a procura por serviços de emergência, pessoas de confiança e o Centro de Valorização da Vida (CVV), pelo número 188.

Nos demais casos, o sistema utiliza o Google Gemini para gerar respostas em linguagem natural.

Quando são identificados sinais de possível sofrimento emocional, são fornecidas instruções adicionais para que a inteligência artificial responda com empatia e atenção.

Caso ocorra uma falha na comunicação com a API, o sistema apresenta uma mensagem informando que não conseguiu responder naquele momento.

### 5.6 Função main()

A função `main()` é responsável pela inicialização do chatbot.

Suas principais responsabilidades são:

- Verificar a disponibilidade das credenciais necessárias.
- Criar a aplicação do Telegram.
- Configurar os manipuladores de comandos e mensagens.
- Registrar as funções responsáveis pelo atendimento.
- Iniciar a execução do bot para receber mensagens.

Essa função centraliza a inicialização e permite que o sistema permaneça disponível para interações enquanto estiver em execução.

## 6. REQUISITOS DO SISTEMA

### 6.1 Requisitos funcionais

Os requisitos funcionais descrevem as funcionalidades oferecidas pelo sistema.

- RF01: O sistema deve permitir a interação por meio do Telegram.
- RF02: O sistema deve apresentar uma mensagem inicial ao receber o comando `/start`.
- RF03: O sistema deve receber e processar mensagens dos usuários.
- RF04: O sistema deve utilizar inteligência artificial para gerar respostas.
- RF05: O sistema deve identificar determinadas expressões relacionadas a possíveis situações de risco.
- RF06: O sistema deve apresentar orientações específicas quando identificar expressões de risco explícito.
- RF07: O sistema deve informar quando ocorrer uma falha na comunicação com a inteligência artificial.

### 6.2 Requisitos não funcionais

- RNF01: O sistema deve utilizar Python como linguagem principal.
- RNF02: A comunicação deve ocorrer por meio da plataforma Telegram.
- RNF03: As credenciais devem ser armazenadas em variáveis de ambiente.
- RNF04: As respostas devem apresentar linguagem acolhedora e compreensível.
- RNF05: O sistema deve apresentar mensagens de segurança e suas limitações de utilização.

## 7. SEGURANÇA E PRIVACIDADE

O Acolhe utiliza um arquivo `.env` para armazenar as credenciais de acesso às APIs.

O arquivo está incluído no `.gitignore`, evitando que as chaves secretas sejam enviadas ao repositório público.

O projeto também considera a importância da privacidade dos usuários, orientando que não sejam compartilhadas informações pessoais ou sensíveis.

O chatbot não possui finalidade diagnóstica e não substitui psicólogos, médicos, serviços de emergência ou acompanhamento profissional.

Em situações de emergência, o usuário deve procurar atendimento especializado. No Brasil, o CVV atende pelo número 188, e o SAMU pode ser acionado pelo número 192 em emergências médicas.

## 8. TESTES E VALIDAÇÃO

Durante o desenvolvimento, foram realizados testes para verificar o funcionamento das principais funcionalidades.

Entre os procedimentos realizados estão:

- Inicialização da aplicação Python.
- Verificação das credenciais de acesso.
- Comunicação com a API do Telegram.
- Teste do comando `/start`.
- Envio e recebimento de mensagens.
- Integração com o Google Gemini.
- Verificação da geração de respostas.
- Teste de mensagens relacionadas a possíveis situações de risco.

Os testes de funcionamento realizados confirmaram que o chatbot consegue iniciar, receber mensagens e responder aos usuários por meio do Telegram.

## 9. LIMITAÇÕES DO SISTEMA

Apesar das funcionalidades implementadas, o projeto apresenta algumas limitações:

- O mecanismo de identificação de risco utiliza comparação textual e pode não interpretar corretamente todos os contextos.
- As respostas geradas dependem da disponibilidade da API do Google Gemini.
- O chatbot não realiza diagnósticos ou avaliações psicológicas.
- O funcionamento depende de conexão com a internet.
- O sistema precisa permanecer em execução para receber e responder às mensagens.
- O projeto não possui banco de dados próprio para armazenamento e consulta de histórico de interações.

## 10. POSSÍVEIS MELHORIAS FUTURAS

Como possibilidades de evolução do projeto, são propostas as seguintes melhorias:

- Implementação de banco de dados SQLite para armazenamento estruturado de informações não sensíveis.
- Desenvolvimento de um painel administrativo para acompanhamento da utilização.
- Ampliação dos mecanismos de identificação de situações de risco.
- Implementação de novas funcionalidades e comandos.
- Aprimoramento das respostas da inteligência artificial.
- Implantação em serviço de hospedagem para disponibilidade contínua.

Essas melhorias poderão ampliar a capacidade de gerenciamento, manutenção e evolução do sistema.

## 11. CONSIDERAÇÕES FINAIS

O desenvolvimento do Projeto Acolhe proporcionou a aplicação prática de conhecimentos relacionados à programação Python, integração de APIs, inteligência artificial, tratamento de mensagens e controle de versão.

A integração entre Telegram e Google Gemini permitiu desenvolver um chatbot funcional, capaz de receber mensagens e gerar respostas em linguagem natural.

Além dos aspectos técnicos, o projeto também destacou a importância da tecnologia no desenvolvimento de soluções digitais voltadas ao acolhimento e ao bem-estar emocional.

Conclui-se que o Acolhe representa uma aplicação prática dos conhecimentos adquiridos durante o curso de Análise e Desenvolvimento de Sistemas, apresentando possibilidades de evolução e aprimoramento em versões futuras.

## 12. REPOSITÓRIO DO PROJETO

O código-fonte e os arquivos do projeto estão disponíveis publicamente no GitHub:

https://github.com/luansilvams06-cmyk/chatbot-acolhe

---

**Projeto Acolhe — Tecnologia que acolhe, inteligência que escuta.**