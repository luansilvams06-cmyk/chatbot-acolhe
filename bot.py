
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

# Expressões que podem indicar intenção ou ação de risco explícita
TERMOS_RISCO_EXPLICITO = [
    "quero me matar",
    "vou me matar",
    "pretendo me matar",
    "planejo me matar",
    "quero tirar minha vida",
    "vou tirar minha vida",
    "quero me suicidar",
    "vou me suicidar",
    "vou me enforcar",
    "vou me jogar",
    "vou me cortar",
    "vou me machucar",
    "tomar todos os remédios",
]

# Expressões que podem indicar sofrimento intenso ou possível risco
TERMOS_POSSIVEL_RISCO = [
    "não vejo sentido em continuar",
    "não vejo saída",
    "não quero mais viver",
    "não aguento mais viver",
    "queria morrer",
    "quero morrer",
    "seria melhor se eu não existisse",
    "nada vai melhorar",
    "nunca mais acordar",
    "desaparecer para sempre",
    "sem esperança",
    "pensando em me machucar",
    "pensando em suicídio",
    "pensando em me suicidar",
    "automutilação",
    "automutilacao",
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
    texto_normalizado = texto.lower().strip()

    risco_explicito = any(
        termo in texto_normalizado
        for termo in TERMOS_RISCO_EXPLICITO
    )

    possivel_risco = any(
        termo in texto_normalizado
        for termo in TERMOS_POSSIVEL_RISCO
    )

    if risco_explicito:
        resposta = (
            "Sinto muito que você esteja passando por isso. 💚\n\n"
            "Sua segurança é muito importante. "
            "Você está em perigo imediato ou pensando em se machucar agora?\n\n"
            "Se houver risco imediato, procure um pronto-socorro "
            "ou ligue para o SAMU (192).\n\n"
            "Se puder, fique perto de alguém de confiança. "
            "Você também pode conversar com o CVV pelo telefone 188."
        )

    else:
        contexto_risco = (
            "A mensagem apresenta sinais de possível sofrimento "
            "intenso ou risco. Acolha sem julgamentos e pergunte "
            "diretamente, com delicadeza, se a pessoa está pensando "
            "em morrer ou se machucar. Não presuma perigo imediato."
            if possivel_risco
            else
            "Não foram identificados sinais claros pelas regras locais. "
            "Responda com acolhimento, sem introduzir assuntos de "
            "suicídio ou automutilação sem motivo."
        )

        try:
            resultado = await cliente_gemini.aio.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=f"{texto}\n\nContexto da análise: {contexto_risco}",
                config={
                    "system_instruction": (
                        "Você é o Acolhe, um assistente virtual de apoio emocional. "
                        "Responda em português brasileiro, com empatia e sem julgamentos. "
                        "Não dê diagnósticos nem prescreva medicamentos. "
                        "Não se apresente como psicólogo ou médico. "
                        "Analise o contexto completo da mensagem. "
                        "Uma negação não elimina automaticamente outros sinais "
                        "preocupantes presentes na mesma mensagem. "
                        "Se houver desesperança ou possível risco, pergunte "
                        "com delicadeza se a pessoa pensa em morrer ou se machucar. "
                        "Não presuma perigo imediato sem indícios. "
                        "Se houver perigo imediato, oriente a procurar um "
                        "pronto-socorro ou ligar para o SAMU (192). "
                        "Incentive o contato com alguém de confiança. "
                        "O CVV atende pelo telefone 188 para apoio emocional. "
                        "Em dificuldades cotidianas sem sinais concretos de risco, "
                        "acolha sem introduzir assuntos de suicídio desnecessariamente. "
                        "Nunca minimize o sofrimento, prometa sigilo absoluto "
                        "ou afirme que consegue garantir a segurança da pessoa."
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
