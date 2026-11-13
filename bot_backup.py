
import os
from dotenv import load_dotenv
from telegram import Update
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

# Palavras e expressões que exigem atenção imediata
TERMOS_DE_RISCO = [
    "quero me matar",
    "tirar minha vida",
    "suicidio",
    "suicídio",
    "me suicidar",
    "me machucar",
    "me cortar",
    "automutilacao",
    "automutilação",
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
    texto = update.message.text.lower()

    if any(termo in texto for termo in TERMOS_DE_RISCO):
        resposta = (
            "Sinto muito que você esteja passando por isso. 💚\n\n"
            "Sua segurança é muito importante.\n"
            "Se você corre risco de se machucar agora, procure "
            "um pronto-socorro ou ligue para o SAMU (192).\n\n"
            "Se puder, fique perto de alguém de confiança e "
            "conte a essa pessoa o que está acontecendo.\n\n"
            "No Brasil, você também pode conversar com o CVV "
            "pelo telefone 188, gratuitamente.\n\n"
            "Se você é menor de idade, procure agora um adulto "
            "de confiança. Não precisa enfrentar isso sozinho."
        )
    else:
        resposta = (
            "Obrigado por compartilhar isso comigo. 💚\n\n"
            "Quero te ouvir sem julgamentos.\n\n"
            "Você gostaria de me contar um pouco mais "
            "sobre o que está sentindo?"
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
