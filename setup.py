import telebot # BIBLIOTECA DO TELEGRAM
from telebot import util
BOT_TOKEN = "5799334689:AAHYCsDa3-Y3e93fnv-dooTWUu2Tb62m6gw" #!TOKEN
bot = telebot.TeleBot(BOT_TOKEN) # CRIA E INICIALIZA O BOT.


# EXEMPLO DE FUNÇÃO A PARTIR DE UM COMANDO EXECUTADO

@bot.message_handler(commands = ['D1'])
def D1 (mensagem):
    large_text = open("./texts/D1.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands = ['D2'])
def D2 (mensagem):
    large_text = open("./texts/D2.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=['D3'])
def D3(mensagem):
    bot.send_message(mensagem.chat.id, """ O que é um Sprint?
    
    Sprint, no framework Scrum, é um período de tempo limitado a um mês ou menos, no qual uma versão incremental e usável de um produto é desenvolvida.
    
""")
# TODAS AS NOSSAS FUNÇÕES DEVERÃO SER CRIADAS AQUI EM CIMA ^ #


# ----------------------------------------------------------------- #

# FUNÇÃO QUE VERIFICA SE O USUÁRIO ENVIOU A MENSAGEM CORRETA E TRANSFERE PARA A FUNÇÃO DE RESPOSTA.
def verificar(mensagem):
        return True

# DECORATOR QUE VAI AGIR A PARTIR DE UMA AÇÃO DO USUÁRIO,
# ELE PEGA A INFORMAÇÃO DO POLLING E DIZ QUANDO ELA SERÁ
# EXECUTADA A PARTIR DE UMA LISTA DE COMANDO.
@bot.message_handler(func=verificar) # DECORATOR QUE ATIVA A PARTIR DA RESPOSTA DA FUNÇÃO "VERIFICAR"
def responder(mensagem):
    bot.reply_to(mensagem, """Olá, estou aqui para te ajudar, selecione a opção relacionada a sua dúvida:"
                           
/D1 O que é SCRUM?

/D2 O que são Metodologias Ágeis?

/D3 O que é um Sprint?


""")

bot.polling() # MANTÉM O BOT SEMPRE ATIVO E RETORNA A CONVERSA DO USUÁRIO.
