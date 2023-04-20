import telebot # BIBLIOTECA DO TELEGRAM
BOT_TOKEN = "5799334689:AAHYCsDa3-Y3e93fnv-dooTWUu2Tb62m6gw" #!TOKEN
bot = telebot.TeleBot(BOT_TOKEN) # CRIA E INICIALIZA O BOT.


# EXEMPLO DE FUNÇÃO A PARTIR DE UM COMANDO EXECUTADO

@bot.message_handler(commands = ['D1'])
def D1 (mensagem):
    print(mensagem) # AQUI ESTÃO AS INFORMAÇÕES DA MENSAGEM!
    bot.send_message(mensagem.chat.id, """ O que é Scrum

Scrum é um conjunto de boas práticas empregado no gerenciamento de projetos complexos, em que não se conhece todas as etapas ou necessidades focado nos membros da equipe, o Scrum torna os processos mais simples e claros, pois mantém registros visíveis sobre o andamento de todas as etapas. Assim, os participantes sabem em que fase o projeto está, o que já foi concluído e o que falta ser feito para a sua entrega. A metodologia também possibilita que produtos sejam apresentados em menor tempo, sem deixar de lado a qualidade. Ela é aplicada a partir de ciclos rápidos, chamados sprints, nos quais há um tempo determinado para que as atividades sejam concluídas – geralmente, entre duas e quatro semanas.""")

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

/D2 O que são Metodologias Ágeis?""")

bot.polling() # MANTÉM O BOT SEMPRE ATIVO E RETORNA A CONVERSA DO USUÁRIO.
