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


## 16 EM DIANTE ##
@bot.message_handler(commands = ['D16'])
def D16 (mensagem):
    large_text = open("./texts/D16.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands = ['D17'])
def D17 (mensagem):
    large_text = open("./texts/D17.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands=['D18'])
def D18(mensagem):
    large_text = open("./texts/D18.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D19'])
def D19(mensagem):
    large_text = open("./texts/D19.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D20'])
def D20(mensagem):
    large_text = open("./texts/D20.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D21'])
def D21(mensagem):
    large_text = open("./texts/D21.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D22'])
def D22(mensagem):
    large_text = open("./texts/D22.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D23'])
def D23(mensagem):
    large_text = open("./texts/D23.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D24'])
def D24(mensagem):
    large_text = open("./texts/D24.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D25'])
def D25(mensagem):
    large_text = open("./texts/D25.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D26'])
def D26(mensagem):
    large_text = open("./texts/D26.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D27'])
def D27(mensagem):
    large_text = open("./texts/D27.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D28'])
def D28(mensagem):
    large_text = open("./texts/D28.txt", "rb").read()
    splitted_text = util.split_string(large_text, 3000)
    print(splitted_text)
    for text in splitted_text:
        bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=['D29'])
def D29(mensagem):
    large_text = open("./texts/D29.txt", "rb").read()
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

/D16 Quais são os artefatos do Scrum?

/D17 O que é o Product Backlog?

/D18 O que é o Sprint Backlog?

/D19 Qual é a duração típica de um sprint?

/D20 Como a abordagem ágil pode ajudar na gestão de projetos?

/D21 Como o Scrum pode ajudar na gestão de projetos?

/D22 Quais são os princípios do manifesto ágil?

/D23 Qual o papel do time de desenvolvimento?

/D24 Como um Sprint é planejado e organizado?

/D25 Qual é o papel do Product Owner em um Sprint?

/D26 Qual é o papel do Scrum Master em um Sprint?

/D27 O que é uma história de usuário?

/D28 Como as histórias de usuário são priorizadas?

/D29 Sobre o AgileBot.

""")

bot.polling() # MANTÉM O BOT SEMPRE ATIVO E RETORNA A CONVERSA DO USUÁRIO.
