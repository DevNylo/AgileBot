import telebot # BIBLIOTECA DO TELEGRAM
import os
from telebot import util
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('BOT_TOKEN') #!TOKEN
bot = telebot.TeleBot(token) # CRIA E INICIALIZA O BOT.


# ESPAÇO PARA FUNÇÕES #

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

# TODAS AS NOSSAS FUNÇÕES DEVERÃO SER CRIADAS AQUI EM CIMA ^ #
@bot.message_handler(commands = ['D3'])
def D3 (mensagem):
    large_text = open("./texts/D3.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands = ['D4'])
def D4 (mensagem):
    large_text = open("./texts/D4.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands = ['D5'])
def D5 (mensagem):
    large_text = open("./texts/D5.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)


## 16 ##
@bot.message_handler(commands = ['D16'])
def D16 (mensagem):
    large_text = open("./texts/D16.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)


# ----------------------------------------------------------------- #

# FUNÇÃO QUE VERIFICA SE O USUÁRIO ENVIOU A MENSAGEM CORRETA E TRANSFERE PARA A FUNÇÃO DE RESPOSTA.
def verificar(mensagem):
        return True

# DECORATOR QUE VAI AGIR A PARTIR DE UMA AÇÃO DO USUÁRIO, ELE PEGA A INFORMAÇÃO DO POLLING E DIZ QUANDO ELA SERÁ EXECUTADA A PARTIR DE UMA LISTA DE COMANDO.
@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, """Olá, estou aqui para te ajudar, selecione a opção relacionada a sua dúvida:"
                           
/D1 O que é SCRUM?

/D2 O que são Metodologias Ágeis?

/D3 O que é um Sprint?

/D4 Como gerenciar o prazo no Scrum?

/D5 Como estimar o custo de um projeto Scrum?


""")

bot.polling() # MANTÉM O BOT SEMPRE ATIVO E RETORNA A CONVERSA DO USUÁRIO.
