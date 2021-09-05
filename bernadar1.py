import telebot, requests, re, json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

PRIVADO = [779455996,1625562699]
#
#
GRUPO = [-1001558388459]
#
#
EXCEPT = []
#
#
ANONY = [] # OFF

bot = telebot.TeleBot("1915223072:AAEb2ZBNBVsj4iLr26NQGR1N0unqP1pag40")

@bot.message_handler(commands=['cnpj'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO



<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')




@bot.message_handler(commands=['vizinhos'])
def byti(men):
            chtid = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001278553553,-1001588604830]
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtém os nomes dos vizinhos do portador do número de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            bot.reply_to(men, '<code>consultando...</code>', parse_mode='html')

                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>' , parse_mode='html')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>',
                                             parse_mode='html')
                            except:
                                bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>️', parse_mode='html')

            else:
                bot.reply_to(men, '''VOCÊ NÃO TEM AUTORIZAÇÃO


<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')



@bot.message_handler(commands=['cpf1','!cpf'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text.replace('cpf1','')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://netinmakerapi.000webhostapp.com/netintohjfkffxfxxxx/CONSULTA%20CPF1/api.php?cpf=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CPF</b> 🔍\n\n<b>• CPF</b>: <code>{req["retorno"]["CPF"]}</code>\n<b>• NOME</b>: <code>{req["retorno"]["Nome"]}</code>\n\n<b>• SEXO</b>: <code>{req["retorno"]["Sexo"]}</code>\n\n<b>• NASCIMENTO</b>: <code>{req["retorno"]["AnoNascimento"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO



<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')



@bot.message_handler(commands=['cpf2'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cpf2')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('vhttp://20.197.179.206:7777/?cpf=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["grauQualidade"]}</code>\n<b>• MATRIZ</b>: <code>{req["nome"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["nomeMae"]}</code>\n\n<b>• NOME</b>: <code>{req["nomePai"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["numeroCns"]}</code>\n<b>• PORTE</b>: <code>{req["paisNascimento"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["numeroCns"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["dataNascimento"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO



<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')



@bot.message_handler(commands=['cnpj'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO



<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')

@bot.message_handler(commands=['ndn'])
def zn(nome):
            id1 = nome.chat.id

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(
        "COMANDOS VIPS", callback_data="cb_yes"),
        InlineKeyboardButton("CHECKERS", callback_data="cb_no")
        ,InlineKeyboardButton("BUSCA CPF", callback_data="cb_yes")
        ,InlineKeyboardButton("BUSCA CNPJ", callback_data="cb_yes")
        ,InlineKeyboardButton("BUSCA PLACA", callback_data="cb_yes")
        ,InlineKeyboardButton("BUSCA VIZINHOS", callback_data="cb_yes")
    )
    return markup
    
   

@bot.message_handler(commands=['menu', 'help', 'start'])
def bniio(men):

    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠️ ERRADO BURRO ⚠️' + '</b>')
    else:
        try:
         menu = f'olá, <pre>{men.from_user.first_name}</pre>\n<b>VEJA SOU UM BOT GRATIS</b>\n\n<b>CLIQUE ABAIXO PARA VER MEUS COMANDOS</b>\n\n<b>• USER DO BOT🤖</b>: @Bernadar_robot'
         bot.reply_to(men, menu, reply_markup=gen_markup() ,parse_mode='HTML')
        except:
                    bot.reply_to(men, 'start', reply_markup=gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_no":
        return bot.edit_message_text("NENHUM NO MOMENTO", call.message.chat.id, call.message.message_id)

           
    elif call.data == "cb_yes":
        return bot.edit_message_text("🚫MENU DO BOT🚫 : /CPF1 , /PLACA, /VIZINHOS , /CNPJ", call.message.chat.id, call.message.message_id)
        

                                                                                    #buttons
                                                                                           
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    textos = {"cb_cnpj": "MENU DO BOT"}
    if call.data not in textos:
        return
    bot.edit_message_text(textos[call.data], call) 
    

@bot.callback_query_handler(func=lambda call: "cb_cnpj" in call.data )
def callback_teste(call):
    return bot.edit_message_text("🚫MENU DO BOT🚫 : /CPF1 , /PLACA, /VIZINHOS , /CNPJ", call.message.chat.id, call.message.message_id)                                                          
                                                                                                                                                                       
@bot.message_handler(commands=['vibbvcffdf'])
def byti(men):
            chtid = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001278553553,-1001588604830]
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtém os nomes dos vizinhos do portador do número de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            bot.reply_to(men, '<code>consultando...</code>', parse_mode='html')

                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>' , parse_mode='html')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>',
                                             parse_mode='html')
                            except:
                                bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>️', parse_mode='html')

            else:
                bot.reply_to(men, '''VOCÊ NÃO TEM AUTORIZAÇÃO


<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')




@bot.message_handler(commands=['cpfndn','!cpf'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text.replace('cpf1','')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://netinmakerapi.000webhostapp.com/netinadmf/CONSULTA%20CPF1/api.php?cpf=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CPF</b> 🔍\n\n<b>• CPF</b>: <code>{req["retorno"]["CPF"]}</code>\n<b>• NOME</b>: <code>{req["retorno"]["Nome"]}</code>\n\n<b>• SEXO</b>: <code>{req["retorno"]["Sexo"]}</code>\n\n<b>• NASCIMENTO</b>: <code>{req["retorno"]["AnoNascimento"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO



<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')





@bot.message_handler(commands=['placa','placa3','veiculo','placa4'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT + ANONY + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json", verify=False)
                    req = url.json()
                    response = f'🔍<b>PLACA ENCONTRADA</b>🔍\n\n<b>• PLACA</b>: <code>{req["placa"]}</code>\n<b>• ANO</b>: <code>{req["ano"]}</code>\n<b>• CHASSI</b>: <code>{req["chassi"]}</code>\n<b>• COR</b>: <code>{req["cor"]}</code>\n<b>• DATA</b>: <code>{req["data"]}</code>\n<b>• ALERME</b>: <code>{req["dataAtualizacaoAlarme"]}</code>\n<b>• VEICULO</b>: <code>{req["dataAtualizacaoCaracteristicasVeiculo"]}</code>\n<b>• ROUBO/FURTO</b>: <code>{req["dataAtualizacaoRouboFurto"]}</code>\n<b>• MARCA</b>: <code>{req["marca"]}</code>\n<b>• MODELO</b>: <code>{req["modelo"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n<b>• SITUAÇÃO</b>: <code>{req["situacao"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                	bot.reply_to(nome, '<b>PLACA NÃO FOI ENCONTRADA</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO

<a href='http://t.me/consultassss'>grupo</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')   		
bot.polling()
