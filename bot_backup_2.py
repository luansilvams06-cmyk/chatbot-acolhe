
import os
from dotenv import load_dotenv
from telegram import Update
from openai import AsyncOpenAI
from google import genai
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Carrega o token do arquivo .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

cliente_gemini = genai.Client(api_key=GEMINI_API_KEY)

# Palavras e expressões que exigem atenção imediata
TERMOS_DE_RISCO = [
    "quero me matar",
    "vou me matar",
    "pensando em suicídio",
    "penso em suicídio",
    "tirar minha vida",
    "tirar minha própria vida",
    "acabar com minha vida",
    "acabar com tudo",
    "dar fim à minha vida",
    "não quero mais viver",
    "não aguento mais viver",
    "queria morrer",
    "quero morrer",
    "seria melhor se eu não existisse",
    "não vejo sentido em continuar",
    "não vejo saída",
    "me suicidar",
    "me machucar",
    "pensando em me machucar",
    "me cortar",
    "me ferir",
    "automutilação",
    "automutilacao",
    "me enforcar",
    "me jogar",
    "tomar todos os remédios",
]

async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "Olá! 💚 Eu sou o Acolhe.\n\n"
        "Estou aqui para oferecer um espaço de conversa "
        "acolhedor e sem julgamentos.\n\n"
        "Você pode falar sobre seus sentimentos, "
        "preocupações ou simplesmente contar como foi seu dia.\n\n"
        "Sou uma ferramenta de apoio, não substituo "
        "psicólogos, médicos ou atendimento de emergência.\n\n"
        "Evite compartilhar dados pessoais ou informações "
        "que identifiquem você.\n\n"
        "Como você está se sentindo hoje?"
    )
    await update.message.reply_text(mensagem)




async def conversar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    # Verifica situações de risco antes de chamar a IA
    texto_normalizado = texto.lower().strip()

    frases_de_negacao = [
        "não penso em tirar minha vida",
        "não estou pensando em tirar minha vida",
        "não quero me matar",
        "não estou pensando em suicídio",
        "não penso em suicídio",
    ]
    tem_negacao = any(frase in texto_normalizado for frase in frases_de_negacao)

    if any(termo in texto_normalizado for termo in TERMOS_DE_RISCO) and not tem_negacao:
        resposta = (
            "Sinto muito que você esteja passando por isso. 💚\n\n"
            "Sua segurança é muito importante.\n"
            "Se você corre risco de se machucar agora, "
            "procure um pronto-socorro ou ligue para o SAMU (192).\n\n"
            "Se puder, fique perto de alguém de confiança.\n"
            "No Brasil, você também pode conversar com o CVV "
            "pelo telefone 188."
        )

    else:
        try:
            resultado = await cliente_gemini.aio.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=texto,
                config={
                    "system_instruction": (
                        "Você é o Acolhe, um assistente virtual de apoio emocional. "
"Responda em português brasileiro, com empatia, respeito e sem julgamentos. "
"Não dê diagnósticos nem prescreva medicamentos. "
"Não se apresente como psicólogo ou médico. "
"Esteja atento a sinais diretos e indiretos de sofrimento emocional, "
"desesperança, pensamentos de morte ou automutilação, mesmo quando "
"a pessoa não usa palavras explícitas. "
"Analise sempre o contexto completo da mensagem antes de identificar "
"uma situação de risco. Não mencione suicídio, automutilação ou "
"pensamentos de morte quando a pessoa estiver apenas relatando "
"tristeza, cansaço, estresse ou dificuldades cotidianas, sem sinais "
"concretos de risco. Não presuma que existe risco sem indícios na fala. "
"Por outro lado, não descarte sinais de risco apenas porque a pessoa "
"usa palavras de negação. "
"Se houver sinais de possível risco, acolha a pessoa, pergunte com "
"delicadeza se ela está em perigo imediato ou pensando em se machucar "
"agora e incentive o contato com alguém de confiança e ajuda profissional. "
"Se houver perigo imediato, oriente a procurar um pronto-socorro ou "
"ligar para o SAMU (192). O CVV atende pelo 188 para apoio emocional. "
"Nunca minimize o sofrimento nem prometa sigilo absoluto. "
"Não afirme que consegue garantir a segurança da pessoa."
                    )
                },
            )

            resposta = resultado.text or (
                "Não consegui formular uma resposta agora. "
                "Pode tentar novamente? 💚"
            )

        except Exception as erro:
            print(f"Erro no Gemini: {erro}")
            resposta = (
                "Desculpe, estou com dificuldade para responder agora. "
                "Tente novamente em alguns instantes. 💚"
            )

    await update.message.reply_text(resposta)




def main():
    print("TESTE A: Entrou na função main()", flush=True)

    if not TOKEN:
        raise ValueError("BOT_TOKEN não encontrado no arquivo .env")

    print("TESTE B: Token encontrado", flush=True)

    app = Application.builder().token(TOKEN).build()

    print("TESTE C: Aplicação criada", flush=True)

    app.add_handler(CommandHandler("start", iniciar))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, conversar)
    )

    print("Acolhe está funcionando!")
    app.run_polling()


if __name__ == "__main__":
    main()
